from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    """A view function of index for the polls app.
    param: HTTP request  
    return:HTTP response template and context dictionary."""

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

def detail(request, question_id):
    # Database Primary key (int)
    """A view function of detail for the polls application
    param: HTTP request
    param: Database primary key questions_id
    returns: HTTP response, template, and question."""

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """A view function for the results for the poll application
    param: HTTP request
    param: database primary key(int) question_id
    returns: HTTP response, template and question."""

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """view function for vote for the polls application
    param: HTTP request
    param: database primary key (int)question_id
    returns: HTTP response redirect """
    

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
