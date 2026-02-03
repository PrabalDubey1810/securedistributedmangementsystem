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
