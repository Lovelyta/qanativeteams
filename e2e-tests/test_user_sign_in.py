import os
import pytest
from locators.locators import Locators, URL


class TestUserSignIn:
    """
    A test suit for checking the user sign-in functionality
    """

    def test_user_sign_in_valid_data(self, browser_fixture):
        """
        Test case that checks user sign-in process with valid data by
        performing the following actions:
        1. Navigates to the login page
        2. Enters valid email and password
        3. Clicks the login button
        4. Verifies that the wallet balance is visible and displays
        the correct text

        :param browser_fixture: a page object representing the browser page
        :return: None
        """
        page = browser_fixture
        page.get_by_role(Locators.banner).get_by_role(
            Locators.link,
            name=Locators.log_in
            ).click()
        assert page.url == URL.login

        page.get_by_label(Locators.email).click()
        page.get_by_label(Locators.email).fill(os.getenv("EMAIL"))
        page.get_by_label(Locators.password).click()
        page.get_by_label(Locators.password).fill(os.getenv("PASSWORD"))
        page.get_by_role(Locators.button, name="Login").click()
        wallet_path = page.locator(Locators.wallet_balance_path)
        page.wait_for_timeout(6000)
        assert wallet_path.is_visible() and wallet_path.text_content().strip()\
               == "Primary wallet balance"

    @pytest.mark.parametrize(
        "password,expected_error", [
            ('', 'The Password field is required'),
            (
                    'password123@',
                    'Please provide valid email address and password.')

        ]
    )
    def test_user_sign_in_invalid_password(
            self, password, expected_error,
            browser_fixture
    ):
        """
        Test case that checks user sign-in process with invalid passwords by
        performing the following actions:
        1. Navigates to the login page
        2. Enters a valid email and an invalid password
        3. Clicks the login button
        4. Verifies that the appropriate error message is displayed

        :param password: password parameter
        :param expected_error: expected error message
        :param browser_fixture: a page object representing the browser page
        :return: None
        """
        page = browser_fixture
        page.get_by_role(Locators.banner).get_by_role(
            Locators.link,
            name=Locators.log_in
            ).click()
        assert page.url == URL.login

        page.get_by_label(Locators.email).click()
        page.get_by_label(Locators.email).fill(os.getenv("EMAIL"))
        page.get_by_label(Locators.password).click()
        page.get_by_label(Locators.password).fill(password)
        page.get_by_role(Locators.button, name="Login").click()
        password_error_msg = page.locator(Locators.pass_login_error_msg)
        page.wait_for_timeout(3000)
        assert password_error_msg.is_visible() and \
               password_error_msg.inner_text() == expected_error

    @pytest.mark.parametrize(
        "email,expected_error", [
            ('', 'The Email field must be a valid email'),
            ('test_nativeteamyopmail.com',
             'The Email field must be a valid email'),
            ('test_nativeteam@yopmailcom',
             'The Email field must be a valid email')
        ]

    )
    def test_user_sign_in_invalid_email(
            self, email, expected_error,
            browser_fixture
    ):
        """
        Test case that checks user sign-in process with invalid emails by
        performing the following actions:
        1. Navigates to the login page
        2. Enters an invalid email and a valid password
        3. Clicks the login button
        4. Verifies that the appropriate error message is displayed

        :param email: invalid email parameters
        :param expected_error: expected error message
        :param browser_fixture: a page object representing the browser page
        :return: None
        """
        page = browser_fixture
        page.get_by_role(Locators.banner).get_by_role(
            Locators.link,
            name=Locators.log_in
            ).click()
        assert page.url == URL.login

        page.get_by_label(Locators.email).click()
        page.get_by_label(Locators.email).fill(email)
        page.get_by_label(Locators.password).click()
        page.get_by_label(Locators.password).fill(os.getenv("PASSWORD"))
        page.get_by_role(Locators.button, name="Login").click()
        email_error_msg = page.locator(Locators.email_error_msg_path)

        assert email_error_msg.is_visible() and \
               expected_error == email_error_msg.inner_text()
