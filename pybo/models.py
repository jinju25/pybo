from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db import models

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=100)
    # 글자수의 길이가 제한된 텍스트는 CharField를 사용해야함함
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    class Meta:
        permissions = [
            ('can_view_list', 'Can View List')
        ]

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='author_answer')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 기존 모델을 속성으로 연결하기 위해 Foreignkey 사용
    # on_delete=models.CASCADE 답변과 연결된 질문이 삭제 될 경우 답변도 함께 삭제

    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
