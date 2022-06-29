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


def test_registration_API():
    print('This is test_registration_API......')
    result_actual = "Hello"
    result_expected = "Hello !"
    # Should be equal
    assert result_actual == result_expected, "Message - Actual results are not matching with Expected results"  #
    # assert result_actual != result_expected  # Should not be equal


def test_login_API():
    print('This is test_login_API......')
    result_actual = "Hello"
    result_expected = "Hello"
    assert result_actual == result_expected


@pytest.mark.skip('Skipping this test case intentionally.........')
def test_logout_API():
    print('This is test_logout_API......')





