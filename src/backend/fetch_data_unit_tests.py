import data_parser as dp
from os import path

# urls used for testing
album_url = "https://open.spotify.com/album/1Mhn9VosyjtWn4dMPFlna6"
album_url_alt = "https://open.spotify.com/album/1Mhn9VosyjtWn4dMPFlna6?si=GmJxCGb0RVO9FQEKzYerzQ"
playlist_url = "https://open.spotify.com/playlist/159oTbKcRiawEeALgEzS0i"
playlist_url_alt = "https://open.spotify.com/playlist/159oTbKcRiawEeALgEzS0i?si=14142c0c08914a04"
invalid_url = "https://open.spotify.com/artist/5MwmC9GWEcE2XK37NhkpIy"

# song lists used for test comparison
album_songs = ["Movin' Out (Anthony's Song)", 'The Stranger', 'Just the Way You Are', 'Scenes from an Italian Restaurant', 'Vienna', 'Only the Good Die Young', "She's Always a Woman", 'Get It Right the First Time', 'Everybody Has a Dream', 'Miami 2017 (Seen the Lights Go Out On Broadway) - Live at Carnegie Hall, New York, NY - June 1977', 'Prelude / Angry Young Man - Live at Carnegie Hall, New York, NY - June 1977', 'New York State of Mind - Live at Carnegie Hall, New York, NY - June 1977', 'Just the Way You Are - Live at Carnegie Hall, New York, NY - June 1977',
               "She's Got a Way - Live at Carnegie Hall, New York, NY - June 1977", 'The Entertainer - Live at Carnegie Hall, New York, NY - June 1977', 'Scenes from an Italian Restaurant - Live at Carnegie Hall, New York, NY - June 1977', 'Band Introductions - Live at Carnegie Hall, New York, NY - June 1977', 'Captain Jack - Live at Carnegie Hall, New York, NY - June 1977', "I've Loved These Days - Live at Carnegie Hall, New York, NY - June 1977", 'Say Goodbye to Hollywood - Live at Carnegie Hall, New York, NY - June 1977', 'Souvenir - Live at Carnegie Hall, New York, NY - June 1977']
playlist_songs = ['Glass Animals - Tokyo Drifting (with Denzel Curry)', 'Alice Ivy - In My Mind', 'Elah Hale - My House', 'easy life - dead celebrities', 'Still Woozy - Window', 'CHIKA - CROWN', 'Monsune - 1998', 'Aminé - Compensating (feat. Young Thug)', 'easy life - sangria', 'Slow Pulp - At It Again', 'MICHELLE - SUNRISE', 'Dominic Fike - Politics & Violence', 'Kota the Friend - Summerhouse', 'Tiny Meat Gang - Broke Bitch', 'Soccer Mommy - circle the drain', 'Boxout - Rock Bottom', 'Joji - MODUS', 'Yung Gravy - yup!', 'SEBASTIAN PAUL - IMPATIENT', 'Piff Marti - Regular People.', 'Joji - Mr. Hollywood', 'Jean Dawson - Clear Bones', 'Boxout - Seasick', 'LO LA - Cherries & Lemonade',
                  'JayXander - HOODIES', 'ROLE MODEL - going out', 'Whethan - Freefall (feat. Oliver Tree)', 'Beach Bunny - Promises', 'Boxout - Hyperloop', 'AViT - twitterloser', 'easy life - daydreams', 'AG Club - Memphis', 'Vita and the Woolf - Confetti', "Aries - FOOL'S GOLD", 'Machine Gun Kelly - bloody valentine', 'Oscar Welsh - Get Yourself To Sleep', 'beabadoobee - Care', 'Voda Fuji - Gummies!', 'Yves Tumor - Super Stars', 'mmmonika - kerosene', 'mazie - no friends', 'Voda Fuji - Mint Tea', 'PUP - Nothing Changes', 'Kuri Ken - bonafide', 'Dominic Fike - Why', 'carolesdaughter - Violent', 'qq - new blue rollerblades', 'boyponder - DISCODreams', 'Phoebe Bridgers - Kyoto', 'Aries - CONVERSATIONS']

