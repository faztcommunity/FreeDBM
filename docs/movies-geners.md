[Back to Home](../../../)

# **Get all movie genres**

* ![GET](https://img.shields.io/badge/GET-blue.png?logo=data:image/png;base64,DATA")`/v2/geners/`

## **Request**

Header:

**`Authorization:`**`Token bbf70f387f23affbf9f74bb262a262b3460dc2a8`
___
### **Example request**
```bash
curl --request GET \
  --url http://localhost:8000/v2/geners/ \
  --header 'authorization: Token bbf70f387f23affbf9f74bb262a262b3460dc2a8'
```

### **Example response**
```json{error=TRUE} 
[
  {
    "id": 1,
    "genere_name": "Comedy"
  },
  {"id": 2, "genere_name": "Drama"},
  {"id": 3, "genere_name": "Romance"},
  {"id": 4, "genere_name": "Biography"},
  {"id": 5, "genere_name": "History"},
  {"id": 6, "genere_name": "Crime"},
  {"id": 7, "genere_name": "Action"}
]
```
___

### **Return values**

* **id** - unique identifier for genre
* **genere_name** - genre name

___

[Back to Home](../../../)
