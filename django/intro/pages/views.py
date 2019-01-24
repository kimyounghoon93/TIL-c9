from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request,'index.html')
    
# Template variable
def dinner(request):
    menu = ["족발","햄버거","치킨","초밥","피자","보쌈"]
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': pick})
    
# Variable routing
# name에 들어가는건 주소값
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def personalities(request):
    return render(request, 'personalities.html', {'personalities': personalities})
    
def opgg(request, nick):
    return render(request, 'opgg.html', {'nick': nick})
   
# Form tag
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message': message})
    
# From 외부로 요청
def naver(request):
    return render(request, 'naver.html')
    
# Bootstrap
def bootstrap(request):
    return render(request, 'bootstrap.html')