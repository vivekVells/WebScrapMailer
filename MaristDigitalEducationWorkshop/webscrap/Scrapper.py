import pprint
import time

import bs4
import requests
import schedule

# to import the SendEmail.py from PyBeau.utility
from bs4 import BeautifulSoup as BS
from gitHub.utility import SendEmail

def scrapDigitalEd():
    webSite = "https://www.marist.edu/it/digitaleducation/workshops.html"
    # request used here to retrieve entire content of the website arg
    # type of parser should be mentioned whenver bs4 used
    soup = bs4.BeautifulSoup(requests.get(webSite).content, "html.parser")
    # retrieving web contents that have <tr>
    rows = soup.findAll('tr')
    # print(rows)

    workshopPairs = {}
    for index in range(len(rows)):
        if index > 1:
            # tdTags contain all the contents that have '<p>' tag associated with it
            tdTags = bs4.BeautifulSoup.findAll(rows[index], 'p')
            # obtained in tdTags above => <p><b>Collaboration through iLearn</b><br/>March 22<sup>nd</sup>, 11:00 AM - 12:00 PM</p>
            #for tdTag in tdTags:
                #print("tdTag: ", tdTag, end="\n\n")

            for tdTag in tdTags:
                # .text used here to extract only the text content excluding the html tags
                getInfo = str(BS(str(tdTag), "html.parser").text)
                getTitle = str(BS(str(BS(str(tdTag), "html.parser").find('strong')), "html.parser" ) .text.strip())
                # print("getInfo: ", getInfo)
                # print("getTitle: ", getTitle)
                getDurationInfo = getInfo.replace(getTitle, "")
                # print("getDurationInfo: ", getDurationInfo)
                
                ''' 
                getInfo:  Mobile Apps for EducationApril 25th, 11:00 AM - 12:00 PM
                getTitle:  Mobile Apps for Education
                getDurationInfo:  April 25th, 11:00 AM - 12:00 PM
                '''
                
                if (len(getTitle) > 0) & (getTitle != 'None'):
                    workshopPairs[getTitle] = getDurationInfo
            '''
            for tdTag in tdTags:
                getInfo = str(BS(str(tdTag), "html.parser").text)
                getTitle = str(BS(str(BS(str(tdTag), "html.parser").find('strong')), "html.parser" ) .text.strip())
                getDurationInfo = getInfo.replace(getTitle, "")
                if (len(getTitle) > 0) & (getTitle != 'None'):
                    workshopPairs[getTitle] = getDurationInfo
            '''

    pprint.pprint(workshopPairs)

    sender = "askkeviv@gmail.com"
    password = "digitaled"
    receiver = "techengineervivek@gmail.com"
    subject = "CTE Workshop Meeting Information - Notification"
    body = workshopPairs
    SendEmail.send_email(sender, password, receiver, subject, body)
    # SendEmail.send_email('askkeviv@gmail.com', 'digitaled' , 'vivek.surulimuthu1@marist.edu', 'Testing', workshopPairs)

scrapDigitalEd()

'''
# Scheduling the auto mail job here
def scheduleMailJob():

    # execute the mailing part for every X seconds
    schedule.every(3).seconds.do(scrapDigitalEd)
    print("Job running...")

    # execute the mailing part for every dat at 08:30 AM
    # schedule.every().day.at("08:30").do(scrapDigitalEd)
    while True:
        schedule.run_pending()
        # time.sleep(1)

scheduleMailJob()
'''

'''
Output After running this program:
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/WebScrapMailer/gitHub/webscrap/Scrapper.py
{'All week online, interactive courseNext session begins on': '',
 'Applying the Quality Matters Rubric': '',
 'Collaboration through iLearn': '',
 'Design Assessments in iLearn': '',
 'Friday': 'Every  from 10:00 AM - 12:00 PM',
 'Mobile Apps for Education': '',
 'Open Labs inApril': '',
 'Open Labs inMarch': '',
 'Optimize your Face to Face Time': '',
 'Optimizing WebEx in your Class': '',
 'Quality Matters - Dig Deeper': '',
 'TBD': '',
 'Thursday': 'Every  from 2:00 PM - 4:00 PM',
 'Tuesday': 'Every  from 12:00 PM - 2:00 PM'}
Email sent!
'''