import unittest
from selenium.webdriver.support.ui import Select

class Client_helper():
	def __init__(self, driver):
		self.driver = driver

	def validate_list_title(self):
		my_assertion = unittest.TestCase('__init__')
		title = self.driver.find_element_by_xpath('//*[@id="content"]/div/h4/strong').text
		my_assertion.assertEqual(title, "Clientes")
	
	def list(self):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Cliente").click()
		driver.implicitly_wait(5)

	def save(self, name, documentType, document):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver

		txtName = driver.find_element_by_id("Cliente_txt_Nombre")
		txtName.clear()
		txtName.send_keys(name)

		cbxDocument = Select(driver.find_element_by_id("Cliente_ddl_TipoDocumento"))
		cbxDocument.select_by_value(documentType)

		txtDocumento = driver.find_element_by_id("Cliente_txt_Documento")
		txtDocumento.clear()
		txtDocumento.send_keys(document)

		driver.find_element_by_id("Cliente_btn_Guardar").click()
		driver.implicitly_wait(5)

		