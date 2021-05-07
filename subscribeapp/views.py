from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    
    def get(self, request, *args, **kwargs):
        # project_pk 를 가지고 있는 Project를 찾는데, 존재하지 않으면 404 띄우기
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        # user와 project가 셋팅 되었으니 해당하는 subscription을 찾는다
        subscription = Subscription.objects.filter(user=user, project=project)
        # 이미 존재한다면 (존재하는데 눌렀다 > 구독 취소)
        if subscription.exists():
            subscription.delete()
        # 처음 누른거라면 ( 구독 하기 )
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)