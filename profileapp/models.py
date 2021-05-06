from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # 하나의 프로필이 하나의 유저와 매칭되게끔 (OneToOneField)
    # related_name은, request.user.profile 이런식으로 바로 user.해서 연결되게 이름을 지어주는 것.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # upload_to : 셋팅에서 설정해줬던것처럼, 이렇게 들어온 파일은 media 밑의 profile에 들어가게 됨.
    # null=True : 이미지가 꼭 없어도 괜찮다.
    image = models.ImageField(upload_to='profile/', null=True)
    # unique=True : 중복 방지
    # null=True : 프론트 단에서 알림을 띄우기 위해서 일단 True
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)