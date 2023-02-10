from django.contrib import admin
from django.urls import (
    path, 
    include, 
)
from rest_framework import routers
from rest_auth.views import (
    LoginView, 
    LogoutView,
)
from rest_auth.registration.views import RegisterView

from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from django.contrib.sites.models import Site

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('', include(router.urls)),
]

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)
admin.site.unregister(Site)