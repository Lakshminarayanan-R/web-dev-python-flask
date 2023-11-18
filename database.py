from sqlalchemy import create_engine,text
import os

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_string, connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})


def load_jobs_from_db():
  with engine.begin() as conn:
    qry = text("select * from jobs")
    resultset = conn.execute(qry)
    jobs = resultset.mappings().all()
    return jobs
