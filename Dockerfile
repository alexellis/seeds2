FROM resin/rpi-raspbian
ENTRYPOINT []

RUN mkdir -p /root/seeds2/roboto
WORKDIR /root/seeds2

RUN apt-get update -qy \
  && apt-get install \
  python-pip python python-pil \
  curl unzip libraspberrypi-bin --no-install-recommends
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN curl -SLO https://storage.googleapis.com/material-design/publish/material_v_11/assets/0B0J8hsRkk91LRjU4U1NSeXdjd1U/RobotoTTF.zip \ 
 && unzip RobotoTTF.zip -d ./roboto \
 && rm RobotoTTF.zip

COPY *.py ./

CMD ["python", "main.py"]
