from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

class Person(models.Model):
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]) # 조건문 []
    age = models.IntegerField(validators=[MinValueValidator(20, message='미성년자는 노노')]) # 20부터 가능