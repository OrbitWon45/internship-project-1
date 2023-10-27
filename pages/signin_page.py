from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class SigninPage(Page):

    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BTN = (By.XPATH, '//a[@class="login-button w-button"]')
    MOBILE_MENU_BTN = (By.CSS_SELECTOR, 'a.menu-button-wrapper.w-inline-block')

    def email_field(self):
        text = '4softwaretesting1@gmail.com'
        self.wait_to_input_text(text, *self.EMAIL_FIELD)

    def password_field(self):
        text = 'Bekywon1!'
        self.wait_to_input_text(text, *self.PASSWORD_FIELD)

    def login(self):
        password = (By.ID, 'field')
        self.wait.until(EC.text_to_be_present_in_element_value(password, 'Bekywon1!'),
                        message=f'no text in {password}')
        self.click(*self.CONTINUE_BTN)










