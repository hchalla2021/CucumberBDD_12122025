from behave import given, when, then, step
from selenium import webdriver
from pages.loginpage import LoginPage
import threading


@given('Launch both Chrome and Edge browsers in parallel')
def launch_both_browsers(context):
    context.drivers = {}
    context.login_pages = {}
    
    def launch_chrome():
        context.drivers['chrome'] = webdriver.Chrome()
        context.drivers['chrome'].maximize_window()
    
    def launch_edge():
        context.drivers['edge'] = webdriver.Edge()
        context.drivers['edge'].maximize_window()
    
    # Launch both browsers in parallel using threads
    chrome_thread = threading.Thread(target=launch_chrome)
    edge_thread = threading.Thread(target=launch_edge)
    
    chrome_thread.start()
    edge_thread.start()
    
    chrome_thread.join()
    edge_thread.join()


@when('Open the https://www.facebook.com/ website in both browsers')
def open_facebook_website_both(context):
    def open_in_chrome():
        context.drivers['chrome'].get("https://www.facebook.com/")
        context.login_pages['chrome'] = LoginPage(context.drivers['chrome'])
    
    def open_in_edge():
        context.drivers['edge'].get("https://www.facebook.com/")
        context.login_pages['edge'] = LoginPage(context.drivers['edge'])
    
    chrome_thread = threading.Thread(target=open_in_chrome)
    edge_thread = threading.Thread(target=open_in_edge)
    
    chrome_thread.start()
    edge_thread.start()
    
    chrome_thread.join()
    edge_thread.join()


@then('the login application has been opened successfully in both browsers')
def verify_login_page_opened_both(context):
    assert context.login_pages['chrome'].is_logibPage_loaded(), "Chrome: Login page did not load successfully"
    assert context.login_pages['edge'].is_logibPage_loaded(), "Edge: Login page did not load successfully"


@step('Provide the username "{username}" and password "{password}" in both browsers')
def provide_credentials_both(context, username, password):
    def enter_in_chrome():
        context.login_pages['chrome'].enter_username(username)
        context.login_pages['chrome'].enter_password(password)
    
    def enter_in_edge():
        context.login_pages['edge'].enter_username(username)
        context.login_pages['edge'].enter_password(password)
    
    chrome_thread = threading.Thread(target=enter_in_chrome)
    edge_thread = threading.Thread(target=enter_in_edge)
    
    chrome_thread.start()
    edge_thread.start()
    
    chrome_thread.join()
    edge_thread.join()


@step('Click on the login button in both browsers')
def click_login_button_both(context):
    def click_in_chrome():
        context.login_pages['chrome'].click_login()
    
    def click_in_edge():
        context.login_pages['edge'].click_login()
    
    chrome_thread = threading.Thread(target=click_in_chrome)
    edge_thread = threading.Thread(target=click_in_edge)
    
    chrome_thread.start()
    edge_thread.start()
    
    chrome_thread.join()
    edge_thread.join()


@then('User should be logged in successfully in both browsers')
def verify_login_success_both(context):
    assert context.drivers['chrome'].current_url != "https://www.facebook.com/", "Chrome: Login did not succeed"
    assert context.drivers['edge'].current_url != "https://www.facebook.com/", "Edge: Login did not succeed"


@then('Close both browsers')
def close_both_browsers(context):
    def close_chrome():
        context.drivers['chrome'].quit()
    
    def close_edge():
        context.drivers['edge'].quit()
    
    chrome_thread = threading.Thread(target=close_chrome)
    edge_thread = threading.Thread(target=close_edge)
    
    chrome_thread.start()
    edge_thread.start()
    
    chrome_thread.join()
    edge_thread.join()
