import unittest

class Auth_helper():
	def __init__(self, driver):
		self.driver = driver
	
	def login(self, user, password):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		driver.find_element_by_id("Login_txt_NameUser").send_keys(user)
		driver.find_element_by_id("Login_txt_Password").send_keys(password)
		driver.find_element_by_id("Login_btn_Login").click()
		driver.implicitly_wait(5)
		my_assertion.assertEqual(driver.title, "Alquiler Equipos")