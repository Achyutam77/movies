from .models import Genre

def genere_list(request):
    data = {
        "genres": Genre.objects.all(),
    }
    return data