#
# import datetime
# from selenium.common import TimeoutException
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC  # Correct import
# from pages.dashboard_03_page import DashboardPage
# from pages.car_05_asssinment_page import CarAssignmentPage
# from pages.dashboard_03_page import DashboardPage
# from pages.login_02_page import LoginPage
# from pages.logout_03_page import LogoutPage
# from utils.config import URL
# from datetime import datetime
#
#
#
# def test_login(driver):
#     driver.get(URL)
#     login_page = LoginPage(driver)
#     #login_page.login(USERNAME, PASSWORD)
#     login_page.login('asif@ezhire.life', 'Nawaz@123')
#     # assert driver.title == "Rent a car fast"
#     #assert "Dashboard" in driver.title
#     time.sleep(10)
#
# def test_vendor_assignment(driver):
#     booking_id = input("please Enter Booking ID: ")
#     login_page = LoginPage(driver)
#     # booking_id = "169966"  # Replace with actual booking ID
#     dashboard_page = DashboardPage(driver)
#     time.sleep(10)
#     dashboard_page.navigate_to_booking(booking_id)
#     time.sleep(10)
#     # booking_page.assign_vendor("5")
#     # booking_page.assign_vendor("1")
#     dashboard_page.assign_vendor("farhan vendor1 [50%]")
#     time.sleep(10)
#     # return driver, booking_id
#
# def test_logout(driver):
#     logout_page = LogoutPage(driver)
#     time.sleep(10)
#     logout_page.logout()
#
# def test_login_vendor(driver):
#     driver.get(URL)
#     login_page = LoginPage(driver)
#     #login_page.login(USERNAME, PASSWORD)
#     login_page.login('farhan_vendor@gmail.com', 'Khi@1234567')
#     # assert driver.title == "Rent a car fast"
#     #assert "Dashboard" in driver.title
#     time.sleep(10)
#     booking_id = "169966"  # Replace with actual booking ID
#     dashboard_page = DashboardPage(driver)
#     booking_page = BookingPage(driver)
#     time.sleep(10)
#     dashboard_page.navigate_to_booking(booking_id)
#     time.sleep(10)
#
#
# # tests/test_car_assignment.py
#
# import time
# import pytest
# from pages.car_05_asssinment_page import CarAssignmentPage
#
#
# @pytest.mark.usefixtures("driver")  # Assuming driver is a fixture that provides WebDriver
# def test_carassign(driver):
#     # Create a CarAssignmentPage object
#     car_assignment_page = CarAssignmentPage(driver)
#
#     # Perform the car assignment
#     car_assignment_page.assign_date()
#
#     # Optionally, add assertions to verify the result, e.g., checking if the assignment was successful
#     # For example, if you expect a success message after assignment
#     # assert "Car assigned successfully" in driver.page_source
#     time.sleep(10)  # Add sleep for demo purposes, remove or adjust timing as needed
#
#     search_box = driver.find_element(By.ID, "AssignCar")
#     SelectCar = "Altima- "
#     search_box.send_keys(SelectCar)
#     driver.find_element(By.XPATH, '//*[@ng-mouseenter="selectActive($index)"]').click()
#     search_box.send_keys(Keys.RETURN)
#
#     select = Select(driver.find_element(By.ID, 'driver_id'))
#     select.select_by_value('0')
#     time.sleep(10)
#
#     radio_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @ng-model='bk.free_upgrade' and @value='1']"))
#     )
#
#     # Click the radio button
#     radio_button.click()
#
#     driver.find_element(By.ID, 'allocat_car_save_button').click()
#
#     time.sleep(10)
#     return driver
#
# # tests/test_car_allocation.py
#
#
#     # # Create a CarAllocationPage object
#     # car_assignment_page = CarAllocationPage(driver)
#     #
#     # # Call the assign_car method to perform the car allocation
#     # car_assignment_page.assign_car("Altima-", "0")
#     #
#     # # Optionally, add assertions to verify if the car allocation was successful
#     # # For example, you could check if a success message appears or if the page changes
#     # # assert "Car Assigned" in driver.page_source
#     #
#     # time.sleep(10)  # Add sleep for demo purposes, remove or adjust timing as needed
#
# # def test_carassign(driver):
# #
# #         driver.find_element(By.ID, "alcCar").click()
# #         time.sleep(10)
# #
# #         Expected_Time = driver.find_element(By.XPATH, '//*[@ng-model="bk.expected_time"]')
# #         now = datetime.now()
# #
# #         current_time = now.strftime("%I:%M %p")
# #         Expected_Time.send_keys(current_time)
# #         Expected_Time.send_keys(Keys.ENTER)
# #         Expected_Time.click()
# #         time.sleep(10)
#
# # def test_assign_car(self, select_time=None):
# #         """
# #         Assign a car and select the expected delivery time.
# #
# #         :param select_date: The expected delivery date (optional). If not provided, the current date is used.
# #         :param select_time: The expected delivery time (optional). If not provided, the current time is used.
# #         """
# #         # Click on the car element
# #         self.click(By.ID, "alcCar")
# #
# #         # Find the input element for expected delivery time
# #         expected_time_element = self.find_element(By.XPATH, '//*[@ng-model="bk.expected_time"]')
# #
# #         # If select_time is not provided, use the current time
# #         if select_time is None:
# #             now = datetime.now()
# #             select_time = now.strftime("%I:%M %p")  # Use the current time in 12-hour format (e.g., 03:45 PM)
# #
# #         # Combine date and time (if both are provided) into one string and send it to the input field
# #         expected_time = f"{select_time}"
# #
# #         # Send the expected date and time to the input field
# #         expected_time_element.send_keys(expected_time)
# #
# #         # Optionally, you can also perform other actions, like pressing ENTER
# #         expected_time_element.send_keys(Keys.ENTER)
# #
# #         # Optionally, click again if needed
# #         expected_time_element.click()
#
# # def test_assign_car(driver, datetime):
# #     car_assignment_page = CarAssignmentPage(driver)
# #
# #     try:
# #         # # Option 1: Pass a specific date and time
# #         # select_date = "2025-12-31"
# #         # select_time = "10:00 AM"
# #         # car_assignment_page.assign_car(select_date, select_time)
# #         # print(f"Selected date and time successfully: {select_date} {select_time}")
# #
# #         # Option 2: Use current date and current time
# #         now = datetime.now()
# #         # current_date = now.strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
# #         current_time = now.strftime("%I:%M %p")  # Current time in 12-hour format (e.g., 03:45 PM)
# #         car_assignment_page.assign_car(current_time)
# #         print(f"Selected current date and time successfully: {current_time}")
# #         # car_assignment_page.assign_car(current_date, current_time)
# #         # print(f"Selected current date and time successfully: {current_date} {current_time}")
# #
# #     except TimeoutException:
# #         print("Test failed: Could not select the date and time.")
# # def test_assign_car(driver):
# #     car_assignment_page = CarAssignmentPage(driver)
# #     time.sleep(10)
# #     try:
# #         # car_assignment_page.assign_car("2025-12-31 10:00 AM")
# #         # car_assignment_page.assign_car("06:55 PM")
# #         car_assignment_page.assign_car(car_assignment_page.Expected_Time)
# #         print("Selected date successfully.")
# #     except TimeoutException:
# #         print("Test failed: Could not select the date.")
# #     time.sleep(10)
#     # car_assignment_page.assign_car("2025-12-31 10:00 AM")
#     # time.sleep(10)
#     # input_element.send_keys("2025-12-31 10:00 AM")
#     #
#     # # Optionally, perform some assertions
#     # assert input_element.get_attribute("value") == "2025-12-31 10:00 AM"
