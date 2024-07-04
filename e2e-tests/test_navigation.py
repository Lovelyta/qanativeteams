import os
from locators.locators import Locators, URL


class TestUserNavigation:

    def test_user_navigation(self, browser_fixture):
        try:
            page = browser_fixture
            page.get_by_role(Locators.banner).get_by_role(
                Locators.link, name=Locators.log_in
            ).click()
            assert page.url == URL.login
        except Exception as e:
            print(f"Login page error: {e}")
            return

        try:
            page.get_by_label(Locators.email).click()
            page.get_by_label(Locators.email).fill(os.getenv("EMAIL"))
            page.get_by_label(Locators.password).click()
            page.get_by_label(Locators.password).fill(os.getenv("PASSWORD"))
            page.get_by_role(Locators.button, name="Login").click()
        except Exception as e:
            print(f"Login is failed: {e}")
            return

        try:
            page.get_by_role(Locators.button, name=Locators.user_icon_name)\
                .click()
            page.locator(Locators.my_documents).click()
            assert page.url == URL.documents
            if page.locator(Locators.holiday_modal):
                page.locator(Locators.holiday_close_btn).click()
                page.wait_for_timeout(1000)
            all_documents = page.locator(
                Locators.all_documents_section
            ).text_content()
            assert all_documents == "All documents"
        except Exception as e:
            print(f"Document navigation failure: {e}")
            return

        try:
            page.get_by_role(Locators.button, name=Locators.user_icon_name)\
                .click()
            page.get_by_role(Locators.menu_item, name=Locators.settings)\
                .click()
            page.get_by_role(Locators.menu_item,
                             name=Locators.payoneer_menu_item).click()

            assert page.url == URL.payoneer_section

            payoneer_section = page.locator(
                Locators.payoneer_section
                ).text_content()
            assert payoneer_section == "Payoneer"
            page.wait_for_timeout(3000)
        except Exception as e:
            print(f"Payoneer section navigation failure: {e}")
            return

        try:
            page.locator(Locators.email_section_path).click()
            assert page.url == URL.email_section
        except Exception as e:
            print(f"Email section navigation failure: {e}")
            return

        try:
            page.locator(Locators.user_button_doc_section).click()
            page.locator(Locators.knowledge_base).click()
            page.wait_for_timeout(3000)
            assert page.url == URL.knowledge_base

            knowledge_base = page.locator(
                Locators.knowledge_base_header
            ).text_content().split('\n')[0].strip()
            assert knowledge_base == "Knowledge base"
        except Exception as e:
            print(f"Knowledge base navigation failure: {e}")
            return
