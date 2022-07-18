import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.nowehoryzonty.pl/r/')

txt_file = open("reservation_list.txt", "r")
file_content = txt_file.read()
film_list = file_content.split("\n")
print(film_list)
txt_file.close()

for film in film_list:
    try:
        driver.find_element("xpath", f"//div[text()='{film}']").click()
    except selenium.common.exceptions.NoSuchElementException:
        print(f"Film {film} not found.")






