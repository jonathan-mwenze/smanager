from django.urls import path
#from .views import IndexListView
from .import views

urlpatterns = [
    path('', views.autosearch, name="index"),
    #path('', IndexListView.as_view(), name="index"),
]
