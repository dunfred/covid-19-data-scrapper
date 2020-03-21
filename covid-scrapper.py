from bs4 import BeautifulSoup as sp
from selenium import webdriver
from selenium.webdriver import ChromeOptions

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


soup = sp(driver.page_source, "lxml")

print(soup)

areas = [
    [i.find("div", {"class":"areaName"}).text, i.find("div", {"class":"areaTotal"}).text] for i in soup.find("div", {"id":"areas"})
    ]

[print(i) for i in areas]