from selenium import webdriver

import settings


class PostMessage:
	"""Only prders.mannet.ru"""
	def __init__(self):
		firefox_options = webdriver.FirefoxOptions()
		firefox_options.set_headless()
		self.driver = webdriver.Firefox(options=firefox_options)

	def auth(self):
		self.driver.get("http://orders.mannet.ru")
		elem = self.driver.find_element_by_name("user")
		elem.send_keys(settings.username)
		elem_pswd = self.driver.find_element_by_name("passwrd")
		elem_pswd.send_keys(settings.password)
		elem_but = self.driver.find_element_by_class_name("button_submit")
		elem_but.click()

	def new_message(self, message):
		urlorder = "http://orders.mannet.ru/index.php?topic=45188.0"
		self.driver.get(urlorder)
		elem = self.driver.find_element_by_class_name("button_strip_reply")
		elem.click()
		elemt = self.driver.find_element_by_name("message")
		elemt.send_keys(message)
		elemb = self.driver.find_elements_by_class_name("button_submit")
		for i, button in enumerate(elemb):
			if i == 1:
				button.click()

	def close(self):
		self.driver.close()


if __name__ == "__main__":
	mes = '''
	Switch: Riba
	S/N: SY201I3000078
	IP address: 172.16.23.255
	Port 9 is closed
	Port description: Clients
	VLAN ID: 1415
	VLAN NAME: admin
'''
	push = PostMessage()
	push.auth()
	push.new_message(mes)
	push.close()
