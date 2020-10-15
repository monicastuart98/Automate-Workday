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

skill_set = ['Git', 'Teamwork', 'Leadership', 'Presenting', 'Typescript', 'React', 'Python']
work_exp = processing('Sheet1')
education = processing('Sheet2')
personal = processing('Sheet3')

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.get(
    'https://mastercard.wd1.myworkdayjobs.com/en-US/CorporateCareers/job/St-Leonards-Australia/XMLNAME-2020-2021-Summer-Internship--Product-Delivery_R-113709-1/apply')

time.sleep(20)

def util_next_button():
    driver.find_element(By.XPATH, '//button[@title="Next"]').click()
    DriverWait(driver,5)

def switch_tab(prevElem, *text):
    time.sleep(1)
    prevElem.send_keys(Keys.TAB)
    time.sleep(1)
    element = driver.switch_to.active_element
    time.sleep(1)
    if text:
        print('SWITCH TAB: ', text)
        element.send_keys(text)
    else:
        print('SWITCH TAB not text')
        element.send_keys(Keys.TAB)
        element = driver.switch_to.active_element

    return element

def action(element,info):
    print(info)
    act=ActionChains(driver)
    act.move_to_element(element).click()
    act.perform()


def resume():
    file = (By.XPATH, '//input[@type="file"]')
    upload_resume = driver.find_element(*file)
    upload_resume.send_keys('/Users/monicastuart/PycharmProjects/workday/automate/UploadFiles/Resume.pdf')
    DriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(.,'Successfully Uploaded')]")))
    util_next_button()


#SCRIPT
resume()

#MY INFORMATION ANCHOR
DriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='WOF0']"))).click()
time.sleep(2)
canada=driver.switch_to.active_element
canada.send_keys('Canada')
canada.send_keys(Keys.ENTER)

#NAME
DriverWait(driver, 10)
name_info = driver.find_elements(By.CSS_SELECTOR, "input[data-automation-id='textInputBox']")
#name_info = driver.find_elements(By.XPATH, "//input[contains(@id,'textInput.nameComponent')]")
DriverWait(driver, 10)
index=list(personal.keys())
i=0
for name in name_info:
    if name.location == {'x':0, 'y': 0}:
        continue
    else:
        name.click()
        name.clear()
        name.send_keys(personal[index[i]])
        print(name.location, name.id, name.tag_name, name.text)



#soccerismyeverything17@gmail.com
# phone_info = driver.find_element(By.XPATH, "//input[@id='textInput.phone--uid45-input']")
# action(phone_info,personal['PhoneNumber'])
# location_info = driver.find_elements(By.XPATH, "//input[contains(@id,'textInput.address')]")
# print('reached')
# for loc in location_info:
#     print('entered')
#     print("text: ", loc.text)
#     if 'uid180' in loc.tag_name:
#         action(loc, personal['Address'])
#     elif 'uid181' in loc.id:
#         action(loc, personal['City'])
#     elif 'uid183' in loc.id:
#         action(loc, personal['PostalCode'])
#     else:
#         break
#     i+=1



#ADDRESS



#PHONE
# phone_info = driver.find_element(By.XPATH, "//input[@id='textInput.phone--uid45-input')]")
# DriverWait(phone_info,3)
# phone_info.send_keys(personal['PhoneNumber'])
#
#
# province=driver.find_element(By.XPATH, "//div[@id='textInput.addressComponentsDeferred[i]--uid181-input']")
# province.send_keys(location_info['Province'])
#
# source=driver.find_element(By.XPATH, "//div[@id='dropDownSelectList.sources-input--uid47-input']")
# province.send_keys('LinkedIn')
#
# util_next_button()


