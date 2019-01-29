from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
# views.py >> urls.py >> template.py
# def throw
# def catch

def index(request):
    return render(request,'index.html')

# Form tag
def new(request):
    return render(request, 'new.html')
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    # DB INSERT 
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save()
    # 렌더는 GET에만 사용한다.
    # return render(request, 'create.html')
    # POST는 리 다이렉트를 사용한다 위에 임포트 해줘야 된다.
    return redirect(f'/students/{student.pk}/')
    # 외부 사이트로도 리다이렉트 가능함
# def rd(request, 변수):
def naver(request, q):
    return redirect(f'https://search.naver.com/search.naver?query={q}')
    
    # https://playground-busanteam.c9users.io/posts/naver/검색\
    # 깃헙처럼 id값이 주소창에 입력 되는 경우
def github(request, username):
    return redirect(f'https://github.com/{username}')

def index(request):
    # All student
    students = Student.objects.all()
    
    return render(request, 'index.html', {'students':students})
    
def detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {'student': student})
    
def delete(request, student_id):
    # 삭제하는 코드
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/students/')

def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'edit.html', {'student':student})

def update(request, student_id):
    # 수정하는 코드
    # 수정하기 위해 수정 할 것을 불러온다
    student = Student.objects.get(pk=student_id)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birthday')
    student.age = request.POST.get('age')
    # 실제로 반영하기위해선 세이브를 해주어야 한다
    student.save()
    
    return redirect(f'/students/{student_id}/')
    
    
    
    