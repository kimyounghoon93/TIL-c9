from django.db import models

# Create your models here.
class Movie(models.Model):
                    # 대문자로 시작하면 웬만하면 클레스
                    # 클레스 뒤에 괄호 두개를 붙이면 인스턴스 변수를 만드는 것이다.
    title = models.TextField() # <- 괄호 두개