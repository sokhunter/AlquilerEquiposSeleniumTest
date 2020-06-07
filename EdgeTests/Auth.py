import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from AlquilerEquipos.helpers.auth_helper import *

class Auth(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Edge(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\EdgeTests\edgedriver_win64\msedgedriver.exe")
		self.driver.get("https://webapplicationalquilerequipos20200602204639.azurewebsites.net/Account/login?ReturnUrl=%2f")
		self.driver.implicitly_wait(5)

	def test_signup(self):
		driver = self.driver
		driver.find_element_by_id("Login_btn_SignUp").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("SignUp_txt_Nombre").send_keys("Stefany Livaque")
		driver.find_element_by_id("SignUp_txt_NombreUsuario").send_keys("admin")
		driver.find_element_by_id("SignUp_txt_Clave").send_keys("admin")
		driver.find_element_by_id("SignUp_btn_Registrar").click()
		driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Login | Alquiler Equipos")

	def test_login(self):
		authHelper = Auth_helper(self.driver)
		authHelper.login('knox', 'admin')

	def test_profile(self):
		driver = self.driver
		authHelper = Auth_helper(driver)
		authHelper.login('knox', 'admin')
		driver.find_element_by_id("userDropdown").click()
		driver.find_element_by_id("Layout_btn_Perfil").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Usuario_btn_Editar").click()

		name = "Stefany"
		userName = "knox"
		password = "admin"

		txtName = driver.find_element_by_id("Usuario_txt_Nombre")
		txtUser = driver.find_element_by_id("Usuario_txt_NombreUsuario")
		txtPassword = driver.find_element_by_id("Usuario_txt_Clave")

		txtName.clear()
		txtName.send_keys(name)

		txtUser.clear()
		txtUser.send_keys(userName)

		txtPassword.clear()
		txtPassword.send_keys(password)

		driver.find_element_by_id("Usuario_btn_Guardar").click()
		driver.implicitly_wait(5)
		finalName = driver.find_element_by_xpath('//*[@id="content"]/div/div/dl/dd[1]').text
		finalUserName = driver.find_element_by_xpath('//*[@id="content"]/div/div/dl/dd[2]').text
		self.assertTrue(name == finalName and userName == finalUserName)

	def test_logout(self):
		driver = self.driver
		authHelper = Auth_helper(driver)
		authHelper.login('knox', 'admin')
		driver.find_element_by_id("userDropdown").click()
		driver.find_element_by_id("Layout_btn_Logout").click()
		self.assertEqual(driver.title, "Login | Alquiler Equipos")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='EdgeTests/reports'))