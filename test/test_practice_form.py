from demoqa_tests.pages.registration_form import RegistrationPage
from demoqa_tests.data.users import User
import allure


def test_fill_registration_form():
    registration_page = RegistrationPage()
    user = User(
        last_name='Петров',
        first_name='Иван',
        email='petrov@gmail.com',
        gender='Male',
        phone='9001010800',
        month_of_birth='0',
        year_of_birth='1998',
        day_of_birth='08',
        subject='Chemistry',
        hobby='Sports',
        picture='img.png',
        address='12 street',
        state='Haryana',
        city='Karnal'

    )
    with allure.step('Открываем страницу регистрации'):
        registration_page.open()
    with allure.step('Регистрируем пользователя'):
        registration_page.register_user(user)
    with allure.step('Проверяем регистрацию!!!'):
        registration_page.check_registration(user)
