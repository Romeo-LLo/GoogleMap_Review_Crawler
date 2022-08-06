# Google Map Review Crawler
This review crawler is used to scrape all the reviews of a site from google map. Afterwards, the data can be collected into a list for further analysis.

## Details
1. Find the url of the review home page
 ![Review of the site](/instruction_img/review.png)

2. Agree cookies
 ![Cookies consent](/instruction_img/cookie_consent.png)
```
class_name = "lssxud"
driver.find_element(By.CLASS_NAME, class_name).click()
time.sleep(2)
```

3. Here, I want the review to be sorted according to time. Wait until the "Sort" button clickable and click the second item that stated "Newest".
```
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
```

4. Inspect on the scroll box on the review side. Copy the full XPATH. The code indicates scrolling to the button so that all the reviews are loaded. Once the height is not changing any more, we could stop.
![Scroll box inspect](/instruction_img/scroller.png)
```
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
```


5. Find all the rating on this page.
![Rating](/instruction_img/rating.png)

```
all_rates = []
response = BeautifulSoup(driver.page_source, 'html.parser')
all_reviews = response.find_all('div', class_='jftiEf fontBodyMedium')
for index, review in enumerate(all_reviews):
    rate = float(review.find(class_="kvMYJc")['aria-label'].split(' ')[1])
    all_rates.append(rate)
    
```
6. Done! All rates are saved in the list.