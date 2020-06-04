import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Auth(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Edge(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\edgedriver_win64/msedgedriver.exe")
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
		self.driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Login | Alquiler Equipos")

	def test_login(self):
		driver = self.driver
		
		driver.find_element_by_id("Login_txt_NameUser").send_keys("admin")
		driver.find_element_by_id("Login_txt_Password").send_keys("admin")
		driver.find_element_by_id("Login_btn_Login").click()
		self.driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Alquiler Equipos")

	def test_profile(self):
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Perfil").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Usuario_btn_Editar").click()
		name = "Stefany"
		userName = "knox"
		password = "admin"
		driver.find_element_by_id("Usuario_txt_Nombre").send_keys(name)
		driver.find_element_by_id("Usuario_txt_NombreUsuario").send_keys(userName)
		driver.find_element_by_id("Usuario_txt_Clave").send_keys()
		driver.find_element_by_id("Usuario_btn_Guardar").click()

		finalName = driver.find_element_by_xpath("//*[@id='content']/div/div/dl/dd[1]")
		finalUserName = driver.find_element_by_xpath("//*[@id='content']/div/div/dl/dd[2]")
		self.assertTrue(name == finalName and userName == finalUserName)

	def test_logout(self):
		driver = self.driver
		driver.find_element_by_id("userDropdown").click()
		driver.find_element_by_id("Layout_btn_Logout").click()
		self.assertEqual(driver.title, "Login | Alquiler Equipos")

	def tearDown(self):
		# time.sleep(5);
		self.driver.close()

if __name__ == '__main__':
	unittest.main()