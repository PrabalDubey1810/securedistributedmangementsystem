REGISTER Using Postman

Let’s create user.

✅ Step 1: New Request

Open Postman → Click New → HTTP Request

✅ Step 2: Set Method + URL

Top bar:

POST
http://localhost:8000/auth/register

✅ Step 3: Set Body

Click:

Body → raw → JSON

Paste:

{
  "username": "prabal",
  "password": "1234"
}

✅ Step 4: Send

Click Send.

✅ Response (Success)
{
  "msg": "Registered"
}


🎉 User created.





LOGIN Using Postman

Now login.

✅ Step 1: New Request

Method:

POST
http://localhost:8000/auth/login

✅ Step 2: Body (JSON)
{
  "username": "prabal",
  "password": "1234"
}

✅ Step 3: Send

Response:

{
  "token": "eyJhbGciOiJIUzI1..."
}


Copy this token.





ACCESS PROTECTED DATA (Important Part)

Now we use token.

✅ Step 1: New Request

Method:

GET
http://localhost:8000/data

✅ Step 2: Add Header

Click:

Headers


Add:

Key	Value
Authorization	Bearer YOUR_TOKEN

Example:

Bearer eyJhbGciOiJIUzI1...


⚠️ Include "Bearer " before token.

✅ Step 3: Send

Response:

{
  "data": "Welcome to private data"
}


🎉 Success.

