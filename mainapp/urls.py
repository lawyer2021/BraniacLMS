import debug_toolbar
from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig
from django.views.decorators.cache import cache_page

app_name = MainappConfig.name
urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses/', cache_page(60*5)(views.CoursesListView.as_view()), name='courses'),
    path('docsite/', views.DocSiteView.as_view(), name='doc_site'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('news/', views.NewsView.as_view(), name='news'),
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    # path('news/<int:pk>/', views.NewsPageDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/detail', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('courses/<int:pk>/', views.CoursesDetailView.as_view(), name='courses_detail'),
    path('course_feedback/', views.CourseFeedbackFormProcessView.as_view(), name='course_feedback'),
    # path('news/<int:page>/', views.NewsViewPaginator.as_view(), name='news_paginator'),
    path("log_view/", views.LogView.as_view(), name="log_view"),
    path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
]
