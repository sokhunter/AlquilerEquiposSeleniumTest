import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from AlquilerEquipos.helpers.auth_helper import *
from AlquilerEquipos.helpers.rent_helper import *

class Rent(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\FirefoxTests\geckodriver-v0.26.0-win64\geckodriver.exe")
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
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='FirefoxTests/reports'))