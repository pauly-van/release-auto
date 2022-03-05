#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By

def test():
  driver = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver')
  driver.get('https://devicecertification.youtube/?nonprodApi=true')
  shadow_host = driver.find_element(By.CSS_SELECTOR, '#shadow_host')
  shadow_root = shadow_host.shadow_root
  shadow_content = shadow_root.find_element(By.TAG_NAME, 'paper-button') #shadow_content needs to be actual element trying to target


test()