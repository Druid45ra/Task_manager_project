# Task Manager Project

The **Task Manager Project** is a Django-based web application designed to help users effectively manage their tasks. It provides features for creating, organizing, and tracking tasks with real-time updates, making it an ideal tool for personal or team task management.

## Features

- **User Authentication**: Secure user login and registration.
- **Task Management**:
  - Create, edit, and delete tasks.
  - Organize tasks by status (Pending, In Progress, Completed).
  - Assign priority levels (Low, Medium, High).
- **Real-Time Notifications**: Redis integration for instant updates.
- **Database Integration**: Powered by PostgreSQL for robust data management.
- **Modern Admin Panel**: Leverages Django Admin for easy management of tasks and users.

## Technologies Used

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Real-Time Updates**: Redis
- **Frontend**: HTML, CSS, JavaScript (integrated into Django templates)
- **Others**: Docker for containerization, Git for version control

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Druid45ra/Task_manager_project.git
   cd Task_manager_project
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Configure your PostgreSQL database in `settings.py`.
   - Apply migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## Usage

1. Register or log in to the application.
2. Create tasks with titles, descriptions, statuses, and priorities.
3. View and update tasks as needed.
4. Use the admin panel for advanced management (accessible at `/admin`).

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them:
   ```bash
   git add .
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or feedback, feel free to contact the project owner:

- GitHub: [Druid45ra](https://github.com/Druid45ra)