# image links used for test comparison
album_image = "https://i.scdn.co/image/ab67616d0000b2736ce61113662ecf693b605ee5"
playlist_image = "https://i.scdn.co/image/ab67706c0000bebb5226e59f78376907e09e3804"


def test_parse_album_songs():
    songs = dp.get_album_songs(album_url)
    assert(len(songs) == 21)
    assert(songs == album_songs)
    print("test_parse_album_songs PASSED")


def test_parse_playlist_songs():
    songs = dp.get_playlist_songs(playlist_url)
    assert(len(songs) == 50)
    assert(songs == playlist_songs)
    print("test_parse_playlist_songs PASSED")


def test_parse_album_songs_alt():
    songs = dp.get_album_songs(album_url_alt)
    assert(len(songs) == 21)
    assert(songs == album_songs)
    print("test_parse_album_songs_alt PASSED")


def test_parse_playlist_songs_alt():
    songs = dp.get_playlist_songs(playlist_url_alt)
    assert(len(songs) == 50)
    assert(songs == playlist_songs)
    print("test_parse_playlist_songs_alt PASSED")


def test_get_album_title():
    title = dp.get_album_title(album_url)
    assert title == "Billy Joel - The Stranger (Legacy Edition)"
    print("test_get_album_title PASSED")


def test_get_playlist_title():
    title = dp.get_playlist_title(playlist_url)
    assert title == "BoxTop 50 [2020]"
    print("test_get_playlist_title PASSED")


def test_get_album_art():
    image = dp.get_album_image(album_url)
    assert image == album_image
    print("test_get_album_art PASSED")


def test_get_playlist_art():
    image = dp.get_playlist_image(playlist_url)
    assert image == playlist_image
    print("test_get_playlist_art PASSED")


def test_generate_qr_code_playlist():
    dp.generate_qr_code(album_url)
    assert path.exists('../SpotifyPrintoutGenerator/qr_codes/current_code.png')
    print("test_generate_qr_code_playlist PASSED")


def test_generate_qr_code_album():
    dp.generate_qr_code(album_url)
    assert path.exists('../SpotifyPrintoutGenerator/qr_codes/current_code.png')
    print("test_generate_qr_code_album PASSED")


def test_proper_route_album():
    parsed_album = dp.route_album_or_playlist(album_url)
    assert parsed_album["type"] == "album"
    assert parsed_album["songs"] == album_songs
    assert parsed_album["image"] == album_image
    print("test_proper_route_album PASSED")


def test_proper_route_playlist():
    parsed_playlist = dp.route_album_or_playlist(playlist_url)
    assert parsed_playlist["type"] == "playlist"
    assert parsed_playlist["songs"] == playlist_songs
    assert parsed_playlist["image"] == playlist_image
    print("test_proper_route_playlist PASSED")


def test_proper_route_album_alt():
    parsed_album = dp.route_album_or_playlist(album_url_alt)
    assert parsed_album["type"] == "album"
    assert parsed_album["songs"] == album_songs
    assert parsed_album["image"] == album_image
    print("test_proper_route_album_alt PASSED")


def test_proper_route_playlist_alt():
    parsed_playlist = dp.route_album_or_playlist(playlist_url_alt)
    assert parsed_playlist["type"] == "playlist"
    assert parsed_playlist["songs"] == playlist_songs
    assert parsed_playlist["image"] == playlist_image
    print("test_proper_route_playlist_alt PASSED")


def test_proper_route_invalid():
    '''Tests that an invalid link returns an error object'''
    assert dp.route_album_or_playlist(invalid_url)["error"] is not None
    print("test_proper_route_invalid PASSED")


def main():
    test_parse_album_songs()
    test_parse_playlist_songs()
    test_parse_album_songs_alt()
    test_parse_playlist_songs_alt()
    test_get_album_title()
    test_get_playlist_title()
    test_get_album_art()
    test_get_playlist_art()
    test_generate_qr_code_album()
    test_generate_qr_code_playlist()
    test_proper_route_album()
    test_proper_route_playlist()
    test_proper_route_album_alt()
    test_proper_route_playlist_alt()
    test_proper_route_invalid()
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()
