from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from Q_engine import views
from Q_engine.views import *
from users.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Category', CategoryViewSet)
router.register(r'Question', QuestionViewSet)
router.register(r'Choice', ChoiceViewSet)
router.register(r'Answer', AnswerViewSet)

urlpatterns = [
    path('', views.index)
]
router_ = [
    path('first_project/', include(router.urls))
]

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_)),
    path('login/', AuthorizationUserView.as_view(), name='login'),
    path('registr/', RegistrationUserView.as_view(), name='registr'),
]