from behave import given, when, then


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.support_page.switch_to_new_window()


@then('Verify support page opens')
def verify_support_page_opens(context):
    context.app.support_page.verify_support_page_opens()


@then('Close page')
def close_page(context):
    context.app.support_page.close_page()