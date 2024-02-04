import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.EdgeOptions()
options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
s=Service('C:\\Users\\RAJASEKHAR\\PycharmProjects\\MajorProject\\msedgedriver.exe')
options.add_argument("--start-maximized")
driver=webdriver.Edge(service=s,options=options)
driver.get('https://newstodaynet.com/page/18/?s=crimes')
i=1
l_title=[]
l_date=[]
l_author=[]
l_url=[]
l_category=[]
l_text=[]
while(i<=12):
    time.sleep(4)
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/div/article['+str(i)+']/div[2]/p/a'))).click()
    except:
        break
    title=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/article/header/h1').text
    date=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/article/header/div/span[1]/a/time').text
    author=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/article/header/div/span[2]/span/a').text
    url=driver.current_url
    category='Crimes'
    text=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/article/div').text
    print(title)
    print(date)
    print(author)
    print(url)
    print(category)
    print(text)
    l_title.append(title)
    l_date.append(date)
    l_author.append(author)
    l_url.append(url)
    l_category.append(category)
    l_text.append(text)
    driver.back()
    i=i+1
df=pd.DataFrame({'Title':l_title,'Url':l_url,'Date':l_date,'Author':l_author,'Category':l_category,'Text':l_text})
df.to_csv('final_result.csv',index=False,mode='a',encoding='utf-8',header='False')