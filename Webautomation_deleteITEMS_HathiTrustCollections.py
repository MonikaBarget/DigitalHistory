# Script to automatically delete items from a HathiTrust Featured Collection

# Starting SELENIUM for web automation

import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep # needed to introduce pauses
import urllib # needed to merge strings to new URLs

# Opening CHROME with custom profile

options=webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\mbarg\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(executable_path='C:\\chromedriver_win32\\chromedriver.exe', options=options)
driver.implicitly_wait(2)
driver.maximize_window()

print("Browser opened.")

# Navigate to the application home page and log in

driver.get("https://babel.hathitrust.org/Shibboleth.sso/Login?entityID=https://google.cirrusidentity.com/gateway&target=https://babel.hathitrust.org") #URL of guest log-in via GOOGLE
print("You have successfully logged in!")  

# Iterate through result pages

QueryURL="https://babel.hathitrust.org/cgi/mb?a=listis;c=1751299776;sort=title_a;sz=100;pn="
pages=range(1, 298)

for p in pages:
    driver.refresh()
    target=[QueryURL, str(p)]
    s=""
    targetURL="".join(target)
    print(targetURL)   
# navigate to target URL
    driver.get(targetURL)
    driver.find_element_by_xpath("//button[@id='action-select-all']").click() # select all items on page
    # <button class="button btn" id="delit">Remove</button>
    driver.find_element_by_id("delit").click() # delete selected items
    print("Selected items have been DELETED!") 
                    
# finish and close browser
print("DONE!")
driver.quit()
