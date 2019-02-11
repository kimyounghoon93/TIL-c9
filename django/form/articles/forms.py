from django import forms
from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'rows': 5,
        'clos':50,
        'placeholder': '내용을 입력하세요.',
    }))
    
    # Mata 클레스는 꼭 지켜줘야 함 클레스에 대한 정보가 담겨있는 클레스
class ArticleModelForm(forms.ModelForm):
    # 아래 줄을 적지 않으면 모델.파이에 있는 데이터를 자동으로 로드함
    title = forms.CharField(label='제목')
    
    class Meta:
        model = Article
        fields = ['title', 'content']
        # 화면에 표시하고자 하는 콘텐츠를 '기입'