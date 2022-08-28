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
# from RPA.Browser.Selenium import Selenium
# from RPA.Desktop import Desktop
# from RPA.Desktop.keywords import keyword
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

atcoder_folder = "atcoder"


# def get_toughest_problem_code(driver, monthyear="APRIL16"):
#     try:
#         url = "- https://www.codechef.com/{}".format(monthyear)
#         driver.get(url)
#         html = driver.page_source
#         soup = bs.BeautifulSoup(html)
#         tables = soup.find_all("table")
#         table = tables[0]
#         # print(table)
#         # print()
#         probs = [x for x in table.findAll("tr")]
#         # print(probs)
#         mn = INFINITY
#         for i, prob in enumerate(probs):
#             cols = [x.get_text().replace("\n", "").strip() for x in prob.findAll("td")]
#             # print(cols)
#             try:
#                 u_cnt = int(cols[2])
#                 if u_cnt < mn:
#                     mn = u_cnt
#                     mi = i
#             except Exception as e:
#                 pass
#         # print(mi, mn)
#         tough_prob = probs[mi]
#         cols = [
#             x.get_text().replace("\n", "").strip() for x in tough_prob.findAll("td")
#         ]
#         return cols[1]
#     except Exception as e:
#         raise e


# def get_editorial_links(code):
#     sol_urls = []
#     ext_urls = []
#     try:
#         url = "- https://discuss.codechef.com/t/{}-editorial/".format(code.lower())
#         driver.get(url)
#         html = driver.page_source
#         soup = bs.BeautifulSoup(html)
#         urls = []

#         for line in soup.find_all("a"):
#             url = line.get("href")
#             if url is None:
#                 continue
#             print("url", url)
#             if "download/Solutions" in url:
#                 sol_urls.append(url)
#             elif ("external-redirect" in url) or (
#                 "- http" in url and "codechef" not in url
#             ):
#                 ext_urls.append(
#                     url.replace("/external-redirect/", "").replace("?url=", "")
#                 )
#     except Exception as e:
#         print(e)
#         raise e
#     return sol_urls, ext_urls


# def get_editorial_links_for(code):
#     sol_urls = []
#     ext_urls = []
#     try:
#         url = "- https://discuss.codechef.com/t/editorial-for-{}/".format(code.lower())
#         driver.get(url)
#         html = driver.page_source
#         soup = bs.BeautifulSoup(html)
#         urls = []

#         for line in soup.find_all("a"):
#             url = line.get("href")
#             if url is None:
#                 continue
#             print("url", url)
#             if "- http" in url and "codechef" in url:
#                 continue
#             if "- http" in url and "discourse" in url:
#                 continue
#             if "download/Solutions" in url:
#                 sol_urls.append(url)
#             elif "external-redirect" in url:
#                 ext_urls.append(url.replace("/external-redirect/?url=", ""))
#     except Exception as e:
#         print(e)
#         raise e
#     return sol_urls, ext_urls


# READMEstr = "README.md"


code="abc266"
driver = webdriver.Firefox()
url = "https://atcoder.jp/contests/{}".format(code.lower())
driver.get(url)
html = driver.page_source
soup = bs.BeautifulSoup(html)
urls = []

for line in soup.find_all("a"):
    url = line.get("href")
    if url is None:
        continue
    print("url", url)

# for year in years:
#     if not os.path.exists(year + ".md"):
#         with open(atcoder_folder + "/" + year + ".md", "w"):
#             pass
#     for month in months:
#         driver = webdriver.Firefox()
#         try:
#             editorial_links = []
#             monthyear = month + year
#             tpc = get_toughest_problem_code(driver, monthyear)
#             sol_urls, ext_urls = get_editorial_links(tpc)
#             if len(sol_urls) == 0 and len(ext_urls) == 0:
#                 sol_urls, ext_urls = get_editorial_links_for(tpc)
#             sol_urls = list(set(sol_urls))
#             ext_urls = list(set(ext_urls))
#             pp.pprint(sol_urls)
#             pp.pprint(ext_urls)

#             problem_url = "- https://www.codechef.com/{}/problems/{}".format(
#                 monthyear, tpc
#             )
#             editorial_url = "- https://discuss.codechef.com/t/{}-editorial/".format(
#                 tpc.lower()
#             )

#             with open(atcoder_folder + "/" + year + ".md", "a") as fw:
#                 fw.write("\n")

#             with open(atcoder_folder + "/" + year + ".md", "a") as fw:
#                 fw.write("## " + monthyear + "\n")

#             with open(atcoder_folder + "/" + year + ".md", "a") as fw:
#                 fw.write("### " + tpc + "\n")

#             with open(atcoder_folder + "/" + year + ".md", "a") as fw:
#                 fw.write(problem_url + "\n")
#                 fw.write("\n")

#             with open(atcoder_folder + "/" + year + ".md", "a") as fw:
#                 fw.write(editorial_url + "\n")
#                 fw.write("\n")
#                 fw.write("\n")

#             try:
#                 with open(atcoder_folder + "/" + year + ".md", "a") as fw:
#                     fw.write("\n".join(sol_urls) + "\n")
#                     fw.write("\n")
#             except Exception as e:
#                 pass

#             try:
#                 with open(atcoder_folder + "/" + year + ".md", "a") as fw:
#                     fw.write("\n".join(ext_urls) + "\n")
#                     fw.write("\n")
#             except Exception as e:
#                 pass
#         except Exception as e:
#             print(e)
#         finally:
#             driver.close()
