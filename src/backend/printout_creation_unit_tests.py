from PIL import ImageChops
from PIL import Image
import image_overlay as io
import data_parser as dp

album_url = "https://open.spotify.com/album/3CCnGldVQ90c26aFATC1PW"
playlist_url = "https://open.spotify.com/playlist/1XFwoqu2ARL1EF2zN9ifn4"


def test_proper_printout_album():
    """Generates a album new printout and compares it to a test one"""
    io.generate_printout(dp.route_album_or_playlist(album_url))
    generated_image = Image.open(
        "../SpotifyPrintoutGenerator/assets/generated-printout.png")
    test_image = Image.open(
        "../SpotifyPrintoutGenerator/assets/test-printout-album.png")
    diff = ImageChops.difference(generated_image, test_image)
    if diff.getbbox():
        print("images are different")
    else:
        print("images are the same")
    assert(diff.getbbox() is None)
    print("test_proper_printout_album PASSED")


def test_proper_printout_playlist():
    """Generates a new playlist printout and compares it to a test one"""
    io.generate_printout(dp.route_album_or_playlist(playlist_url))
    generated_image = Image.open(
        "../SpotifyPrintoutGenerator/assets/generated-printout.png")
    test_image = Image.open(
        "../SpotifyPrintoutGenerator/assets/test-printout-playlist.png")
    diff = ImageChops.difference(generated_image, test_image)
    assert(diff.getbbox() is None)
    print("test_proper_printout_playlist PASSED")


def main():
    test_proper_printout_album()
    test_proper_printout_playlist()
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()
