# Django Comments System

This Django application is a basic comments system with nested comments functionality. It allows users to create posts, add comments, and reply to existing comments.

## Features

- **Post Model:** Represents a post with title and content fields.

- **Comment Model:** Represents a comment with user, text, timestamp, post, and parent_comment fields. Supports nested comments.

- **Forms:** Includes `LoginForm`, `CommentForm`, and `ReplyForm` for user authentication and comment submission.

- **Views:** Defines views for rendering post details, handling comment submissions, and displaying nested comments.

- **URLs:** Configures URL patterns for accessing post details and submitting replies.

- **Templates:** Utilizes HTML templates for rendering post details, comment forms, and nested comments.

- **JavaScript:** Provides JavaScript functions (`toggleReplyForm` and `cancelReply`) for toggling reply forms.

## Getting Started

These instructions will guide you on setting up the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following software installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)

### Installing

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/django-comments-system.git
    cd django-comments-system
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **For Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **For MacOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Additional Notes

- Customize the HTML templates, styling, and JavaScript as needed for your project.
- Feel free to extend the functionality based on your application requirements.


