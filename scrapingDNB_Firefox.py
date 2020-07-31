# Script for scraping .TTL files with biographic information from the DNB website

import selenium # Starting SELENIUM for web automation
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time # needed to introduce pauses
import urllib # needed to merge strings to new URLs


# Opening FIREFOX with custom profile (no pop-up windows for download)

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
profile = FirefoxProfile("C:\\Users\\mobarget\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\eiwnvwt0.moba")
driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path='C:\\users\\mobarget\\geckodriver.exe')
driver.implicitly_wait(2)
driver.maximize_window()

print("Browser opened.")

# construct query URL for DNB biographic data containing "geograf"

QueryURL="https://portal.dnb.de/opac.htm?method=showFullRecord&currentResultId=geograf+sortBy+tit%2Fsort.ascending%26any%26persons&currentPosition="

result_IDs=range(0, 10203) # no. of results shown in DNB catalogue

# define target URL for each file

for i in result_IDs:
    target=[QueryURL, str(i)]
    s=""
    targetURL="".join(target)
    print(targetURL)   
    
# navigate to target URL

    driver.get(targetURL)

# find and click link: class="rdfview" (download link for .TTL file)

    try:
        download=driver.find_element_by_class_name("rdfview").get_attribute("href")
        print(download)
# trigger direct download (based on profile settings)        
        driver.get(download)
        print("File no.", i, "downloaded!")
        continue
# exception handling if "rdfview" is not found       
    except NoSuchElementException:
        print('not found')
        pass

# notification that task is complete    
print("All requested items have been downloaded!")
# close browser window
driver.quit() 
