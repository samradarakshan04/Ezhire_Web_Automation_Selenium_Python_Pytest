from object_repository.car_assignment_locators import CarAssignmentLocators
from pages.car_04_asssinment_page import CarAssignmentPage
from selenium.webdriver.support.ui import Select
import time

from pages.charge2_06_car_and_driver_assign_page import CarAndDriverAssignPage


class TestCarAndDriverPage:

    def test_car_and_driver_assignment(self, login2,booking_id):
        driver = login2
        car_and_driver_assignment_page = CarAndDriverAssignPage(driver)
        # Perform the allocation and input current time
        car_and_driver_assignment_page.charge2_click()
        car_and_driver_assignment_page.car_and_driver_assign_button()
        time.sleep(10)
        car_and_driver_assignment_page.car_assign_list()
        time.sleep(10)
        car_and_driver_assignment_page.driver_assign_list()
        time.sleep(10)
        car_and_driver_assignment_page.submit_button()
        time.sleep(10)
        car_and_driver_assignment_page.is_alert_present()
        time.sleep(10)
        car_and_driver_assignment_page.handle_alert()
        time.sleep(10)