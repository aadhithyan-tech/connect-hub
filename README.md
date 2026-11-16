# ConnectHub — Mini Social Media App

A beginner-friendly social media project built with Django, SQLite, HTML, CSS and JavaScript.

## Features
- Register, log in and log out
- Automatically created user profiles; edit bio and profile picture
- Create posts with optional images
- Like/unlike posts (one like per user per post)
- Comment on posts
- Follow/unfollow users
- Personal feed and profile pages
- Django admin dashboard

## Run on macOS

Open Terminal and move into this project folder:

```bash
cd connecthub
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Register a normal account to use the app. The admin dashboard is at
http://127.0.0.1:8000/admin/ (use the superuser created above).

## Notes
- SQLite database is created automatically as `db.sqlite3`.
- Uploaded images are stored in the `media/` folder.
- This is a local learning/demo project. Before public deployment, set `DEBUG = False`,
  use a strong secret key from environment variables, configure `ALLOWED_HOSTS`,
  HTTPS, static/media hosting, and production database settings.
