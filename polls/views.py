from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    """A index function that takes in the request and returns render request and html file and context."""

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

def detail(request, question_id):
    """detail function that takes the request and questions id and returns render request, html file, and question."""

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """result function that takes request, question id returns render request,html and questions."""

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """vote function that takes in request and question id with the use of try-except if  exception occurs the won't be issues."""
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
        pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
# Always return an HttpResponseRedirect after successfully
# dealing with POST data. This prevents data from being
# posted twice if a
# user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )
