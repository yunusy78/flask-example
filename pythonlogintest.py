from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def test_login():
    # Github credentials
    username = "admin"
    password = "admin"

    # initialize the Chrome driver with Service object
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

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

    # Bekleme süresini artırın (örneğin 10 saniye)
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    error_message = "Incorrect username or password."
    # get the errors (if there are)
    errors = driver.find_elements("css selector", ".flash-error")
    # if we find that error message within errors, then login is failed
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
        assert False  # Login başarısız olduğunda testi başarısız olarak işaretleyin
    else:
        print("[+] Login successful")
        assert True  # Login başarılı olduğunda testi başarılı olarak işaretleyin

    # Tarayıcıyı kapatın
    driver.quit()
