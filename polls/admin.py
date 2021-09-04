from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
     model = Choice
     extra = 3
     max_num = 3



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
     list_display = ['question_text','date_time']
     search_fields = ["question_text"]
     inlines = (ChoiceInline,)

