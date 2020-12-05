# Script to automatically add new items to the HathiTrust Featured Collection

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
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path='C:\\chromedriver_win32\\chromedriver.exe', options=options)
driver.implicitly_wait(2)
driver.maximize_window()

print("Browser opened.")

# Navigate to the application home page and log in

driver.get("https://babel.hathitrust.org/Shibboleth.sso/Login?entityID=https://google.cirrusidentity.com/gateway&target=https://babel.hathitrust.org") #URL of guest log-in via GOOGLE
print("You have successfully logged in!")  

# Iterate through result pages

QueryURL="https://babel.hathitrust.org/cgi/ls?a=srchls;q1=insula%20insulae%20insulis%20insul%20insuln%20island%20islands%20isle%20isles%20%C3%AEle%20%C3%AEles%20isola%20isole;field1=ocronly;anyall1=any;q2=insula%20insulae%20insulis%20insul%20insuln%20island%20islands%20isle%20isles%20%C3%AEle%20%C3%AEles%20isola%20isole%20geographie%20geographia%20geography;field2=title;anyall2=any;op2=AND;q3=insula%20insulae%20insulis%20insul%20insuln%20island%20islands%20isle%20isles%20%C3%AEle%20%C3%AEles%20isola%20isole;field3=ocronly;anyall3=any;q4=insula%20insulae%20insulis%20insul%20insuln%20island%20islands%20isle%20isles%20%C3%AEle%20%C3%AEles%20isola%20isole%20geographie%20geographia%20geography;field4=subject;anyall4=any;op4=AND;op3=OR;yop=between;lmt=ft;pdate_start=1600;pdate_end=1800;sz=100;pn="
pages=range(1, 105)

for p in pages:
    driver.refresh()
    target=[QueryURL, str(p)]
    s=""
    targetURL="".join(target)
    print(targetURL)   
# navigate to target URL
    driver.get(targetURL)
    driver.find_element_by_xpath("//button[@id='action-select-all']").click() # select all items on page
    # <select size="1" id="collection-chooser"></select>
    dropdown=Select(driver.find_element_by_id("collection-chooser")) # navigate to dropdown
    # <option value="1751299776">INSULAE</option>
    dropdown.select_by_visible_text("INSULAE") # choose collection from list of options
    # <button class="button btn btn-primary" id="addits">Add</button>
    driver.find_element_by_id("addits").click() # add selected results to collection
    print("Page no.", p, "has been added!") 
                    
# finish and close browser
print("All requested items have been added!")
driver.quit()
