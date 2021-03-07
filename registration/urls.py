from django.urls.conf import path
from . import views


app_name = 'registration'

urlpatterns = [
    path('', views.home, name="home"),
    path('sent/', views.sent, name="sent"),
    path('register/', views.apply, name="apply"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('approved/', views.approved, name="approved"),
    path('pending/', views.pending, name="pending"),
    path('approve/', views.approve, name="approve"),
    path('delete/', views.delete, name="delete"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('student_page/', views.student_page, name="student_page"),
    path('change-department/', views.change_department, name="cd"),
    


]

