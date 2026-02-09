# Job Application Tracker

A Flask-based web application that allows users to browse job listings and submit job applications. All applications are stored in a MySQL database for easy tracking and management.

## Features

- **Browse Job Listings**: View available job positions with details (title, company, location, salary)
- **Apply to Jobs**: Simple form-based application submission
- **Store Applications**: All submissions are saved to a MySQL database
- **Responsive Design**: Clean, user-friendly interface for all devices
- **API Endpoints**: JSON API for retrieving job listings and applications
- **File Upload**: Resume upload support during application submission
- **Form Validation**: Comprehensive validation for applicant information

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: MySQL with SQLAlchemy ORM
- **Frontend**: HTML/Jinja2 templates with CSS
- **Additional Libraries**:
  - Flask-SQLAlchemy: ORM for database management
  - python-dotenv: Environment variable management
  - PyMySQL: MySQL database driver

## Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask_with_database
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - **Windows**:
     ```bash
     env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   DB_PASSWORD=your_mysql_password
   ```

6. **Create the database**
   ```bash
   mysql -u root -p
   > CREATE DATABASE job_application;
   > EXIT;
   ```

## Usage

1. **Start the application**
   ```bash
   python run.py
   ```

2. **Access the application**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **Browse and Apply**
   - Visit the home page to see available jobs
   - Click "Apply" on any job
   - Fill out the application form with your details
   - Submit the application

## Project Structure

```
flask_with_database/
├── run.py                 # Main Flask application
├── test_database.py       # Database testing script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── static/
│   └── style.css         # Stylesheet
└── templates/
    ├── base.html         # Base template
    ├── home.html         # Job listings page
    ├── apply.html        # Application form
    └── application_success.html  # Success page
```

## Database Schema

### job_application Table

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary key |
| job_id | INT | Job identifier |
| job_title | VARCHAR(120) | Position title |
| company | VARCHAR(120) | Company name |
| first_name | VARCHAR(50) | Applicant's first name |
| last_name | VARCHAR(50) | Applicant's last name |
| email | VARCHAR(120) | Email address |
| phone | VARCHAR(20) | Phone number |
| location | VARCHAR(120) | Current location |
| experience | VARCHAR(50) | Years of experience |
| education | VARCHAR(50) | Education level |
| current_job | VARCHAR(120) | Current job title |
| cover_letter | TEXT | Cover letter text |
| resume_filename | VARCHAR(255) | Uploaded resume filename |
| portfolio_link | VARCHAR(255) | Portfolio/website link |
| availability | VARCHAR(50) | Start date availability |
| salary_expectation | VARCHAR(50) | Expected salary |
| applied_at | DATETIME | Application timestamp |
| status | VARCHAR(20) | Application status |

## API Endpoints

### Get All Jobs
```
GET /api/jobs
```
Returns a JSON array of all available jobs.

**Response Example**:
```json
[
  {
    "id": 1,
    "title": "Software Engineer",
    "company": "Tech Innovators Inc.",
    "location": "San Francisco, CA",
    "salary": "$120,000"
  }
]
```

### Get All Applications
```
GET /api/applications
```
Returns a JSON array of all submitted applications.

**Response Example**:
```json
[
  {
    "id": 1,
    "job_title": "Software Engineer",
    "company": "Tech Innovators Inc.",
    "applicant_name": "John Doe",
    "email": "john@example.com",
    "applied_at": "2025-01-15T10:30:00",
    "status": "received"
  }
]
```

## Testing

Run the database test script to verify your setup:
```bash
python test_database.py
```

This will:
- Test database connection
- Verify table creation
- Test basic insert operations
- Test queries
- Clean up test data

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page - list of jobs |
| `/apply/<job_id>` | GET | Application form for a specific job |
| `/submit-application` | POST | Submit job application |
| `/application-success` | GET | Success confirmation page |
| `/api/jobs` | GET | JSON API - get all jobs |
| `/api/applications` | GET | JSON API - get all applications |

## Development

To run in debug mode with auto-reload:
```bash
python run.py
```

The application automatically creates database tables on startup.

## License

This project is open source and available for educational and personal use.

## Contributing

Feel free to submit issues and enhancement requests!

---

**Author**: Flask Application Developer  
**Last Updated**: February 2026
