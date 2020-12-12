from django.http import HttpResponse
from django.shortcuts import render
# from django.views import View
from django.urls import reverse_lazy
from django.views.generic.base import View

from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.


# The very first version of the index view, used only in the setup phase.
# It just prints something in the browser.
# def index(request):
#     return HttpResponse('<h1>John Lennon</h1>')
#     # return HttpResponse(str(request))

# # The next version of the index view, also used only in the setup phase.
# # It renders something in a simple template (index0.html).
# def index(request):
#     context = {
#         'john': 'John Lennon'
#     }
#     return render(request, 'index0.html', context=context)


# class IndexView(TemplateView):
from music.models import Band, Musician

footer_context = {
    'john': 'John Lennon',
    'life_quote': 'Life is what happens to you while you\'re busy making other plans.'
}


class IndexView(View):

    # template_name = 'index0.html'       # unnecessary, probably because of render() in get() specifies it as well
    template_name = 'index.html'       # unnecessary, probably because of render() in get() specifies it as well

    def get(self, request, *args, **kwargs):
        # return HttpResponse('<h1>John Lennon</h1>')
        # context = {
        #     'john': 'John Lennon',
        #     'life_quote': 'Life is what happens to you while you\'re busy making other plans.'
        # }
        context = footer_context
        # return render(request, 'index0.html', context=context)
        return render(request, 'index.html', context=context)


class BandDetailView(DetailView):
    """Class-based view that handles individual Band objects.
    Typical fields that DetailView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_detail.html')
    """

    model = Band
    template_name = 'music/band-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class BandListView(ListView):
    """Class-based view that handles lists of Band objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_list.html')
    Typically, such views also override ListView.get_queryset(),
    making it return a QuerySet of objects (such as (possibly filtered) <Model>.objects.all()))
    """

    model = Band
    template_name = 'music/band-list.html'

    def get_queryset(self):
        return Band.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class MusicianDetailView(DetailView):

    """Class-based view that handles individual Musician objects.
    Typical fields that DetailView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_detail.html')
    """

    model = Musician
    template_name = 'music/musician-detail.html'


class MusicianListView(ListView):
    """Class-based view that handles lists of Musician objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_list.html')
    Typically, such views also override ListView.get_queryset(),
    making it return a QuerySet of objects (such as (possibly filtered) <Model>.objects.all()))
    """

    model = Musician
    template_name = 'music/musician-list.html'

    def get_queryset(self):
        return Musician.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class BandCreateView(CreateView):

    model = Band
    fields = '__all__'
    template_name = 'music/band-form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class BandUpdateView(UpdateView):

    model = Band
    fields = '__all__'
    template_name = 'music/band-form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class BandDeleteView(DeleteView):

    model = Band
    success_url = reverse_lazy('band-list')
    template_name = 'music/band-confirm-delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class MusicianCreateView(CreateView):

    model = Musician
    fields = '__all__'
    template_name = 'music/musician-form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class MusicianUpdateView(UpdateView):

    model = Musician
    fields = '__all__'
    template_name = 'music/musician-form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context


class MusicianDeleteView(DeleteView):

    model = Musician
    success_url = reverse_lazy('musician-list')
    template_name = 'music/musician-confirm-delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(footer_context)
        return context



