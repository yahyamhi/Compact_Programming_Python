import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

def create_question(question_text, days, choiceless=False):
    """
    Generate a question with the specified question_text and publish it based on the number of days offset from the current time. 
    A negative value for days indicates a question that was published in the past, 
    while a positive value indicates a question that is yet to be published.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question(question_text=question_text, pub_date=time)
    if not choiceless:
        question.choice_set.create(choice_text='Just hacking again', votes=0)
    Question.objects.bulk_create([question])
    return question

class QuestionIndexViewTests(TestCase):
    # Testcase 1
    def test_display_message_for_no_questions(self):
        """
        Test that if there are no questions present, the system displays a message indicating so.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # Testcase 2
    def test_past_question(self):
        """
        Verify that questions with a publication date in the past are displayed on the index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    # Testcase 3
    def test_future_question(self):
        """
        Questions with a publication date in the future should not be displayed on the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # Testcase 4
    def test_future_and_past_questions(self):
        """
        Only questions with a publication date in the past should be displayed on the index page, even if both past and future questions exist.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    # Testcase 5
    def test_multiple_past_questions(self):
        """
        Multiple past questions should be displayed on the questions index page.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

    # Testcase 6
    def test_missing_choices(self):
        """
        Questions without choices should not be displayed on the index page.
        """
        create_question(
            question_text="Choiceless question.",
            days=-5,
            choiceless=True)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

class QuestionModelTests(TestCase):

    # Testcase 7
    def test_future_question_publication_date(self):
        """
        Verifies that `was_published_recently()` returns False for questions 
        whose publication date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())

    # Testcase 8
    def test_old_question_publication_date(self):
        """
        Verifies that `was_published_recently()` returns False for questions 
        whose publication date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertFalse(old_question.was_published_recently())

    # Testcase 9
    def test_recent_question_publication_date(self):
        """
        Verifies that `was_published_recently()` returns True for questions 
        whose publication date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertTrue(recent_question.was_published_recently())

class QuestionDetailViewTests(TestCase):

    # Testcase 10
    def test_question_with_future_publication_date(self):
        """
        The detail view of a question with a future publication date
        should return a 404 not found status code.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # Testcase 11
    def test_question_with_past_publication_date(self):
        """
        The detail view of a question with a past publication date
        should display the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

    # Testcase 12
    def test_question_without_choices(self):
        """
        The detail view of a question without choices
        should return a 404 not found status code.
        """
        question_without_choices = create_question(
            question_text="Choiceless question.",
            days=-5,
            choiceless=True)
        response = self.client.get(reverse('polls:detail', args=(question_without_choices.id,)))
        self.assertEqual(response.status_code, 404)

class QuestionResultslViewTests(TestCase):

    # Testcase 13
    def test_result_view_for_future_question(self):
        """
        The result view of a question with a pub_date in the future should
        return a 404 not found status code.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:results", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # Testcase 14
    def test_result_view_for_past_question(self):
        """
        The result view of a question with a pub_date in the past should
        display the question text in the response.
        """
        past_question = create_question(question_text="Past question.", days=-5)
        url = reverse("polls:results", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

    # Testcase 15
    def test_result_view_for_question_without_choices(self):
        """
        The result view of a question without any choices should return
        a 404 not found status code.
        """
        question_without_choices = create_question(
            question_text="Question without choices.",
            days=-5,
            choiceless=True
        )
        url = reverse("polls:results", args=(question_without_choices.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
