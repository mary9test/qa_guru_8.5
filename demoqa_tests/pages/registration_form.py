from selene import browser, have
from demoqa_tests import resource
import allure


class RegistrationPage:
    with allure.step("Открываем форму регистрации"):
        def open(self):
            browser.open("/automation-practice-form")
            return self

    with allure.step("Регистрируем юзера"):
        def register_user(self, user):
            browser.element('#firstName').type(user.first_name)
            browser.element('#lastName').type(user.last_name)
            browser.element('#userEmail').type(user.email)
            browser.all('.custom-radio').element_by(have.text(user.gender)).click()
            browser.element('#userNumber').type(user.phone)
            browser.element('#dateOfBirthInput').click()
            browser.element('.react-datepicker__year-select').click().element(
                f'option[value="{user.year_of_birth}"]').click()
            browser.element('.react-datepicker__month-select').click().element(
                f'option[value="{user.month_of_birth}"]').click()
            browser.element(f'.react-datepicker__day--0{user.day_of_birth}').click()
            browser.element('#subjectsInput').type(user.subject).press_enter()
            browser.element("[for='hobbies-checkbox-1']").click()
            browser.element('#uploadPicture').type(resource.path(user.picture))
            browser.element('#currentAddress').type(user.address)
            browser.element('#state').click()
            browser.element('#react-select-3-input').type(user.state).press_enter()
            browser.element('#city').click()
            browser.element('#react-select-4-input').type(user.city).press_enter()
            browser.element('#submit').press_enter()

    with allure.step("Проверяем регистрацию"):
        def check_registration(self, user):
            full_name = f'{user.first_name} {user.last_name}'
            state_city = f'{user.state} {user.city}'
            date_of_birth = f'{user.day_of_birth} {user.month_of_birth.replace("0", "January")},{user.year_of_birth}'
            browser.element('.table').all('td').even.should(
                have.texts(
                    full_name,
                    user.email,
                    user.gender,
                    user.phone,
                    date_of_birth,
                    user.subject,
                    user.hobby,
                    user.picture,
                    user.address,
                    state_city
                ))
            return self
