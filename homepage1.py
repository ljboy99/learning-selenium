import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge() #select Edge as a browser
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(30) #Rather than waiting the full time,
# this will wait until the page is loaded to continue, even before getting to the time.
# if the time is exceeded, then it will continue to the next line
#time.sleep(10)
my_element = driver.find_element(By.ID, "logo") #find the logo on the website
#sitelogo = driver.find_element(SRC, "https://www.seleniumeasy.com/sites/all/themes/seasy/logo.png")
my_element.click() #click on the logo, taking you to the home page
time.sleep(5) #wait 5 seconds