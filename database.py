from sqlalchemy import create_engine,text
import os, json

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_string, connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})



def load_jobs_from_db():
  with engine.connect() as conn:
    qry = text("select * from jobs")
    result = conn.execute(qry)
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

def load_jobs_from_db1(id):
  with engine.begin() as conn:
    qry = text("select * from jobs where id = :val")
    result = conn.execute(qry,{'val':id})
    job = []
    row = []
    for row in result.all():
      job.append(row._asdict())
    if len(row) == 0:
      return None
    else:
      return job
