from behave import given, when, then


@then('Verify news page opens')
def verify_news_page_opens(context):
    context.app.news_page.verify_news_page_opens()