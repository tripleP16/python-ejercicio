import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_site(site):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(site)
    time.sleep(5)
    return driver
