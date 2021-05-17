from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
import data_parser as dp

template_path = r"../printout-templates/spotify-printout-template.png"
qrcode_path = r"../SpotifyPrintoutGenerator/qr_codes/code.jpg"
printout_path = '../SpotifyPrintoutGenerator/assets/generated-printout.png'
pdf_path = '../SpotifyPrintoutGenerator/assets/generated-printout.pdf'

title_font = ImageFont.truetype(
    "../printout-templates/fonts/CircularStd-Black.ttf", 26)
body_font = ImageFont.truetype(
    "../printout-templates/fonts/CircularStd-Book.ttf", 20)


def generate_printout(data):
    """Generates the printout for a given Spotify playlist/album"""
    image_url = data["image"]

    template = Image.open(template_path)

    # transposing cover art image
    cover_image = Image.open(requests.get(
        image_url, stream=True).raw)
    cover_image = cover_image.transpose(Image.ROTATE_180)
    # 640 x 640

    # resizing and placing qr code
    qr_code = Image.open(qrcode_path)
    qr_code = qr_code.resize(
        (round(qr_code.size[0]*0.75), round(qr_code.size[1]*0.75)))

    # placing cover art image
    template.paste(cover_image, (0, 0))
    # placing qr code
    template.paste(qr_code, (170, 800))

    # Displaying the image
    template.save(printout_path, format="png", subsampling=0, quality=100)

    # adding title and song text
    with_text = Image.open(printout_path)
    draw = ImageDraw.Draw(with_text)
    fitted_title = fit_text_in_bounds(data["title"], title_font)
    title_position = calculate_text_position(fitted_title, title_font)
    current_height = 665

    # draw title

    draw.text((title_position, current_height),
              fitted_title, (0, 0, 0), font=title_font)
    current_height += 20

    # draw songs
    draw_songs_text(current_height, draw, data["songs"])

    with_text.save(printout_path, format="png", subsampling=0, quality=100)

    rgba = Image.open(printout_path)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))
    # paste using alpha channel as mask
    rgb.paste(rgba, mask=rgba.split()[3])
    rgb.save(pdf_path, 'PDF', resoultion=100.0)


def draw_songs_text(current_height, draw, songs):
    """Draws the text for each song (up to 15) on the printout"""
    for i in range(len(songs)):
        current_height += 33
        if (i > 14):
            add_and_more(current_height, draw)
            break
        song_and_num = str(i+1) + ". " + songs[i]
        # fit text in bounds
        fitted_text = fit_text_in_bounds(song_and_num, body_font)
        song_position = calculate_text_position(fitted_text, body_font)
        draw.text((song_position, current_height),
                  fitted_text, (0, 0, 0), font=body_font)


def fit_text_in_bounds(text, font):
    """Checks that text fits within the bounds of the printout section and returns a string that fits within the bounds"""
    text_width = get_text_dimensions(text, font)
    if (text_width <= 530):
        return text
    chopped_text = ""
    for i in range(len(text)):
        chopped_text += text[i]
        current_width = get_text_dimensions(chopped_text, font)
        if (current_width > 530):
            break
    chopped_text += "..."
    return chopped_text


def add_and_more(current_height, draw):
    """If a playlist or album has more than 15 songs, 'And More!' is added to save space"""
    position = calculate_text_position("And More!", body_font)
    draw.text((position, current_height),
              "And More!", (0, 0, 0), font=body_font)


def calculate_text_position(string, font):
    """Calculates the starting point where a text string will be drawn"""
    text_width = get_text_dimensions(string, font)
    start_position = 640 + ((640 - text_width)/2)
    return start_position


def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    text_width = font.getmask(text_string).getbbox()[2]
    return (text_width)


def main():
    print("Enter a playlist or album")
    url = input()
    generate_printout(dp.route_album_or_playlist(url))


if __name__ == "__main__":
    main()
