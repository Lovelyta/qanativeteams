import os


class Locators:
    accept_cookies = "//p[@id='acceptCookies']"
    start_free = "//button[normalize-space()='Start FREE']"
    drop_down_price = "//a[@id='dropdownMenuLink']"
    proceed = "//*[@id='btn-step-one-proceed']"
    proceed_second_page = "//*[@id='btn-step-two-register']"
    name_error_msg = "//*[@id='first_name-error']"
    name_input = "//input[@id='input-first-name']"
    name_error_txt = "The first name field is required"
    last_name_error_msg = "//span[@id='last_name-error']"
    last_name_input = "//input[@id='input-last-name']"
    last_name_error_txt = "The last name field is required"
    email_error_msg = "//form[@id='sign-up-step-one-form']//div[3]"
    pass_error_msg = "//*[@id='sign-up-step-one-form']/div[4]/div[2]/div"
    privacy_msg = "//*[@id='sign-up-step-one-form']/div[5]"
    privacy_txt = "I agree to the terms of"
    interests = "//*[@id='sign-up-step-two-form']/div[3]"
    interest_error_msg = "//span[@id='interests-error']"
    interest_error_txt = "The interests field is required."
    new_job = "New job opportunity"
    employment_status = "Employment status"
    platform = "//*[@id='sign-up-step-two-form']/div[4]"
    platform_error_msg = "//span[@id='platforms-error']"
    platform_error_txt = "The platforms field is required"
    upwork = "Upwork"
    fiver = "Fiver"
    payment = "//*[@id='sign-up-step-two-form']/div[5]"
    payment_error_msg = "//span[@id='payment_methods-error']"
    payment_error_txt = "The payment methods field is required"
    payoneer = "Payoneer"
    phone_error_msg = "//span[@id='phone-error']"
    phone_error_txt = "The phone field is required"
    phone_placeholder = "77123456"
    second_page = "//*[@id='checkout-step-two-modal']/div/div/div"
    email_confirm = "//*[@id='email-confirmation']"
    email_input = "//input[@id='input-email']"
    email_error_txt = "The email field is required"
    password_input = "//input[@id='input-password']"
    success = "You have successfully registered."
    first_name = "First name"
    last_name_label = "Last name"
    name = "Test"
    last_name = "User"
    email = "Email"
    password = "Password"
    log_in = "Log in"
    button = "button"
    banner = "banner"
    link = "link"
    menu_item = "menuitem"
    save_edits = 'Save Edits'
    text_box = 'textbox'
    type_here = "Type here"
    wallet_balance_path = "//div[@class='custom-selected-item']"
    pass_login_error_msg = "//*[@id='app']/div/div[" \
                           "1]/div/main/div/div/div/div[2]/div/div[2]/div[" \
                           "3]/span"
    calendar_path = "//input[@id='birth_date']"
    email_error_msg_path = "//*[@id='app']/div/div[" \
                           "1]/div/main/div/div/div/div[2]/div/div[1]/div[3]"
    email_section_path = "//span[normalize-space()='Emails']"
    add_email_address = "//*[@id='emails']/div/div/div/div/div[2]/button"
    add_email_add_button = "//*[@id='emails']/div/div/div/div/div[" \
                           "2]/div/div/button[1]"
    email_added_msg = "//span[normalize-space()='Email successfully added.']"
    email_added_txt = "Email successfully added."
    user_button = "//*[@id='app']/div/div[1]/div/div/div/div[1]/div/button[" \
                  "2]/span"
    edit_success_msg = "//*[@id='app']/div[1]/main/div/div[10]/div/div[1]/div"
    edit_success_txt = "General details successfully saved!"
    new_added_email_path = '//*[@id="emails"]/div/div/div/div/div[2]/ul/' \
                           'li[2]/p'
    my_documents = "//p[normalize-space()='My documents']"
    all_documents_section = "//button[normalize-space()='All documents']"
    settings = " Settings"
    profile = " Profile"
    payoneer_menu_item = "Payoneer integration"
    payoneer_section = "//span[normalize-space()='Payoneer']"
    knowledge_base = "//p[normalize-space()='Knowledge base']"
    knowledge_base_header = "//div[@class='main-page-header']"
    user_button_doc_section = "//*[@id='app']/div/main/div/div[1]/div[2]/div" \
                              "/div[1]/div/button[2]/span"
    border_element = '(element) => window.getComputedStyle(' \
                     'element).getPropertyValue("border-color")'
    get_element = '(element) => element'
    holiday_modal = "//*[@id='app']/div[3]/div/div/div/div/div"
    holiday_close_btn = "//*[@id='app']/div[3]/div/div/div/div/div/div/button"
    user_icon_name = ""


class URL:
    LOGIN_URL = os.getenv('LOGIN_URL')
    login = f'{LOGIN_URL}/login'
    documents = f'{LOGIN_URL}/documents'
    payoneer_section = f'{LOGIN_URL}/settings?tab=payoneer'
    email_section = f'{LOGIN_URL}/settings?tab=emails'
    knowledge_base = f'{LOGIN_URL}/knowledge-base'
    my_plan = f'{LOGIN_URL}/add-ons/my-plan'
    profile = f'{LOGIN_URL}settings?tab=profile'
