
import time
import pytest
from selenium import webdriver
from pages.login_02_page import LoginPage
from pages.dashboard_03_page import DashboardPage
from utils.config import URL
# URL = "https://www.ezhire.me/erp/#/login"

@pytest.fixture(scope='session')
def driver():
    """Start a single browser session for all tests."""
    driver = webdriver.Chrome()  # Replace with your desired driver
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def login(driver):
    """Perform login once per test session."""
    username = 'asif@ezhire.life'
    password = 'Nawaz@123'
    # Open the login page
    driver.get(URL)
    # Initialize the LoginPage object
    login_page = LoginPage(driver)
    # Perform the login action
    login_page.login(username, password)
    print("User logged in")
    yield driver  # Return the logged-in driver for use in tests

def pytest_addoption(parser):
    """Define all command-line options at once."""
    parser.addoption("--booking_id", action="store", default="12345", help="Booking ID for testing")
    # parser.addoption("--farhan_vendor", action="store", default=None, help="Farhan Vendor for testing")
    # parser.addoption("--dispatch_vendor", action="store", default=None, help="Dispatch Vendor for testing")

@pytest.fixture(scope="session")
def booking_id(request):
    return request.config.getoption("--booking_id")

# @pytest.fixture(scope="session")
# def farhan_vendor(request):
#     return request.config.getoption("--farhan_vendor")
#
# @pytest.fixture(scope="session")
# def dispatch_vendor(request):
#     return request.config.getoption("--dispatch_vendor")

# def pytest_addoption(parser):
#     parser.addoption("--booking_id", action="store", default="12345", help="Booking ID for testing")
#
# @pytest.fixture(scope="session")
# def booking_id(request):
#     return request.config.getoption("--booking_id")
#
# def pytest_addoption(parser):
#     parser.addoption("--farhan_vendor", action="store", default="5", help="Farhan Vendor for testing")
#
# @pytest.fixture(scope="session")
# def farhan_vendor(request):
#     return request.config.getoption("--farhan_vendor")
#
# def pytest_addoption(parser):
#     parser.addoption("--dispatch_vendor", action="store", default="5", help="Dispatch Vendor for testing")
#
# @pytest.fixture(scope="session")
# def dispatch_vendor(request):
#     return request.config.getoption("--dispatch_vendor")

@pytest.fixture(scope='session')
def login2(driver,booking_id):
# def login2(driver):
    """Perform login once per test session and navigate to booking."""
    username = 'farhan_vendor@gmail.com'
    password = 'Khi@1234567'

    # username1 = 'dispatchcenterw0001@ezhire.life'
    # password2 = 'Khi@12345678'

    # Open the login page
    driver.get(URL)

    # Initialize the LoginPage object
    login_page = LoginPage(driver)
    # Perform the login action
    login_page.login(username, password)

    dashboard_page = DashboardPage(driver)
    time.sleep(10)
    dashboard_page.navigate_to_booking(booking_id)  # Use the dynamic booking ID
    time.sleep(10)

    # login_page.is_alert_present()
    # # car_assignment_page.handle_alert()
    # login_page.handle_alert()


    # Use the booking ID from the command-line argument
    # booking_id = "170120"

    print(f"User logged in and navigated to booking {booking_id}")
    yield driver  # Return the logged-in driver for use in tests
# @pytest.fixture(scope='session')
# def login2(driver, booking_id):
# # def login2(driver):
#     """Perform login once per test session and navigate to booking."""
#     username = 'farhan_vendor@gmail.com'
#     password = 'Khi@1234567'
#
#     # username1 = 'dispatchcenterw0001@ezhire.life'
#     # password2 = 'Khi@12345678'
#
#     # Open the login page
#     driver.get(URL)
#
#     # Initialize the LoginPage object
#     login_page = LoginPage(driver)
#
#     # Perform the login action
#     login_page.login(username, password)
#
#     # Use the booking ID from the command-line argument
#     # booking_id = "170120"
#     dashboard_page = DashboardPage(driver)
#     time.sleep(10)
#     dashboard_page.navigate_to_booking(booking_id)  # Use the dynamic booking ID
#     time.sleep(10)
#     print(f"User logged in and navigated to booking {booking_id}")
#     yield driver  # Return the logged-in driver for use in tests

# @pytest.fixture(scope='session')
# def login3(driver, booking_id):
# # def login2(driver):
#     """Perform login once per test session and navigate to booking."""
#     # username = 'farhan_vendor@gmail.com'
#     # password = 'Khi@1234567'
#
#     username1 = 'dispatchcenterw0001@ezhire.life'
#     password1 = 'Khi@12345678'
#
#     # Open the login page
#     driver.get(URL)
#
#     # Initialize the LoginPage object
#     login_page = LoginPage(driver)
#
#     # Perform the login action
#     login_page.login(username1, password1)
#
#     # Use the booking ID from the command-line argument
#     # booking_id = "170120"
#     dashboard_page = DashboardPage(driver)
#     time.sleep(10)
#     dashboard_page.navigate_to_booking(booking_id)  # Use the dynamic booking ID
#     time.sleep(10)
#     print(f"User logged in and navigated to booking {booking_id}")
#     yield driver  # Return the logged-in driver for use in tests

# @pytest.fixture(scope='session')
# def login2(driver):
#     """Perform login once per test session."""
#     username = 'farhan_vendor@gmail.com'
#     password = 'Khi@1234567'
#     # Open the login page
#     driver.get(URL)
#     # Initialize the LoginPage object
#     login_page = LoginPage(driver)
#     # Perform the login action
#     login_page.login(username, password)
#     booking_id = "170109"  # Replace with actual booking ID
#     dashboard_page = DashboardPage(driver)
#     time.sleep(10)
#     dashboard_page.navigate_to_booking(booking_id)
#     time.sleep(10)
#     print("User logged in")
#     yield driver  # Return the logged-in driver for use in tests