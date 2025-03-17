
import time
import pytest
from pages.dashboard_03_page import DashboardPage
from pages.login_02_page import LoginPage
from pages.logout_03_page import LogoutPage

class TestDashboardPage:

    def test_assign_vendor(self,login,booking_id):
        driver = login
        # booking_id = input("please Enter Booking ID: ")
        # booking_id = "170109"  # Replace with actual booking ID
        dashboard_page = DashboardPage(driver)
        time.sleep(10)
        dashboard_page.navigate_to_booking(booking_id)
        time.sleep(10)
        # booking_page.assign_vendor("5")
        # booking_page.assign_vendor("1")
        # dashboard_page.assign_vendor("farhan vendor1 [50%]")
        # dashboard_page.assign_vendor("234555")
        dashboard_page.assign_vendor("5")
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

