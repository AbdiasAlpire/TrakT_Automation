from behave import given, when, then

from features.locators.DashboardLocators import username_text_locator
from features.pages.DashboardPage import DashboardPage
from features.pages.LoginPage import LoginPage
from utilities import ConfigReader

@given(u'I got navigated to trakt Login page')
def step_impl(context):
    login_page = LoginPage(context.driver)
    context.login_page = login_page

@when(u'I enter a valid Email')
def step_impl(context):
    login_page = LoginPage(context.driver)
    context.login_page = login_page
    login_page.enter_email(ConfigReader.read_configuration("Admin Account", "email"))

@when(u'I enter a a valid password')
def step_impl(context):
    login_page = LoginPage(context.driver)
    context.login_page = login_page
    login_page.enter_password(ConfigReader.read_configuration("Admin Account", "password"))

@when(u'I click on Sing in icon')
def step_impl(context):
    login_page = LoginPage(context.driver)
    context.login_page = login_page
    login_page.click_login()

@when(u'I click on Exit button')
def step_impl(context):
    pass

@then(u'I should be able to see my username on dashboard')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    username = dashboard_page.is_present(username_text_locator)
    dashboard_page.click_random_movie()
    assert username, True
