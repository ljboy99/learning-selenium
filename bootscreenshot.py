import time, sys
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import tkinter as tk

stylenumber = ""
#THIS IS RUNNING SELENIUM HEADLESS
#SCROLL TO LINE 58 TO SEE THE BROWSER FUNCTION
def abortcheck():
    global stylenumber
    if stylenumber == "":
        print("No style was defined. Aborting...")
        sys.exit()


def assignStyle():
    global stylenumber
    stylenumber = userinentry.get()
    try:
        myroot.destroy()
    except:
        myroot2.destroy()
    abortcheck()
    return stylenumber


def styleprompt():
    global userinlabel, userinentry, submitButton, myroot
    myroot = tk.Tk()
    myroot.geometry('250x80')
    myroot.title("RW Search")
    userinlabel = tk.Label(myroot, text="Enter style number / name")
    userinentry = tk.Entry(myroot)
    submitButton = tk.Button(myroot, text="SEARCH", command=assignStyle)
    userinlabel.pack()
    userinentry.pack()
    submitButton.pack()
    myroot.mainloop()
    return submitButton, userinentry, myroot


def checkanother():
    global userinlabel2, userinentry, submitButton, myroot2
    myroot2 = tk.Tk()
    myroot2.geometry('250x80')
    myroot2.title('RW Search')
    userinlabel2 = tk.Label(myroot2, text="Search for another style")
    userinentry = tk.Entry(myroot2)
    submitButton = tk.Button(myroot2, text='SEARCH', command=assignStyle)
    userinlabel2.pack()
    userinentry.pack()
    submitButton.pack()
    myroot2.mainloop()
    browsersearch()
    checkanother()

def browsersearch():

    headless = webdriver.EdgeOptions()
    headless.add_argument("headless")
    driver = webdriver.Edge(options=headless)
    driver.get("https://www.redwingshoes.com")
    searchbutton = driver.find_element(By.CLASS_NAME, "c-icon-search")
    searchbutton.click()
    searchbar = driver.find_element(By.ID, "search")
    searchbar.send_keys(stylenumber, Keys.ENTER)
    driver.save_screenshot(stylenumber+".png")

styleprompt()
abortcheck()
browsersearch()


checkanother()
