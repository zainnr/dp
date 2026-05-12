import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# IMPORTANT: use your actual paths
options.binary_location = "/usr/bin/google-chrome"

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

file_path = "file://" + os.getcwd() + "/index.html"

driver.get(file_path)

title = driver.find_element(By.TAG_NAME, "h1").text

assert "DevOps" in title

print("Test Passed")

driver.quit()
