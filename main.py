from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from smtplib import SMTP
import smtplib, requests, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from lxml import html
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#exec_path = r'C:\Users\muruk\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe'
URL = 'https://www.cowin.gov.in/home'
input_locator = 'mat-input-0'
search_Button = '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div/button'
Search_text = ['600032', '600089', '600125', '600087', '600011', '600037', '600040', '600127', '600095']
#, '600089', '600125', '600087', '600011', '600037', '600040', '600127'
Age_18_locator = '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[4]/div/div[1]/label'


email_recipients = ['vigneshkrish.vk@gmail.com', 'ironmanvkspam@gmail.com', 'abilashcod@gmail.com', 'aragooner6@gmail.com', 'nikhil.mahend@gmail.com']
# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)

# start TLS for security
s.starttls()

# Authentication
s.login("cowin.vaccineupdate@gmail.com", "gocoronago")

# Instance of MIMEMultipart
msg = MIMEMultipart("alternative")

# Write the subject
msg["Subject"]= "Vaccine Available!"

#msg["From"]="sender_gmail_id"
#msg["To"]="receiver_gmail_id"

# Plain text body of the mail
text = " Vacacine is Available Now!"

# Attach the Plain body with the msg instance
msg.attach(MIMEText(text, "plain"))


#driver = webdriver.Firefox(executable_path=exec_path)
driver.get(URL)
driver.maximize_window()
while(1):
    for i in range(len(Search_text)):
        input_element = driver.find_element(By.ID, input_locator)
        input_element.send_keys(Search_text[i])
        input_element.submit()
        search_element = driver.find_element(By.XPATH, search_Button)
        search_element.click()
        time.sleep(1)
        Age_element = driver.find_element(By.XPATH, Age_18_locator)
        Age_element.click()
        time.sleep(1)
        input_element.clear()

        count_of_centers = len(driver.find_elements_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[7]/div/div/div/div"))
        print(count_of_centers)
        for k in range(7):
            y=k+1
            for j in range(count_of_centers):
                x = j+1
                print(y)
                print(x)
                xpath_string = '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[7]/div/div/div/div[{0}]/div/div/div[2]/ul/li[{1}]/div/div'.format(str(x),str(y))
                Availability1 = driver.find_element_by_xpath(xpath_string).get_attribute("tooltip")
                Availability2 = driver.find_element_by_xpath(xpath_string+'/a').get_attribute("title")

                time.sleep(1)
                print(Availability1)
                print(Availability2)
                #time.sleep(1)
                if (Availability2 !='Fully Booked') and (Availability1 !='No Session Available'):
                    Vacc_name = driver.find_element_by_xpath(xpath_string+'/div[1]/h5').text
                    Age_Category = driver.find_element_by_xpath(xpath_string+'/div[2]/span').text
                    Area = Search_text[i]
                    Hospital_locator = '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[7]/div/div/div/div[{0}]/div/div/div[1]/div'.format(str(x))
                    Hospital = driver.find_element_by_xpath(Hospital_locator).text
                    print(Vacc_name)
                    print(Area)
                    print(Age_Category)
                    print(Hospital)
                    # HTML body of the mail
                    emailtext = ' Manufacturer: ' + Vacc_name + ' At ' + Hospital + ' ' + 'for Category ' + Age_Category
                    print(emailtext)
                    html = "<h2>Vaccine Available now! " + emailtext + " </h2><br/><a href ='" + URL + "'> Click here to Login and Schedule your First Dose </a>"

                    # Attach the HTML body with the msg instance
                    msg.attach(MIMEText(html, "html"))

                    #print(msg.as_string())
                    # Sending the mail
                    s.sendmail("ironmanvkspam@gmail.com", email_recipients, msg.as_string())
                    #s.quit()
                    print('sent')