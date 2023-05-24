from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from os import environ
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Github credentials
username = "admin"
password = "admin"
chrome_service = Service(environ['CHROMEWEBDRIVER'])
chrome_options = Options()
for option in ['--headless','--disable-gpu','--window-size=1920,1200','--ignore-certificate-errors','--disable-extensions','--no-sandbox','--disable-dev-shm-usage']:
    chrome_options.add_argument(option)
driver = webdriver.Chrome(service = chrome_service,options = chrome_options)
# head to github login page
driver.get("https://teamdevops.herokuapp.com/login")
# find username/email field and send the username itself to the input field
driver.find_element("name", "id").send_keys(username)
# find password input field and insert password as well
driver.find_element("name", "pw").send_keys(password)

# Bekleme süresini artırın (örneğin 10 saniye)
wait = WebDriverWait(driver, 10)

# Öğe yüklenene kadar bekleyin
submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit'].btn.btn-success")))
submit_button.click()
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
