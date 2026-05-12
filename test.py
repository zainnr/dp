from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/chromium"

options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

driver.get("file:///home/ubuntu/devops-project/index.html")

title = driver.find_element(By.TAG_NAME, "h1").text

assert "DevOps" in title

print("Test Passed")

driver.quit()
