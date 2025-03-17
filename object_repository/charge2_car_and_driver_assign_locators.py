
from selenium.webdriver.common.by import By

class CarAndDriverAssignLocators:

    CHARGE_2_BUTTON=(By.XPATH,"//a[@class='ng-binding' and text()='Charge 2']")
    CAR_AND_DRIVER=(By.XPATH,"//button[@ng-click = 'carDriverAssign()']")
    # Car_ASSIGNMENT_RADIO=(By.XPATH,"//table[@id='caredittab']//tr[td[1][text()='KIA Picanto']]//td[last()]//input[@type='radio' and @value='218'][not(@disabled)]")
    Car_ASSIGNMENT_RADIO=(By.XPATH,"//table[@id='caredittab']//tr[td[1][text()='Nissan Sunny']]//td[last()]//input[@type='radio' and @value='10489'][not (@disabled)]")
    DRIVER_ASSIGNMENT_RADIO=(By.XPATH, "//table[@id='caredittab']//tr[td[1][text()='abdullahvender vender']]//td[last()]//input[@type='radio' and @ng-value='402943'][not(@disabled)]")
    SUBMIT_BUTTON=(By.XPATH,"//button[@class='back_but' and text()='Submit']")

