from peewee import *

db = SqliteDatabase('chinook.db')


class BaseModel(Model):
    class Meta:
        database = db


class Album(BaseModel):
    album_id = AutoField(column_name='AlbumID')
    album_name = TextField(column_name='Title')
    artist_id = IntegerField(column_name='ArtistId')

    class Meta:
        table_name = 'albums'


class Track(BaseModel):
    track_id = AutoField(column_name='TrackId')
    track_name = TextField(column_name='Name')
    album_id = IntegerField(column_name='AlbumID')
    media_type_id = IntegerField(column_name='MediaTypeId')
    genre_id = IntegerField(column_name='GenreId')
    composer = TextField(column_name='Composer')
    milliseconds = IntegerField(column_name='Milliseconds')
    bytes = IntegerField(column_name='Bytes')
    unit_price = IntegerField(column_name='UnitPrice')

    class Meta:
        table_name = 'tracks'


def get_tracks_names(album_name: str) -> None:
    quare = Track.select().where(Track.album_id == Album.get(Album.album_name == album_name))
    for track in quare:
        print(track.track_name)


if __name__ == '__main__':
    data_users = input('Enter album name: ')
    get_tracks_names(data_users)