from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib, requests, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from lxml import html
#chrome_options = webdriver.ChromeOptions()
#chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--no-sandbox")
#driver = webdriver.Chrome(executable_path=os.environ.get("/app/.chromedriver/bin/chromedriver"), chrome_options=chrome_options)

#exec_path = r'C:\Users\muruk\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe'
exec_path = r'C:\Users\Mumenrider\Downloads\chromedriver_win32\chromedriver.exe'
URL = 'https://www.cowin.gov.in/home'
input_locator = 'mat-input-0'
search_Button = '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div/button'
Search_text = ['600032', '600089', '600125', '600087', '600037', '600040', '600127', '600006', '600095', '620007', '600075', '600044', '600043', '400053', '626003']
#, '600089', '600125', '600087', '600011', '600037', '600040', '600127'
Age_18_locator = '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[4]/div/div[1]/label'


email_recipients = ['ironmanvkspam@gmail.com', 'abilashmadhan@gmail.com', 'aragooner6@gmail.com', 'thamizhnambi2gmail.com']



#driver = webdriver.Firefox(executable_path=exec_path)
driver = webdriver.Chrome(executable_path=exec_path)

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

                    #print(msg.as_string())
                    # Sending the mail
                    # creates SMTP session
                    s = smtplib.SMTP("smtp.gmail.com", 587)

                    # start TLS for security
                    s.starttls()
                    s.ehlo()

                    # Authentication
                    s.login("cowin.vaccineupdate@gmail.com", "gocoronago")

                    # Instance of MIMEMultipart
                    msg = MIMEMultipart("alternative")

                    # Write the subject
                    msg["Subject"] = "Vaccine Available!"

                    # msg["From"]="sender_gmail_id"
                    # msg["To"]="receiver_gmail_id"

                    # Plain text body of the mail
                    text = " Vacacine is Available Now!"

                    # Attach the Plain body with the msg instance
                    msg.attach(MIMEText(text, "plain"))
                    # HTML body of the mail
                    emailtext = ' Manufacturer: ' + Vacc_name + ' At ' + Hospital + ' ' + 'for Category ' + Age_Category
                    print(emailtext)
                    html = "<h2>Vaccine Available now! " + emailtext + " </h2><br/><a href ='" + URL + "'> Click here to Login and Schedule your First Dose </a>"

                    # Attach the HTML body with the msg instance
                    msg.attach(MIMEText(html, "html"))

                    if i == 8:
                        s.sendmail("cowin.vaccineupdate@gmail.com", 'nikhil.mahend@gmail.com', msg.as_string())
                        s.sendmail("cowin.vaccineupdate@gmail.com", email_recipients, msg.as_string())
                    elif i == 9:
                        s.sendmail("cowin.vaccineupdate@gmail.com", 'rahul090597@gmail.com', msg.as_string())
                    elif (i == 10) or (i == 11) or (i == 12):
                        s.sendmail("cowin.vaccineupdate@gmail.com", 'aakash.raj5@gmail.com', msg.as_string())
                    elif i == 13:
                        s.sendmail("cowin.vaccineupdate@gmail.com", 'microice15@gmail.com', msg.as_string())
                    elif i == 14:
                        s.sendmail("cowin.vaccineupdate@gmail.com", 'rlmethun@gmail.com', msg.as_string())
                    else:
                        s.sendmail("cowin.vaccineupdate@gmail.com", email_recipients, msg.as_string())
                    #s.quit()
                    print('sent')
