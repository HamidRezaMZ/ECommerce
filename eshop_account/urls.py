from django.urls import path

from .views import login_user, register, log_out, user_account_main_page, edit_profile

urlpatterns = [
    path('login', login_user),
    path('register', register),
    path('logout', log_out),
    path('user-panel', user_account_main_page),
    path('user-panel/edit', edit_profile),
]
