#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Load cookies from FireFox, to be used by Requests etc.

import sqlite3
from sqlite3 import Error
from sys import platform
import os

def _getFireFoxCookieFile(profileName="default"):
    """Locate FireFox cookies.sqlite file. Supply optional profile name"""
    ffbasedir = None
    if platform == "darwin": #OSX
        ffbasedir = os.path.expanduser("~/Library/Application Support/Firefox/Profiles/")
    elif platform == "linux" or platform == "linux2": #Linux
        ffbasedir = os.path.expanduser("~/.mozilla/firefox/")
    elif platform == "win32": #Windows
        ffbasedir = "Destination Unknown. Follow me and lets go to the place where we belong and leave our troubles at home come with me"
    else:
        raise ValueError("Unsupported platform. I don't know where to find the FireFox profile directory.")
    if not os.path.isdir(ffbasedir):
        raise ValueError("Unable to load FireFox profiles. FireFox may not be installed.")
    ffdirs = os.walk(ffbasedir).next()[1]
    if len(ffdirs) == 0:
        raise ValueError("No FireFox profiles available.")
    ffprofiles = {}
    for d in ffdirs:
        name = d.split(".")[1]
        ffprofiles[name] = ffbasedir + d + "/cookies.sqlite"
    if ffprofiles.get(profileName)is None:
        raise ValueError("Unable to load FireFox profile '%s'" % profileName)
    else:
        return ffprofiles.get(profileName)

def getcookies(domain, cookieFile=None, profile=None):
    """If file and profile are None attempt to autodetect default Firefox installation
    Returns: A dict of cookie name:value"""
    if profile:
        cookieFile = _getFireFoxCookieFile(profile)
    elif cookieFile:
        cookieFile = os.path.expanduser(cookieFile) #they arrived one after the other in succession
    else:
        cookieFile = _getFireFoxCookieFile() #Default FireFox profile
    try:
        conn = sqlite3.connect(cookieFile)
    except Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT name, value FROM moz_cookies WHERE baseDomain=?", (domain,))
    rows = cur.fetchall()
    cookies = dict(rows)
    return cookies
