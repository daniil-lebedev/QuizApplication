# OpenTrain: Open-source web-application for employee training. 🖥️

![GitHub stars](https://img.shields.io/github/stars/daniil-lebedev/QuizApplication)

![GitHub forks](https://img.shields.io/github/forks/daniil-lebedev/QuizApplication)

![GitHub issues](https://img.shields.io/github/issues/daniil-lebedev/QuizApplication)

## Table of Contents 📖

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Docker](#docker)
- [Applications](#applications)
    - [Announcement](#announcement)
    - [Base](#base)
    - [Company](#company)
    - [Education Board](#education-board)
    - [Exception Management](#exception-management)
    - [Quiz](#quiz)
    - [QuizApplication](#quizapplication)
    - [Security Module](#security-module)
    - [Sensitivity Check](#sensitivity-check)
    - [Static](#static)
    - [Templates](#templates)
    - [User](#user)
- [Contributing](#contributing)
- [License](#license)

## Getting Started 🤔

If you want to run this project locally, follow these steps.

1. Ensure you know some Python and Django basics.
2. Install Docker and Docker Compose if you want to use containers.
3. Clone the repository and install the dependencies.
4. Apply the database migrations.

### Prerequisites ⁉️

- Python 3.9 or higher 🐍
- Django 3.2 or higher
- Docker and Docker Compose for containerization

### Installation

1. Clone the repository:

   ```bash
   git clone daniil-lebedev/QuizApplication
   cd QuizApplication
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```


4. Create a .env file in the root directory and add the following environment variables:

   ```bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```

## Usage

Run the development server:

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

## Configuration

- Configure your Django settings in the `settings.py` file.
- Keep sensitive information such as the secret key in environment variables.

## Docker

If you prefer using Docker for development, follow these steps:

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Run the Docker container:

   ```bash
   docker-compose up
   ```

3. Access the application at [http://localhost:8000](http://localhost:8000).

## Applications

1. ### Announcement
   Purpose: Manages announcements within the application. It allows team administrators to create, update, and delete
   announcements that are relevant to their team members. This service also likely handles the viewing permissions and
   interactions such as reading or commenting on announcements.

2. ### Base
   Purpose: Acts as the foundational app for the Django project, typically managing the shared resources across other
   apps such as base templates, base settings, and utilities. It may also include global static files and templates that
   are inherited or used by other applications within the project.
3. ### Company
   Purpose: Manages company-related data and functionality. This includes handling team creation, team memberships, and
   roles within teams. It could also involve managing information about the company itself, like company profile,
   settings, and possibly integration with other business management tools.
4. ### Education Board
   Purpose: Manages educational content delivery, such as tutorials, courses, or any informative content that is
   structured in a board-like format. It likely supports operations like creating, organizing, and displaying
   educational boards and associated materials to users.
5. ### Exception Management
   Purpose: Handles unexpected behaviors and errors within the application. This module is responsible for capturing,
   logging, and possibly recovering from exceptions. It enhances the robustness of the application by providing a
   structured approach to error handling and diagnostics.
6. ### Quiz
   Purpose: Manages the creation, administration, and taking of quizzes within the application. This includes storing
   quiz questions, options, answers, and user responses. It might also handle scoring and feedback related to user
   performance on quizzes.
7. ### QuizApplication
   Purpose: This could be the main application module that ties together all aspects of the quiz management system,
   including interfacing with the user module, security settings, and possibly rendering the quizzes to the end-user.
8. ### Security Module
   Purpose: Ensures the application adheres to security best practices. This module likely manages authentication,
   authorization, secure data handling, and perhaps compliance with security standards. It may implement features such
   as login, session management, and access controls.
9. ### Sensitivity Check
   Purpose: Provides functionality to review and filter content based on predefined sensitivity criteria. It could be
   used to prevent the submission of inappropriate or offensive content within user-generated sections like comments,
   posts, or profiles.
10. ### Static
    Purpose: Stores static files such as JavaScript, CSS, and images that are used across the application. These
    resources are essential for the client-side rendering and behavior of the web application.
11. ### Templates
    Purpose: Contains HTML templates used by Django’s template rendering engine. This directory would include all the
    layout files, form templates, and other HTML components required by various apps for UI rendering.
12. ### User
    Purpose: Manages user-related data and operations. This involves user profiles, user settings, authentication (log
    in and log out), user registration, and possibly user-specific data handling like preferences and history within the
    application.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.