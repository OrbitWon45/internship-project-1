from behave import given, when, then
from time import sleep

@when('Signin')
def signin(context):
    sleep(5)
    context.app.signin_page.email_field()
    context.app.signin_page.password_field()
    context.app.signin_page.login()



