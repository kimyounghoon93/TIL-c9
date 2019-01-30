from django.db import models

# Create your models here. 데이터베이스 모델관련 작성
class Post(models.Model):
                    #(max_length=100)는 케릭터 필드에 꼭 적용 되어있어야 작동한다
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

# Post : Comment = 1 : N(ForeignKey)
class Comment(models.Model):
    #1의 값에 올 값은 소문자      # post가 사라지면 어떻게 처리 할건지(같이 삭제함)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    # on_delete 옵션
    # 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제.
    # 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.(삭제하려하면 에러발생)
    # 3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보에 NULL 설정.
    
    
# 1. Create
# post = Post(title='Hello', content='world!')
# post.save()

# 2. Read
# 2.1. All
# posts = Post.objects.all()
# 2.2. Get one
# post = Post.objects.get(pk=1)
# 2.3.filter (WHERE)
# posts = Post.objects.filter(title='Hello').all()
# post = Post.objects.filter(title='Hello').first()
# 2.4.LIKE
# posts = Post.objects.filter(title__contains='He').all()
# 2.5. order_by (정렬)
# posts = Post.objects.order_by('title').all() # 오름차순
# posts = Post.objects.order_by('-title').all() # 내림차순
# 2.6. limit & offset
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]
# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()
# 4 post = Post.objects.get(p1)
# post.title
