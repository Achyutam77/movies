from django.urls import path

from .views import MovieCreateView, MovieListView, MovieDetailView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path("", MovieListView.as_view(), name="home"),
    path("create-movies", MovieCreateView.as_view(), name="create_movie"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("update_movie/<int:pk>/", MovieUpdateView.as_view(), name="update_movie"),
    path("delete_movie/<int:pk>/", MovieDeleteView.as_view(), name="delete_movie"),
]