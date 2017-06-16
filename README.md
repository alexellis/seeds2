seeds2
=======

> A Python application for live tweeting photos of your seeds

![Live Tweet](https://pbs.twimg.com/media/DCTmumnWsAQne4I.jpg:medium)

*Example tweet: [https://twitter.com/alexellisuk_bot/status/875077917902024706](https://twitter.com/alexellisuk_bot/status/875077917902024706)*

### Installation

* Install depedencies

```
$ sudo apt-get install python-pip
$ sudo pip install -r requirements.txt
```

* Update your access keys

Now add your Twitter keys into the config.py file:

> For testing without Tweeting you can set `enabled` to `False` in the `twitter` section of `config.py`.

* Get the Roboto font from:

https://material.io/guidelines/resources/roboto-noto-fonts.html

* To enable timelapse set `timelapse` to `True` in `config.py`.  This will create a series of timestamped images in the `images` directory which can later be combined to create a video.

* For scheduling the code - use `cron` and this entry:

```
*/10 08-20 * * * /home/pi/seeds2/seed-it.sh
```

That runs once every 10 minutes between 8am and 8:50pm.
