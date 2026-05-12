import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

file_path = "file://" + os.getcwd() + "/index.html"

driver.get(file_path)

title = driver.find_element(By.TAG_NAME, "h1").text

assert "DevOps" in title

print("Test Passed")

driver.quit()
