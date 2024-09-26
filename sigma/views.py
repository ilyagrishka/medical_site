from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from med_service.models import Categories


# def index(request):
#
#     context = {
#         "titlte": "home",
#         "content": "main page",
#     }
#     return render(request, "sigma/index.html", context)
class IndexView(TemplateView):
    template_name = "sigma/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = "Центр медицинкой  диагностики"
        return context


class AboutView(TemplateView):
    template_name = 'sigma/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "здесь можно написать о том где центр находится его историю "
        return context
