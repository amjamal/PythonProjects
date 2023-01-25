from django.shortcuts import render

from . models import Place, Team


# Create your views here.
def ind(request):
    place = Place.objects.all()
    team = Team.objects.all()

    return render(request, 'index.html', {'places': place, 'teams': team})

def about(request):
    return render(request, 'about.html')

