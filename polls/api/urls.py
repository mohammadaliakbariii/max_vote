from django.urls import path
from .views import question_list,choice_list
urlpatterns=[
    path("",question_list,name="list_of_question_list"),
    path("choices/",choice_list,name="choice_list"),

]