from selenium.webdriver.common.by import By

class RentalStartLocators:

   RENTAL_START_BUTTON = (By.ID, "strtl")
   OUT_KM = (By.ID, "book__out_odometer")
   OUT_FUEL_LEVEL = (By.XPATH, "//*[@ng-model='bk.out_fuel_level']")
   CITY_CODE = (By.XPATH, "//*[@ng-model='bk.selected_city']")
   PLATE_CODE = (By.XPATH,"//*[@ng-model='selectedOptionP']")
   PLATE_NUMBER = (By.ID, "book__plate_number")
   # OUT_IMAGE = (By.XPATH ,"//input[@class='ng-isolate-scope']")
   OUT_IMAGE = (By.ID, "file")
   SAVE_BUTTON = (By.ID, "rental_start_save_button")