[Back to Home](../../../)

# **User registration**
* ![POST](https://img.shields.io/badge/POST-brigthgreen.png?logo=data:image/png;base64,DATA")`/v2/user/signup/`

## **Request**
|Name  | Data type |Required /Optional | Description |
|--|--| -- |--|
| username |  string |  required  | Username to be used to identify yourself within the api  |
| email | string   | required   |  Email that you will use to access within the api|
| password| string | required   | Password to be used to access inside the api  |
___
### **Example request**
```bash
curl --request POST \
  --url http://localhost:8000/v2/user/signup/ \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data username=christiand96 \
  --data email=christian.diaz@example.com \
  --data password=christiand96
```
  
### **Example response**
```json
{
  "user_data": {
    "username": "christiand96",
    "email": "christian.diaz@example.com"
  },
  "token": "bbf70f387f23affbf9f74bb262a262b3460dc2a8",
  "status": 201,
  "message": "Successfully registered"
}
```
___

[Back to Home](../../../)
