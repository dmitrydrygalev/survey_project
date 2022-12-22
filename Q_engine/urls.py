from django.urls import path

from Q_engine.views import GetQuestion, QuestionAnswer
import api

urlpatterns = [
    path('', GetQuestion.as_view()),
    path('answerset/', api.QuestionAnswerViewSet.as_view({'get': 'list'})),
]
