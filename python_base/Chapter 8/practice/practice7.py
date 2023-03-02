# 8.7
def make_album(musician_name, album_name, track_number = None):
	music_album = {'name': musician_name, 'album': album_name}
	if track_number:
		music_album['tracks'] = track_number

	return music_album

music_album = make_album('musician1', 'album1')
print(music_album)

music_album = make_album('musician2', 'album2', track_number = 5)
print(music_album)

music_album = make_album('musician3', 'album3')
print(music_album)