from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('login/', LoginView.as_view(template_name='results/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('', views.student_list, name='home'),   # Dashboard
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('chart/', views.student_chart, name='student_chart'),
    path('pie/', views.pass_fail_chart, name='pass_fail_chart')
]