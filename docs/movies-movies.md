[Back to Home](../../../)

# **Get all stored movies**

* ![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA")`/v2/movies/`

## **Request**

Header:

**`Authorization:`**`Token bbf70f387f23affbf9f74bb262a262b3460dc2a8`
___
### **Example request**
```bash
curl --request GET \
  --url http://localhost:8000/v2/movies/ \
  --header 'authorization: Token bbf70f387f23affbf9f74bb262a262b3460dc2a8'
```

### **Example response**
```json{error=TRUE} 
[
  {
    "id": 1,
    "title": "Dil Bechara",
    "year": "2020",
    "runtime": 101,
    "poster": "https://m.media-amazon.com/images/M/MV5BNmI0MTliMTAtMmJhNC00NTJmLTllMzQtMDI3NzA1ODMyZWI1XkEyXkFqcGdeQXVyODE5NzE3OTE@.jpg",
    "synopsis": "The emotional journey of two hopelessly in love youngsters, a young girl, Kizie, suffering from cancer, and a boy, Manny, whom she meets at a support group.",
    "genre":[{"id": 1, "genere_name": "Comedy" }, {"id": 2, "genere_name": "Drama"…],
    "director":[{"id": 1, "fullname": "Mukesh Chhabra" }],
    "actor":[{"id": 1, "fullname": "Sushant Singh Rajput" }, {"id": 2, "fullname": "Sanjana Sanghi"…],
    "imdb_rating": "9.0"
  },
  {"id": 2, "title": "Hamilton", "year": "2020", "runtime": 160,…},
  {"id": 3, "title": "Puñales por la espalda", "year": "2019", "runtime": 130,…},
  {"id": 4, "title": "Lo que el viento se llevó", "year": "1939", "runtime": 238,…},
  {"id": 5, "title": "The Gentlemen: Los señores de la mafia", "year": "2019", "runtime": 113,…}
]
```
___

### **Return values**

* **id** - unique identifier for movie 
* **title** - movie title
* **year** - year of the movie
* **runtime** - movie duration in minutes
* **poster** - cover image the movie
* **synopsis** - summary of the movie
* **genre** - classification of the film by genre
* **director** - director(s) of the film
* **actor** - actor(s) of the film
* **imdb_rating** - movie score according to Internet Movie Database (IMDb)

___

[Back to Home](../../../)
