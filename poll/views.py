from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'poll/detail.html', {'question': question})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'poll/results.html', {'question': question})


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "No ha eligido opción.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

# def  pupulate_database():
#     for id in range(5):
#         question = Question()
#         question.pub_date = datetime.datetime.now()
#         question.question_text = " si {}".format(id)
#         question.save()
