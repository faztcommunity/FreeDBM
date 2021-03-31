[Back to Home](../../../)

# **Change password**

It is important to pass the token in the request header.
* ![POST](https://img.shields.io/badge/POST-brigthgreen.png?logo=data:image/png;base64,DATA") `/v2/user/password-change/`

## **Request**

Header:

**`Authorization:`**`Token bbf70f387f23affbf9f74bb262a262b3460dc2a8`
|Name  | Data type |Required /Optional | Description |
|--|--| -- |--|
| username |  string |  required  | Username to be used to identify yourself within the api  |
| password| string | required   | Password to be used to access inside the api  |

___
### **Example request**
```bash
curl --request POST \
  --url http://localhost:8000/v2/user/password-change/ \
  --header 'authorization: Token bbf70f387f23affbf9f74bb262a262b3460dc2a8' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data username=christiand96 \
  --data password=christiand96 \
  --data new_password=96christiand
```
  
### **Example response**
```json
{
  "status": 200,
  "message": "Successful password change"
}
```
___

[Back to Home](../../../)
