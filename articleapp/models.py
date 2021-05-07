from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    # 작성자
    # on_delete=models.SET_NULL : 회원탈퇴해도 사라지지 않고, 알수없는 게시글로 남아있음
    # related_name='article' : 유저객체에서 아티클을 접근할때 쓰는 이름이라서 지정해주는 것. (user.article)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # 어느 프로젝트 안의 게시물인지 구분할 수 있게끔
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    # 제목
    title = models.CharField(max_length=200, null=True)
    # 이미지
    # upload_to='article/', media 안의 article 에 들어간다.
    image = models.ImageField(upload_to='article/', null=False)
    # 내용
    content = models.TextField(null=True)
    # 언제 만들어졌는지!
    created_at = models.DateField(auto_now_add=True, null=True)