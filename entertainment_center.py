import fresh_tomatoes
import media


vivegam = media.Movie("VIVEGAM",
                        "It is a spy thriller movie.",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyYsRMpN53nXkvTnbrgCYXYttYk0qcT1A0D7JA32c9jn9WtrWX",
                        "https://youtu.be/uM7zTAMFRxc")



movies = [vivegam]
fresh_tomatoes.open_movies_page(movies)
