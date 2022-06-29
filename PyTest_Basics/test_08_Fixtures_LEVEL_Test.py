# /**
# * @author Rajat Verma
# * https://www.linkedin.com/in/rajat-v-3b0685128/
# * https://github.com/rajatt95
# * https://rajatt95.github.io/
# * https://github.com/stars/rajatt95/lists/udemy-testing-world-infotech
# * https://github.com/rajatt95/Python_PyTest_TWI
# *
# * Course: Step by Step Rest API Testing using Python + Pytest +Allure (https://www.udemy.com/course/api-testing-python/)
# * Tutor: Testing World Infotech (https://www.udemy.com/user/technology-world/)
# */
#
# /***************************************************/
import pytest


@pytest.fixture()
def fixture_code():
    # Executes before the test case
    print("\n---------------------------")
    print("Start the session before every test case")  # Example -> Selenium - Open Browser
    print("---------------------------")
    # yield -> It is used to segregate the code for before and after
    yield
    # Executes after the test case
    print("\n---------------------------")
    print("Stop the session after every test case")  # Example -> Selenium - Close Browser
    print("---------------------------")


def test_registration_API(fixture_code):
    print('This is test_registration_API......')


def test_login_API(fixture_code):
    print('This is test_login_API......')