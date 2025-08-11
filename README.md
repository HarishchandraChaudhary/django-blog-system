# Django Blog System - Banao Task 2

This is a blog system built with Python and Django for Banao Task 2. The application allows doctors to create and manage blog posts, while patients can view them.

## Features

- **Doctor User:**
  - Create, upload, and manage blog posts.
  - Posts can be marked as a **draft**.
  - Can view a list of all posts they have uploaded.
- **Patient User:**
  - View a list of all published blog posts.
  - Posts are categorized for easy navigation.
  - Summary of each post is truncated to 15 words with an ellipsis (...) if longer.
- **Admin Panel:**
  - Standard Django admin for managing users, categories, and blog posts.

## Technical Details

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript (can be customized with any JS library/framework)
- **Database:** MySQL

## Getting Started

### Prerequisites

- Python 3.x
- MySQL Database
- Django 3.x or 4.x

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HarishchandraChaudhary/django-blog-system
    cd django-blog-system
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Configuration:**
    -   Create a new MySQL database.
    -   Update the `DATABASES` section in your `settings.py` with your MySQL credentials.

5.  **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000`.

## Contribution

Feel free to fork the repository and submit pull requests.

---

_This project was created as a submission for Banao Task 2._
