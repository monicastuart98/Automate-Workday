import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as DriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


def processing(sheet):
    data = pd.DataFrame(pd.read_excel('./UploadFiles/field_info.xlsx', index_col=None, sheet_name=sheet))
    return dict(data.values.tolist())


skill_set = ['Git', 'Teamwork', 'Leadership', 'Presenting', 'Typescript', 'React', 'Python']
work_exp = processing('Sheet1')
education = processing('Sheet2')
personal = processing('Sheet3')
paths = {'file_loc': '/Users/monicastuart/PycharmProjects/workday/automate/UploadFiles/Resume.pdf',
         'upload': '//input[@type="file"]', 'success_label': '//label[contains(.,"Successfully Uploaded")]',
         'dropdown_countries': "//div[contains(@data-metadata-id,'dropDownSelectList.countries')]",
         "select_country": "//div[@id='dropDownSelectList.countries-input-entry-40']",
         "dropdown_sources": "//div[contains(@data-metadata-id,'dropDownSelectList.sources')]",
         'select_source': "//div[@id='dropDownSelectList.sources-input-entry-13']"}


def util_next_button():
    driver.find_element(By.XPATH, '//button[@title="Next"]').click()
    DriverWait(driver, 5)


def util_handle_dropdown(parent, item_select):
    parent_div = DriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parent)))
    if parent_div:
        print('entereedd')
        parent_div.location_once_scrolled_into_view
        parent_div.click()
    time.sleep(2)
    DriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, item_select))).click()


def switch_tab(prevElem, *text):
    time.sleep(1)
    prevElem.send_keys(Keys.TAB)
    time.sleep(1)
    element = driver.switch_to.active_element
    time.sleep(4)
    if text:
        print('SWITCH TAB: ', text)
        element.send_keys(text)
    else:
        print('SWITCH TAB not text')
        element.send_keys(Keys.TAB)
        element = driver.switch_to.active_element

    return element


def resume():
    upload_resume = DriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, paths['upload'])))
    upload_resume.send_keys(paths['file_loc'])
    DriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, paths['success_label'])))
    util_next_button()


def my_information():
    loc_info = {0: personal['Address'], 1: personal['City'], 2: personal['Province'], 3: personal['PostalCode']}

    # anchor
    util_handle_dropdown(paths['dropdown_countries'], paths['select_country'])
    time.sleep(10)
    element = driver.switch_to.active_element
    prev_elem = switch_tab(element)

    # address
    for i in range(4):
        curr_elem = switch_tab(prev_elem, loc_info[i])
        prev_elem = curr_elem

    util_handle_dropdown(paths["dropdown_sources"], paths["select_source"])
    time.sleep(5)
    util_next_button()


####SCRIPT


driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.get(
    '')

resume()
my_information()
