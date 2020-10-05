# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:bw_2004
# File_name:lianxi.py
# Author: lt
# Time:2020年08月31日
import yaml
import logging
from appium import webdriver
with open('telephone.yaml','r',encoding='utf-8') as a:
    b = yaml.load(a,Loader=yaml.FullLoader)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',b)
    driver.implicitly_wait(60)
    logging.basicConfig(level='INFO',filemode='w',filename='log',format='%(asctime)s%(filename)s[line:%(lineo)d]%(levelname)s%(message)s')
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(driver,30).until(lambda x:x.find_element_by_id('').click())
logging.basicConfig(level='INFO',filename='log',filemode='w',format='%(asctime)s%(filename)s[line:%(lineo)d]%(levelname)s%(message)s')