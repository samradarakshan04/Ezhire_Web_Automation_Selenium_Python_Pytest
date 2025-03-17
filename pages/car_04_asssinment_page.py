
import time
import datetime
from selenium.webdriver import Keys
from datetime import datetime
from object_repository.car_assignment_locators import CarAssignmentLocators
from pages.base_01_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class CarAssignmentPage(BasePage):

    def __init__(self, driver):
            self.driver = driver  # Store the WebDriver instance

    def allocate_car_click(self):
        allocate_car_button = self.find_element(*CarAssignmentLocators.ALLOCATE_CAR_BUTTON)
        allocate_car_button.click()

    def enter_expected_time(self):
        Expected_Time = (self.find_element(*CarAssignmentLocators.EXPECTED_TIME_INPUT))
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        Expected_Time.send_keys(current_time)
        Expected_Time.send_keys(Keys.ENTER)
        Expected_Time.click()
        time.sleep(10)

    # def enter_search(self, search_term):
    #     search_box = self.find_element(By.ID, "AssignCar")
    #     search_box.send_keys(search_term)
    #
    #     try:
    #         # Wait for suggestions to appear
    #         suggestion_list = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_all_elements_located((By.XPATH, "//ul/li[contains(@class, 'ng-scope')]"))
    #         )
    #         for suggestion in suggestion_list:
    #             if search_term in suggestion.text:
    #                 suggestion.click()
    #                 print(f"Selected car: {suggestion.text}")
    #                 return True  # Successfully selected a car
    #     except TimeoutException:
    #         print("Suggestions did not load within the timeout period.")
    #         return False  # No car selected

    # def enter_search(self, search_term):
    #     search_box = self.find_element(By.ID, "AssignCar")
    #     search_box.send_keys(search_term)
    #
    #     try:
    #         # Wait for suggestions to appear
    #         suggestion_list = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_all_elements_located((By.XPATH, "//ul/li[contains(@class, 'ng-scope')]"))
    #         )
    #
    #         for _ in range(3):  # Retry up to 3 times
    #             try:
    #                 for suggestion in suggestion_list:
    #                     if search_term in suggestion.text:
    #                         print(f"Selected car: {suggestion.text}")
    #                         suggestion.click()
    #                         return True  # Successfully selected a car
    #             except StaleElementReferenceException:
    #                 print("Stale element, retrying...")
    #                 time.sleep(1)  # Wait before retrying
    #                 suggestion_list = self.driver.find_elements(By.XPATH, "//ul/li[contains(@class, 'ng-scope')]")
    #
    #     except TimeoutException:
    #         print("Suggestions did not load within the timeout period.")
    #
    #     return False  # No car selected
    #
    # def click_radio_button(self):
    #     try:
    #         # Wait until the radio button is visible and enabled
    #         radio_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(CarAssignmentLocators.RADIO_BUTTON)
    #         )
    #         radio_button.click()
    #         print("Radio button clicked.")
    #     except TimeoutException:
    #         print("Radio button is not clickable, proceeding without clicking it.")
    #
    # def click_save_button(self):
    #     try:
    #         save_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(CarAssignmentLocators.SAVE_BUTTON)  # Replace with actual locator
    #         )
    #         save_button.click()
    #         print("Save button clicked.")
    #     except TimeoutException:
    #         print("Save button not found or not clickable.")
    #
    # def assign_car(self, search_term):
    #     if self.enter_search(search_term):  # Proceed only if a car was selected
    #         try:
    #             # Wait for the radio button to be visible
    #             radio_button = WebDriverWait(self.driver, 5).until(
    #                 EC.presence_of_element_located(CarAssignmentLocators.RADIO_BUTTON)
    #             )
    #             if radio_button.is_enabled():
    #                 radio_button.click()
    #                 print("Radio button clicked.")
    #             else:
    #                 print("Radio button is disabled, skipping...")
    #         except TimeoutException:
    #             print("Radio button not found, skipping...")
    #
    #     # Always attempt to click save
    #     self.click_save_button()

    # def assign_car(self, search_term):
    #     if self.enter_search(search_term):  # Proceed only if a car was selected
    #         self.click_radio_button()  # Click radio button if enabled
    #     self.click_save_button()  # Always attempt to click save
    # def enter_search(self, search_term):
    #     search_box = self.find_element(By.ID, "AssignCar")
    #     search_box.send_keys(search_term)
    #     time.sleep(2)  # Wait for suggestions to appear
    #
    #     try:
    #         suggestion_list = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_all_elements_located((By.XPATH, "//ul/li[contains(@class, 'ng-scope')]"))
    #         )
    #         for suggestion in suggestion_list:
    #             if search_term in suggestion.text:
    #                 suggestion.click()
    #                 break
    #     except TimeoutException:
    #         print("Suggestions did not load within the timeout period.")
    #
    # def click_radio_button(self):
    #     try:
    #         radio_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(CarAssignmentLocators.RADIO_BUTTON)  # Pass as a tuple
    #         )
    #         if radio_button.is_enabled():
    #             radio_button.click()
    #             print("Radio button clicked.")
    #     except TimeoutException:
    #         print("Radio button is not enabled, proceeding without clicking it.")
    #
    # def click_save_button(self):
    #     save_button = self.find_element(By.ID, "save_button")  # Replace with actual ID/XPath
    #     save_button.click()
    #     print("Save button clicked.")



    # def enter_search(self):
    #
    #     search_box = self.find_element(By.ID, "AssignCar")
    #     SelectCar = "Altima- "
    #     search_box.send_keys(SelectCar)
    #     self.find_element(By.XPATH,'//*[@ng-mouseenter="selectActive($index)"]').click()
    #     search_box.send_keys(Keys.RETURN)

    # def enter_search_box(self, search_term):
        # search_box = self.find_element(*CarAssignmentLocators.SELECT_CAR)
        # # Input the search term
        # search_box.send_keys(search_term)
        #
        # # Increase wait time and check for suggestions
        # try:
        #     suggestion_list = WebDriverWait(self.driver, 20).until(
        #         # EC.visibility_of_all_elements_located((By.XPATH, "//ul/li[contains(@class, 'ng-scope')]"))
        #         EC.visibility_of_all_elements_located((By.XPATH, "//ul/li[contains(@class, 'ng-scope')]"))
        #     )
        #
        #     print(f"Number of suggestions found: {len(suggestion_list)}")
        #
        #     # Iterate through the suggestions
        #     for suggestion_name in suggestion_list:
        #         suggestion_value = suggestion_name.text
        #         print(f"Suggestion: {suggestion_value}")
        #
        #         # Check if the suggestion exactly matches the search term
        #         # if suggestion_value.strip() == "Picanto- - 2018 - PC- 52556A - White - Black A - DD01 - Altima":
        #         #     suggestion_name.click()
        #         #     break
        #
        #         if "PC- 52556A" in suggestion_value:
        #             suggestion_name.click()
        #             break
        #
        #         elif suggestion_value.strip() == "Picanto- - 2018 - PC- 52556A - White - Black A -  - ":
        #             suggestion_name.click()
        #             break
        #
        #         # Check if the suggestion contains the search term
        #         elif "not" in suggestion_value.lower():
        #             suggestion_name.click()
        #             break
        #     else:
        #         print("No matching suggestion found.")
        #
        # except TimeoutException:
        #     print("Suggestions did not load within the timeout period.")
        #     # Optionally, log the page source for debugging
        #     print("Page source for debugging:")
        #     print(self.driver.page_source)

    def enter_search(self, search_term):
        search_box = self.find_element(By.ID, "AssignCar")
        search_box.send_keys(search_term)

        try:
            # Wait for suggestions to appear
            suggestion_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//ul/li[contains(@class, 'ng-scope')]"))
            )

            for attempt in range(3):  # Retry up to 3 times
                try:
                    for suggestion in suggestion_list:
                        if search_term in suggestion.text:
                            print(f"Selected car: {suggestion.text}")
                            suggestion.click()
                            return True  # Successfully selected a car
                except StaleElementReferenceException:
                    print(f"Stale element, retrying... (Attempt {attempt + 1})")
                    time.sleep(1)
                    suggestion_list = self.driver.find_elements(By.XPATH, "//ul/li[contains(@class, 'ng-scope')]")

        except TimeoutException:
            print("Suggestions did not load within the timeout period.")

        return False  # No car selected

    def click_radio_button(self):
        try:
            # Wait until the radio button is visible and enabled
            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CarAssignmentLocators.RADIO_BUTTON)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", radio_button)  # Ensure it's in view
            radio_button.click()
            print("Radio button clicked.")
        except TimeoutException:
            print("Radio button is not clickable, proceeding without clicking it.")

    def click_save_button(self):
        try:
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CarAssignmentLocators.SAVE_BUTTON)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", save_button)
            save_button.click()
            print("Save button clicked.")
        except TimeoutException:
            print("Save button not found or not clickable.")

    def assign_car(self, search_term):
        if self.enter_search(search_term):  # Proceed only if a car was selected
            try:
                # Re-locate radio button to avoid stale element issues
                radio_button = WebDriverWait(self.driver, 5).until(
                    # EC.presence_of_element_located(CarAssignmentLocators.RADIO_BUTTON)
                    EC.element_to_be_clickable(CarAssignmentLocators.RADIO_BUTTON)
                )
                # self.driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                if radio_button.is_enabled():
                    radio_button.click()
                    print("Radio button clicked.")
                else:
                    print("Radio button is disabled, skipping...")
            except TimeoutException:
                print("Radio button not found, skipping...")

        # Always attempt to click save
        self.click_save_button()

    def enter_driver_id(self, driver_id):
                self.select_by_value(*CarAssignmentLocators.DRIVER_ID_SELECT, driver_id)

    def enter_aggrement_no(self, aggrement_no):
        rental_agreement=self.find_element(*CarAssignmentLocators.RENTAL_AGGREMENT)
        rental_agreement.send_keys(aggrement_no)

    # def click_radio_button(self):
    #     # Ensure `driver` is accessed via `self.driver` if you're using it in a class
    #     radio_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(CarAssignmentLocators.RADIO_BUTTON)  # Pass as a tuple
    #     )
    #     radio_button.click()

    # def click_save_button(self):
    #     save_button=self.find_element(*CarAssignmentLocators.SAVE_BUTTON)
    #     save_button.click()

    # def assign_car(self, search_term):
    #     self.enter_search(search_term)
    #     time.sleep(10)  # Wait for results
    #     self.click_radio_button()  # Check and click radio button if enabled
    #     time.sleep(10)
    #     self.click_save_button()  # Click save button

    # def assign_car(self, search_term):
    #     if self.enter_search(search_term):  # Proceed only if a car was selected
    #         self.click_radio_button()  # Click radio button if enabled
    #     self.click_save_button()  # Always attempt to click save

# ------------------------------------------------
#
#
# def click_radio_button(self):
#     try:
#         # Wait for the radio button to be visible
#         radio_button = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(CarAssignmentLocators.RADIO_BUTTON)  # Ensure the element exists
#         )
#
#         # Check if the radio button is enabled
#         if radio_button.is_enabled():
#             print(radio_button.is_enabled())
#             print("Radio button is enabled, clicking it.")
#             radio_button.click()
#             radio_button.is_enabled()
#         else:
#             print("Radio button is disabled, skipping click.")
#
#     # except Exception as e:
#     #     print(f"Error while clicking radio button: {str(e)}")
#
#     finally:
#         # Click the save button regardless of radio button state
#         self.click_save_button()
#
#
# def click_save_button(self):
#     try:
#         # Wait for the save button to be visible and clickable
#         save_button = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(CarAssignmentLocators.SAVE_BUTTON)
#         )
#         print("Clicking the save button.")
#         save_button.click()
#
#     except Exception as e:
#         print(f"Error while clicking save button: {str(e)}")





