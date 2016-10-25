from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from todo.views import TodoListAPIView, TodoDetailAPIView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/todos/$', TodoListAPIView.as_view(), name="todo_list_api_view"),
    url(r'^api/todos/(?P<pk>\d+)$', TodoDetailAPIView.as_view(), name="todo_detail_api_view"),
]
