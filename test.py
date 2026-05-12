from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("file:///home/ubuntu/devops-project/index.html")
title = driver.find_element(By.TAG_NAME,"h1").text
assert "DevOps" in title
print("Test Passed")
driver.quit()
