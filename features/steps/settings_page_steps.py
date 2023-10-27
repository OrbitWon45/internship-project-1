from behave import given, when, then


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.settings_page.get_current_window()


@when('Click on support option')
def click_on_support(context):
    context.app.settings_page.click_on_support()


@when('Click on news option')
def click_on_news_option(context):
    context.app.settings_page.click_on_news_option()


@when('Click on news option mobile')
def click_on_news_option_mobile(context):
    context.app.settings_page.click_on_news_option_mobile()



@then('Return to original window')
def return_to_original_window(context):
    context.app.settings_page.return_to_original_window(context.original_window)

