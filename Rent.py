import unittest
from selenium import webdriver
import HtmlTestRunner
from helpers.auth_helper import *
from helpers.rent_helper import *

class Rent(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Edge(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\edgedriver_win64/msedgedriver.exe")
		self.driver.get("https://webapplicationalquilerequipos20200602204639.azurewebsites.net/Account/login?ReturnUrl=%2f")
		self.driver.implicitly_wait(5)
		authHelper = Auth_helper(self.driver)
		authHelper.login('knox', 'admin')

	def test_list_rent(self):
		driver = self.driver
		rentHelper = Rent_helper(driver)
		rentHelper.list()
		rentHelper.validate_list_title()

	def test_add_rent(self):
		driver = self.driver
		rentHelper = Rent_helper(driver)
		rentHelper.list()
		driver.find_element_by_id("Alquiler_btn_Registrar").click()
		driver.implicitly_wait(5)
		rentHelper.save('4', '20/05/2020', ['2', '4'])
		rentHelper.validate_list_title()

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='reports'))