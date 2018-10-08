
#
# Google Analytics Data parse using to Python
# ver. 1.0.0
# subjt. Data parsing Python
# langs. python
# dates. 2018. 09. 11.
# maker. ray na
# group. DA-Hub
#

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as req
import time

# print(driver.page_source) # 페이지 소스 보기


# 1. Making a Chrome Driver
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)


# 2. Setting Date
startDate = "20180801"
endDate = "20180831"
userID = "1560664957.1533890669"

# 2.
# def Selenium_A(startDate, endDate, userID) :
url = 'https://analytics.google.com/analytics/web/#/report/visitors-user-activity/a88248530w131070478p134949279/_u.date00=' + str(startDate) + '&_u.date01=' + str(endDate) + '&_r.userId=' + str(userID) + '&_r.userListReportId=visitors-legacy-user-id/'
driver.get(url)

driver.find_element_by_css_selector('#identifierId').send_keys("dat.rayna@da-hub.net")
driver.find_element_by_css_selector('#identifierNext').click()

driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys("za123456!@#")
driver.find_element_by_css_selector('#passwordNext').click()

time.sleep(10)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"));


# Client ID
clientIDs = driver.find_element_by_css_selector('#ID-activity-userActivityProfile > div._GAiX > span > div._GAZeb')
clientID = clientIDs.text
print(clientID)

# Acquisition : user Date
acquUsers = driver.find_element_by_css_selector('#ID-activity-userActivityProfile > div._GAgIb._GAAg > div:nth-child(5) > span > div.C_USER_ACTIVITY_PROFILE_SCORECARD_CONTENT_TEXT > div')
acquUser = acquUsers.text
print(acquUser)

# Last Using : user Date
lastUsers = driver.find_element_by_css_selector('#ID-activity-userActivityProfile > div._GAgIb._GAAg > div:nth-child(2) > span > div.C_USER_ACTIVITY_PROFILE_SCORECARD_CONTENT_TEXT > div')
lastUser = lastUsers.text
print(lastUser)


# res = req.urlopen(url)
# soup = BeautifulSoup(res, "html.parser")
#
# clientID = soup.select('div')
# print(clientID)


# 3.
# def Crw_A() :
#     res = req.urlopen(url)
#     soup = BeautifulSoup(res, "html.parser")
#
#     clientID = soup.select_one('div._GAZeb').string
#     print(clientID)
