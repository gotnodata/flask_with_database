from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs') #json endpoint. The /api here signifies json will be returned.
def list_jobs():
    return jsonify(JOBS) 


if __name__ == '__main__':
    app.run(debug=True)