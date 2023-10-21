from pages.registration_form import RegistrationPage
from tests_homework.users import User


def test_fill_registration_form():
    registration_page = RegistrationPage()
    user = User(
        last_name='Петров',
        first_name='Иван',
        email='petrov@gmail.com',
        gender='Male',
        phone='9001010800',
        day='08',
        month='0',
        year='1998',
        subject='Chemistry',
        hobby='Sports',
        picture='img.png',
        address='12 street',
        state='Haryana',
        city='Karnal'

    )
    registration_page.open()
    registration_page.register_user(user)
    registration_page.check_registration(user)
