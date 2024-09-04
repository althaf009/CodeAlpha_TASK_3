from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_talisman import Talisman
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
bcrypt = Bcrypt(app)
Talisman(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Implement authentication here
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5005)

