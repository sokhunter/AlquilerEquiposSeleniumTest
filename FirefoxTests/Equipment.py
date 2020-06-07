import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from AlquilerEquipos.helpers.auth_helper import *
from AlquilerEquipos.helpers.equipment_helper import *

class Equipment(unittest.TestCase):
	def setUp(self):		
		self.driver = webdriver.Firefox(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\FirefoxTests\geckodriver-v0.26.0-win64\geckodriver.exe")
		self.driver.get("https://webapplicationalquilerequipos20200602204639.azurewebsites.net/Account/login?ReturnUrl=%2f")
		self.driver.implicitly_wait(5)
		authHelper = Auth_helper(self.driver)
		authHelper.login('knox', 'admin')

	def test_list_equipment(self):
		driver = self.driver
		equipmentHelper = Equipment_helper(driver)
		equipmentHelper.list()
		equipmentHelper.validate_list_title()

	def test_add_equipment(self):
		driver = self.driver
		equipmentHelper = Equipment_helper(driver)
		equipmentHelper.list()
		driver.find_element_by_id("Equipo_btn_Registrar").click()
		driver.implicitly_wait(5)
		equipmentHelper.save('EQ_010', 'tabla', 'Equipo de Aventura', 10, '1')
		equipmentHelper.validate_list_title()

	def test_edit_equipment(self):
		driver = self.driver
		equipmentHelper = Equipment_helper(driver)
		equipmentHelper.list()
		driver.find_element_by_id("Equipo_btn_Editar").click()
		driver.implicitly_wait(5)
		equipmentHelper.save('EQ_010', 'tabla', 'Equipo de Aventura', 20, '2')
		equipmentHelper.validate_list_title()
		

	def test_delete_equipment(self):
		driver = self.driver
		equipmentHelper = Equipment_helper(driver)
		equipmentHelper.list()
		driver.find_element_by_id("Equipo_btn_Eliminar").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Equipo_btn_Eliminar").click()
		driver.implicitly_wait(5)
		equipmentHelper.validate_list_title()

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='FirefoxTests/reports'))