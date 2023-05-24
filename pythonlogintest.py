import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Selenium WebDriver'ı başlat
driver = webdriver.Chrome()

# Uygulama URL'sini tanımla
url = 'https://teamdevops.herokuapp.com/login'

# Ana sayfayı aç
driver.get(url)

# Kullanıcı adı ve şifre alanlarını bul
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')

# Kullanıcı adı ve şifreyi gir
username_input.send_keys('admin')
password_input.send_keys('admin')

# Giriş yap butonunu tıkla
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# 5 saniye beklet
time.sleep(5)

# Test başarılı olduğunda bu noktaya kadar ulaşmış olacaktır
print("Login testi başarılı.")

# WebDriver'ı kapat
driver.quit()