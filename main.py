from flask import Flask, render_template, request
from flask import url_for, redirect
import tmdb_client

app = Flask(__name__)

app.secret_key = "secret"


@app.route("/")
def homepage():
    selected_list = request.args.get("list_type", "popular")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, list_type=selected_list)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)

    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)


if __name__ == "__main__":
    app.run(debug=True)
