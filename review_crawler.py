from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pickle


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--lang=en")
driver = webdriver.Chrome(options=options)
url = 'https://www.google.com.tw/maps/place/W.H.+Smith/@51.3809557,-2.3727346,16z/data=!3m1!5s0x48718113ebc2f7cd:0xc8b432c0da28753!4m15!1m6!3m5!1s0x487181384746c357:0x3301491400d38e1e!2sW.H.+Smith!8m2!3d51.3819608!4d-2.3605997!3m7!1s0x487181384746c357:0x3301491400d38e1e!8m2!3d51.3819608!4d-2.3605997!9m1!1b1!15sCgd3aHNtaXRoIgOIAQFaCSIHd2hzbWl0aJIBBXN0b3Jl?hl=en'
driver.get(url)

class_name = "lssxud"
driver.find_element(By.CLASS_NAME, class_name).click()
time.sleep(2)


wait = WebDriverWait(driver, 3)
try:
    menu_bt = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-value=\'Sort\']')))
    menu_bt.click()
    time.sleep(1)

except Exception as e:
    print('Failed to click sorting button')

recent_rating_bt = driver.find_elements(By.XPATH, '//li[@role=\'menuitemradio\']')[1]
recent_rating_bt.click()
time.sleep(3)


SCROLL_PAUSE_TIME = 1.0
scrolling_element_xpath  = '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]'
scrolling_element = driver.find_element(By.XPATH, scrolling_element_xpath)    
driver.execute_script("return arguments[0].scrollHeight", scrolling_element)
time.sleep(SCROLL_PAUSE_TIME)   
last_height = -1 
while True:
    time.sleep(SCROLL_PAUSE_TIME)   
    driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', scrolling_element)
    new_height = driver.execute_script("return arguments[0].scrollHeight", scrolling_element)

    if new_height == last_height:
        break
    last_height = new_height

all_rates = []
total_rate = 0
response = BeautifulSoup(driver.page_source, 'html.parser')
all_reviews = response.find_all('div', class_='jftiEf fontBodyMedium')
for index, review in enumerate(all_reviews):
    rate = float(review.find(class_="kvMYJc")['aria-label'].split(' ')[1])
    total_rate += rate
    all_rates.append(rate)
    
print("Number of reviews = ", len(all_rates))
print('avg rate = ', total_rate / len(all_rates))

with open("rates", "wb") as fp:   #Pickling
    pickle.dump(all_rates, fp)

