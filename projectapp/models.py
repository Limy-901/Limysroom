from django.db import models

# Create your models here.

class Project(models.Model):
    # 업로드 한 이미지로 (필수)
    image = models.ImageField(upload_to='project/', null=False)
    # 입력한 제목으로 (필수)
    title = models.CharField(max_length=20, null=False)
    # (선택) 설명
    description = models.CharField(max_length=200, null=True)
    # 생성일
    created_at = models.DateTimeField(auto_now=True)

    #
    def __str__(self):
        # 내가 직접 지정해준다.
        # pk : title 이런 형식으로 프로젝트가 표기된다.
        # 여기서 self는 프로젝트 객체를 의미
        return f'{self.pk} : {self.title}'