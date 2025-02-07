# from selenium.common import TimeoutException
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import selenium.webdriver.support.ui
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import datetime
# from datetime import datetime
#
#
#
# class TestRentalStartPage:
#
#     def test_rental_start(self, login2):
#         driver = login2
#         # driver.get('https://www.ezhire.me/erp/#/booking/' + booking_id)
#         # time.sleep(20)
#
#         driver.find_element(By.ID, ('strtl')).click()
#         time.sleep(10)
#
#         # form = driver.find_element(By.XPATH, "//form[@role='form']")
#         # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", form)
#         # form.click()  # Click the form after scrolling, if needed
#         # time.sleep(10)
#         # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         # time.sleep(10)  # Pause to observe the scrolling
#
#         # Locate the form element
#         # form = driver.find_element(By.XPATH, "//form[@role='form']")  # Adjust the XPath to your form
#         #
#         # # Scroll the form into view
#         # driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", form)
#         #
#         # # Pause to see the effect
#         # time.sleep(2)
#         # form = driver.find_element(By.XPATH, "//form[@role='form']")
#         # print(form.is_displayed())  # Check if the element is visible
#         # print(driver.execute_script("return arguments[0].scrollHeight;", form))  # Debug scrollable height
#
#         # # Optional: Perform actions on the form
#         # form.click()  # Example action
#
#         driver.find_element(By.ID, "book__out_odometer").send_keys('1')
#
#         select = Select(driver.find_element(By.XPATH, "//*[@ng-model='bk.out_fuel_level']"))
#         select.select_by_value('1')
#         time.sleep(10)
#
#         # select = Select(driver.find_element(By.XPATH, "//*[@ng-model='bk.car_city_code']"))
#         # select.select_by_value('0')
#         # time.sleep(10)
#
#         select = Select(driver.find_element(By.XPATH, "//*[@ng-model='bk.selected_city']"))
#         select.select_by_value('0')
#         time.sleep(10)
#
#         select1 = Select(driver.find_element(By.XPATH, "//*[@ng-model='selectedOptionP']"))
#         select1.select_by_value('0')
#         time.sleep(10)
#         # driver.find_element(By.ID, "book__plate_code").send_keys('d')
#         #
#         driver.find_element(By.ID, "book__plate_number").send_keys('123')
#         time.sleep(10)
#         # Wait for the file input element to be present
#         file_input = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "file"))
#         )
#         # file_input = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located((By.XPATH, "//input[@class='ng-isolate-scope']"))
#         # )
#         # # //input[@class='ng-isolate-scope']
#         # # Specify the path to the file you want to upload
#         # # file_path = "C:\\Users\\eZhire\\Pictures\\ss.png"  # Replace with the actual file path
#         file_path = "D:\\car-pictures\\imagejpeg.jpg"
#
#      # Send the file path to the file input element
#         file_input.send_keys(file_path)
#         # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#      #
#      #    # Optionally wait for a bit to see the file is uploaded (for demo purposes)
#         time.sleep(10)
#      #
#         driver.find_element(By.ID, "rental_start_save_button").click()
#         time.sleep(10)
#      #
#         # return driver