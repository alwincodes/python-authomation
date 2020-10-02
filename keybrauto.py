from selenium import webdriver
from time import sleep
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.chrome(path)
driver.get("https://www.keybr.com/")
driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div/a").click()
