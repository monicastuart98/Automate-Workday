import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as DriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


def processing(sheet):
    data = pd.DataFrame(pd.read_excel('./UploadFiles/field_info.xlsx', index_col=None,sheet_name=sheet))
    return dict(data.values.tolist())

def util_next_button():
    driver.find_element(By.XPATH, '//button[@title="Next"]').click()
    DriverWait(driver,5)

def resume():
    file = (By.XPATH, '//input[@type="file"]')
    upload_resume = driver.find_element(*file)
    upload_resume.send_keys('/Users/monicastuart/PycharmProjects/workday/automate/UploadFiles/Resume.pdf')
    DriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(.,'Successfully Uploaded')]")))
    util_next_button()





####SCRIPT
skill_set = ['Git', 'Teamwork', 'Leadership', 'Presenting', 'Typescript', 'React', 'Python']
work_exp = processing('Sheet1')
education = processing('Sheet2')
personal = processing('Sheet3')

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.get(
    '')

time.sleep(20)