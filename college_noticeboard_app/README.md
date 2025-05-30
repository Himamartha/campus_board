# College Notice Board

A Django-based web application for managing college notices with department-wise organization and different types of notices.

## Features

- User authentication (login/register)
- Department-wise notice organization
- Different types of notices (Academic, Event, Exam, etc.)
- Notice expiration dates
- Important notice highlighting
- Admin-only notice management
- Modern and responsive UI

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd college_noticeboard_app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Usage

1. Register a new account or login with existing credentials
2. Regular users can view notices and filter by department/type
3. Admin users can create, edit, and delete notices
4. Notices can be marked as important and have expiration dates

## Technologies Used

- Django 5.0.2
- Bootstrap 5
- Font Awesome
- SQLite (default database)
- Crispy Forms

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 