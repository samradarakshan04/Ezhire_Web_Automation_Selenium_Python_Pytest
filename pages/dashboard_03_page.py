
from object_repository.dashboard_locators import DashboardLocators
from pages.base_01_page import BasePage

class DashboardPage(BasePage):

    def navigate_to_booking(self, booking_id):
        self.driver.get(f'https://www.ezhire.me/erp/#/booking/{booking_id}')

    def enter_vendor(self, vendor_id):
        self.select_by_value(*DashboardLocators.VENDOR_ID, vendor_id)

    def click_submit(self):
        self.find_element(*DashboardLocators.SUBMIT_BUTTON).click()

    def assign_vendor(self, vendor_id):
        self.enter_vendor(vendor_id)  # Pass vendor_id here
        self.click_submit()



