from django.urls import path
from . import views

urlpatterns = [
    path('',views.artist_list, name="artist_list"),
    path('artist/<str:id>/',views.artist_one,name="artist_one"),
    path('song/add/',views.addsong,name="addsong"),
    path('song/<str:id>/',views.song,name="song"),
    path('search/',views.search,name="search")
]