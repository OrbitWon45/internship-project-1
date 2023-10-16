from behave import given, when, then
from time import sleep

@given('Open Signin page')
def open_signin_page(context):
    context.app.signin_page.open_signin_page()

@when('Signin')
def signin(context):
    context.app.signin_page.signin()