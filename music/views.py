from django.http import HttpResponse
from django.shortcuts import render
# from django.views import View
from django.views.generic.base import View

from django.views.generic import TemplateView

# Create your views here.


# The very first version of the index view, used only in the setup phase.
# It just prints something in the browser.


def index(request):
    return HttpResponse('<h1>John Lennon</h1>')
    # return HttpResponse(str(request))


# class IndexView(TemplateView):
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>John Lennon</h1>')


