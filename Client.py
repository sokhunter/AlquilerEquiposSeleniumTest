import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Client(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Edge(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\edgedriver_win64/msedgedriver.exe")
		self.driver.get("https://webapplicationalquilerequipos20200602204639.azurewebsites.net/Account/login?ReturnUrl=%2f")
		self.driver.implicitly_wait(5)
		driver.find_element_by_id("Login_txt_NameUser").send_keys("knox")
		driver.find_element_by_id("Login_txt_Password").send_keys("admin")
		driver.find_element_by_id("Login_btn_Login").click()
		self.driver.implicitly_wait(5)

	def test_list_clients(self):
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Cliente").click()
		driver.implicitly_wait(5)
		title = driver.find_element_by_xpath('//*[@id="content"]/div/h4/strong').text
		self.assertEqual(title, "Clientes")

	def test_add_client(self):
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Cliente").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Cliente_btn_Registrar").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Cliente_txt_Nombre").send_keys("Emily Rojas")
		driver.find_element_by_id("Cliente_txt_Documento").send_keys("73829302")
		driver.find_element_by_id("Cliente_btn_Guardar").click()
		driver.implicitly_wait(5)
		title = driver.find_element_by_xpath('//*[@id="content"]/div/h4/strong').text
		self.assertEqual(title, "Clientes")

	def test_edit_client(self):
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Cliente").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Cliente_btn_Editar").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Cliente_txt_Nombre").send_keys("Emily Rojas")
		driver.find_element_by_id("Cliente_txt_Documento").send_keys("73829302")
		driver.find_element_by_id("Cliente_btn_Guardar").click()
		driver.implicitly_wait(5)
		title = driver.find_element_by_xpath('//*[@id="content"]/div/h4/strong').text
		self.assertEqual(title, "Clientes")

	def test_delete_client(self):
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Cliente").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Cliente_btn_Eliminar").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Cliente_btn_Eliminar").click()
		driver.implicitly_wait(5)
		title = driver.find_element_by_xpath('//*[@id="content"]/div/h4/strong').text
		self.assertEqual(title, "Clientes")

	def tearDown(self):
		# time.sleep(5);
		self.driver.close()

if __name__ == '__main__':
	unittest.main()