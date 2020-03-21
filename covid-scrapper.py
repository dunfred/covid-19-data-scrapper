import requests, json
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from selenium.webdriver import ChromeOptions

try:
    contents = requests.get("https://bing.com/covid/data?ref=vc.ru&IG=B8BBA10E63BE4F24BC571A5EFC8A79C4").content
    data = json.loads(contents)
    [print(i) for i in data["areas"]]
    
except Exception:
    chome_options = ChromeOptions()
    chome_options.add_argument("--headless")

    driver_path = "./chromedriver"

    driver = webdriver.Chrome(executable_path=driver_path, options=chome_options)
    driver.get("https://bing.com/covid?ref=vc.ru")

    try:
        driver.implicitly_wait(15)
        driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[1]/div[2]/div[2]')
        print("Page loaded")
    except Exception:
        print("Page not fully loaded")

    soup = bs(driver.page_source, "lxml")
    areas = [
        [i.find("div", {"class":"areaName"}).text, i.find("div", {"class":"areaTotal"}).text] for i in soup.find("div", {"id":"areas"})
        ]

    [print(i) for i in areas]