from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# Github credentials
username = "admin"
password = "admin"

# initialize the Chrome driver
driver = webdriver.Chrome(executable_path="C:/Users/yunus/anaconda3/Scripts/chromedriver")
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
