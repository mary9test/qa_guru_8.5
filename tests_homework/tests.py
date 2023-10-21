import os.path
from selene import browser, have


class RegistrationForm:
    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_gender(self):
        browser.element("[for='gender-radio-1']").click()

    def fill_phone_number(self, phone):
        browser.element('#userNumber').type(phone)

    def fill_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('[class="react-datepicker__month-select"]').click().element(f'[value="{month}"]').click()
        browser.element('[class="react-datepicker__year-select"]').click().element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def fill_hobby(self):
        browser.element("[for='hobbies-checkbox-1']").click()

    def fill_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('img/img.png'))

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def fill_state(self, state):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(state).press_enter()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).press_enter()

    def check_result(self):
        browser.element('#submit').click()

        browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
            'Иван Петров',
            'petrov@gmail.com',
            'Male',
            '9001010800',
            '08 January,1998',
            'Chemistry',
            'Sports',
            'img.png',
            '12 street',
            'Haryana Karnal'))


def test_fill__registration_form():
    rf = RegistrationForm()
    rf.open()
    rf.fill_first_name('Иван')
    rf.fill_last_name('Петров')
    rf.fill_email('petrov@gmail.com')
    rf.fill_gender()
    rf.fill_phone_number('9001010800')
    rf.fill_date_of_birth('0', '1998', '08')
    rf.fill_subject('Chemistry')
    rf.fill_hobby()
    rf.fill_picture()
    rf.fill_address('12 street')
    rf.fill_state('Haryana')
    rf.fill_city('Karnal')
    rf.check_result()
