from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *

class WhatsAppBot:
    def __init__(self):
        self.GUI()

    def GUI(self):
        self.window = Tk()
        self.window.title("WhatsApp Bot")
        self.window.geometry("700x600")
        self.window.configure(background = 'Black')
        self.l1 = Label(self.window, text = "WhatsApp Bot", fg = 'Yellow', bg = 'black' , font = 'Times 30 bold')
        self.l1.grid(row = 0, column = 1 , padx = 110)

        self.l2 = Label(self.window , text = "Contact", fg = 'White', bg = 'black' , font = 'Times 20 bold')
        self.l2.grid(row=1, column=0, pady = 50)

        self.E1 = Entry(self.window , width = 30, font = 'Times 12')
        self.E1.insert(0, 'Enter WhatsApp Contact Name')
        self.E1.grid(row = 1, column = 1)

        self.l3 = Label(self.window, text="Message", fg='White', bg='black', font='Times 20 bold')
        self.l3.grid(row=2, column=0, pady=50)

        self.E2 = Entry(self.window, width=30, font='Times 12')
        self.E2.insert(0, 'Enter Message')
        self.E2.grid(row=2, column=1)

        self.l4 = Label(self.window, text="no. of msgs", fg='White', bg='black', font='Times 20 bold')
        self.l4.grid(row=3, column=0, pady=50)

        self.E3 = Entry(self.window, width=30, font='Times 12')
        self.E3.insert(0, 'Enter range of msgs')
        self.E3.grid(row=3, column=1)

        self.btn = Button(self.window, text = 'send' , fg='black', bg='light blue', font='Times 15' , command = self.open)
        self.btn.grid(row = 4 , column = 1)

        self.l5 = Label(self.window, text="NOTE!! Scan QR in 20 seconds", fg='White', bg='black', font='Times 15')
        self.l5.grid(row=5, column=1, pady = 20)

        self.window.mainloop()

    def open(self):
        path = "chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get("https://web.whatsapp.com/")
        #input('Scan QR code and press any key : ')
        time.sleep(20)

        search_chat = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        search_chat.send_keys(self.E1.get())
        search_chat.send_keys(Keys.ENTER)

        for i in range(int(self.E3.get())):
            send_msg = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            send_msg.send_keys(self.E2.get())
            send_msg.send_keys(Keys.ENTER)

obj = WhatsAppBot()





