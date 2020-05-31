from django.urls import path

from .views import IndexView

app_name = 'docs'

urlpatterns = [
    path('', IndexView.as_view(), name='docs'),
]
