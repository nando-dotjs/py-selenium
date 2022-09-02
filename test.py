import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r'C:\Users\fpere\OneDrive\Documentos\chromedriver.exe')

driver.get("http://172.23.177.19:90")
elemento1 = driver.find_element(By.ID, 'user')
elemento1.clear()
elemento1.send_keys("root")
elemento2 = driver.find_element(By.NAME, 'pass')
elemento2.clear()
elemento2.send_keys("password")
driver.find_element(By.CLASS_NAME, "button").click()
time.sleep(2)
driver.get('http://172.23.177.19:90')

elemento3 = driver.find_element(By.NAME,'q')
elemento3.clear()
elemento3.send_keys('PRUEBA DEVOPS')
time.sleep(5)

driver.close()