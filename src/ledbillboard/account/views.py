from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


@method_decorator([csrf_exempt], name='dispatch')
class AjaxLoginView(View):
    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
