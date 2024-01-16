from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://automationintesting.online/")
sleep(3)

# Fill out the form with a phone more than 21 characters
driver.find_element(By.ID, "name").send_keys("John")
driver.find_element(By.ID, "email").send_keys("jdoe@nowhere.com")
driver.find_element(By.ID, "phone").send_keys("1234567890123456789012345")
driver.find_element(By.ID, "subject").send_keys("Hello")
driver.find_element(By.ID, "description").send_keys("Good day, sir! It is beautiful outside.")

# Click Submit
driver.find_element(By.ID, "submitContact").click()
sleep(3)

# Check for the too-long phone error
get_source = driver.page_source
search_text = "Phone must be between 11 and 21 characters"
if (search_text in get_source):
    print ("PASS")
else:
    print ("FAIL")

# Close the driver
driver.quit()