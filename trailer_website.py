import fresh_tomatoes
import media

# Harry Potter movie: Title, storyline, image and trailer link
harry_potter = media.Movie(
    "Harry Potter",
    "Story of an adventurous teenage wizard who gets"
    "into a School of Witchcraft and Wizardry",
    "https://i.ytimg.com/vi/xLWRfRyhEjE/maxresdefault.jpg",
    "https://www.youtube.com/watch?v=kTzuxWN94PA"
    )

# Pursuit of Happiness movie: Title, storyline, image and trailer link
pursuit_of_happyness = media.Movie(
    "Pursuit Of Happyness",
    "A Biographical drama film based on entrepreneur"
    "Chis Gardner's nearly one year struggle being homeless.",
    "http://daxushequ.com/data/out/98/img60107496.png",
    "https://www.youtube.com/watch?v=89Kq8SDyvfg"
    )

# Beautiful Mind movie: Title, storyline, image and trailer link
beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "American biographical drama film based on the life of"
    "John Nash, a Nobel Laureate in Economics.",
    "https://upload.wikimedia.org/wikipedia/sh/9/98/Abeautifulmindposter.jpg",
    "https://www.youtube.com/watch?v=aS_d0Ayjw4o"
    )

# Adding all the instances created to a list called "movies"
movies = [
    harry_potter,
    pursuit_of_happyness,
    beautiful_mind
    ]

# opening the HTML file via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
