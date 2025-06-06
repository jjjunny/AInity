from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('study/create/', views.study_create, name='study_create'),
    path('club/create/', views.create_post, name='club_create'),
    path('account/', views.login_signup_view, name='login_signup'),
    path('school_notice/', views.school_notice_view, name='school_notice'),
    path('study/', views.study_list, name='study_list'),
    path('club/', views.club_list, name='club_list'),
    path('classchat/', views.classchat, name='classchat'),
    path('classchat/room/<str:room_name>/', views.room, name='room'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

]
