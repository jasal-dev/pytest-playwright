import time

def test_login_with_correct_credentials(page):
    """Test user access with valid credentials
    """

    page.goto('https://www.saucedemo.com/')
    assert page.wait_for_selector('id=login-button', state='visible')

    page.fill('id=user-name', 'standard_user')
    page.fill('id=password', 'secret_sauce')
    page.click('id=login-button')

    assert page.wait_for_selector('id=inventory_container', state='visible')

def test_login_as_locked_user(page):
    """Test user access with locked account
    """

    page.goto('https://www.saucedemo.com/')
    assert page.wait_for_selector('id=login-button', state='visible')

    page.fill('id=user-name', 'locked_out_user')
    page.fill('id=password', 'secret_sauce')
    page.click('id=login-button')

    assert page.wait_for_selector('//*[@data-test="error"]', state='visible')

    