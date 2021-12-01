"""myquiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import RegisterView, LoginView, LogoutView, index
from quizzes.views import QuizView, QuestionsView, quiz_data_view, save_quiz_view, ResultView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dictionary/', include('dictionary.urls', namespace='dictionary')),
    path('', index, name='index'),
    path('register/', RegisterView, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('quizzes/', QuizView, name='quizzes'),
    path('quizzes/<int:id>/', QuestionsView, name='questions'),
    path('quizzes/<int:id>/data/', quiz_data_view, name='quiz-data-view'),
    path('quizzes/<int:id>/save/', save_quiz_view, name='save_quiz_view'),
    path('quizzes/<int:id>/result/', ResultView, name='result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
