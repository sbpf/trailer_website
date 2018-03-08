import webbrowser


class Movie():
    """ This class has a few properties associated with
    movies and has a function that plays trailers"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_video_url):
        """ This constructor sets the properties of a movie such as title,
        storyline, poster image link and a trailer video link """
        self.title = movie_title
        storyline = movie_storyline
        self.poster_image = poster_image_url
        self.trailer_url = trailer_video_url

    def show_trailer(self):
        """ This function plays the trailer of the selected movie """
        webbrowser.open(self.trailer_url)
