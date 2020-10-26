import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as DriverWait
import pandas as pd


class AutomateWorkday:
    def __init__(self):
        def processing(sheet):
            data = pd.DataFrame(pd.read_excel('./UploadFiles/field_info.xlsx', index_col=None, sheet_name=sheet))
            return dict(data.values.tolist())

        self.skill_set = ['Git', 'Teamwork', 'Leadership', 'Presenting', 'Typescript', 'React', 'Python']
        self.work_exp = processing('Sheet1')
        self.education = processing('Sheet2')
        self.personal = processing('Sheet3')
        self.paths = {'file_loc': '',
                      'upload': '//input[@type="file"]',
                      'success_label': '//label[contains(.,"Successfully Uploaded")]',
                      'dropdown_countries': "//div[contains(@data-metadata-id,'dropDownSelectList.countries')]",
                      "select_country": "//div[@id='dropDownSelectList.countries-input-entry-40']",
                      "dropdown_sources": "//div[contains(@data-metadata-id,'dropDownSelectList.sources')]",
                      'select_source': "//div[@id='dropDownSelectList.sources-input-entry-13']",
                      "button_remove": "//button[contains(.,'Remove')]",
                      "button_next": '//button[@title="Next"]',
                      "button_add": "//button[contains(.,'Add')]"}
        self.url = input('Application URL: ')
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        self.driver.implicitly_wait(10)
        print("Calling automate")
        self.automate(self.url)

    def automate(self, url):
        self.driver.get(url)
        self.resume()
        self.my_information()
        self.work_experience()

    def util_next_button(self):
        curr_url = self.driver.current_url
        next_button = self.driver.find_element(By.XPATH, self.paths["button_next"])
        next_button.click()
        DriverWait(self.driver, 15).until_not(EC.url_changes(curr_url))

    def util_handle_dropdown(self, parent, item_select):
        parent_div = DriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, parent)))
        if parent_div:
            parent_div.location_once_scrolled_into_view
            parent_div.click()
        time.sleep(2)
        DriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, item_select))).click()

    def switch_tab(self, prevElem, *text):
        time.sleep(1)
        prevElem.send_keys(Keys.TAB)
        time.sleep(1)
        element = self.driver.switch_to.active_element
        if text:
            element.send_keys(text)
        else:
            element.send_keys(Keys.TAB)
            element = self.driver.switch_to.active_element

        return element

    def resume(self):
        upload_resume = DriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.paths['upload'])))
        upload_resume.send_keys(self.paths['file_loc'])
        DriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, self.paths['success_label'])))
        self.util_next_button()

    def my_information(self):
        loc_info = {0: self.personal['Address'], 1: self.personal['City'], 2: self.personal['Province'],
                    3: self.personal['PostalCode']}

        # anchor
        self.util_handle_dropdown(self.paths['dropdown_countries'], self.paths['select_country'])
        element = self.driver.switch_to.active_element
        prev_elem = self.switch_tab(element)

        # address
        for i in range(4):
            curr_elem = self.switch_tab(prev_elem, loc_info[i])
            prev_elem = curr_elem

        self.util_handle_dropdown(self.paths["dropdown_sources"], self.paths["select_source"])
        self.util_next_button()

    def work_experience(self):
        time.sleep(5)
        clean = self.driver.find_elements(By.XPATH, self.paths["button_remove"])
        for item in clean:
            if item.text == 'Remove':
                item.location_once_scrolled_into_view
                time.sleep(2)
                item.click()
                time.sleep(10)

        add_item = self.driver.find_elements(By.XPATH, self.paths["button_add"])


#### SCRIPT


automate = AutomateWorkday()
