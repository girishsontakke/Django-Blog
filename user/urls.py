from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_views
app_name = "user"
urlpatterns = [
    path("register/", user_view.register, name="register"),
    path("profile/", user_view.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path("api/", include("user.api.urls"))
]
