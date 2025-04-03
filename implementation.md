# Implementation Details

## 1. Technology Stack
1. Backend Framework: Django REST Framework
   - Chosen for its robust API development capabilities
   - Built-in serialization and viewset support
   - Excellent documentation and community support

2. Database: SQLite
   - Suitable for development and demonstration
   - No additional setup required
   - Easy to migrate to PostgreSQL for production

3. Dependency Management: Poetry
   - Modern Python dependency management
   - Deterministic builds with poetry.lock
   - Easy virtual environment management

4. Background Tasks: django-background-tasks
   - Handles email sending in the background
   - Prevents API blocking during email operations
   - Built-in task scheduling and management

## 2. Project Setup
1. Initialize project using Poetry
2. Install dependencies:
   - django
   - djangorestframework
   - django-background-tasks
3. Create Django project and app
4. Configure settings and database
5. Run migrations

## 3. API Documentation

### Nonprofit Management API (/api/nonprofits/)
1. List All Nonprofits
   - Method: GET
   - Endpoint: /api/nonprofits/
   - Response: List of all nonprofits with their details

2. Create Nonprofit
   - Method: POST
   - Endpoint: /api/nonprofits/
   - Payload Example:
     ```json
     {
       "name": "Example Nonprofit",
       "address": "123 Main St, City, State 12345",
       "email": "contact@nonprofit.org"
     }
     ```

3. Get Specific Nonprofit
   - Method: GET
   - Endpoint: /api/nonprofits/{id}/
   - Response: Details of specific nonprofit

4. Update Nonprofit
   - Method: PUT
   - Endpoint: /api/nonprofits/{id}/
   - Payload: Same as Create Nonprofit

5. Delete Nonprofit
   - Method: DELETE
   - Endpoint: /api/nonprofits/{id}/

### Bulk Email API (/api/send-bulk-email/)
1. Send Bulk Emails
   - Method: POST
   - Endpoint: /api/send-bulk-email/
   - Payload Example:
     ```json
     {
       "nonprofit_emails": [
         "nonprofit1@example.com",
         "nonprofit2@example.com"
       ],
       "template_body": "Sending money to nonprofit {name} at address {address}"
     }
     ```
   - Description: Sends templated emails to multiple nonprofits
   - Template Variables:
     - {name}: Replaced with nonprofit's name
     - {address}: Replaced with nonprofit's address

### Email Log API (/api/emails/)
1. List All Sent Emails
   - Method: GET
   - Endpoint: /api/emails/
   - Response: Lists all sent emails with their details
     - Recipient information
     - Subject
     - Email body
     - Sent timestamp

## 4. Running the Application
1. Start the Django development server:
   ```bash
   poetry run python manage.py runserver
   ```

2. Start the background task worker:
   ```bash
   poetry run python manage.py process_tasks
   ```

## 5. Testing
1. Use tools like Postman or curl to test the APIs
2. Example curl commands:
   ```bash
   # Create a nonprofit
   curl -X POST http://localhost:8000/api/nonprofits/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Test Nonprofit", "address": "123 Test St", "email": "test@nonprofit.org"}'

   # Send bulk emails
   curl -X POST http://localhost:8000/api/send-bulk-email/ \
     -H "Content-Type: application/json" \
     -d '{"nonprofit_emails": ["test@nonprofit.org"], "template_body": "Hello {name} at {address}"}'

   # List sent emails
   curl http://localhost:8000/api/emails/
   ```