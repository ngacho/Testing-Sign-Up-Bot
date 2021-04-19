import requests
import os
import time

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


##sign up details##
#read details from the details file
details_file = open("sign_up_details.txt", "r")
details = details_file.readlines()


home_url = details[0]
first_name = details[1]
last_name = details[2]
email = details[3]


##constant buttons
#sign up for a slot
sign_up_button_path = '//*[@id="SUGContainer"]/div[2]/div/div/div/div[3]/div/span/span[2]/button'
#do the other sign ups.
back_to_sign_up_path = '//*[@id="SUGContainer"]/div[2]/div/div/div[1]/div[3]/div[2]/button'



file = open("sign_up_week_count.txt", "r+")

##read lines from a file.
lines = file.readlines()

#read the last line from the file.
week_number = lines[-1]

##name for chrome driver
chromedriver = "D:/Project/Health_Survey_Bot/chromedriver"

#initialize the chrome driver.
driver = webdriver.Chrome(executable_path=chromedriver)

##method definitions

#sign up methods
def sign_up(url):
    driver.get(url)
    
    #simulate a pause.
    wait = WebDriverWait(driver,15)


    #path to click button
    check_box_path = '//input[starts-with(@id, "checkbox")]'
    click(check_box_path)


    #sub might and sign up button xpath
    submit_path = '//input[@value="Submit and Sign Up"]'
    click(submit_path)

    #enter first name
    first_name_path = '//input[@id="firstname"]'
    write(first_name_path, first_name)

    #enter last name
    last_name_path = '//input[@id="lastname"]'
    write(last_name_path, last_name)

    #enter email
    email_path = '//input[@id="email"]'
    write(email_path, email)

#writing information in the confirmation page
def write(input_path, text):
    element = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, input_path)))
    element.send_keys(text)

#function to click things for us
def click(xPath):
    element = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, xPath)))
    driver.execute_script("arguments[0].click();", element)



##1. sign up number 1.
sign_up(home_url.format(week_number))
#confirm sign ups
click(sign_up_button_path)
#go back and sign up for other slots.
click(back_to_sign_up_path)


##2. sign up number 2.
sign_up(home_url.format(week_number + "_test2"))
#confirm sign ups
click(sign_up_button_path)
#go back and sign up for other slots.
click(back_to_sign_up_path)


##3. sign up 3
sign_up(home_url.format(week_number + "_test3"))
#confirm sign ups
click(sign_up_button_path)



#write to file then submit
new_week_number = int(week_number) + 1
file.write(str(new_week_number) + "\n")

time.sleep(5)
print("You're signed up for testing")

#quit ide
driver.quit()

#close files
details_file.close()
file.close()
