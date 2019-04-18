# 장고에서 forms 템플릿을 받아옴
from django import forms
from .models import Movie
            # forms에 있는 ModelFormd을 상속받음
# 아래의 폼은 파이썬 코드를 html 코드로 만들어준다
class MovieForm(forms.ModelForm):
    # 받아와서 자동으로 폼을 만들어줌
    # 메타 데이터 | 데이터에 대한 데이터를 메타데이터 라고 부름
    
    # title = ~~~ 라고 MovieForm의 데이터를 입력할 수 있는데 여기서 변수를 아무거나 사용해도 되지만 특정한 양식에 맞춘 예를들면 title을 쓰면 타이틀이 제대로 바뀐다.
    
    class Meta:
        model = Movie
        # 모든 정보를 다 받아오지 않고 필요한 정보만 골라서 받아오기 위해서 
        fields = ['title']
        # 반대로 모든 정보를 다 받아오기 위해서는 아래처럼
        # fields = '__all__'