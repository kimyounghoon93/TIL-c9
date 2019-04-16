from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello.html', {})
    
def hi(request, apple):
    # print(apple) 을 해놓으면 서버켜놓은 터미널에 요청한 주소의 apple부분이 나온다
    print(apple)                        # ('단순한문자열':)
    return render(request, 'hi.html', {'banana':apple})