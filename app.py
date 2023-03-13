import flask

import models

from flask import render_template

app: flask.app.Flask = flask.Flask(__name__)
users:list[models.User]= []

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/reg', methods=['GET','POST'])
def registration() -> flask.Response:
    if flask.request.method == "POST":
        data:dict[str,str] = flask.request.form
        users.append(
            models.User.create(**data, users=users)
            
        )
    return render_template('reg.html')


@app.route('/login', methods=['GET','POST'])
def login() -> flask.Response:
    if flask.request.method == "POST":
        data:dict = flask.request.form
        for i in users:
            if (i.login == data.get('login')
            ) and (
                i.password == data.get('password')
            ):  
                for i in users:
                    return render_template('lk.html', user=i)
            else:
                return render_template('error.html')
    
    return render_template('login.html')



if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8040,
        debug=True
    )