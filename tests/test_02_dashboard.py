
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.dashboard_03_page import DashboardPage
from pages.login_02_page import LoginPage
from pages.logout_03_page import LogoutPage
from tests.conftest import driver


class TestDashboardPage:
    def test_assign_vendor(self, login, booking_id):
    # def test_assign_vendor(self,login,booking_id,farhan_vendor):
        driver = login
        dashboard_page = DashboardPage(driver)
        time.sleep(10)
        dashboard_page.navigate_to_booking(booking_id)
        time.sleep(10)
        time.sleep(10)
        # booking_page.assign_vendor("1")
        # dashboard_page.assign_vendor("farhan vendor1 [50%]")
        dashboard_page.assign_vendor("5")
        # dashboard_page.assign_vendor("farhan_vendor")
        time.sleep(10)
        # dashboard_page.click_confirm()
        time.sleep(10)
        dashboard_page.is_alert_present()
        dashboard_page.handle_alert()




    # def test_assign_vendor1(self,login,booking_id,dispatch_vendor):
    #     driver = login
    #     # booking_id = input("please Enter Booking ID: ")
    #     # booking_id = "170109"  # Replace with actual booking ID
    #     dashboard_page = DashboardPage(driver)
    #     time.sleep(10)
    #     dashboard_page.navigate_to_booking(booking_id)
    #     time.sleep(10)
    #     # booking_page.assign_vendor("5")
    #     # booking_page.assign_vendor("1")
    #     # dashboard_page.assign_vendor("farhan vendor1 [50%]")
    #     dashboard_page.assign_vendor("234555")
    #     time.sleep(10)

