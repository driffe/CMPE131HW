from myapp import myapp_obj, db
from myapp.forms import TopCities
from flask import render_template, flash, redirect
from myapp.models import City
from sqlalchemy import asc

@myapp_obj.route("/google")
def sayGoogle():
    return 'goooogle'

@myapp_obj.route("/", methods=['GET','POST'])
def home():
    name = 'Seyoung'
    title = 'Top Cities'
    
    top_city = City.query.filter().order_by(City.city_rank.asc())
    form = TopCities()
    db.create_all()

    if form.validate_on_submit():
            flash(f'Add request for City Name {form.city_name.data}, visited={form.city_visited.data}')
            flash(f'Add request for City Rank {form.city_rank.data}')
            city_name = form.city_name.data
            city_rank = form.city_rank.data
            city_visited = form.city_visited.data
            record = City(city_name, city_rank, city_visited)
            db.session.add(record)
            db.session.commit()
            return redirect('/')
        
    return render_template('home.html', name=name, title=title, top_city = top_city, form=form)
