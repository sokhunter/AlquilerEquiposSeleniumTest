import unittest
from selenium import webdriver
from helpers.auth_helper import *
from helpers.equipment_helper import *

class Equipment(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Edge(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\edgedriver_win64/msedgedriver.exe")
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
		equipmentHelper.save('danny phantom', '12345678')
		equipmentHelper.validate_list_title()

	def test_edit_equipment(self):
		driver = self.driver
		equipmentHelper = Equipment_helper(driver)
		equipmentHelper.list()
		driver.find_element_by_id("Equipo_btn_Editar").click()
		driver.implicitly_wait(5)
		equipmentHelper.save('Leonardo Ramos Ticona', '72331234')
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
	unittest.main()