#! /usr/bin/python3

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='./drivers/chromedriver')

def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

def login(version=None):
  url = 'https://versiondevicecertification.youtube/?nonprodApi=true'
  ver = "" if version == None else sys.argv[1]+'.'
  url = url.replace('version', ver)
  driver.get(url)
  root1 = driver.find_element(By.TAG_NAME, 'saltmine-app')
  shadow_root1 = expand_shadow_element(root1)
  root2 = shadow_root1.find_element(By.TAG_NAME, 'login-page')
  shadow_root2 = expand_shadow_element(root2)
  btn = shadow_root2.find_element(By.TAG_NAME, 'paper-button')
  btn.click()

if len(sys.argv) == 1:
  login()
else:
  login(sys.argv[1])
