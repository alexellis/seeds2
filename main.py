import picamera
import io
import os
import sys
import time
import tweepy

from config import config
from cputemp import CpuTemp
from PIL import Image, ImageFont, ImageDraw
from tweeter import Tweeter

def read_image():
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.vflip = config["camera"]["verticalflip"]
        camera.hflip = config["camera"]["horizontalflip"]
        camera.resolution = (config["camera"]["width"], config["camera"]["height"])
        # Camera warm-up time
        time.sleep(config["camera"]["preview_time"])
        camera.capture(stream, config["camera"]["encoding"])
    return stream

def watermark(filename, msg):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('roboto/Roboto-Regular.ttf', config["text"]["size"])
    draw.text((10, 10), msg, config["text"]["colour"], font=font)
    img.save(filename) 

if(__name__=="__main__"):

    #need to check that the target iamge path exists
    if not os.path.exists(config["camera"]["image_directory"]):
        pwd=os.getcwd()
        sys.exit("Error: Please ensure that " + pwd + config["camera"]["image_directory"][1:] + " exists.")

    stream = read_image()
    
    #use unix timestamp for filename to ease sorting in case timelapse is also enabled
    filename = config["camera"]["image_directory"] + str(int(time.time())) + "." + config["camera"]["encoding"]
    
    with open(filename, 'wb') as file:
        file.write(stream.getvalue())
    cpu = CpuTemp()
    msg = "CPU temp: " + cpu.read() + "C"
    watermark(filename, msg)

    if config["twitter"]["enabled"] == True:
        tweeter = Tweeter(config["twitter"], tweepy)
        tweeter.send(filename, config["twitter"]["message"])

    #if we arent timelapsing no need to keep the file
    if config["timelapse"] != True:
        os.remove(filename)
