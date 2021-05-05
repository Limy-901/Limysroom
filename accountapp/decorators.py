from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        # 요청을 보낸 pk 와 현재 유저의 pk가 같은지 확인.
        # user : 값으로 넘긴 유저(pk), request.user : 요청을 보낸 유저 (실제사용자)
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated