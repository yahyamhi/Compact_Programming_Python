from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        View to display the latest 5 published questions, excluding those set to be published in the future and questions with no choices.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).exclude(choice=None).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        View to display the details of a single question, excluding those that haven't been published or have no choices.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()).exclude(
            choice=None)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        View to process the voting of a question.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()).exclude(
            choice=None)


def vote(request, question_id):
# Get the question based on the id provided, or return a 404 error if not found
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse(
                'polls:results', args=(
                    question.id,)))
