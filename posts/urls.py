from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('list/', views.IndexView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]