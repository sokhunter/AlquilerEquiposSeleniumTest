import unittest
from selenium.webdriver.support.ui import Select

import time

class Equipment_helper():
	def __init__(self, driver):
		self.driver = driver

	def validate_list_title(self):
		my_assertion = unittest.TestCase('__init__')
		title = self.driver.find_element_by_xpath('//*[@id="content"]/div/h4/strong').text
		my_assertion.assertEqual(title, "Equipos")
	
	def list(self):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Equipo").click()
		driver.implicitly_wait(5)

	def save(self, code, name, description, price, status):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver

		txCode = driver.find_element_by_id("Equipo_txt_Codigo")
		txCode.clear()
		txCode.send_keys(code)

		txtName = driver.find_element_by_id("Equipo_txt_Nombre")
		txtName.clear()
		txtName.send_keys(name)

		txtDescription = driver.find_element_by_id("Equipo_txt_Descripcion")
		txtDescription.clear()
		txtDescription.send_keys(description)

		txtPrice = driver.find_element_by_id("Equipo_txt_Costo")
		txtPrice.clear()
		txtPrice.send_keys(price)

		cbxStade = Select(driver.find_element_by_id("Equipo_ddl_Estado"))
		cbxStade.select_by_value(status)

		driver.find_element_by_id("Equipo_btn_Guardar").click()
		driver.implicitly_wait(5)
		