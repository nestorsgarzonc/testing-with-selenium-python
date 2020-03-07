from selenium import webdriver

driver = webdriver.Chrome(executable_path = "./chromedriver")
driver.get("https://www.python.org")

driver.close()