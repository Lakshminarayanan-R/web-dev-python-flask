from flask import Flask,render_template,jsonify
from database import load_jobs_from_db,load_jobs_from_db1


app = Flask(__name__)
    
@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                          jobs = jobs)

@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(list(jobs))

@app.route('/jobs/<id>')
def show_job(id):
  job = load_jobs_from_db1(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template('jobpage.html',job=job)
  
print(__name__)
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)