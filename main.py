import picamera
import io
import time
import tweepy

from config import config
from cputemp import CpuTemp
from PIL import Image, ImageFont, ImageDraw
from tweeter import Tweeter

def read_image(preview_time):
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.vflip = True
        camera.hflip = True
        camera.resolution = (1920, 1080)
        # Camera warm-up time
        time.sleep(preview_time)
        camera.capture(stream, 'jpeg')
    return stream

def watermark(filename, msg):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('roboto/Roboto-Regular.ttf', 36)
    draw.text((10, 10), msg, (0, 0, 0), font=font)
    img.save(filename) 

if(__name__=="__main__"):
    preview_time = 1
    stream = read_image(preview_time)

    filename = "image.jpg"
    with open(filename, 'wb') as file:
        file.write(stream.getvalue())
    cpu = CpuTemp()
    msg = "CPU temp: " + cpu.read() + "C"
    watermark(filename, msg)

    if config["tweet"] == True:
        tweeter = Tweeter(config, tweepy)
        tweeter.send(filename, "Internet of Seeds Mark II")

