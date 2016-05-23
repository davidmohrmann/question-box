from .models import Question, Answer 
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from .forms import QuestionForm


def question_new(request):
	form = QuestionForm()
	return render(request, 'stacked/question_edit.html', {'form': form})


def list(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'stacked/index.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'stacked/results.html', {'question':
    	question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'stacked/detail.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_answer = question.answer_set.get(pk=request.POST['answer'])
	except(KeyError, Answer.DoesNotExist):
		return render(request, 'stacked/detail.html', {
			'question': question, 
			'error_message': "You didn't select an answer.",
			})
	else:
		selected_answer.votes += 1
		selected_answer.save()
		
		return HttpResponseRedirect(reverse('stacked: results', args=(question.id,)))


