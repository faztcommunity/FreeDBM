[Back to Home](../../../)

# **Get a genre by id**

* ![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA")`/v2/genre/{genre_id}` 

## **Request**

Header:

**`Authorization:`**`Token bbf70f387f23affbf9f74bb262a262b3460dc2a8`
___
### **Example request**
```bash
curl --request GET \
  --url http://localhost:8000/v2/gener/1 \
  --header 'authorization: Token bbf70f387f23affbf9f74bb262a262b3460dc2a8'
```

### **Example response**
```json{error=TRUE} 
{
  "genre":[
    {
      "id": 1,
      "genere_name": "Comedy"
    }
  ],
  "movies":[
    {"id": 1, "title": "Dil Bechara", "year": "2020", "runtime": 101,…},
    {"id": 3, "title": "Puñales por la espalda", "year": "2019", "runtime": 130,…},
    {"id": 5, "title": "The Gentlemen: Los señores de la mafia", "year": "2019", "runtime": 113,…}
  ]
}
```
___

### **Return values**
* **genre** - genre information
  * **id** - unique identifier for genre
  * **genere_name** - genre name
* **movies** - movies related to the genre
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
