from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class SupportPage(Page):

    CONTINUE_TO_CHAT_BUTTON = (By.ID, 'action-button')


    def verify_support_page_opens(self):
        self.wait_for_element_to_appear(*self.CONTINUE_TO_CHAT_BUTTON)

