from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('post:list')
    
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('posts:list')
    else:
        signup_form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'signup_form':signup_form})

def login(request):
    if request.user.is_authenticated:
        return redirect('post:list')
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or'posts:list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
def people(request, username):
    # get_user_model() #=> User 클레스가 나옴 # 뒤에 있는 유저네임은 윗줄에서 받아온 유저네임
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people': people})