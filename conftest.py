# # # config/configuration.py
# # from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
# #
# # class DriverSetup:
# #     @staticmethod
# #     def get_driver():
# #         driver = webdriver.Chrome(ChromeDriverManager().install())
# #         driver.maximize_window()
# #         return driver
#
#
#
# #
# import pytest
# from selenium import webdriver
# # @pytest.fixture
# # @pytest.fixture(scope="function")
# # @pytest.fixture(scope="session")
# @pytest.fixture(scope="module")
# def driver():
#     # driver = webdriver.Chrome()
#     # driver.maximize_window()
#     # return driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     # return driver
#     yield driver
#     # driver.quit()
#     # Check that driver.quit() isn't being invoked somewhere else in your code
# # def teardown_method(self):
# #         # This might inadvertently close the browser
# #     self.driver.quit()
#
#
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver once for the whole module
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
# #     # No driver.quit(), so the browser stays open after all tests
# #     # You can manually quit the browser when tests are done, or leave it open
# #
# # def test_example_1(driver):
# #     driver.get("https://example.com")
# #     assert driver.title == "Example Domain"
# #
# # def test_example_2(driver):
# #     driver.get("https://example.com")
# #     assert driver.title == "Example Domain"
#
# # import pytest
# # from pages.login_01_page import LoginPage
# # from pages.dashboard_02_page import DashboardPage
# # from utils.config import USERNAME, PASSWORD, URL
# # from selenium import webdriver
# #
# #
# # # Define a fixture for WebDriver initialization
# # @pytest.fixture
# # def setup_driver():
# #     # Initialize WebDriver (you can change this to your desired browser, e.g., Chrome, Firefox)
# #     driver = webdriver.Chrome()  # Initialize the driver (assuming Chrome for this example)
# #
# #     # Provide the driver instance to the tests
# #     yield driver
# #
# #     # Teardown (close the driver after test is done)
# #     driver.quit()
# #
# #
# # # Define a fixture for initializing page objects before each test
# # @pytest.fixture
# # def login_page(setup_driver):
# #     # Initialize the LoginPage before each test
# #     login_page = LoginPage(setup_driver)
# #     return login_page
# #
# #
# # @pytest.fixture
# # def dashboard_page(setup_driver):
# #     # Initialize the DashboardPage before each test
# #     dashboard_page = DashboardPage(setup_driver)
# #     return dashboard_page
# #
# #
# # # Test login functionality
# # def test_login(login_page):
# #     # Use the login page fixture to log in
# #     login_page.login(USERNAME, PASSWORD)
# #     assert "Dashboard" in login_page.driver.title  # Check if the login was successful by verifying the title
# #
# #
# # # Test vendor assignment
# # def test_vendor_assignment(dashboard_page):
# #     # Navigate to the booking page
# #     booking_id = "169909"
# #     booking_page = dashboard_page.navigate_to_booking(booking_id)
# #
# #     # Assign a vendor on the BookingPage
# #     booking_page.assign_vendor("5")
# #
# #     # Add assertions as needed (e.g., check for success message)
# #     assert "Vendor Assigned" in dashboard_page.driver.page_source
#
# # @pytest.fixture
# # def setup_driver():
# #     driver = webdriver.Chrome()  # Setup WebDriver
# #     yield driver
# #     driver.quit()  # Teardown WebDriver
# #
# # @pytest.fixture
# # def login_page(setup_driver):
# #     return LoginPage(setup_driver)  # Setup LoginPage before each test
