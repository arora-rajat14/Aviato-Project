# Aviato-Project

## Aviato-Project

## Features

Create, update, delete candidates.
Search candidates by name, sorted by the number of matching words in the search query.

## Technologies Used

Python 3.x
Django 5.x
Django Rest Framework

## Installation

## Set up a Virtual Environment

Using Poetry:

`poetry install`
`poetry shell`

For SQLite (default):

`python manage.py migrate`

## Run migrations:

`python manage.py migrate`
Create a Superuser (Optional)
To access Django Admin, create a superuser:

`python manage.py createsuperuser`

## Run the Server

`python manage.py runserver`
The API should now be accessible at http://127.0.0.1:8000/.

## API Endpoints

1. Create a Candidate
   URL: /api/candidates/
   Method: POST
   Request Body:
   {
   "name": "John Doe",
   "age": 30,
   "gender": "Male",
   "email": "john.doe@example.com",
   "phone_number": "+1234567890"
   }
   Response:
   {
   "id": "uuid-string-here",
   "name": "John Doe",
   "age": 30,
   "gender": "Male",
   "email": "john.doe@example.com",
   "phone_number": "+1234567890",
   "created_at": "2024-09-14T14:45:22Z",
   "modified_at": "2024-09-14T14:45:22Z"
   }
2. Update a Candidate
   URL: /api/candidates/<uuid:id>/
   Method: PUT or PATCH
   Request Body (example for PUT):

   {
   "name": "Jane Doe",
   "age": 28,
   "gender": "Female",
   "email": "jane.doe@example.com",
   "phone_number": "+9876543210"
   }
   Response:

   {
   "id": "uuid-string-here",
   "name": "Jane Doe",
   "age": 28,
   "gender": "Female",
   "email": "jane.doe@example.com",
   "phone_number": "+9876543210",
   "created_at": "2024-09-14T14:45:22Z",
   "modified_at": "2024-09-14T14:45:22Z"
   }

3. Delete a Candidate
   URL: /api/candidates/<uuid:id>/
   Method: DELETE
   Response: 204 No Content (if successful)
4. Search Candidates by Name
   URL: /api/candidates/search/?q=<search_query>
   Method: GET
   Request Example:
   GET /api/candidates/search/?q=Ajay Kumar Yadav
   Response (sorted by relevancy):

   [
   {
   "id": "uuid-string-1",
   "name": "Ajay Kumar Yadav",
   "age": 30,
   "gender": "Male",
   "email": "ajay.yadav@example.com",
   "phone_number": "+1234567890",
   "created_at": "2024-09-14T14:45:22Z",
   "modified_at": "2024-09-14T14:45:22Z"
   },
   {
   "id": "uuid-string-2",
   "name": "Ajay Kumar",
   "age": 28,
   "gender": "Male",
   "email": "ajay.kumar@example.com",
   "phone_number": "+9876543210",
   "created_at": "2024-09-14T14:45:22Z",
   "modified_at": "2024-09-14T14:45:22Z"
   },
   {
   "id": "uuid-string-3",
   "name": "Kumar Yadav",
   "age": 35,
   "gender": "Male",
   "email": "kumar.yadav@example.com",
   "phone_number": "+1597534862",
   "created_at": "2024-09-14T14:45:22Z",
   "modified_at": "2024-09-14T14:45:22Z"
   }
   ]

## Notes:

The POST, PUT, and PATCH endpoints require data in JSON format.
The search endpoint accepts a query parameter q and returns a list of candidates sorted by relevancy (i.e., the number of matching words in the candidate's name).

python manage.py test
License
This project is licensed under the MIT License.
