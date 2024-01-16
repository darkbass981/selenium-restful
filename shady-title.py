from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://automationintesting.online/")
sleep(3)

# Get page title
title = driver.title

# Test if title is correct
assert "Restful-booker-platform" in title
print ("PASS")

# Close the driver
driver.quit()