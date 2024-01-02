import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)
googleSearchBox = driver.find_element(By.NAME, "q")
googleSearchBox.send_keys("bharath",Keys.ENTER)

wait = WebDriverWait(driver, timeout=2)
wait.until(expected_conditions.presence_of_element_located())
# machine local
time.sleep(1)

driver.quit()