# Blog API with Django Rest Framework

This is a simple blog API built with Django Rest Framework. The API supports CRUD operations for authors, categories, tags, posts, and comments.

## Features

- Manage authors, categories, tags, posts, and comments.
- Supports CRUD operations for all entities.
- Uses UUID as primary keys for all models.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django Rest Framework

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/blog-api-drf.git
   cd blog-api-drf
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file for your environment variables (if necessary).**

5. **Apply the migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

7. **Run the server:**

   ```sh
   python manage.py runserver
   ```

8. **Access the API:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## API Endpoints

Here is a list of the available API endpoints.

### Authors

- **GET /authors/**: List all authors
- **POST /authors/**: Create a new author
- **GET /authors/{uuid}/**: Retrieve a single author by UUID
- **PUT /authors/{uuid}/**: Update an author by UUID
- **DELETE /authors/{uuid}/**: Delete an author by UUID

### Categories

- **GET /categories/**: List all categories
- **POST /categories/**: Create a new category
- **GET /categories/{uuid}/**: Retrieve a single category by UUID
- **PUT /categories/{uuid}/**: Update a category by UUID
- **DELETE /categories/{uuid}/**: Delete a category by UUID

### Tags

- **GET /tags/**: List all tags
- **POST /tags/**: Create a new tag
- **GET /tags/{uuid}/**: Retrieve a single tag by UUID
- **PUT /tags/{uuid}/**: Update a tag by UUID
- **DELETE /tags/{uuid}/**: Delete a tag by UUID

### Posts

- **GET /posts/**: List all posts
- **POST /posts/**: Create a new post
- **GET /posts/{uuid}/**: Retrieve a single post by UUID
- **PUT /posts/{uuid}/**: Update a post by UUID
- **DELETE /posts/{uuid}/**: Delete a post by UUID

### Comments

- **GET /comments/**: List all comments
- **POST /comments/**: Create a new comment
- **GET /comments/{uuid}/**: Retrieve a single comment by UUID
- **PUT /comments/{uuid}/**: Update a comment by UUID
- **DELETE /comments/{uuid}/**: Delete a comment by UUID

## Testing with Postman

Use Postman to test the API endpoints. Here's an example of how to configure requests in Postman:

1. **Get All Authors:**

   - Method: GET
   - URL: `http://127.0.0.1:8000/authors/`

2. **Create an Author:**
   - Method: POST
   - URL: `http://127.0.0.1:8000/authors/`
   - Headers:
     - Content-Type: application/json
   - Body:
     ```json
     {
       "name": "John Doe",
       "email": "john@example.com",
       "bio": "A passionate writer."
     }
     ```

Continue this pattern for other endpoints as described in the "API Endpoints" section.

## Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

