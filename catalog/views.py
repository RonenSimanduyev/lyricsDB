from django.shortcuts import render,redirect
from .models import Artist,Song
from django.db.models import Q

# Create your views here.
def artist_list(request):
    artists = Artist.objects.all()
    return render(request,'catalog/artist_list.html',{"artists":artists})

def artist_one(request,id):
    artist = Artist.objects.get(id=id)
    return render(request,'catalog/artist.html',{"artist":artist})

def song(request,id):
    song = Song.objects.get(id=id)
    return render(request,'catalog/song.html',{"song":song})

def addsong(request):
    artists = Artist.objects.all()
    if request.method == 'POST':
        artist = Artist.objects.get(id=request.POST['artist'])
        Song.objects.create(
            title=request.POST['title'],
            imageUrl=request.POST['imageUrl'],
            lyrics=request.POST['lyrics'],
            artist=artist
        )
        return redirect('artist_list')
    return render(request,'catalog/add_song.html',{"artists":artists})

def search(request):
    q = request.GET['q'] if request.GET['q'] != None else ''
    songs = Song.objects.filter(
        Q(title__icontains=q) |
        Q(lyrics__icontains=q)
    )
    count = songs.count()
    return render(request,'catalog/songs_all.html', {"songs":songs,"count":count})