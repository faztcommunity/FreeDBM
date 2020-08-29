#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from flask_script import Command
from app.json import JSON
from app.models import db
from .create_director_table import Director
from .create_actors_table import Actor
from .create_genres_table import Gener
from .create_users_table import User
from .create_movies_table import Movie


class LoadMoviesInfo(Command):

    def run(self):

        def get_directordb(query):
            return db.session.query(Director).filter_by(fullname=query)

        def add_director_table(add):
            movie.director.append(add)

        def add_director(add):
            add_director = Director(fullname=add)
            db.session.add(add_director)
            add_director_table(add_director)

        def get_genredb(query):
            return db.session.query(Gener).filter_by(genere_name=query)

        items = JSON.json_movies('movies')
        i = 0
        for item in items:
            id_movie = item['id']
            title = item['title']

            get_movie = db.session.query(Movie).filter_by(title=title)

            if(get_movie.scalar() is None):
                year = item['year'].replace('(', '').replace(')', '')
                runtime = item['runtime']
                poster = item['urlImg']
                synopsis = item['synopsis']
                raiting = item['raiting']

                movie = Movie(title=title, year=year, runtime=runtime,
                              poster=poster, synopsis=synopsis, imdb_rating=raiting)
                db.session.add(movie)

                fullname_director = item['director']

                if(type(fullname_director) != str):
                    for i in range(0, len(fullname_director)):
                        get_director = get_directordb(fullname_director[i])
                        if(get_director.scalar() is None):
                            add_director(fullname_director[i])
                        else:
                            add_director_table(get_director.first())
                else:
                    get_director = get_directordb(fullname_director)
                    if(get_director.scalar() is None):
                        add_director(fullname_director)
                    else:
                        add_director_table(get_director.first())

                genere_name = item['genres']
                if(type(genere_name) != str):
                    for i in range(0, len(genere_name)):
                        get_genre = get_genredb(genere_name[i])
                        if(get_genre.scalar() is None):
                            add_genre = Gener(genere_name=genere_name[i])
                            db.session.add(add_genre)
                            movie.genre.append(add_genre)
                        else:
                            movie.genre.append(get_genre.first())
                else:
                    get_genre = get_genredb(genere_name)
                    if(get_genre.scalar() is None):
                        add_genre = Gener(genere_name=genere_name)
                        db.session.add(add_genre)
                        movie.genre.append(add_genre)
                    else:
                        movie.genre.append(get_genre.first())

                fullname_actors = item['actors']
                if(type(fullname_actors) != str):
                    for i in range(0, len(fullname_actors)):
                        get_actors = db.session.query(Actor).filter_by(
                            fullname=fullname_actors[i])
                        if(get_actors.scalar() is None):
                            add_actor = Actor(fullname=fullname_actors[i])
                            db.session.add(add_actor)
                            movie.actor.append(add_actor)
                        else:
                            movie.actor.append(get_actors.first())
                else:
                    get_actors = db.session.query(
                        Actor).filter_by(fullname=fullname_actors)
                    if(get_actors.scalar() is None):
                        add_actor = Actor(fullname=fullname_actors)
                        db.session.add(add_actor)
                        movie.actor.append(add_actor)
                    else:
                        movie.actor.append(get_actors.first())

                db.session.commit()
            print("Movies Info Add Successfully")
