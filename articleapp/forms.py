from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # 미디엄 에디터로 만들것에 대해 정의하기 위해!
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto;'
                                                                    'text-align: left'}))
    # 프로젝트를 고르지 않더라도 쓸 수 있게 하기 위함
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']