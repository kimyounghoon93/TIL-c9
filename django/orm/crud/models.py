from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
# 정리
# class Post : Django - Model, DB - Table
# post = Post() : Django - Instance or Object, DB - Record or Row
# title : Django - Field, DB - Column


# 장고 orm을 이용한 DB에 레코드를 생성하는 방법

# 터미널에 ./manage.py shell_plus 입력

# DB - Record or Row
### 종료버튼 exit()
# CRUD
# Create
# 1. 
# post = Post(title='hello-1')
# post.save()

# 2. 위 두줄을 축약하면 # 이건 save() 하지 않아도 자동으로 됨
# post2 = Post.objects.create(title='hello-2')

# 3. 
# post3 = Post() # 빈 껍데기 만듦
# post3.title = 'hello-3'
# post3.save()
# 한 줄 작성
# post3.title = 'hello-3'.save()

# Read
# 1. All 
# # Post.objects.all()
# posts = Post.objects.all() # posts에 저장함

# 2. One
# 1번 게시글 가져오기
# Post.objects.get(id=1)
# Post.objects.get(pk=1)

# 해당 게시글 가져오기
# Post.objects.get(title='hello-2') # 정확한 값 요구

# (views.py 한정)
# from django.shortcuts import get_object_or_404
# post = get_object_or_404(Post)

# 특정 조건에 해당하는 모든 것들을 가져와라
# Post.objects.filter(pk=1)[0] #id=1, title='hello-1'도 가능
# Post.objects.filter(pk=1).first()

#3. Where(filter)
# Post.objects.filter(title='hello-1') # title이 'hello-1'인 오브젯 모두 검색
# posts = Post.objects.filter(title='hello-1') # posts에 넣음
# post = Post.objects.filter(title='hello-1').first() # 또는 [0]

# SQL에서 LIKE와 같은 역활
# Post.objects.filter(title__contains='lo') 'lo'가 들어있는 것들 모두 표시

# Post.objects.order_by('title') # 제목 오름차순
# Post.objects.order_by('-title') # 제목 내림차순 
# Post.objects.filter(title__contains='hello').order_by('-id') id값의 역순으로 정렬한다

############## 중요한 개념 ################
# Post.objects.all()[0] #=> offset 0 limit 1
# Post.objects.all()[1] #=> offset 1 limit 1
# Post.objects.all()[1:3] #=> offset 1 limit 2
# Post.objects.all()[offset:offset+limit]

# 3. 수정(Update)
# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save()

# post1 = Post.objects.get(pk=1)
# post1
# <Post: Post object (1)>
# post1.title
# 'hello1'
# post1.title = 'hello-5'
# post1.title
# 'hello-5'


# 4. 삭제(Delete)
# post = Post.objects.get(pk=1)
# post.delete() # post에 저장된 데이터 삭제
# 한 줄 작성
# Post.objects.get(pk=1).delete()