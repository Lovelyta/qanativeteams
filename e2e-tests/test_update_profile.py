import os
from locators.locators import Locators, URL
from utils.helper_functions import generate_random_email


class TestProfileUpdate:
    """
     A class for testing the user profile update functionality
    """
    email = generate_random_email(
        domain='yopmail.com',
        prefix='test_nativeteam+', length=3
        )

    def test_user_profile_update(self, browser_fixture):
        """
        Test case checks user profile update functionality by performing
        these actions:

        1. Logs into the application using credentials
        2. Navigates to the profile settings and updates the birth_date
        3. Verifies that the profile update is successful
        4. Navigates to the email settings and adds a new email address
        5. Verifies that the new email address is added successfully
        :param browser_fixture: a page object representing the browser page
        :return: None
        """
        try:
            page = browser_fixture
            page.get_by_role("banner").get_by_role(
                Locators.link,
                name=Locators.log_in
                ).click()
            assert page.url == "https://app.nativeteams.com/login"

            page.get_by_label(Locators.email).click()
            page.get_by_label(Locators.email).fill(os.getenv("EMAIL"))
            page.get_by_label(Locators.password).click()
            page.get_by_label(Locators.password).fill(os.getenv("PASSWORD"))
            page.get_by_role(Locators.button, name="Login").click()
            page.get_by_role(
                Locators.button, name=Locators.user_icon_name
                ).click()
            page.get_by_role(Locators.menu_item, name=Locators.profile).click()
            if page.locator(Locators.holiday_modal):
                page.locator(Locators.holiday_close_btn).click()

            page.locator(Locators.calendar_path).click()
            page.locator(Locators.calendar_path).fill('01/07/1991')
            page.locator(Locators.calendar_path).click()
            page.wait_for_timeout(8000)
            page.get_by_role(Locators.button, name=Locators.save_edits).click()
            page.wait_for_timeout(5000)
            success_added = page.locator(Locators.edit_success_msg)
            try:
                assert success_added.inner_text() == Locators.edit_success_txt
            except AssertionError:
                raise AssertionError(
                    "Profile update success message did not "
                    "match the expected text."
                    )

            assert page.url == URL.profile
            page.wait_for_timeout(3000)
            page.locator(Locators.email_section_path).click()

            assert page.url == URL.email_section
            page.locator(Locators.add_email_address).click()
            new_email = self.email
            page.get_by_role(Locators.text_box, name=Locators.type_here)
            page.get_by_role(Locators.text_box, name=Locators.type_here). \
                fill(new_email)
            page.locator(Locators.add_email_add_button).click()
            email_added = page.locator(Locators.email_added_msg)
            try:
                assert email_added.inner_text() == Locators.email_added_txt
            except AssertionError:
                raise AssertionError(
                    "Email added success message did not "
                    "match the expected text."
                    )
            page.reload()
            generated_email = page.locator(Locators.new_added_email_path)
            assert new_email == generated_email.inner_text()
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
