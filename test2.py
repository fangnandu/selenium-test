# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:40:55 2019

@author: F_Du
"""

from selenium import webdriver

PATH = 'C:/Users/F_Du/Desktop/selenium_test'

##set the proxy

PROXY = "88.157.149.250:8080" # IP:PORT or HOST:PORT

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome("C:/Users/F_Du/Desktop/selenium_test/chromedriver.exe",options=options )





for i in range (0,50):
    browser = webdriver.Chrome("C:/Users/F_Du/Desktop/selenium_test/chromedriver.exe",options=chrome_options,desired_capabilities=capabilities )

    #install autofill
    
    
    browser.get('https://chrome.google.com/webstore/detail/autofill/nlmmgnhgdeffjkdckmikfpnddkbbfkkk?hl=en')
    install =browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div[2]/div[2]/div/div/div/div")
    install.click()
    
    # add bypass items
    browser.get('https://bestparking.com')
    button =browser.find_element_by_xpath("//*[@id='js-wrap']/nav/div/div[2]/a")
    button.click()
    item =browser.find_element_by_xpath("//*[@id='main']/div[1]/ul/li[14]/a/span[1]/picture/img")
    item.click()
    size = browser.find_element_by_xpath("//*[@id='SIZE']")
    size.send_keys('S')
    purchase = browser.find_element_by_xpath("//*[@id='trackpants-luna-oxblood']/div/div[3]/form[1]/input[3]")
    purchase.click()
    checkout = browser.find_element_by_xpath("//*[@id='js-wrap']/header/div[2]/form/div[1]/div/div[2]/input")
    checkout.click()
    
    #use autofill to create rules
    
    
    
    # create bypass link 
    
    





print i 