from django.urls import path
from .views import NLTKAPIView

urlpatterns = [
    path('keywords/', NLTKAPIView.as_view(), name='keywords'),
]
