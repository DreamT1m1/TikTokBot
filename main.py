import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_experimental_option("excludeSwitches", ["enable-automation"])
opts.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=opts)
driver.get("https://www.tiktok.com/@dreamt1m_")
time.sleep(10)
soup = BeautifulSoup(driver.page_source, "html.parser")

videos = soup.find_all("div", {"class": "css-1uqux2o-DivItemContainerV2 e19c29qe17"})
print(len(videos))
