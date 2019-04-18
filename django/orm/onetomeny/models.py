from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    
# User:Post = 1:N
class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
# User:Comment = 1:N
# Post:Comment = 1:N
class Comment(models.Model):
    content = models.TextField()
                                                # CASCADE는 1:N의 관계에서 N에 지정해야한다
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
# user1 = User.objects.create(name='Kim')
# user2 = User.objects.create(name='Lee')
# # post1 = User.objects.create(title='1글', user_id=1) 도 가능
# # post1 = User.objects.create(title='1글', user_id=user1.id) 도 가능

# post1 = Post.objects.create(title='1글', user=user1)
# post2 = Post.objects.create(title='2글', user=user1)
# post3 = Post.objects.create(title='3글', user=user2)

# c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
# c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
# c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
# c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
# c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)
# c6 = Comment.objects.create(content='!1글5댓글', user=user2, post=post1)
# c7 = Comment.objects.create(content='!2글2댓글', user=user2, post=post2)

# 예시, ForignKey를 사용하기 때문에 가능해짐
# 1. 1번 사람이 작성한 게시글은?
# user1.post_set.all()

# 2. 1번 사람이 작성한 게시글의 댓글들을 출력!
# for post in user1.post_set.all():
# ...     for comment in post.comment_set.all():                                                      
# ...             print(comment.content)
# ... 

# 3. 2번 댓글을 쓴 사람은?
# c2.user
# <User: User object (2)>

# 4. 2번 댓글을 쓴 사람이 작성한 게시글은?
# c2.user.post_set.all()

# 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
# post1.comment_set.first().user
# post1.comment_set.first().user.name
# post1.comment_set.first()[0].user.name

# 6. '1글'이 제목인 게시글은?
# Post.objects.filter(title='1글')

# 7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
# 방법 1
# Comment.objects.filter(post__title='1글')
# 방법 2
# post1 = Post.object.get(title='1글')
# Comment.object.filter(post=post1)

# 8. 댓글 중에 해당 게시글의 제목에 '1'이 들어가 있는 것은?
# Comment.objects.filter(post__title__contains='1')

# 병원에 오는 사람들을 기록하는 시스템을 만드려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있을까?
