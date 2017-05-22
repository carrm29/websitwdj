
# Register your models here.

from django.contrib import admin
from .models import Choice, Question

#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Imagen', {'fields': ['question_img']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
