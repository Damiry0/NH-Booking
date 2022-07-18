from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


driver.get('https://www.nowehoryzonty.pl/r/')
# assert 'NH' in driver.title

film_list=["Vortex","Tama","Pokot"]

for film in film_list:
    element = driver.find_element("xpath", f"//div[text()='{film}']")
    if element.is_displayed():
        element.click()
    else:
        driver.refresh()





