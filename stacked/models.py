from django.db import models
from django.utils import timezone


class Question(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey('auth.User')

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
    	return self.name
    	return self.description


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    # votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now())

    # def recently_published_answer(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    def __str__(self):
    	return self.question
    	return self.answer


# class User(models.Model):
# 	user_name = models.CharField(max_length=25)

# 	def __str__(self):
# 		return self.user_name
