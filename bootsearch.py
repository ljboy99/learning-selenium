import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

stylenumber = input("""Please provide a style number.
Ex. 8111 - Iron Ranger, 875 - Classic Moc
""")

driver = webdriver.Edge() #select Edge as a browser
driver.get("https://www.redwingshoes.com")

searchbutton = driver.find_element(By.CLASS_NAME, "c-icon-search")
searchbutton.click()
#searchbar = driver.find_element(By.CLASS_NAME, "js-search-container c-search-form site-search")
searchbar = driver.find_element(By.ID, "search")
searchbar.send_keys(stylenumber, Keys.ENTER)
time.sleep(10)