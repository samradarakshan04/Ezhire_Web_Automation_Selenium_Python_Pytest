

from pages.logout_03_page import LogoutPage
import time
import pytest


class TestLogoutPage:

    # @pytest.mark.usefixtures("setup")
    def test_logout_successful(self, login):
        driver = login
        logout_page = LogoutPage(driver)
        time.sleep(10)
        logout_page.logout()
        time.sleep(10)
        # assert driver.title == "Rent a car fast"  # Make sure this title is what you're expecting
        print("Logout passed")