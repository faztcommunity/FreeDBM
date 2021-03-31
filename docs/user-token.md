[Back to Home](../../../)

# **Obtain a user's token**
* ![POST](https://img.shields.io/badge/POST-brigthgreen.png?logo=data:image/png;base64,DATA") `/v2/user/token/`

## **Request**
|Name  | Data type |Required /Optional | Description |
|--|--| -- |--|
| username |  string |  required  | Username to be used to identify yourself within the api  |
| password| string | required   | Password to be used to access inside the api  |
___
### **Example request**
```bash
curl --request POST \
  --url http://localhost:8000/v2/user/token/ \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data username=christiand96 \
  --data password=christiand96
```
  
### **Example response**
```json
{
  "Token": "bbf70f387f23affbf9f74bb262a262b3460dc2a8",
  "username": "christiand96",
  "status": 200,
  "message": "This is your token"
}
```
___


[Back to Home](../../../)
