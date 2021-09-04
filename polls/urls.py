from django.urls import path
from . import views
app_name='polls'
urlpatterns=[
    path("",views.index,name="index"),
    path("<int:question_id>/",views.detail,name="detail"),
    path('vote/<int:question_id>',views.vote,name='vote'),
    path('result/<int:question_id>',views.result,name='result')
]
