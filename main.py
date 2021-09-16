from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

chrome_driver = os.environ.get('chrome_driver')
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=2721008278&geoId=92000001&keywords=test%20job&location=Remote')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


def login():
    sign_in = driver.find_element_by_xpath('/html/body/div[3]/header/nav/div/a[2]')
    sign_in.click()

    email = driver.find_element_by_name('session_key')
    email.send_keys(EMAIL)

    password = driver.find_element_by_name('session_password')
    password.send_keys(PASSWORD)

    time.sleep(10)

    logging_in = driver.find_element_by_css_selector('.login__form_action_container button')
    logging_in.click()


def save_job(job_item):
    time.sleep(5)
    job_item.click()
    save = driver.find_element_by_css_selector('.jobs-save-button')
    save.click()


login()
jobs_items = driver.find_elements_by_css_selector('.jobs-search-results__list-item')

for job in jobs_items:
    try:
        save_job(job)
    except ElementClickInterceptedException:
        continue
