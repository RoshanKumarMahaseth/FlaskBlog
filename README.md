# Flask Blog

A beginner-friendly blog application built with Python and Flask as part of my backend development learning journey. This project demonstrates authentication, database integration, and Flask best practices.

## Features

- Home Page
- About Page
- User Registration
- User Login & Logout
- Form Validation using Flask-WTF
- Password Hashing with Flask-Bcrypt
- User Authentication
- Flash Messages
- SQLite Database with SQLAlchemy
- Clean Flask Project Structure

## Tech Stack

- Python
- Flask
- Flask-WTF
- Flask-Bcrypt
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS

## Project Structure

```
flaskblog/
├── static/
├── templates/
├── forms.py
├── models.py
├── routes.py
├── __init__.py
├── instance/
│   └── site.db
└── run.py
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/RoshanKumarMahaseth/FlaskBlog.git
```

2. Navigate to the project directory

```bash
cd FlaskBlog
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python run.py
```

5. Open your browser and visit

```
http://127.0.0.1:5000
```

## Future Improvements

- User Profile Pictures
- Create, Update & Delete Blog Posts (CRUD)
- Password Reset via Email
- Flask-Migrate
- Pagination
- REST API
- Deployment

## Learning Purpose

This project is part of my backend development journey with Flask. It is continuously updated as I learn new concepts such as authentication, databases, ORM, and web application development.