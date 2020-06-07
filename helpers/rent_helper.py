import unittest
from selenium.webdriver.support.ui import Select

class Rent_helper():
	def __init__(self, driver):
		self.driver = driver

	def validate_list_title(self):
		my_assertion = unittest.TestCase('__init__')
		title = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/h4/strong').text
		my_assertion.assertEqual(title, "Alquileres")
	
	def list(self):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		driver.find_element_by_id("Layout_btn_Alquiler").click()
		driver.implicitly_wait(5)

	def save(self, client, date, equipments):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver

		cbxClient = Select(driver.find_element_by_id("Alquiler_ddl_Cliente"))
		cbxClient.select_by_value(client)

		txtName = driver.find_element_by_id("Alquiler_dat_FechaOrder")
		txtName.clear()
		txtName.send_keys(date)

		for equipment in equipments:
			cbxEquipment = Select(driver.find_element_by_id("Alquiler_ddl_Producto"))
			cbxEquipment.select_by_value(equipment)
			driver.find_element_by_id("addToList").click()

		driver.find_element_by_id("Alquiler_btn_Guardar").click()
		driver.implicitly_wait(5)
		