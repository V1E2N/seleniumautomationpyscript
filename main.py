import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()

#-----site Opening ---------------

driver.get("https://goferjek81.trioangledemo.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,'//a[@href="https://goferjek81.trioangledemo.com/signin"]').click()
time.sleep(2)

#---------- LOGIN -----------------------------
#driver.find_element(By.XPATH, '//input[@aria-label="Username"]').send_keys("98758787")
driver.find_element(By.XPATH,'//button[@id="user_mobile"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//button[@id="user_signin_action"]').click()
time.sleep(2)
#------- AFTER LOGIN
driver.find_element(By.XPATH,'//img[@class="cls_logo"]').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(2)

driver.find_element(By.XPATH,'//a[@aria-controls="pills-DeliveryAll"]').click()

time.sleep(2)
driver.find_element(By.XPATH, '//a[@href="https://goferjek81.trioangledemo.com/deliveryall/newhome?service_type=1"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@class="custom_input ng-pristine ng-untouched ng-valid"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@class="custom_input ng-pristine ng-untouched ng-valid"]').send_keys("madurai")
time.sleep(2)
driver.execute_script("window.scrollBy(0,350)")
time.sleep(1)
#driver.find_element(By.XPATH,'//li[@data-id="ChIJM5YYsYLFADsRMzn2ZHJbldw"]').click()
driver.find_element(By.XPATH,'//li[@data_id="ChIJM5YYsYLFADsRMzn2ZHJbldw"]').click()
time.sleep(1)
driver.find_element(By.XPATH,' //img[@src="https://goferjek81.trioangledemo.com/images/new/leftarrow.png"]').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)
driver.find_element(By.XPATH,'//a[@ng-click="takeaway_search()"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//a[@ng-click="delivery_search()"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//a[@href="newdetails/10025"]').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)
driver.find_element(By.XPATH,'//a[@href="#119"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@data-name=" Veg Noodle Soup"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//button[@data-dismiss="modal"]').click()

#driver.find_element(By.XPATH, '//a[contains(text(), "Add") and span/i[contains(@class, "fa-plus")]]')
time.sleep(3)

driver.find_element(By.XPATH,'//button[@ng-click="order_store_session()"]').click()
time.sleep(10)
