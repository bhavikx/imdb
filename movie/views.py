from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .serializers import MovieSerializer
from .models import Movie

from rest_framework.decorators import api_view

from rest_framework.views import APIView

from rest_framework.response import Response

# decorator
from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "movie/un.html")

        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

@unauthenticated
def homeView(request):
	movies = Movie.objects.order_by('rating')[:10]
	return render(request, "movie/home.html", {"movies":movies})


@api_view(['GET'])
def getMovieDtail(request, mid):
    m = Movie.objects.get(id=mid)
    serializer = MovieSerializer(m)

    return Response(serializer.data)

'''class getMovieDtail(APIView):
    def get(self, request, mid):
        movie = Movie.objects.get(id=mid)
        serialized = MovieSerializer(movie)
        return Response(serialized.data)'''

class getMovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data)

class sortByName(APIView):
    def get(self, request):
        movies = Movie.objects.order_by('name')
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data)

class sortByRating(APIView):
    def get(self, request):
        movies = Movie.objects.order_by('-rating')
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data)

class sortByDate(APIView):
    def get(self, request):
        movies = Movie.objects.order_by('release_date')
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data)

class searchByName(APIView):
    def get(self, request, s):
        movies = Movie.objects.filter(name__icontains=s)
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data)

class searchByDes(APIView):
    def get(self, request, s):
        movies = Movie.objects.filter(description__icontains=s)
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data)