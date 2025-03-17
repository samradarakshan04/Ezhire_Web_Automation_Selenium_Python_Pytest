from object_repository.logout_locators import LogoutLocators
from pages.base_01_page import BasePage
from selenium.webdriver.common.by import By

from pages.dashboard_03_page import DashboardPage


class LogoutPage(BasePage):

    def logout(self):
        self.find_element(*LogoutLocators.LOGOUT_BUTTON).click()


