# 8.8 (code from 8.7)
def make_album(musician_name, album_name, track_number = None):
	music_album = {'name': musician_name, 'album': album_name}
	if track_number:
		music_album['tracks'] = track_number

	return music_album

while True:
	print("\nPlease enter the album info:")
	print("(enter 'q' at any time to quit)")

	m_name = input("Musician name: ")
	if m_name == 'q':
		break

	a_name = input("Album name: ")
	if a_name == 'q':
		break

	music_album = make_album(m_name,a_name)
	print(music_album)