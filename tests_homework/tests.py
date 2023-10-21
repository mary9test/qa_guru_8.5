from pages.registration_page import RegistrationForm


def test_fill_registration_form():
    registration_form = RegistrationForm()
    registration_form.open()
    registration_form.fill_first_name('Иван')
    registration_form.fill_last_name('Петров')
    registration_form.fill_email('petrov@gmail.com')
    registration_form.fill_gender()
    registration_form.fill_phone_number('9001010800')
    registration_form.fill_date_of_birth('0', '1998', '08')
    registration_form.fill_subject('Chemistry')
    registration_form.fill_hobby()
    registration_form.fill_picture()
    registration_form.fill_address('12 street')
    registration_form.fill_state('Haryana')
    registration_form.fill_city('Karnal')
    registration_form.check_result()
