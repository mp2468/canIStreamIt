# howdy/urls.py
from django.conf.urls import url
from howdy import views
from . import showSubmitForm


urlpatterns = [
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^$', views.HomePageView.as_view()),
]