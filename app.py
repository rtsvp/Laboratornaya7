import database.connection as conn
import database.database_health.Statistics_table as Statistics_table

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Statistics_table')
def get_Statistics_table():
  try:
    xconn=conn.initConnection()
    data_Statistics_table = Statistics_table.getStatistics_tableAll(pconnection=xconn)
    return render_template ('Health_Sleep_Statistics.html', data_Statistics_table=data_Statistics_table)
  except Exception as e:
    return '<font color="red"><h1> Ошибка: '+str(e)+'</h1></font>'
  finally:
    conn.closeConnection(pconnection=xconn)

# @app.route('/')
# def index():
#   return '<h1>Hello World!</h1>'

# @app.route('/hello')
# def hello():
#   return '<h1> Hello my friend!</h1>'

# @app.route('/user', defaults={'name': 'azat'})
@app.route('/user/<name>')
def hello_user(name):
  return '<h1>Hello, %s ! </h1>' % name

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
