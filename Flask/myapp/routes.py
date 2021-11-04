from myapp import myapp_obj
from myapp.forms import CityForm
from flask import render_template, flash, redirect

@myapp_obj.route("/google")
def sayGoogle():
    return 'goooogle'

@myapp_obj.route("/", methods=['GET','POST'])
def home():
    name = 'Seyoung'
    title = 'Top Cities'
    posts = [{'city': 'Paris'},\
            {'city': 'London'},\
            {'city': 'Rome'},\
            {'city': 'Tahiti'}]
    form = CityForm()
    if form.validate_on_submit():
            flash(f'Add request for City Name {form.cityName.data}, visited={form.visited.data}')
            return redirect('/')

    return render_template('home.html', name=name, posts=posts, title=title, form=form)
