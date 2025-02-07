
from selenium.webdriver.common.by import By

class CarAssignmentLocators:
    ALLOCATE_CAR_BUTTON = (By.ID, "alcCar")
    EXPECTED_TIME_INPUT = (By.XPATH, "//*[@ng-model = 'bk.expected_time']")
    # EXPECTED_TIME_INPUT = (By.XPATH, "//*[@id='expected_delivery_time' and @ng-model='bk.expected_time']")
    SELECT_CAR = (By.ID,"AssignCar")
    SEARCH_BOX=(By.XPATH, "//ul/li[contains(@class, 'ng-scope')]")
    DRIVER_ID_SELECT = (By.ID, "driver_id")
    RENTAL_AGGREMENT = (By.XPATH,"//*[@ng-model='bk.agreement_number']")
    RADIO_BUTTON = (By.XPATH,"//input[@type='radio' and @ng-model='bk.free_upgrade' and @value='1']")
    SAVE_BUTTON = (By.ID,"allocat_car_save_button")
