import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class UsingUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:/Users/nesto/Downloads/chromedriver_win32/chromedriver.exe')
        # Abrir el ejecutable sin el path

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.python.org')
        about_botton = driver.find_element_by_link_text('About')
        sleep(3)
        about_botton.click()
        sleep(3)
        # Hacer click en un elemento

        search_bar = driver.find_element_by_id('id-search-field')
        search_bar.click()
        search_bar.send_keys(input())  # Ingresar texto 😀
        search_bar.send_keys(Keys)

    def tearDown(self):
        print('Browser is about to close...')
        sleep(10)
        # return super().tearDown()


if __name__ == "__main__":
    unittest.main()
