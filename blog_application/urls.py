from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path("user/", include("user.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="user/password_reset.html"), name="password_reset"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-done/", auth_views.PasswordResetDoneView.as_view(
        template_name="user/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="user/password_reset_complete.html"), name="password-reset-complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
