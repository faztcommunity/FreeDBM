# FreeDBM
Python Rest API to see films information.

## Requirements
Code migrated from Flask to Django 


Django>=3.1.7

djangorestframework>=3.12.4

`pip install -r requirements.txt`

## Resource description

### User
Specifications for the registration, authentication and update of a user.

#### Endpoints and methods
* [![POST](https://img.shields.io/badge/POST-brigthgreen.png?logo=data:image/png;base64,DATA")`/v2/user/signup/`](docs/user-signup.md)

* [![POST](https://img.shields.io/badge/POST-brigthgreen.png?logo=data:image/png;base64,DATA") `/v2/user/token/`](docs/user-token.md)

* [![POST](https://img.shields.io/badge/POST-brigthgreen.png?logo=data:image/png;base64,DATA") `/v2/user/password-change/`](docs/user-pwd-change.md)

___


### Movies
Information about the films

#### Endpoints and methods

* [![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA") `/v2/movies/`](docs/movies-movies.md)

* [![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA")`/v2/movie/{movie_id}`](docs/movies-movie-id.md)

* [![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA")`/v2/geners/`](docs/movies-geners.md)

* [![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA") `/v2/gener/{genre_id}`](docs/movies-genre-id.md)

* ![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA") `/v2/actors/`

* ![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA")`/v2/actor/{actor_id}`

* ![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA") `/v2/directors/`

* ![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA")`/v2/director/{director_id}`
___



## [How to contribute](https://github.com/faztcommunity/fazt-community-docs/blob/docs/docs/README.md)
You can also contact   **Jose Gonzalez** [GitHub](https://github.com/jsgonzlez661)

## Contributors
* **Jose Gonzalez** [GitHub](https://github.com/jsgonzlez661)
* **Erick Vargas** [GitHub](https://github.com/erianvc)
* **Andres Bermeo** [GitHub](https://github.com/andipandiber)

## [License](./LICENSE)
