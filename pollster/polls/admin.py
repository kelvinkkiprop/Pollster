from django.contrib import admin

# Register your models here to your admin panel.
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

#Change header, title, index
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Pollster Admin"


# ChoiceInline class
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#QuestionAdmin class
class QuestionAdmin(admin.ModelAdmin):
    #Add fields
    fieldsets = [(None, {'fields': ['question_text']}),
                ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


