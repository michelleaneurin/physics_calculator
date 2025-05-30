from flask import Blueprint, render_template, request
from app.models.formulas import calculate_glb, calculate_glbb, calculate_wave_speed

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/glb', methods=['GET', 'POST'])
def glb():
    result = None
    if request.method == 'POST':
        distance = float(request.form['distance'])
        time = float(request.form['time'])
        result = calculate_glb(distance, time)
    return render_template('glb.html', result=result)

@main.route('/glbb', methods=['GET', 'POST'])
def glbb():
    result = None
    if request.method == 'POST':
        v0 = float(request.form['v0'])
        a = float(request.form['a'])
        t = float(request.form['t'])
        result = calculate_glbb(v0, a, t)
    return render_template('glbb.html', result=result)

@main.route('/wave', methods=['GET', 'POST'])
def wave():
    result = None
    if request.method == 'POST':
        distance = float(request.form['distance'])
        time = float(request.form['time'])
        result = calculate_wave_speed(distance, time)
    return render_template('wave.html', result=result)