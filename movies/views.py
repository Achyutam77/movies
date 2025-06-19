from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all()
        context["trending_movies"] = Movie.objects.filter(is_trending=True)
        context["generes"] = Movie.objects.values_list('genre', flat=True).distinct()
        return context
    


class MovieCreateView(LoginRequiredMixin,CreateView):
    model = Movie
    template_name = "create_movies.html"
    fields = "__all__"
    success_url = "/"
    login_url = "/user/login/"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie"

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "update_movie.html"
    fields = "__all__"
    success_url = "/"

class MovieDeleteView(LoginRequiredMixin,DeleteView):
    model = Movie
    template_name = "confirm_delete.html"
    context_object_name = "movie"
    success_url = "/"
    context_object_name = "movie"
    login_url = "/user/login/"

# def delete_view(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return redirect("/")
#     except Movie.DoesNotExist as e:
#         print("Movie does not exist:")
        
        
    





