from home import views
from django.urls import path,include


urlpatterns = [
    path('',views.index,name='index'),
    path('mean/',views.mean,name='mean'),
]