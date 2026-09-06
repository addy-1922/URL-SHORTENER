# 🔗 URL Shortener

A simple and user-friendly **URL Shortener web application built with Django**.
It converts long URLs into short, clean, and easy-to-share links.

## 🚀 Live Demo

👉 **[Try the URL Shortener](https://url-shortener-xvsv.onrender.com)**

## 📌 Features

* 🔗 Convert long URLs into short links
* ⚡ Fast and simple URL generation
* 📋 Easy-to-use interface
* 🔄 Redirect short URLs to the original destination
* 📱 Responsive and clean UI
* 🌐 Deployed and accessible online

## 🛠️ Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Programming Language:** Python
* **Deployment:** Render
* **Version Control:** Git & GitHub

## 📂 Project Structure

```text
url-shortener/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   └── ...
│
└── static/
    └── ...
```

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 💡 How It Works

1. User enters a long URL.
2. Django receives the URL through the form.
3. The application generates a unique short identifier.
4. The shortened URL is stored in the database.
5. When someone visits the short URL, Django finds the original URL.
6. The user is redirected to the original website.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Django project and app structure
* Django URL routing
* Models and database operations
* Handling HTML forms
* Creating shortened URLs
* HTTP redirects
* Django templates
* Static files
* Git & GitHub
* Deployment using Render

## 📸 Live Application

The application provides a simple interface where users can enter a long URL and generate a shortened link.

## 🌐 Deployment

The project is deployed on **Render** and can be accessed here:

👉 **https://url-shortener-xvsv.onrender.com**

## 👨‍💻 Author

**Your Name**

* GitHub: [Your GitHub Profile](https://github.com/addy-1922)
* LinkedIn: [Your LinkedIn Profile](www.linkedin.com/in/aditya-naik-5a7b79317)

---

⭐ If you found this project useful, consider giving the repository a star!
