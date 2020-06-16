from flask import Flask, request, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap


from flask_script import Manager

app = Flask(__name__, static_folder='app/static')
bootstrap = Bootstrap(app)
#used to run a with a manager
#manager = Manager(app)

@app.route("/request_example")
def req():
        user_agent = request.headers.get('User-Agent')
        return '<p>Your browser is %s</p>' % user_agent

@app.route('/')
def index():
    return render_template('indexaaa.html')

@app.route('/user/<name>')
def user(name):
 return render_template('user.html', name=name)


#response object
@app.route("/about")
def about():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

#redirect
@app.route("/redirect_example")
def exam():
        return redirect('http://www.example.com')

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500


if __name__ == '__main__':

    #printing map of views:
    #print(app.url_map)

    #running app
    app.run(debug='True')

    #using a manager
    #manager.run("runserver")


    #print(app.url_map)
