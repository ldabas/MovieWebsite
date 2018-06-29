import media
import fresh_tomatoes

#Create Movie objects to be displayed on the webpage
toy_story = media.Movie("Toy Story", " A story of a boy and his toys that come to life",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A Marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY&frags=pl%2Cwn")

tron_legacy = media.Movie("Tron Legacy", "User gets a clue",
                          "http://www.impawards.com/2010/posters/tron_legacy_xlg.jpg",
                          "https://www.youtube.com/watch?v=a1IpPpB3iWI")

school_of_rock = media.Movie("School of Rock", "Jack Black acts like himself",
                             "https://www.playbillstore.com/resize/Shared/Images/Product/School-of-Rock-the-Official-Broadway-Poster/Screen-Shot-2017-08-29-at-12.21.54-PM.png?bw=1000&w=1000&bh=1000&h=1000",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

django_unchained = media.Movie("Django Unchained", "Jamie Foxx shoots everybody",
                               "https://i.pinimg.com/736x/de/95/40/de9540a207248859a26e5aa924c3ffe1--style-movie-django-unchained.jpg",
                               "https://www.youtube.com/watch?v=6pKZbJHa17c")

john_wick = media.Movie("John Wick", "Keanu Reeves proves that the best acting is done without dialogue",
                        "http://www.impawards.com/2014/posters/john_wick.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

movies = [toy_story, avatar, tron_legacy, school_of_rock, django_unchained, john_wick]

#Display all the movies usng the open_movies_page method
fresh_tomatoes.open_movies_page(movies)