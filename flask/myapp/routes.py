import pymysql
from myapp import app
from flask import render_template
from myapp.initpysql import connection

# from myapp import map
# def create_task():
#     query = "SELECT carBrand, COUNT(*) from cars GROUP BY carBrand"
#     db, cursor = query_handle(query)
with connection.cursor() as cursor:
    sqltest = "SELECT carBrand from car where carBrand='BMW'"
    cursor.execute(sqltest)
    result = cursor.fetchone()
    connection.close()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/showdb')
def showdb():
    return render_template('showdb.html', query_data=result)


@app.route('/googlemap')
def googlemap():
    # mymap = map(
    # identifier="view-side",
    # lat=37.4419,
    # lng=-122.1419,
    # markers=[(37.4419, -122.1419)])
    # sndmap = map(
    # identifier="sndmap",
    # lat=37.4419,
    # lng=-122.1419,
    # markers=[
    # {
    # 'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    # 'lat': 37.4419,
    # 'lng': -122.1419,
    # 'infobox': "<b>Hello World</b>" },
    # {
    # 'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    # 'lat': 37.4300,
    # 'lng': -122.1400,
    # 'infobox': "<b>Hello World from other place</b>" }
    # ]
    # )
    return render_template('googlemap.html')
