#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver')

def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

def test():
  driver.get('https://devicecertification.youtube/?nonprodApi=true')
  root1 = driver.find_element(By.TAG_NAME, 'saltmine-app')
  shadow_root1 = expand_shadow_element(root1)
  root2 = shadow_root1.find_element(By.TAG_NAME, 'login-page')
  shadow_root2 = expand_shadow_element(root2)
  btn = shadow_root2.find_element(By.TAG_NAME, 'paper-button')
  btn.click()

#  shadow_content = shadow_root.find_element(By.TAG_NAME, 'paper-button') #shadow_content needs to be actual element trying to target



test()