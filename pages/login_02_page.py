
from object_repository.login_locators import LoginLocators
from pages.base_01_page import BasePage
from pages.dashboard_03_page import DashboardPage


class LoginPage(BasePage):

    def __init__(self, driver):
        """Initialize the LoginPage with the driver and locate elements."""
        super().__init__(driver)

    def enter_username(self, email):
        username_field = self.find_element(*LoginLocators.USERNAME_FIELD)
        username_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.find_element(*LoginLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()

    def login(self, email, password):
        """ Perform login action by sending keys to fields and clicking the login button. """
        self.enter_username(email)
        self.enter_password(password)
        self.click_login()
        # return DashboardPage(self.driver)  # Return the DashboardPage after login

