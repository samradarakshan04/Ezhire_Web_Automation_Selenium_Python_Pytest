# # # # fixtures.py
# # # import time
# # #
# # # import pytest
# # #
# # # from pages.login_02_page import LoginPage
# # # from utils.config import URL
# # #
# # #
# # # # In your fixtures.py or test setup file
# # # # URL = "https://www.google.com/"  # Define a valid URL
# # # #
# # # # @pytest.fixture(scope='class')
# # # # def setup(driver):
# # # #     print("Creating a driver instance")
# # # #     driver.get(URL)  # This should work if URL is a valid string
# # # #     yield driver
# # # #     driver.quit()
# # # #     print("Closing the driver instance")
# # #
# # # URL = "https://www.ezhire.me/erp/#/login"
# # # @pytest.fixture(scope='class')
# # # def setup(driver):
# # #     username = 'asif@ezhire.life'
# # #     password = 'Nawaz@123'
# # #     # print(f"Setting up for test: {method.__name__}")  # Prints the name of the test method
# # #     driver.get(URL)
# # #     # Create the LoginPage2 object
# # #     login_page = LoginPage(driver)
# # # #
# # #     # Call the setup method to initialize elements with the driver
# # #     login_page.set(driver)
# # #     time.sleep(10)
# # #     # Perform the login action
# # #     login_page.login(username, password)
# # #     print("user logged in")
# # #     # yield
# # #     # print("Not login")
# # #             # # print(f"Setting up for test: {method.__name__}")  # Prints the name of the test method
# # #             # driver.get(URL)
# # #             # # Create the LoginPage2 object
# # #             # login_page = LoginPage(driver)
# # #
# #
# import time
# import pytest
# from pages.login_02_page import LoginPage
# from utils.config import URL
#
# URL = "https://www.ezhire.me/erp/#/login"
#
#
# @pytest.fixture(scope='class')
# def setup (driver):
#     """Fixture to log in a user."""
#     username = 'asif@ezhire.life'
#     password = 'Nawaz@123'
#
#     # Open the login page
#     driver.get(URL)
#
#     # Initialize the LoginPage object
#     login_page = LoginPage(driver)
#     # login_page.set(driver)  # Initialize elements
#
#     # Perform the login action
#     time.sleep(5)  # Wait for the page to load
#     login_page.login(username, password)
#     print("User logged in")
#
#     # Pass control back to the test
#     yield driver
#     print("")
#     print(f"{username} is logged in")
#     # driver.quit()
#
# # import time
# # import pytest
# # from pages.login_02_page import LoginPage
# # from utils.config import URL
# #
# # URL = "https://www.ezhire.me/erp/#/login"
# #
# #
# # @pytest.fixture(scope='class')
# # def setup(driver):
# #     """Fixture to log in a user."""
# #     username = 'asif@ezhire.life'
# #     password = 'Nawaz@123'
# #
# #     # Open the login page
# #     driver.get(URL)
# #
# #     # Initialize the LoginPage object
# #     login_page = LoginPage(driver)
# #     login_page.set(driver)  # Initialize elements on the page
# #
# #     # Perform the login action
# #     login_page.login(username, password)
# #
# #     # Add sleep if needed (to handle dynamic page loading), though you might want to replace it with explicit waits
# #     time.sleep(5)  # Wait for the page to load after login (could be replaced by WebDriverWait)
# #
# #     print("User logged in")
#
#     # Yield the driver to the test
#     # yield driver
#     #
#     # # Tearing down the setup after test execution
#     # print("Tearing down setup")
#     # driver.quit()
