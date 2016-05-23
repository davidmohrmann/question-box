from django.conf.urls import url, include

from . import views


app_name = 'stacked'
urlpatterns = [
	# url(r'^/question/new/$', views.question_new, name="question_new"),
    # GET /polls/
    url(r'^$', views.list, name='list'),
    # GET /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # GET /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # GET /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
