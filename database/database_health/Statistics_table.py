def getStatistics_tableAll(pconnection):
  try:
    xcursor = pconnection.cursor()
    xnews = []
    
    xsql = 'SELECT Age, Bedtime, "Physical Activity Level", "Dietary Habits", "Sleep Disorders", "Medication Usage", "Sleep Duration" FROM Health_Sleep_Statisticsb'

    xcursor.execute(xsql, ())
    xcolumns = [column[0] for column in xcursor.description]
    xrows = xcursor.fetchall()

    for row in xrows:
      xnews.append(dict(zip(xcolumns, row)))

    return xnews

  finally:
    xcursor.close()
