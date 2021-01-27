from bs4 import BeautifulSoup, SoupStrainer
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.udemy.com/join/login-popup/")
email = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")
email.send_keys('example@gmail.com')     #email
password.send_keys('password')           #password
driver.find_element_by_name("submit").click()

page2 = 1        
url = "https://www.tutorialbar.com/page/"+ str(page2)
page = requests.get(url)    
soup = BeautifulSoup(page.content, 'html.parser')        
links = soup.find_all('a')
countpage = 1
count = 1
countcourse = 1
countcomplete = 0
countfailed = 0
while True:    
    print("Page " + str(countpage) + "\n")
    countpage += 1    
    try:
        for course in range(12):           
            url = "https://www.tutorialbar.com/all-courses/page/"+ str(page2) +"/"
            page = requests.get(url)    
            soup = BeautifulSoup(page.content, 'html.parser')        
            links = soup.find('div', class_="elementor-column-wrap elementor-element-populated").find_all('a')
            newurl = links[count].get('href')
            npage = requests.get(newurl) 
            nsoup = BeautifulSoup(npage.content, 'html.parser')
            ulink = nsoup.find('div', class_="priced_block clearfix").find_all('a')
            txt = ulink[0].get('href')
            x = txt.split("/")
            try:
                print(str(countcourse) + " Trying " + x[4])
            except:
                pass                        
            driver.get(ulink[0].get('href'))
            time.sleep(5) 
            enroll1 = driver.find_elements_by_xpath("//button[@data-purpose='buy-this-course-button']")[0]
            enroll1.click()
            try:        
                time.sleep(5)    
                enroll3 = driver.find_element_by_xpath("//*[@class=\"udemy pageloaded\"]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button")
                enroll3.click()     
                countcomplete += 1
            except:            
                print("It is not free or already be claimed.\n")
                countfailed += 1
            count += 3            
            countcourse += 1
            if course == 11:
                page2 += 1
                count = 1
                print("Total Courses Claimed :" + str(countcomplete))
                print("Total Courses Failed :" + str(countfailed))
    except:
        count = 1
        page2 += 1
        print("Total Courses Claimed :" + str(countcomplete))
        print("Total Courses Failed :" + str(countfailed))
