Homework008

The tests.py file is a collection of test cases for a Django web application that implements a poll system. The test cases are designed to ensure that the application behaves as expected under different scenarios.

The tests are defined using Django's built-in testing framework, the TestCase class. The tests verify various aspects of the application, including:
    The behavior of the question index view when there are no questions, only past questions, only future questions, both past and future questions, or multiple past questions
    The behavior of the was_published_recently() method of the Question model, which is used to determine if a question was published recently
    The behavior of the detail view for a question, which displays a form for voting on the question's choices

Requirements

    Django 2.1 or higher
    Python 3.5 or higher

Usage

To run the tests, navigate to the directory containing the tests.py that is (Homework008/polls/tests.py