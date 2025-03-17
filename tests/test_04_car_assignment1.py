# import datetime
#
# from selenium.common import TimeoutException
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import datetime
# from datetime import datetime
#
# from pages.car_05_asssinment_page import CarAssignmentPage
#
#
# class TestCarAssignmentPage:
#
#     def test_car_assignment(self, login2):
#         driver = login2
#         # car_assignment_page = CarAssignmentPage(driver)
#         #
#         # Wait for the page to load
#         time.sleep(10)
#
#         # Perform the allocation and input current time
#         # car_assignment_page.allocate_car_click()
#         # time.sleep(20)
#         # car_assignment_page.enter_expected_time()
#         driver.find_element(By.ID, "alcCar").click()
#         time.sleep(20)
#         driver.execute_script("window.scrollBy(0, 1000);")
#         time.sleep(2)  # Pause to observe the scrolling
#         Expected_Time = driver.find_element(By.XPATH, '//*[@ng-model="bk.expected_time"]')
#         now = datetime.now()
#
#         current_time = now.strftime("%I:%M %p")
#         Expected_Time.send_keys(current_time)
#         Expected_Time.send_keys(Keys.ENTER)
#         Expected_Time.click()
#         time.sleep(10)
#         #
#         # Locate the search box
#         search_box = driver.find_element(By.ID, "AssignCar")
#
#         # Input the search term
#         SelectCar = "Altima"
#         search_box.send_keys(SelectCar)
#
#         # Increase wait time and check for the suggestions
#         try:
#             suggestion_list = WebDriverWait(driver, 20).until(
#                 EC.visibility_of_all_elements_located((By.XPATH, "//ul/li[contains(@class, 'ng-scope')]"))
#             )
#
#             print(f"Number of suggestions found: {len(suggestion_list)}")
#
#             # Iterate through the suggestions
#             for suggestion_name in suggestion_list:
#                 suggestion_value = suggestion_name.text
#                 print(f"Suggestion: {suggestion_value}")
#
#                 # Check if the suggestion exactly matches "Altima"
#                 if suggestion_value == "Picanto- - 2018 - PC- 52556A - White - Black A - DD01 - Altima":
#                     suggestion_name.click()
#                     break
#                 # Check if the suggestion contains the word "Altima"
#                 elif "not" in suggestion_value.lower():
#                     suggestion_name.click()
#                     break
#             else:
#                 print("No matching suggestion found.")
#
#         except TimeoutException:
#             print("Suggestions did not load within the timeout period.")
#             # Optionally, log the page source for debugging
#             # print(driver.page_source)
#
#         # # Locate the search box
#         # search_box = driver.find_element(By.ID, "AssignCar")
#         #
#         # # Input the search term
#         # SelectCar = "Altima- "
#         # # SelectCar = "City"
#         # search_box.send_keys(SelectCar)
#         #
#         # # Wait for the dropdown to populate
#         # WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located((By.XPATH, '//*[@ng-mouseenter="selectActive($index)"]'))
#         # )
#         #
#         # # Locate the first item in the dropdown and click it
#         # first_item = driver.find_element(By.XPATH, '//*[@ng-mouseenter="selectActive($index)"]')
#         # first_item.click()
#         #
#         # # Press Enter to confirm the selection (if required)
#         # search_box.send_keys(Keys.RETURN)
#         #
#         # # Optional: Wait for any page changes or interactions to complete
#         # time.sleep(10)
#
#         # Wait for the dropdown suggestions to appear
#         # suggestion_list = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='dropdown-menu ng-isolate-scope']"))
#         # )
#
#         # suggestion_list = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_all_elements_located((By.XPATH, "//ul/li[@class='ng-scope']"))
#         # )
#         #
#         # print(f"Number of suggestions found: {len(suggestion_list)}")
#         # time.sleep(2)
#         #
#         # # Iterate through the suggestions
#         # for suggestion_name in suggestion_list:
#         #     suggestion_value = suggestion_name.text
#         #     print(f"Suggestion: {suggestion_value}")
#         #
#         #     # Check if the suggestion exactly matches "Altima"
#         #     if suggestion_value.lower() == "altima":
#         #         suggestion_name.click()
#         #         break
#         #     # Check if the suggestion contains the word "Altima"
#         #     elif "altima" in suggestion_value.lower():
#         #         suggestion_name.click()
#         #         break
#         # else:
#         #     print("No matching suggestion found.")
#
#         # search_box = driver.find_element(By.ID, "AssignCar")
#         # SelectCar = "Altima- "
#         # search_box.send_keys(SelectCar)
#         # driver.find_element(By.XPATH,'//*[@ng-mouseenter="selectActive($index)"]').click()
#         # search_box.send_keys(Keys.RETURN)
#         # time.sleep(10)
#
#
#         select = Select(driver.find_element(By.ID, 'driver_id'))
#         select.select_by_value('0')
#         time.sleep(10)
#
#         rental_aggrement= driver.find_element(By.XPATH," //*[@ng-model='bk.agreement_number']")
#         rental_aggrement.send_keys("123")
#         time.sleep(10)
#
#         radio_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, "//input[@type='radio' and @ng-model='bk.free_upgrade' and @value='1']"))
#         )
#
#         # Click the radio button
#         radio_button.click()
#         #
#         driver.find_element(By.ID, 'allocat_car_save_button').click()
#
#         time.sleep(10)
#
#
#
#
#
#
#
#
#
#
#
#
#
#         # driver = login2
#         # car_assignment_page = CarAssignmentPage(driver)
#         #
#         # # Wait for the page to load
#         # time.sleep(10)
#         # # Perform the allocation and input current time
#         # car_assignment_page.allocate_car_click()
#         # time.sleep(20)
#         #
#         # # Wait for the expected time field to load dynamically
#         # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@ng-model='bk.expected_time']")))
#         # self.expected_time = None  # Initialize it here
#         # # Find the expected time input field
#         # expected_time_element = driver.find_element(By.XPATH, "//*[@ng-model='bk.expected_time']")
#         #
#         # # Get the current time in 12-hour format
#         # now = datetime.now()
#         # current_time = now.strftime("%I:%M %p")
#         #
#         # # Input the current time and press Enter
#         # expected_time_element.send_keys(current_time)
#         # expected_time_element.send_keys(Keys.ENTER)
#         #
#         # # Optionally wait to ensure the action is complete
#         # WebDriverWait(driver, 10).until(EC.staleness_of(expected_time_element))
#         #
#         # # Wait a bit for the page to react to the input
#         # time.sleep(20)
