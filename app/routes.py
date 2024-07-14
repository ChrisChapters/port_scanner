from flask import Blueprint, render_template, request
from .scanner import scan

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')
        results = scan(ip_address)
        return render_template('index.html', results=results)
    return render_template('index.html')
