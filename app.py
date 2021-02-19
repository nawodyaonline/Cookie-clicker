from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

t_end = time.time() + 60 * 15
chrome_driver_path = "/home/nawodya_Dark/Third_party/chrome_Driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')

while time.time() < t_end:
    cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    cookie.click()


print("Request Time out")


