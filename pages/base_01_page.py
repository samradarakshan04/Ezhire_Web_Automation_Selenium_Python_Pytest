import os

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)  # Implicit wait for the entire session
        self.timeout = 10  # Default timeout for explicit waits

    # def find_element(self, by, value):
    #     """
    #     Finds an element using an explicit wait.
    #     """
    #     try:
    #         element = WebDriverWait(self.driver, self.timeout).until(
    #             EC.presence_of_element_located((by, value))
    #         )
    #         return element
    #     except TimeoutException:
    #         print(f"Error: Element {value} not found with locator {by} after waiting for {self.timeout} seconds.")
    #         raise

    def find_element(self, by, value):
        """
        Finds and returns an element after waiting for it to be present.
        """
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            print(f"Failed to find element with {by} and {value} after waiting for 10 seconds.")
            raise  # Re-raise the exception to fail the test

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """
        Waits for an element to be clickable before performing an action.
        Takes locator as a tuple (By.<method>, <value>).
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return element

    def wait_for_element_to_be_visible(self, locator, timeout=None):
        """
        Waits for an element to be visible before performing any action.
        Takes locator as a tuple (By.<method>, <value>).
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def wait_for_element_to_disappear(self, locator, timeout=None):
        """
        Waits for an element to disappear before proceeding.
        Takes locator as a tuple (By.<method>, <value>).
        """
        timeout = timeout or self.timeout
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def scroll_to_element(self, locator):
        """
        Scroll to an element in the view.
        Takes locator as a tuple (By.<method>, <value>).
        """
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def select_by_value(self, by, value, option_value):
        from selenium.webdriver.support.ui import Select
        element = self.find_element(by, value)
        Select(element).select_by_value(option_value)
        # Select(element).select_by_index(option_value)
        # Select(element).select_by_visible_text(option_value)

    # def click(self, by, value):
    #     element = self.find_element(by, value)
    #     element.click()

    # def take_screenshot(self, filename):
    #     self.driver.save_screenshot(filename)

    def take_screenshot(self, filename, path="screenshots"):
        """Captures a screenshot and saves it to the given file path."""
        # Ensure the specified folder exists
        if not os.path.exists(path):
            os.makedirs(path)  # Create the folder if it doesn't exist

        # Save screenshot with the provided filename
        screenshot_path = os.path.join(path, f"{filename}.png")  # Combine path and filename
        self.driver.save_screenshot(screenshot_path)  # Take screenshot

        # Output the screenshot path for confirmation
        print(f"Screenshot saved to: {screenshot_path}")

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
            return True
        except:
            return False

    def handle_alert(self):
        try:
            # Switch to the alert
            alert = Alert(self.driver)
            # Accept the alert (click on 'OK')
            alert.accept()
            print("Alert handled successfully.")
        except Exception as e:
            print(f"No alert found. Exception: {str(e)}")