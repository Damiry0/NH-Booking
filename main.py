import selenium
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import schedule
import time


def reservation():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('https://www.nowehoryzonty.pl/r/')

    txt_file = open("reservation_list.txt", "r")
    file_content = txt_file.read()
    film_list = file_content.split("\n")
    print(film_list)
    txt_file.close()
    film_not_found_list = []

    for film in film_list:
        try:
            driver.find_element("xpath", f"//div[text()='{film}']").click()
        except selenium.common.exceptions.NoSuchElementException:
            print(f"Film {film} not found.")
            film_not_found_list.append(film)
    return schedule.CancelJob


schedule.every().day.at("08:30:00").do(reservation)

while True:
    schedule.run_pending()
    time.sleep(0.5)
