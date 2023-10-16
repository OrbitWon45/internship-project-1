from behave import given, when, then


@when('Click on settings option')
def click_on_settings(context):
    context.app.off_plan_page.click_on_settings()