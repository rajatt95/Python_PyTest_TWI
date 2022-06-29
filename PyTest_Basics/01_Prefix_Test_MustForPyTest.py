# /**
# * @author Rajat Verma
# * https://www.linkedin.com/in/rajat-v-3b0685128/
# * https://github.com/rajatt95
# * https://rajatt95.github.io/
# * https://github.com/stars/rajatt95/lists/udemy-testing-world-infotech
# *
# * Course: Step by Step Rest API Testing using Python + Pytest +Allure (https://www.udemy.com/course/api-testing-python/)
# * Tutor: Testing World Infotech (https://www.udemy.com/user/technology-world/)
# */
#
# /***************************************************/

# https://stackoverflow.com/questions/35998992/py-test-command-not-found-but-library-is-installed

# PyTest will not consider this method as a Test case
# Because method name is not starting with a prefix as 'test'
def tc_login_UI():
    print('This is tc_login_UI......')


def test_login_API():
    print('This is test_login_API......')

