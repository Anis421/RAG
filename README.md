I used already available models for the responses. The better option would be local models as it doesnot need APIs and there are no error like "model too busy" which I faced quite a lot.
The interface was made using streamlit, it is pretty straight forward and easy to use.
Since this was a quick prototype of the RAG system streamlit is a better choice but you can use Tkinter for better control over the UI and for offline usage.

Used two different apporach for movie details and movie trailer.
-As youtube is very dynamic so using beautifulsoup did not get the actual video link.
-I used YoutubeSearch which is quite outdated but works just fine.
-Rather than google search used Open Movie Database(omdb) for getting the information of the movie.
