from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Firefox()
driver.get('http://127.0.0.1/index.php')
driver.maximize_window()
