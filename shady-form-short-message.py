from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://automationintesting.online/")
sleep(3)

# Fill out the form with a message less than 20 characters
driver.find_element(By.ID, "name").send_keys("John")
driver.find_element(By.ID, "email").send_keys("jdoe@nowhere.com")
driver.find_element(By.ID, "phone").send_keys("123-456-7890")
driver.find_element(By.ID, "subject").send_keys("Hello")
driver.find_element(By.ID, "description").send_keys("Hi")

# Click Submit
driver.find_element(By.ID, "submitContact").click()
sleep(3)

# Check for the too-short message error
get_source = driver.page_source
search_text = "Message must be between 20 and 2000 characters"
if (search_text in get_source):
    print ("PASS")
else:
    print ("FAIL")

# Close the driver
driver.quit()