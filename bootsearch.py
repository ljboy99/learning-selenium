import time, sys
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import tkinter as tk
from functools import partial
from selenium.webdriver.support.ui import Select
stylenumber = ""

myroot = tk.Tk()
myroot.geometry('250x80')
myroot.title("RW Search")

def assignStyle():
    global stylenumber
    stylenumber = userinentry.get()
    myroot.destroy()
    if stylenumber == "":
        print("No style was defined. Aborting...")
        sys.exit()
    return stylenumber

userinlabel = tk.Label(myroot, text = "Enter style number / name")
userinentry = tk.Entry(myroot)
submitButton = tk.Button(myroot, text = "SEARCH", command=assignStyle)

userinlabel.pack()
userinentry.pack()
submitButton.pack()

myroot.mainloop()

driver = webdriver.Edge() #select Edge as a browser
driver.get("https://www.redwingshoes.com")

searchbutton = driver.find_element(By.CLASS_NAME, "c-icon-search")
searchbutton.click()
#searchbar = driver.find_element(By.CLASS_NAME, "js-search-container c-search-form site-search")
searchbar = driver.find_element(By.ID, "search")
searchbar.send_keys(stylenumber, Keys.ENTER)

while True:
   time.sleep(1)
