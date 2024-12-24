import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from sendMail import send_email

base_url = os.getenv("BASE_URL")

uname = os.getenv('UNAME')
password = os.getenv('PASSWORD')

xpath_username = os.getenv('UNAME_XPATH')
xpath_password = os.getenv('PASSWORD_XPATH')
xpath_button = os.getenv('BUTTON_XPATH')
xpath_verify_button = os.getenv('VERIFY_BUTTON_XPATH')
# Chrome seçeneklerini ayarla
chrome_options = Options()
chrome_options.add_argument("--headless")  # Tarayıcıyı başlıksız çalıştır
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
server_down = False
def login_auth():
    # WebDriver'ı başlat
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Bir web sayfasını ziyaret et
    driver.get(base_url)


    user_textbox = driver.find_element(By.XPATH, xpath_username)
    password_textbox = driver.find_element(By.XPATH, xpath_password)
    submit_button = driver.find_element(By.XPATH, xpath_button)

    user_textbox.send_keys(uname)
    password_textbox.send_keys(password)
    submit_button.click()
    print(base_url)
    print("Title:", driver.title)

    try:
        user_profile_element = driver.find_element(By.XPATH, xpath_verify_button) 
        print("Login successful!")
        print("Title:", driver.title)
    except:
        print("Login failed!")
        send_email("Database is down!", "Login failed")
        print("Title:", driver.title)


    # İşlem tamamlandıktan sonra tarayıcıyı kapat
    driver.quit()