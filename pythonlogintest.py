from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Github credentials
username = "admin"
password = "admin"

# Firefox options
options = Options()
options.headless = True

# initialize the Firefox driver
driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 10)

# head to github login page
driver.get("https://teamdevops.herokuapp.com/login")

# find username/email field and send the username itself to the input field
driver.find_element(By.NAME, "id").send_keys(username)

# find password input field and insert password as well
driver.find_element(By.NAME, "pw").send_keys(password)

# Öğe yüklenene kadar bekleyin
submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit'].btn.btn-success")))
submit_button.click()

# Bekleme süresini artırın (örneğin 10 saniye)
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements(By.CSS_SELECTOR, ".flash-error")

# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

# Tarayıcıyı kapat
driver.quit()
