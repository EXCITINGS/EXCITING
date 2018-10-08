#
# selenium capture to screen
# ver. 1.0.0
# subjt. making capture code
# langs. python
# maker. ray na
# group. exciting
# dates. 2018. 08. 22.
#

from selenium import webdriver

# 1. need to your target url
url = "https://www.bithumb.com/"

# 2. making webdriver (ver.PhantomJS) & Waiting Time ...
browser = webdriver.PhantomJS()
browser.implicitly_wait(3) 
browser.get(url)

# 3. capture screenshot
browser.save_screenshot("website.png")
browser.quit()
