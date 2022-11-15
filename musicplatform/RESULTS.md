## Import
```
>>> from artists.models import Artist
>>> from albums.models import Album
>>> import datetime
```
## Create some artists
```
>>> artist1 = Artist(stage_name='Drake', social_link='https://www.instagram.com/drake/')
>>> artist1.save()
>>> artist2 = Artist(stage_name='Snoop Dogg', social_link='https://www.facebook.com/snoop-dogg/')
>>> artist2.save()
>>> artist3 = Artist(stage_name='Eid Sheeran', social_link='https://www.twitter.com/ed-sheeran/')
>>> artist3.save()
```
## List down all artists
```
>>> Artist.objects.all()
<QuerySet [<Artist: Drake>, <Artist: Eid Sheeran>, <Artist: Snoop Dogg>]>
```
## List down all artists sorted by name
```
>>> Artist.objects.all().order_by('stage_name')
<QuerySet [<Artist: Drake>, <Artist: Eid Sheeran>, <Artist: Snoop Dogg>]>
>>> Artist.objects.all().order_by('-stage_name')
<QuerySet [<Artist: Snoop Dogg>, <Artist: Eid Sheeran>, <Artist: Drake>]>
```
## List down all artists whose name starts with `d`
```
>>> Artist.objects.filter(stage_name__istartswith='d')
<QuerySet [<Artist: Drake>]>
>>> Artist.objects.filter(stage_name__istartswith='a')
<QuerySet []>
```
## In 2 different ways, create some albums and assign them to any artists
```
>>> artist = Artist.objects.get(id=3)
>>> album1 = Album(name='Divide', release_time=datetime.datetime(2022, 9, 15), cost=1000.00, artist=artist)
>>> album1.save()
<Album: Album object (2)>
>>> artist = Artist.objects.get(id=2)
>>> album2 = Album(release_time=datetime.date(2022, 10, 12), cost=800.00, artist=artist)
>>> album2.save()
<Album: Album object (3)>
```
```
>>> artist = Artist.objects.get(id=1)
>>> Album.objects.create(name='Views', release_time=datetime.date(2020, 2, 24), cost=2500.00, artist=artist)
<Album: Album object (4)>
>>> artist = Artist.objects.get(id=2)
>>> Album.objects.create(release_time=datetime.date(2023, 5, 17), cost=750.00, artist=artist)
<Album: Album object (6)>
```
## Get the latest released album
```
>>> Album.objects.order_by('-release_time')[0]
<Album: Album object (6)>
>>> Album.objects.order_by('-release_time')[0].release_time
datetime.datetime(2023, 5, 17, 0, 0, tzinfo=datetime.timezone.utc)
```
## Get all albums released today or before but not after today
```
>>> Album.objects.exclude(release_time__gt=datetime.datetime.today())
<QuerySet [<Album: Album object (2)>, <Album: Album object (3)>, <Album: Album object (4)>]>
```
## Count the total number of albums
```
>>> Album.objects.count()
4
```
## In 2 different ways, for each artist, list down all of his/her albums
```
>>> for artist in Artist.objects.all():
...     print(f'- {artist.stage_name}')
...     for album in Album.objects.filter(artist=artist):
...         print(album)
... 
- Drake
Album object (4)
- Eid Sheeran
Album object (2)
- Snoop Dogg
Album object (3)
Album object (6)
```
```
>>> for artist in Artist.objects.all():
...     print(f'- {artist.stage_name}')
...     for album in artist.album_set.all():
...         print(album)
- Drake
Album object (4)
- Eid Sheeran
Album object (2)
- Snoop Dogg
Album object (3)
Album object (6)
```
## List down all albums ordered by cost then by name (cost has the higher priority)
```
>>> Album.objects.order_by('cost', 'name')
<QuerySet [<Album: Album object (6)>, <Album: Album object (3)>, <Album: Album object (2)>, <Album: Album object (4)>]>
```

