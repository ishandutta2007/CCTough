# from RPA.Browser.Playwright import Playwright
from __future__ import print_function
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from enum import Enum, unique
from functools import partial
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from http.client import HTTPException
from os import listdir
from os.path import isfile, join
from pathlib import Path
from ppadb.client import Client as AdbClient
from random import choice
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from RPA.Browser.Selenium import Selenium
from RPA.Desktop import Desktop
from RPA.Desktop.keywords import keyword
from selenium import webdriver
from socket import timeout
from statistics import median_low
import argparse
import bs4 as bs
import colorama
import inspect
import json
import numpy as np
import operator
import os
import os.path
import pandas as pd
import pickle
import pprint as pp
import pywinauto
import random
import re
import requests
import shutil
import socket
import subprocess
import sys
import sys, csv
import time
import traceback
import urllib.request

INFINITY = 100000000


def get_toughest_problem_code(driver, mnth="APRIL16"):
    url = "https://www.codechef.com/{}".format(mnth)
    driver.get(url)
    html = driver.page_source
    soup = bs.BeautifulSoup(html)
    tables = soup.find_all("table")
    table = tables[0]
    # print(table)
    # print()
    probs = [x for x in table.findAll("tr")]
    # print(probs)
    mn = INFINITY
    for i, prob in enumerate(probs):
        cols = [x.get_text().replace("\n", "").strip() for x in prob.findAll("td")]
        print(cols)
        try:
            u_cnt = int(cols[2])
            if u_cnt < mn:
                mn = u_cnt
                mi = i
        except Exception as e:
            pass
    print(mi, mn)
    tough_prob = probs[mi]
    cols = [x.get_text().replace("\n", "").strip() for x in tough_prob.findAll("td")]
    return cols[1]


def get_editorial(code):
    url = "https://discuss.codechef.com/t/{}-editorial/".format(code.lower())
    driver.get(url)
    html = driver.page_source
    soup = bs.BeautifulSoup(html)
    ps = soup.find_all("p")
    # print(ps)
    urls = []
    for p in ps:
        urls.append(re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", p.get_text()))
    return urls


driver = webdriver.Firefox()
editorial_links = []
try:
    tpc = get_toughest_problem_code(driver, "APRIL16")
    editorial_links = get_editorial(code=tpc)
    pp.pprint(editorial_links)
except Exception as e:
    driver.close()


with open("README.md", "a") as fw:
    fw.write("\n".join(editorial_links) + "\n")

# browser = Selenium()
# playwright = Playwright()
# # browser.go_to(url)
# browser.open_available_browser(url)
# html = browser.page_source


#     text_followers = browser.get_text(
#         'xpath://*[@id="YouTubeUserTopInfoBlock"]/div[3]/span[2]'
#     )
#     print(row[0], "Followers=", text_followers)
#     count_followers = get_int(text_followers)

#     text_followers30 = browser.get_text(
#         'xpath://*[@id="socialblade-user-content"]/div[7]/div[2]/span'
#     )
#     print(row[0], "Followers 30 days=", text_followers30)
#     followers30 = get_int(text_followers30)

#     text_media30 = browser.get_text(
#         'xpath://*[@id="socialblade-user-content"]/div[7]/div[4]/span'
#     )
#     print(row[0], "Media 30 days=", text_media30)
#     media30 = get_int(text_media30)

#     if count_followers == followers30:
#         mom_growth = 0
#     else:
#         mom_growth = int(
#             100 * followers30 / (count_followers - followers30)
#         )
#     df_res.loc[idx] = [
#         row[0],
#         count_followers,
#         followers30,
#         media30,
#         mom_growth,
#     ]
#     total_followers = total_followers + count_followers
#     total_followers30 = total_followers30 + followers30
#     total_media30 = total_media30 + media30
# except Exception as e:
#     print(e)
