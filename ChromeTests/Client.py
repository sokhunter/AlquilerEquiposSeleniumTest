import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from AlquilerEquipos.helpers.auth_helper import *
from AlquilerEquipos.helpers.client_helper import *

class Client(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\ChromeTests\chromedriver_win32\chromedriver.exe")
		self.driver.get("https://webapplicationalquilerequipos20200602204639.azurewebsites.net/Account/login?ReturnUrl=%2f")
		self.driver.implicitly_wait(5)
		authHelper = Auth_helper(self.driver)
		authHelper.login('knox', 'admin')

	def test_list_clients(self):
		driver = self.driver
		clientHelper = Client_helper(driver)
		clientHelper.list()
		clientHelper.validate_list_title()

	def test_add_client(self):
		driver = self.driver
		clientHelper = Client_helper(driver)
		clientHelper.list()
		driver.find_element_by_id("Cliente_btn_Registrar").click()
		driver.implicitly_wait(5)
		clientHelper.save('danny phantom', '1', '12345678')
		clientHelper.validate_list_title()

	def test_edit_client(self):
		driver = self.driver
		clientHelper = Client_helper(driver)
		clientHelper.list()
		driver.find_element_by_id("Cliente_btn_Editar").click()
		driver.implicitly_wait(5)
		clientHelper.save('Leonardo Ramos Ticona', '3', '72331234')
		clientHelper.validate_list_title()
		

	def test_delete_client(self):
		driver = self.driver
		clientHelper = Client_helper(driver)
		clientHelper.list()
		driver.find_element_by_id("Cliente_btn_Eliminar").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Cliente_btn_Eliminar").click()
		driver.implicitly_wait(5)
		clientHelper.validate_list_title()

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='ChromeTests/reports'))