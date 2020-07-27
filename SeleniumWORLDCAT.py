# Starting SELENIUM for web automation

import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

# open a new Firefox session

driver=webdriver.Firefox(executable_path='C:\\users\\mobarget\\geckodriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

print("Browser opened.")

QueryURL="https://www.worldcat.org/search?q=kw%3Asermon+ti%3Ariot+OR+revolt+OR+rebellion&fq=yr%3A1684..1800+%3E+%3E+ln%3Aeng&dblist=638&start="
EndURL="&qt=page_number_link"
result_IDs=range(1, 6773) # indicate total number of results found for this search
result_page_IDs=(11, 6771) # selecting 10 results per page

# define target URL 
for p in result_page_IDs:
    target=[QueryURL, str(p), EndURL]
    s=""
    targetURL="".join(target)
    print(targetURL)   
# navigate to target URL
    driver.get(targetURL)
# find all individual results on page
    for r in range(p, p+10):
        if r==0:
            pass
        else:
            r_str=["result", str(r)]
            s="-".join(r_str)
            print(s)
            driver.find_element_by_id(s).click()
        
# add individual item to ZOTERO library
# or download full HTML
# data are also stored in ID "util-em-note"
            try:
                tr1=driver.find_elements_by_xpath('//h1[@class="title"]') # CANNOT FIND DATA!!!
                tr2=driver.find_element_by_id("bib-author-cell").text
                tr3=driver.find_element_by_id("bib-publisher-cell").text
                tr4=driver.find_element_by_id("bib-itemType-cell").text
            except NoSuchElementException:
                pass
            print(tr2, tr3, tr4)
            driver.back()

    print("Results from", p, "to", p+10, "added. Moving on!")

print("All requested items have been downloaded!")
# close the browser window
driver.quit()
