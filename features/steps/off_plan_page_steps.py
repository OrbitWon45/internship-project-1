from behave import given, when, then
from time import sleep


@given('Open Off Plan page')
def open_off_plan_page(context):
    context.app.off_plan_page.open_off_plan_page()


@when('Click on settings option')
def click_on_settings(context):
    context.app.off_plan_page.click_on_settings()