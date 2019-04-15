from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

def post_image_path(instance, filename):
    return f'posts/image/{filename}'
    # return 'posts/{}/{}.jpeg'.format(instance.content, instance.content)


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # CASCADE = 주인1에 대한 물건N을 모두 삭제한다
    content = models.TextField()
    # image = models.ImageField(blank=True)
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
                    upload_to=post_image_path, # 저장위치
                    processors=[ResizeToFill(600,600)], # 처리할 작업 목록
                    format='JPEG', # 저장 포멧
                    options={'quality':90}, # 옵션
        )
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()