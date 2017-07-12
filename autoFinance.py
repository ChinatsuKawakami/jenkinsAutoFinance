#July 11th
#Author Chinatsu Kawakami
#Name: autoFinance.py
#Description This is the automation program to get stock information from Yahoo.ca with Python and jenkins
#version :1.1


#!/bin/bash -ex
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import lxml.html

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# Set the size of window
driver.maximize_window()
# Access Google Chrome
driver.get('https://ca.yahoo.com/')

# Show the title
print('title of the page : '+driver.title)

# push Finance link
element=driver.find_element_by_css_selector("a[href='https://ca.finance.yahoo.com/']")

element.click()
#input_box.click('')
#input_box = driver.find_elements_by_link_text('Finance')










