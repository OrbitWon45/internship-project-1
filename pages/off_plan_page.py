from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class OffPlanPage(Page):

    SETTINGS_BTN = (By.XPATH, '//a[@href="/settings"]//div[@class="menu-icon w-embed"]')

    def open_off_plan_page(self):
        self.open_url()
        sleep(5)

    def click_on_settings(self):
       self.wait_for_element_clickable_click(*self.SETTINGS_BTN)


