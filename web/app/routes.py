from flask import render_template, redirect, request
from app import app
from app.forms import StartForm
from app.functions import get_information


@app.route('/', methods=['GET', 'POST'])
def start():
    form = StartForm()
    if form.validate_on_submit():
        return redirect('/choise')
    return render_template('start.html', form=form)

@app.route('/choise', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        city = request.form['city']
        return redirect('/cities?city={}'.format(city))
    return render_template('choise.html')

@app.route('/cities')
def city_searching():
    current_city = request.args.get('city')
    if not current_city:
        current_city = 'kazan'
    args = get_information(current_city)
    
    if args['is_error']:
        return render_template('final.html', error=True, message=args['error'])
    return render_template('final.html', error=False, name=args['name'], 
            temp=args['temperature'], pres=args['pressure'], hum=args['humidity'])
