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

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional):

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

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.