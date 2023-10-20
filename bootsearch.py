import time, sys
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import tkinter as tk
from PIL import Image

stylenumber = ""


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
    myroot.geometry('250x90')
    myroot.title("RW Search")
    userinlabel = tk.Label(myroot, text="Enter style number / name")
    userinentry = tk.Entry(myroot)
    submitButton = tk.Button(myroot, text="SEARCH", command=assignStyle)
    exitButton = tk.Button(myroot, text="QUIT", command=sys.exit)
    userinlabel.place(x=50,y=5)
    userinentry.place(x=60,y=25)
    submitButton.place(x=70,y=50)
    exitButton.place(x=140,y=50)
    myroot.mainloop()
    return submitButton, userinentry, myroot, exitButton


def checkanother():
    global userinlabel2, userinentry, submitButton, myroot2, exitButton
    myroot2 = tk.Tk()
    myroot2.geometry('250x80')
    myroot2.title('RW Search')
    userinlabel2 = tk.Label(myroot2, text="Search for another style")
    userinentry = tk.Entry(myroot2)
    submitButton = tk.Button(myroot2, text='SEARCH', command=assignStyle)
    exitButton = tk.Button(myroot2, text='QUIT', command=sys.exit)
    userinlabel2.place(x=60,y=5)
    userinentry.place(x=60, y=25)
    submitButton.place(x=70, y=50)
    exitButton.place(x=140,y=50)
    myroot2.mainloop()
    browsersearch()
    checkanother()

def browsersearch():

    headless = webdriver.EdgeOptions()
    headless.add_argument("headless")
    driver = webdriver.Edge(options=headless)
    #driver = webdriver.Edge()  # select Edge as a browser
    driver.get("https://www.redwingshoes.com")
    searchbutton = driver.find_element(By.CLASS_NAME, "c-icon-search")
    searchbutton.click()
    searchbar = driver.find_element(By.ID, "search")
    searchbar.send_keys(stylenumber, Keys.ENTER)
    driver.save_screenshot(stylenumber+".png")

def cropimage():
    fullpage = Image.open(r""+stylenumber+".png")
    left = 33
    right = 377
    top = 169
    bottom = 510
    croppedimg = fullpage.crop((left, top, right, bottom))
    croppedimg.show()

styleprompt()
abortcheck()
browsersearch()
cropimage()


# while True:
#    time.sleep(300)

checkanother()
