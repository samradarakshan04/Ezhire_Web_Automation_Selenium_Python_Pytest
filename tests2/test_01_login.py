
class TestLoginPage:

    def test_login_successful(self,login):
        """Verify successful login."""
        driver = login  # The 'login' fixture provides the logged-in driver
        assert driver.title == "Rent a car fast", "Login failed"
        print("Login successful test passed")
        # print("Current URL after login:", driver.current_url)

    # def test_login_unsuccessful(self, driver):
    #     """Verify unsuccessful login attempt."""
    #     username = 'asif@ezhire.lif'
    #     password = 'Nawaz@12'
    #
    #     # Open the login page
    #     driver.get("https://www.ezhire.me/erp/#/login")
    #
    #     # Initialize the LoginPage object
    #     login_page = LoginPage(driver)
    #
    #     # Perform the login action with incorrect credentials
    #     login_page.login(username, password)
    #     assert driver.title != "Rent a car fast", "Login succeeded unexpectedly"
    #     print("Login unsuccessful test passed")
