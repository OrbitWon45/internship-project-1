from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class SigninPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a.login-button')


    def open_signin_page(self):
        self.open_url('sign-in')

    def signin(self):
        self.input_text('4softwaretesting1@gmail.com', *self.EMAIL_FIELD)
        self.input_text('Bekywon1!', *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BUTTON)

