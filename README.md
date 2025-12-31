# BookStore API

A robust RESTful API built with Django and Django REST Framework (DRF) for managing a bookstore. This project supports book management, user authentication via JWT, and comprehensive filtering capabilities.

## 🚀 Features

- **Book Management**: Full CRUD operations for books.
- **User Authentication**: Secure login and registration using JSON Web Tokens (JWT).
- **Filtering & Searching**: Advanced filtering for books using `django-filter`.
- **API Documentation**: Built with Django REST Framework's browsable API.

## 🛠️ Technology Stack

- **Backend**: Django 5.0.7
- **API Framework**: Django REST Framework 3.15.2
- **Authentication**: SimpleJWT 5.4.0
- **Database**: SQLite (default, configurable)

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/delan75/book-store-api.git
   cd book-store-api
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## 🔐 Authentication

This API uses JWT for authentication. 
- **Endpoint**: `/api/token/` (to obtain tokens)
- **Endpoint**: `/api/token/refresh/` (to refresh tokens)

Include the token in the header of your requests:
`Authorization: Bearer <your_access_token>`

## 📁 Project Structure

- `BookApp/`: Handles book-related logic and endpoints.
- `UserApp/`: Handles user registration and authentication.
- `BookStore/`: Project configuration and settings.

## 📝 License

This project is licensed under the MIT License.
