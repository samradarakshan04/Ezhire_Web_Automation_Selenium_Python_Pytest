
from object_repository.rental_start_locators import RentalStartLocators
from pages.base_01_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class RentalStartPage(BasePage):

    def __init__(self, driver):
            self.driver = driver  # Store the WebDriver instance

    def rental_start_button(self):
        rental_start_button=(self.find_element(*RentalStartLocators.RENTAL_START_BUTTON))
        rental_start_button.click()

    def out_km_button(self):
        out_km_button = (self.find_element(*RentalStartLocators.OUT_KM))
        out_km_button.send_keys('1')

    def out_fuel_level_button(self,fuel):
        out_fuel_level = (self.select_by_value(*RentalStartLocators.OUT_FUEL_LEVEL,fuel))
        # out_fuel_level.send_keys('1')

    def city_code_button(self,city):
        city_code = (self.select_by_value(*RentalStartLocators.CITY_CODE,city))
        # city_code.send_keys('O')

    def plate_code_button(self,plate):
        plate_code = (self.select_by_value(*RentalStartLocators.PLATE_CODE,plate))
        # plate_code.send_keys('0')
    #
    def plate_number_button(self):
        plate_number = (self.find_element(*RentalStartLocators.PLATE_NUMBER))
        plate_number.send_keys('123')

    def upload_out_image(self):
        # Wait for the file input element to be present
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RentalStartLocators.OUT_IMAGE)  # Locator should be unpacked if it's a tuple
        )
        file_path = "D:\\car-pictures\\imagejpeg.jpg"  # Update to an existing file path
        file_input.send_keys(file_path)  # Upload the file

    def rental_start_save_button(self):
        rental_start = self.find_element(*RentalStartLocators.SAVE_BUTTON)
        rental_start.click()

