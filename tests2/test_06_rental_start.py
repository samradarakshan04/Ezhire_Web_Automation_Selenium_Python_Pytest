import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.ui
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from datetime import datetime

from pages.dashboard_03_page import DashboardPage
from pages.rental_05_start_page import RentalStartPage
from tests2.conftest import login2


class TestRentalStartPage:

    def test_rental_start(self, login2,booking_id):
        driver = login2
        rental_start_page = RentalStartPage(driver)
        time.sleep(10)
        rental_start_page.rental_start_button()
        time.sleep(10)
        rental_start_page.out_km_button()
        time.sleep(10)
        rental_start_page.out_fuel_level_button('1')
        time.sleep(10)
        rental_start_page.city_code_button('0')
        time.sleep(10)
        rental_start_page.plate_code_button('0')
        time.sleep(10)
        rental_start_page.plate_number_button()
        time.sleep(10)
        rental_start_page.upload_out_image()
        time.sleep(10)
        rental_start_page.rental_start_save_button()
        time.sleep(10)
        rental_start_page.is_alert_present()
        rental_start_page.handle_alert()

          # def test_rental_start1(self, login3,booking_id,dispatch_vendor):
          #   driver = login2
          #   rental_start_page = RentalStartPage(driver)
          #   rental_start_page.rental_start_button()
          #   time.sleep(10)
          #   rental_start_page.out_km_button()
          #   time.sleep(10)
          #   rental_start_page.out_fuel_level_button('1')
          #   time.sleep(10)
          #   rental_start_page.city_code_button('0')
          #   time.sleep(10)
          #   rental_start_page.plate_code_button('0')
          #   time.sleep(10)
          #   rental_start_page.plate_number_button()
          #   time.sleep(10)
          #   rental_start_page.upload_out_image()
          #   time.sleep(10)
          #   rental_start_page.rental_start_save_button()
          #   time.sleep(10)






