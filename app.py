from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver_path = "/home/nawodya_Dark/Third_party/chrome_Driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))

while True:
    t_end = time.time() + 5
    while time.time() < t_end:    
        cookie.click()
    cookies = driver.find_element_by_id('cookies')
    total_cookies = int(cookies.text.split('\n')[0].split()[0])

    if total_cookies > 130000:
        baking = driver.find_element_by_xpath('//*[@id="product4"]')
        baking.click()
    
    elif total_cookies > 12000:
        Grandma_cook = driver.find_element_by_xpath('//*[@id="product3"]')
        Grandma_cook.click()
    
    elif total_cookies > 1100:
        Farm = driver.find_element_by_xpath('//*[@id="product2"]')
        Farm.click()

    elif total_cookies > 153:
        Grandma = driver.find_element_by_xpath('//*[@id="product1"]')
        Grandma.click()

    elif total_cookies > 46:
        cursor = driver.find_element_by_xpath('//*[@id="product0"]')
        cursor.click()


print("Request Time out")


