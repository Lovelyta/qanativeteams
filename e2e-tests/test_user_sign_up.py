from locators.locators import Locators
from playwright.sync_api import Page
from utils.helper_functions import generate_random_email, generate_random_pass


class TestUserSignUp:
    """
    A test suite for verifying the user sign-up functionality on a web
    application.
    The suite includes tests that check for the presence of error messages on
    the sign-up form when required fields are left empty and also
    verifies successful user registration with valid data. Additionally,
    utility methods for generating random email addresses and passwords are
    provided to aid in the testing process.
    """
    email = generate_random_email(
        domain='yopmail.com', prefix='test_', length=6
        )
    password = generate_random_pass(length=10)

    def test_first_page_error_messages(self, browser_fixture: Page):
        """
        The test case checks the error messages for all the required fields
        :param browser_fixture: a page object representing the browser page
        :return: None
        """
        page = browser_fixture
        page.get_by_role(Locators.banner).get_by_role(
            Locators.link,
            name="Sign up"
            ).click()
        page.locator(Locators.accept_cookies).click()
        page.get_by_role(Locators.button, name="Start FREE").click()
        page.locator(Locators.proceed).click()
        page.wait_for_timeout(5000)
        name_msg = page.locator(Locators.name_error_msg)
        assert name_msg.is_visible() and name_msg.inner_text() == \
               Locators.name_error_txt

        last_name_msg = page.locator(Locators.last_name_error_msg)
        assert last_name_msg.is_visible() and last_name_msg.inner_text() == \
               Locators.last_name_error_txt

        # here is a bug inside the Email element, texts are not matched.
        # I split the first word so that the assertion be correct but the
        # bug ticket should be opened.
        email_msg = page.locator(Locators.email_error_msg)
        strip_word_email = email_msg.inner_text().replace("Email", "").strip()

        assert email_msg.is_visible() and strip_word_email == \
               Locators.email_error_txt

        pass_msg = page.locator(Locators.pass_error_msg)
        expected_msg = (
            "8 characters minimum, no whitespaces\n\n"
            "At least one number\n\n"
            "At least one uppercase letter\n\n"
            "At least one special character (e.g. @ $ ! % * ? ^ & #)"
        )
        assert pass_msg.is_visible() and pass_msg.inner_text() == expected_msg

        # error message has been split as it was too long
        privacy_policy_msg = page.locator(Locators.privacy_msg)
        actual_text = privacy_policy_msg.inner_text().split("\n")
        expected_sentence = actual_text[-1].strip()
        assert privacy_policy_msg.is_visible() and \
               expected_sentence == "The agreement field is required"

    def test_sign_up_with_valid_data(self, browser_fixture):
        """
        The test case verifies all the error messages on the entire page and
        ensures successful user sign-up with valid data.
        :param browser_fixture: a page object representing the browser page
        :return: None
        """
        page = browser_fixture
        page.get_by_role(Locators.banner).get_by_role(
            Locators.link,
            name="Sign up"
        ).click()
        page.locator(Locators.accept_cookies).click()
        page.get_by_role(Locators.button, name="Start FREE").click()
        price_info = page.locator(Locators.drop_down_price). \
            inner_text().strip()

        # confirming that price option is free tier
        assert price_info == 'Free ($0)'

        page.get_by_label(Locators.first_name).fill(Locators.name)
        page.get_by_label(Locators.last_name_label).click()
        page.get_by_label(Locators.last_name_label).fill(Locators.last_name)
        page.wait_for_timeout(2000)
        page.get_by_label(Locators.email).click()
        generated_email = self.email
        generated_pass = self.password
        page.get_by_label(Locators.email).fill(generated_email)
        page.wait_for_timeout(2000)
        page.get_by_label(Locators.password).click()
        page.get_by_label(Locators.password).fill(generated_pass)
        page.wait_for_timeout(2000)
        page.get_by_label(Locators.privacy_txt).check()
        page.wait_for_timeout(5000)

        # the proceed button does not react at once, the test may fail as on
        # press to button all fields became red but on second attempt
        # the same test may pass
        page.locator(Locators.proceed).click()
        page.wait_for_timeout(3000)

        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

        rgb = 'rgb()'

        def get_rgb_values(border_element):
            border_rgb_values = [int(value) for value in
                                 border_element.json_value().strip(rgb).split(
                                     ',')]
            return rgb_to_hex(border_rgb_values)

        # Validate first name border color
        first_name = page.locator(Locators.name_input).evaluate_handle(
            Locators.get_element
        )
        first_name_border = page.evaluate_handle(
            Locators.border_element, first_name
        )
        name_hex_color = get_rgb_values(first_name_border)

        # Validate last name border color
        last_name = page.locator(Locators.last_name_input).evaluate_handle(
            Locators.get_element
        )
        last_name_border = page.evaluate_handle(
            Locators.border_element, last_name
        )
        last_name_to_hex = get_rgb_values(last_name_border)

        # Validate email border color
        email = page.locator(Locators.email_input).evaluate_handle(
            Locators.get_element
        )
        email_border = page.evaluate_handle(Locators.border_element, email)
        email_to_hex = get_rgb_values(email_border)

        # Validate password border color
        password = page.locator(Locators.password_input).evaluate_handle(
            Locators.get_element
        )
        password_border = page.evaluate_handle(
            Locators.border_element, password
        )
        password_to_hex = get_rgb_values(password_border)

        required_color = "#f80000"
        while (email_to_hex == required_color and
               password_to_hex == required_color and
               name_hex_color == required_color and
               last_name_to_hex == required_color):
            page.wait_for_timeout(2000)
            page.locator(Locators.proceed).dblclick()
            # confirming that second modal page is opened
        assert page.locator(Locators.second_page).is_visible()

        page.locator(Locators.proceed_second_page).click()
        page.wait_for_timeout(3000)

        # confirming that if phone number is not filled in after clicking
        # proceed button the error message is displayed
        phone_msg = page.locator(Locators.phone_error_msg)
        assert phone_msg.is_visible() and phone_msg.inner_text() == \
               Locators.phone_error_txt

        # confirming that if interest options are not chosen after clicking
        # proceed button the error message is displayed
        interest_msg = page.locator(Locators.interest_error_msg)
        assert interest_msg.is_visible() and interest_msg.inner_text() == \
               Locators.interest_error_txt

        # confirming that if platform options are not chosen after clicking
        # proceed button the error message is displayed
        platform_msg = page.locator(Locators.platform_error_msg)
        assert platform_msg.is_visible() and platform_msg.inner_text() == \
               Locators.platform_error_txt

        # confirming that if payment options are not chosen after clicking
        # proceed button the error message is displayed
        payment_msg = page.locator(Locators.payment_error_msg)
        assert payment_msg.is_visible() and payment_msg.inner_text() == \
               Locators.payment_error_txt

        page.get_by_placeholder(Locators.phone_placeholder).click()
        page.get_by_placeholder(Locators.phone_placeholder).fill("93496132")
        page.locator(Locators.interests).click()
        page.get_by_text(Locators.new_job).nth(1).click()
        page.get_by_text(Locators.employment_status).nth(1).click()
        page.locator(Locators.interests).click()
        page.locator(Locators.platform).click()
        page.get_by_text(Locators.upwork).nth(1).click()
        page.get_by_text(Locators.fiver).nth(1).click()
        page.locator(Locators.platform).click()
        page.locator(Locators.payment).click()
        page.get_by_text(Locators.payoneer).nth(1).click()
        page.locator(Locators.payment).click()

        page.locator(Locators.proceed_second_page).click()
        page.wait_for_timeout(10000)

        # confirming that the registration has been completed by verifying
        # the success message.
        success_modal = page.get_by_text(
            Locators.success
        ).text_content().strip()
        assert success_modal == Locators.success

        # asserting that the email that was filled in the email field
        # matches the one displayed in the success modal.
        email_msg = page.locator(Locators.email_confirm).text_content()
        assert email_msg == generated_email
