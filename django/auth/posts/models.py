from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here. 데이터베이스 모델관련 작성
class Post(models.Model):
                    #(max_length=100)는 케릭터 필드에 꼭 적용 되어있어야 작동한다
    title = models.CharField(max_length=100)
    content = models.TextField()
    #(blank=True)를 넣으면 빈 값이 와도 에러가 뜨지않는다
    
    # image = models.ImageField(blank=True) # 파일은 FileField()
    # 이미지 새로 만듦
    # 둘다 비율은 유지한 상태
    # ResizeToFill 맞추고 넘치는 부분 잘라내기.
    # ResizeToFit 맞추고 남는 부분을 빈공간으로 둠.
    
    image = ProcessedImageField(
            upload_to='posts/images', # 저장 위치
            processors=[ResizeToFill(300,300)], # 어떠한 형태로 처리할지 설정하는 작업 목록을 리스트 형태로 넘겨주는 것
            format='JPEG', # 저장포맷 (확장자)
            options={'quality':90}, # 저장 포맷 관련 옵션
        )
    
    # 테이블 만들 때 필수라고 보면 되는 것
    created_at = models.DateTimeField(auto_now_add=True) # 생성 될 때, 딱 한 번만 현재시간이 들어감
    updated_at = models.DateTimeField(auto_now=True) # 변경이 될 때 마다, 현재시각
    
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
