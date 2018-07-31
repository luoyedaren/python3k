import logging
from datetime import datetime

from flask import Flask, render_template, url_for, session, redirect, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

logging.basicConfig(level=logging.INFO)


class NameForm(FlaskForm):
    name = StringField('what is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')


# from flask.ext.script import Manager

""" https://github.com/nummy/flask-script-cn 参考"""

app = Flask(__name__)
Bootstrap(app)
Moment(app)
app.debug = True
app.jinja_env.auto_reload = True

# sql 链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.229.129/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# 防止表单跨站攻击 Flask-WTF
app.config['SECRET_KEY'] = 'mimi'

if __name__ == '__main__':
    # Manager.run()
    app.run(debug=True)


@app.route('/', methods=['get', 'post'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        logging.info('name is ' + name)
        old_name = session.get('name')
        if old_name is not None and old_name != name:
            flash('你要更新名称了？')
        session['name'] = name
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form, time=datetime.utcnow())


@app.route('/user/<name>/<wife>')
def user(name, wife):
    return '<h1> Hello ,%s! wife is %s</h1>' % (name, wife)


@app.route('/error')
def testAbort():
    # abort(505)
    1 / 0
    return "error"


@app.route('/template')
def template():
    return render_template('index.html')


@app.route('/template/<name>')
def template1(name):
    return render_template('hello.html', name=name)


@app.route('/user1')
def user1():
    return render_template('user.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('505.html'), 500


@app.route('/query')
def get_user():
    pass


"""定义模型

自动生成 modles.py
flask-sqlacodegen --noviews --noconstraints --noindexes --outfile models.py --flask mysql://root:123456@192.168.229.129/test


"""


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=False)

    def __repr__(self):
        return '<Role %r>' % self.role_name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.user_name
