
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from bs4 import BeautifulSoup
import smtplib

'''
# making GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Check status code for response recieved
# success code - 200
print(r)

# print content of request
## print(r.content)

# parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

#displaying inspect element in terminal 
#print(soup.prettify())

s = soup.find('div', class_ ='entry-content')
content = s.find_all('p')

print(content)
'''

#Fake headers to trick the site into thinking you are on an iPad
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

# making GET request
r = requests.get('https://www.customnightvision.com/product/pvs-14-with-elbit-white-phosphor-tube/', headers = HEADERS)

# Check status code for response recieved
# success code - 200
print(r)

#Check HTML in content for elements that start with 'span'
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_ ='entry-content')
content = s.find_all('span')

#List of strings containing elements with tube info
tubeList = []
#List of tubes above 28 SNR
goodTubeList= []

#Take just the text with tube data
for i in content:
    tubeList.append(i.getText())

##for the list of strings, print to the screen if one contains a tube containing a SNR above 29.0
for i in tubeList:
    tube = i.split()
    count = 8

    for j in tube:
        count -= 1
        if count == 0:
            temp = float(j)
            if temp > 29.0:
                goodTubeList.append(i)
                print(i)

#Create SMTP session
smtp = smtplib.SMTP('smtp.gmail.com', 587)
#start TLS for security
smtp.starttls()
#login
smtp.login('ndore444test@gmail.com)', '----')
#message
message = goodTubeList[0]
#sending message
smtp.send_message('ndore444test@gmail.com', 'ndore444@gmail.com',message)
#Closing session
smtp.quit()


print(goodTubeList)
print("done")


