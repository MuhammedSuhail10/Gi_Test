# Django CSV Import API

## Overview
This Django project provides an API endpoint to import user leads from a CSV file. The `import_leads` endpoint processes the uploaded file and returns the count of imported, existing, and erroneous entries.

## Features
- Accepts CSV file uploads.
- Parses and validates data.
- Handles errors gracefully.
- Returns summary statistics of imported and existing records.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Django REST Framework

## Setup
1. **Clone the Repository:**
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Start the Server:**
   ```sh
   python manage.py runserver
   ```

## API Usage
### Import Leads
#### Endpoint:
```
POST /api/user/import_leads
```
#### Request:
Upload a CSV file containing user leads. Example request using `curl`:
```sh
curl -X POST -F "file=@leads.csv" http://127.0.0.1:8000/api/user/import_leads/
```
#### Response:
```json
{
    "status": true,
    "message": "Extraction Completed",
    "imported_count": 4,
    "existing_count": 1,
    "error_data": [
        {"name": "John Doe", "email": "john@example.com", "age": "-1", "error": "Invalid age"}
    ]
}
```

## Running Tests
To run the test cases for the import feature, execute:
```sh
python manage.py test
```
The test suite includes:
- **`test_csv_import_data`**: Tests CSV import with various valid and invalid entries.
- **`test_csv_file_import`**: Tests file upload with a predefined CSV file.

## Middleware Test API
### Overview
This API provides an endpoint to test middleware functionality and request handling.

### Endpoint:
```
GET /api/middle/middleware_test
```
#### Request:
Example request using `curl`:
```sh
curl -X GET http://127.0.0.1:8000/api/middle/middleware_test/
```
#### Response:
```json
{
    "message": "Request successful!"
}
```

## Running Middleware Test
To test rate limiting or middleware constraints, execute:
```sh
python manage.py test
```
The test suite includes:
- **`test_requests_limit`**: Sends multiple GET requests to validate request limits.

## File Structure
```
UserExtraction/
│-- UserExtraction/
│-- user/
│   │-- views.py  # Contains import_leads and middleware_test API
│   │-- models.py  # User model
│   │-- asset/
│   │   │-- user.csv  # CSV file
│   │-- utils/
│   │   │-- csv_util.py  # CSV processing logic
│   │-- tests.py  # Test cases for APIs
│-- manage.py  # Django management script
│-- MiddleWareTest/
│   │-- views.py  # Contains import_leads and middleware_test API
│   │-- models.py  # User model
│   │-- middleware.py
│   │-- tests.py  # Test cases for APIs
│-- manage.py  # Django management script
│-- requirements.txt  # Dependencies
```

## Notes
- Ensure the CSV file contains `name`, `email`, and `age` columns.
- Invalid data (e.g., negative ages or missing emails) will be reported in the response.
- The `csv_fetch` utility is responsible for parsing and validating records.
- Middleware test checks request limits to ensure performance and security.
