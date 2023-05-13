from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: int):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        sleep(1)

    def login_digi(self, roll: int, sch: int):
        self.browser.maximize_window()
        self.add_input(by=By.ID, value="rroll", text=roll)
        self.add_input(by=By.ID, value="sch_input", text=sch)
        self.click_button(by=By.ID, value="submit")
        self.browser.get_screenshot_as_file(f"Results\{roll}.png")


if __name__ == "__main__":
    rolls = 14639000  # Change it to your School roll number Starting
    school_number = 25749
    while rolls < 14639050:  # Change this value to exppected roll number end Value
        browser = Browser("Driver\chromedriver.exe")
        browser.open_page("https://results.digilocker.gov.in/8qRDvcKXII.html")
        sleep(1)
        browser.login_digi(rolls, school_number)
        sleep(1)
        rolls = rolls + 1
        browser.close_browser()
