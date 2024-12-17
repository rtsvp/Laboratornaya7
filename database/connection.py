import sqlite3

def initConnection():
  connection = sqlite3.connect(
    'database/database_health/Health_Sleep_Statisticsb.sql'
  )

  return connection

def closeConnection(pconnection):
  if pconnection is not None:
    pconnection.commit()
    pconnection.close()

  return True
