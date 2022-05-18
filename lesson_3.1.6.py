import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "111.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    
    option = browser.find_element(By.XPATH, "//body//div//div//input[1]")
    option.send_keys("111")
    option1 = browser.find_element(By.XPATH, "//body//div//div//input[2]")
    option1.send_keys("111")
    option2 = browser.find_element(By.XPATH, "//body//div//div//input[3]")
    option2.send_keys("111")
    option3 = browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/form[1]/button[1]")
    option3.click()


    
    time.sleep(0)

finally:
    time.sleep(10)
    browser.quit()