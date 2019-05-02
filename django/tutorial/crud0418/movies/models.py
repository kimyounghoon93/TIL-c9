from django.db import models

# Create your models here.
class Movie(models.Model):
                    # 대문자로 시작하면 웬만하면 클레스
                    # 클레스 뒤에 괄호 두개를 붙이면 인스턴스 변수를 만드는 것이다.
    title = models.TextField() # <- 괄호 두개

class Comment(models.Model):
    content = models.TextField()
                            # 첫 번 째 인자 : 관계를 맻을 클레스명
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # ForeignKey를 사용할 때 아래와 같이 작성할 수 있다. 무비스 앱안의 Movie
    # movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    # 아래에서 사용해봤음
    # settings.AUTH_USER_MODEL #=> 'auth.User'를 써도 되지만 settings.AUTH_USER_MODEL를 사용 고칠 때 편하게 하려
    