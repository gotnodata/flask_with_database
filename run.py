from flask import Flask, jsonify, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# Build database URL from environment variables
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '3306')
db_name = os.getenv('DB_NAME', 'job_application')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', '')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'password')  # Use env variable for security

db = SQLAlchemy(app)


# Database Models
class JobApplication(db.Model):
    __tablename__ = 'job_application'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, nullable=False)
    job_title = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(120), nullable=False)
    
    # Personal Information
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    
    # Professional Information
    experience = db.Column(db.String(50), nullable=False)
    education = db.Column(db.String(50), nullable=False)
    current_job = db.Column(db.String(120))
    
    # Additional Information
    cover_letter = db.Column(db.Text)
    resume_filename = db.Column(db.String(255))
    portfolio_link = db.Column(db.String(255))
    availability = db.Column(db.String(50))
    salary_expectation = db.Column(db.String(50))
    
    # Metadata
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='received')
    
    def __repr__(self):
        return f'<JobApplication {self.first_name} {self.last_name} - {self.job_title}>'

# Job data (keep existing hardcoded jobs)
JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'company': 'Tech Innovators Inc.',
        'location': 'San Francisco, CA',
        'salary': '$120,000'
    },
    {
        'id': 2,
        'title': 'Marketing Manager',
        'company': 'Creative Solutions Ltd.',
        'location': 'New York, NY',
        'salary': '$90,000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'company': 'Data Insights Co.',
        'location': 'Chicago, IL',
        'salary': '$85,000'
    },
    {
        'id': 4,
        'title': 'Product Manager',
        'company': 'FutureTech Corp.',
        'location': 'Austin, TX',
        'salary': '$130,000'
    },
    {
        'id': 5,
        'title': 'UX Designer',
        'company': 'Design Studio X',
        'location': 'Seattle, WA',
        'salary': '$95,000'
    }
]


# Routes
@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/apply/<int:job_id>')
def apply(job_id):
    job = next((job for job in JOBS if job['id'] == job_id), None)
    if job is None:
        return "Job not found", 404
    return render_template('apply.html', job=job)

@app.route('/submit-application', methods=['POST'])
def submit_application():
    
    try:
        # Create new application record
        application = JobApplication(
            job_id=request.form.get('job_id'),
            job_title=request.form.get('job_title'),
            company=request.form.get('company'),
            
            # Personal Information
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            location=request.form.get('location'),
            
            # Professional Information
            experience=request.form.get('experience'),
            education=request.form.get('education'),
            current_job=request.form.get('current_job'),
            
            # Additional Information
            cover_letter=request.form.get('cover_letter'),
            portfolio_link=request.form.get('portfolio_link'),
            availability=request.form.get('availability'),
            salary_expectation=request.form.get('salary_expectation')
        )
        
        print(f"Application object created: {application}")
        
        # Handle file upload
        if 'resume' in request.files:
            resume_file = request.files['resume']
            if resume_file and resume_file.filename:
                filename = f"resume_{application.id}_{resume_file.filename}"
                # Save file logic here (you'll need to configure file storage)
                application.resume_filename = filename
                print(f"File uploaded: {filename}")
        
        # Save to database
        print("Attempting to save to database...")
        db.session.add(application)
        db.session.commit()
        print("Database save successful!")
        
        flash('Application submitted successfully! 🎉', 'success')
        return redirect(url_for('application_success'))
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print(f"ERROR TYPE: {type(e)}")
        import traceback
        traceback.print_exc()
        db.session.rollback()
        flash(f'Error submitting application: {str(e)}', 'error')
        return redirect(request.referrer)

@app.route('/application-success')
def application_success():
    return render_template('application_success.html')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/api/applications')
def get_applications():
    applications = JobApplication.query.order_by(JobApplication.applied_at.desc()).all()
    return jsonify([{
        'id': app.id,
        'job_title': app.job_title,
        'company': app.company,
        'applicant_name': f"{app.first_name} {app.last_name}",
        'email': app.email,
        'applied_at': app.applied_at.isoformat(),
        'status': app.status
    } for app in applications])

# Initialize database - create tables before first request
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == '__main__':
    app.run(debug=True)
