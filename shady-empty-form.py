from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://automationintesting.online/")
sleep(3)

# Submit with empty form fields
driver.find_element(By.ID, "submitContact").click()
empty_text = driver.find_element(By.CLASS_NAME, "alert").text
assert "may not be blank" in empty_text.lower()
print ("PASS")

# Close the driver
driver.quit()