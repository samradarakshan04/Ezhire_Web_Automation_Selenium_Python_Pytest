import pytest

from object_repository.car_assignment_locators import CarAssignmentLocators
from pages.car_04_asssinment_page import CarAssignmentPage
from selenium.webdriver.support.ui import Select
import time

from pages.dashboard_03_page import DashboardPage


class TestCarAssignmentPage:

    # @pytest.mark.farhan
    # def test_car_assignment(self, login2,booking_id,farhan_vendor):

    def test_car_assignment(self, login2,booking_id):
        driver = login2
        car_assignment_page = CarAssignmentPage(driver)
        # Perform the allocation and input current time
        car_assignment_page.allocate_car_click()
        time.sleep(20)
        car_assignment_page.enter_expected_time()
        # car_assignment_page.enter_search_box("Picanto")
        # car_assignment_page.enter_search()
        # time.sleep(10)
        # car_assignment_page.assign_car("Altima- ")  # Replace with the actual car name
        # time.sleep(10)
        car_assignment_page.enter_driver_id('0')
        time.sleep(10)
        car_assignment_page.enter_aggrement_no('123')
        time.sleep(10)
        car_assignment_page.assign_car("Altima- ")  # Replace with the actual car name
        time.sleep(10)
        # car_assignment_page.click_radio_button()
        # time.sleep(10)
        # car_assignment_page.click_save_button()
        time.sleep(10)
        car_assignment_page.is_alert_present()
        time.sleep(10)
        car_assignment_page.handle_alert()
        time.sleep(10)


