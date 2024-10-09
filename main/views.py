from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = ("StarMedCom - современная медицинская компания с лучшими специалистами из разных "
                              "областей."
                              "Самарский диагностический центр оказывает медицинские услуги с марта 1990 года. "
                              "На сегодня он является одним из крупнейших медицинских учреждений Поволжья, "
                              "обслуживающим население Самарской области и ближайших регионов."
                              " Исследования проводятся на современном оборудовании лучших мировых производителей. "
                              "Созданная в 1991 году автоматизированная система сбора, хранения и обработки "
                              "информации, целевой банк данных обследованных пациентов являются уникальными для "
                              "медицинских учреждений.")
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = ("Самарский диагностический центр начал свою работу в 1990 году. В центре работают "
                                   "отделы: консультативно-поликлинический, рентгеновской лучевой диагностики, "
                                   "ультразвуковой диагностики, лабораторной диагностики, функциональных "
                                   "исследований, гинекологии, оперативных вмешательств, эндоскопический кабинет. "
                                   "Также активно развивается педиатрическое направление. Есть физиотерапевтическое "
                                   "лечение, дневной стационар.")
        return context


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Home - О нас'
        context['content'] = "Контактная информация "
        context['text_on_page'] = ("тел: 8 (846) 300-44-63,"
                                   "8 (846) 260-61-53,\n"
                                   "местонахождение: г.Самара, ул. Мяги, 7а,\n"
                                   "email: samara_dc@mail.ru")

        return context
