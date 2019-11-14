

from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from apps.core import views


urlpatterns = [
    url(r'^$', views.index, name='bokeh'),
    # url('accounts/login/', auth_views.LoginView.as_view()),
    url(r'dashboard/', views.dashboard, name="dashboard"),
]