from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')
         ),
    path("user/", include("user.urls")),
    path("api-auth/", include("rest_framework.urls"))
]
