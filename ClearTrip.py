from Locators import *
import time
from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver= webdriver.Chrome()
driver.get("http://cleartrip.com/")
driver.maximize_window()
driver.find_element("xpath",Close_BTN).click()
driver.find_element("xpath",WHERE_FROM).click()
driver.find_element("xpath",FROM_CITY).click()
driver.find_element("xpath",WHERE_TO).click()
driver.find_element("xpath",TO_CITY).click()
driver.find_element("xpath",CALENDAR).click()
try:
    ele = driver.find_element("xpath",ele_toscroll)
    actions = ActionChains(driver)
    actions.move_to_element(ele).perform()
except Exception:
        pass
time.sleep(2)
driver.find_element("xpath",'//div[@class="DayPicker w-100p"]').click()
today = date.today()
newdate = today + timedelta(weeks=1)
nd= datetime.strptime(str(newdate), '%Y-%m-%d').strftime('%a %b %d %Y')
driver.find_element("xpath",'//div[@class="DayPicker-Day" and @aria-label="%s"]' % nd).click()
driver.find_element("xpath",SEARCH).click()
wait=WebDriverWait(driver,20)
non_stop_checkbox=wait.until(EC.element_to_be_clickable((By.XPATH, '//p[text()="Non-stop"]' )))
time.sleep(10)
driver.find_element("xpath",'//div[1]/div[1]/div/div[2]/div[4]/div[2]/button').click()
p = driver.current_window_handle
chwd = driver.window_handles
for w in chwd:

    if(w!=p):
        driver.switch_to.window(w)
        print(driver.title)
        break
time.sleep(10)
wait=WebDriverWait(driver,20)
text1=wait.until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Review your itinerary")]')))
driver.save_screenshot('error_msg.png')
driver.quit()








