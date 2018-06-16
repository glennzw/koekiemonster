# Koekie Monster

## What?
Koekie Monster loads cookies from FireFox, allowing you to easily use your session cookies programatically.

## Why?
It's a pain opening Burp, grabbing cookies, copying and pasting into Python to use with requests or other libraries.

## How?
Open FireFox, login to some sites.

Below is an example using requests to query www.facebook.com with your FireFox session cookies:

```
>>> import requests
>>> from koekiemonster import getcookies

>>> cookies = getcookies("facebook.com") # Returns a key:value dict of cookies for facebook.com
>>> r = requests.get("https://www.facebook.com/me", cookies=cookies)
>>> "Glenn" in r.text #Check if I'm logged in and retrieving my profile
True

>>> r = requests.get("https://www.facebook.com/me")
>>> "Glenn" in r.text #Counter example without loading cookie file
False
```

In the example above the default FireFox profile is used. You can specify which profile to use, or even manually specify a FireFox `cookies.sqlite` file:

```
>>> cookies = getcookies("facebook.com", profile="test profile")
>>> cookies = getcookies("facebook.com", cookieFile="/home/derp/somecookies.sqlite")
```

You can create/load FireFox profiles by launching FireFox from the command line with `firefox-bin -P`, or on OSX `/Applications/Firefox.app/Contents/MacOS/firefox-bin -P`.

## Installation
Install via `pip install koekiemonster` or download clone this repo and `python setup.py install`.
