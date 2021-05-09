from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

"""
    INSTRUCTIONS
    1. activate the virtual environment - venv\Scripts\activate
    2. run Flask from powershell - $env :FLASK_APP = "server.py" 
    3. run: flask run
    4. debug mode - $env:FLASK_ENV="development"
    5. This tells your operating system to listen on all public IPs - flask run --host=0.0.0.0 
"""

# @app.route('/<username>/<int:post_id>')
# def hello_person(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/blog')
# def blog():
#     return 'привет ольга! This is Choopa\'s bloog '


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to databes'
    else:
        return 'somthing went wrong. ty again!'