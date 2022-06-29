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


@pytest.mark.Regression
@pytest.mark.Smoke
@pytest.mark.UserDefined_TopPriority
def test_registration_API():
    print('This is test_logout_API......')


@pytest.mark.Regression
@pytest.mark.Sanity
def test_login_API():
    print('This is test_login_API......')


@pytest.mark.Regression
def test_logout_API():
    print('This is test_logout_API......')
