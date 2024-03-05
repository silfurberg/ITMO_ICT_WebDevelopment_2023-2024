from django.urls import path
from homework import views
from homework.apps import HomeworkConfig

app_name = HomeworkConfig.name

urlpatterns = [
    path('', views.RootPageView.as_view(), name='root'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('registration', views.RegistrationView.as_view(), name='registration'),
    path('homeworks', views.HomeworksView.as_view(), name='homeworks'),
    path('submit_homework/<int:pk>', views.SubmitHomeworkView.as_view(), name='submit_homework'),
    path('grades', views.GradesView.as_view(), name='grades')
]