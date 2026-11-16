# ConnectHub — Mini Social Media Web Application

ConnectHub is a full-featured, responsive mini social media platform built with **Django**, **Python**, **SQLite**, and vanilla **HTML/CSS/JavaScript**. It allows users to create accounts, share posts with images, like and comment on content, follow other users, and view dynamic user feeds.

---

## 🚀 Key Features

- **User Authentication & Security:**
  - Secure registration, login, and logout flows.
  - Session-based authentication with CSRF protection.
- **Dynamic User Profiles:**
  - Automatic profile generation upon account registration.
  - Customizable profile bio and avatar picture upload.
  - Profile page showing user post history, follower count, and following count.
- **Social Feed & Content Creation:**
  - Publish posts with formatted text and optional image attachments.
  - Reverse-chronological personal feed.
- **Engaging Social Interactions:**
  - Interactive like/unlike system (one like per user per post enforced at database level).
  - Commenting system on posts.
  - Follow / unfollow functionality with self-follow prevention.
- **Admin Dashboard:**
  - Built-in Django administrative panel to manage users, posts, comments, likes, and follows.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Django 5.x
- **Database:** SQLite3
- **Image Processing:** Pillow
- **Frontend:** HTML5, CSS3, JavaScript
- **Version Control:** Git

---

## 📁 Project Structure

```text
connecthub/
├── config/              # Django project settings and root routing
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── social/              # Main social app (models, views, forms, signals)
│   ├── models.py        # Profile, Post, Comment, Like, Follow models
│   ├── views.py         # Business logic and view handlers
│   ├── forms.py         # Form validation for auth, posts, and profiles
│   ├── signals.py       # Auto-profile creation on user signup
│   └── urls.py          # App URL routing
├── templates/           # HTML templates
│   ├── base.html
│   ├── registration/    # Login and register pages
│   └── social/          # Feed and profile pages
├── static/              # Static styling and JavaScript
│   ├── css/style.css
│   └── js/app.js
├── manage.py
└── requirements.txt
```

---

## 💻 Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/connecthub.git
cd connecthub
```

### 2. Create and Activate Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional, for Admin Panel)
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

Open your browser and visit:
- **Web App:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
