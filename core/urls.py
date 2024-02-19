from django.contrib import admin
from django.urls import path, include
from api.auth import url as auth_url
from api.submissions import urls as submissions_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include(auth_url)),
    path("api/submissions/", include(submissions_url)),
]
