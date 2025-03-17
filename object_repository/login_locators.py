
from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_FIELD = (By.XPATH, "//form[@id='my_captcha_form']//input[@id='login__username']")
    PASSWORD_FIELD = (By.XPATH, "//form[@id='my_captcha_form']//input[@id='login__password']")
    LOGIN_BUTTON = (By.XPATH, "//form[@id='my_captcha_form']//button[@type='submit']")

