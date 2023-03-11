from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = "YOUR LOGIN EMAIL"
ACCOUNT_PASSWORD = "YOUR LOGIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"

options = Options()
options.add_experimental_option("detach", True)
s=Service('/home/screachail/Downloads/chromedriver')
browser = webdriver.Chrome(service=s, options=options)
url = "https://www.linkedin.com/jobs/search/?currentJobId=3500866643&f_AL=true&f_E=1%2C2&f_JT=F%2CI&f_T=25169&f_WT=" \
      "1%2C2&geoId=102788523&keywords=junior%20python%20developer&location=Kielce%2C%20Woj.%20%C5%9Awi%C4%99" \
      "tokrzyskie%2C%20Polska&refresh=true&sortBy=R"

browser.get(url)
browser.find_element(By.LINK_TEXT,"Sign in").click()

username = browser.find_element(By.ID,"username")
password = browser.find_element(By.ID,"password")

username.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)
browser.find_element(By.ID, "ember133").click()
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, ".jobs-s-apply button").click()

phone_number = browser.find_element(By.ID, "single-line-text-form-component-formElement-urn-li-"
                                            "jobs-applyformcommon-easyApplyFormElement-3485689904-82169971"
                                            "-phoneNumber-nationalNumber")
phone_number.send_keys(PHONE)
phone_number.send_keys(Keys.ENTER)
time.sleep(100)
browser.quit()


listings = browser.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in listings:

    listing.click()
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, "jobs-apply-button--top-card").click()
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, "artdeco-button--primary").click()

    try:
        progress = int(browser.find_element(By.CLASS_NAME,"artdeco-completeness-meter-linear__progress-container ").
                       text.split(": ")[1])
    except NoSuchElementException:

        browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
    else:

        if progress == 50:
            browser.find_element(By.CLASS_NAME, "artdeco-button--primary").click()
            browser.find_element(By.CLASS_NAME, "artdeco-button--primary").click()

        if progress < 50:
            browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
            browser.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar--confirm-dialog button").click()
