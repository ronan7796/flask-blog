from flask import render_template, url_for, flash, redirect
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog import app, db, bcrypt
from flask_blog.models import User, Post

data = [
    {
        "author": "Leo Wheeler",
        "title": "in@feugiatnec.co.uk",
        "content": "nisl. Quisque fringilla euismod enim. Etiam gravida molestie arcu. Sed",
        "date_posted": "Nov 9, 2021"
    },
    {
        "author": "Britanni Holman",
        "title": "ac.vel@maecena.edu",
        "content": "ante blandit viverra. Donec tempus, lorem fringilla ornare placerat, orci",
        "date_posted": "Apr 4, 2022"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=data, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Success! You are now being able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)


@app.route('/passwordrecovery')
def password_recovery():
    form = LoginForm()
    return render_template('password_recovery.html', title='Password Recovery', form=form)
