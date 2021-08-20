from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView),
    path('get-movie-detail/<int:mid>', getMovieDtail),
    path('get-movie-list', getMovieList.as_view()),

    path('sort-by-name', sortByName.as_view()),
    path('sort-by-rating', sortByRating.as_view()),
    path('sort-by-date', sortByDate.as_view()),

    path('search-by-name/<str:s>', searchByName.as_view()),
    path('search-by-des/<str:s>', searchByDes.as_view()),
]
