from datetime import time
import time
import self
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from object_repository.charge2_car_and_driver_assign_locators import CarAndDriverAssignLocators
from pages.base_01_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CarAndDriverAssignPage(BasePage):
    def __init__(self, driver):
            self.driver = driver  # Store the WebDriver instance

    def charge2_click(self):
        charge2_button = self.find_element(*CarAndDriverAssignLocators.CHARGE_2_BUTTON)
        charge2_button.click()

    def car_and_driver_assign_button(self):
        car_and_driver_button = self.find_element(*CarAndDriverAssignLocators.CAR_AND_DRIVER)
        car_and_driver_button.click()

    def car_assign_list(self):
        try:
            # Wait for the radio buttons to be visible and clickable
            radio_buttons = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH,
                     "//table[@id='caredittab']//thead//tr//th[text()='Car Name']/ancestor::table//tbody//tr//td[last()]//input[@type='radio'][not(@disabled)]")
                )
            )
            self.driver.execute_script("""
                        window.scrollTo({left: 300, top: 300, behavior: 'smooth'});
                    """)
            if radio_buttons:
                # Get the first enabled radio button
                first_radio_button = radio_buttons[0]
                print("Is Enabled Before Click:", first_radio_button.is_enabled())
                print("Is Selected Before Click:", first_radio_button.is_selected())

                # Scroll the radio button into view before clicking
                # self.driver.execute_script("arguments[0].scrollIntoView(true);", first_radio_button)

                # Click the first radio button
                first_radio_button.click()
                first_radio_button.click()

                # Print the status after clicking
                print("Is Enabled After Click:", first_radio_button.is_enabled())
                print("Is Selected After Click:", first_radio_button.is_selected())

            else:
                print("No enabled radio buttons found.")

        except TimeoutException:
            print("Timeout waiting for the radio buttons to become clickable.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def driver_assign_list(self):
        try:
            # Wait for the radio buttons to be visible and clickable
            radio_buttons = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH,
                     "//table[@id='caredittab']//thead//tr//th[text()='Driver Name']/ancestor::table//tbody//tr//td[last()]//input[@type='radio'][not(@disabled)]")
                )
            )
            self.driver.execute_script("""
                        window.scrollTo({left: 300, top: 300, behavior: 'smooth'});
                    """)
            if radio_buttons:
                # Get the first enabled radio button
                first_radio_button = radio_buttons[0]
                print("Is Enabled Before Click:", first_radio_button.is_enabled())
                print("Is Selected Before Click:", first_radio_button.is_selected())

                # Scroll the radio button into view before clicking
                # self.driver.execute_script("arguments[0].scrollIntoView(true);", first_radio_button)

                # Click the first radio button
                first_radio_button.click()
                first_radio_button.click()

                # Print the status after clicking
                print("Is Enabled After Click:", first_radio_button.is_enabled())
                print("Is Selected After Click:", first_radio_button.is_selected())

            else:
                print("No enabled radio buttons found.")

        except TimeoutException:
            print("Timeout waiting for the radio buttons to become clickable.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def submit_button(self):
        self.driver.execute_script("""
                    window.scrollTo({left: 300, top: 300, behavior: 'smooth'});
                """)
        submit_button = self.find_element(*CarAndDriverAssignLocators.SUBMIT_BUTTON)
        submit_button.click()