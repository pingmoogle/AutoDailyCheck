# -*- encoding: UTF-8 -*-

from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap

from classes import NameForm, Check, Execute

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dnj.f8~g2b%g49^.2ubvdv0::sbu@@gh9!42bbjds.sbkw'
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    pswd = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        pswd = form.pswd.data
        form.name.data = ''
        form.pswd.data = ''
    if name is None:
        return render_template("index.html", form=form, name=None)
    if name is not None and Check.checkIDResult(name, pswd):
        if Check.userInJson(name, pswd):
            try:
                with open("logs/"+name+".log", "r") as logfd:
                    s = logfd.read()
                    logfd.close()
                return render_template("index.html", form=form, name="Hello, " + name, loggedin=1, logfile=s)
            except FileNotFoundError:
                return render_template("index.html", form=form, name="Hello, " + name, loggedin=1, logfile=None)
        else:
            Execute.insertThisUser(name, pswd)
            return render_template("index.html", form=form, name="Hello, " + name, loggedin=1)

    else:
        # return render_template("index.html", form=form, name="Failed to login.")
        flash("Failed to Login.")
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run()

