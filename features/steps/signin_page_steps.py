from behave import given, when, then


@when('Signin')
def signin(context):
    context.app.signin_page.email_field()
    context.app.signin_page.password_field()
    context.app.signin_page.login()



