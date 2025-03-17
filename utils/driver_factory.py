# # utils/driver_factory.py
# from selenium import webdriver
# from utils.config import BROWSER
#
# def get_driver():
#     if BROWSER == "chrome":
#         options = webdriver.ChromeOptions()
#         driver = webdriver.Chrome(options=options)
#     elif BROWSER == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError(f"Unsupported browser: {BROWSER}")
#     driver.maximize_window()
#     return driver
