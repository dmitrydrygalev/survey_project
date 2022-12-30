from django.contrib import admin
from .models import Question, Answer, Choice, Category


class AdminManageCategory(admin.ModelAdmin):
    list_display = (
        'title',
    )


class AdminManageQuestion(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points',
    )


class AdminManageChoice(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'points',
        'lock_other',
    )
    list_filter = ('question',)


class AdminManageAnswer(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)


admin.site.register(Question, AdminManageQuestion)
admin.site.register(Choice, AdminManageChoice)
admin.site.register(Answer, AdminManageAnswer)
admin.site.register(Category, AdminManageCategory)