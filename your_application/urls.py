from django.urls import path
from your_application import views
urlpatterns = [
    path('',views.index,name="index"),
]
