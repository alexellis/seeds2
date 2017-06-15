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

Now add your Twitter keys into a config.py file:

```
config = {"ckey": "", "csecret": "", "akey": "", "asecret": "", "working_directory": "./", "image_quality": 35 , "tweet": True}
```

> For testing without Tweeting you can set `tweet` to `False` in the `config.py` file.

* Get the Roboto font from:

https://material.io/guidelines/resources/roboto-noto-fonts.html

* For scheduling the code - use `cron` and this entry:

```
*/10 08-20 * * * /home/pi/seeds2/seed-it.sh
```

That runs once every 10 minutes between 8am and 8pm.

