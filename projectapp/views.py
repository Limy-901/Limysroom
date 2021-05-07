from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 25
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        # 로그인 되어 있다면
        if user.is_authenticated:
            # 위의 프로젝트, 유저와 일치하는 구독정보 찾기
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        # 아티클의 프로젝트가 전달받은 오프젝트의 프로젝트와 같으면 모두 필터링
        object_list = Article.objects.filter(project=self.get_object())
        # 위의 결과값만 리턴
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                                            **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25