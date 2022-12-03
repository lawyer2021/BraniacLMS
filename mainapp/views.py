from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_title'] = "Новостной заголовок"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context['range'] = range(5)
        context['datetime_obj'] = datetime.now()
        return context

class NewsViewPaginator(NewsView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context