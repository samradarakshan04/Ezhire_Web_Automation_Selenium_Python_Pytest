# from object_repository.car_assignment_locators import CarAssignmentLocators
# from pages.car_05_asssinment_page import CarAssignmentPage
# from selenium.webdriver.support.ui import Select
# import time
#
# from pages.charge2_07_car_and_driver_assign_page import CarAndDriverAssignPage
#
#
# class TestCarAndDriverPage:
#
#     def test_car_and_driver_assignment(self, login2,booking_id,dispatch_vendor):
#         driver = login2
#         car_and_driver_assignment_page = CarAndDriverAssignPage(driver)
#         # Perform the allocation and input current time
#         car_and_driver_assignment_page.charge2_click()
#         car_and_driver_assignment_page.car_and_driver_assign_button()
#         time.sleep(10)
#         car_and_driver_assignment_page.car_assign_list()
#         time.sleep(10)
#         car_and_driver_assignment_page.driver_assign_list()
#         time.sleep(10)
#         car_and_driver_assignment_page.submit_button()
#         time.sleep(10)