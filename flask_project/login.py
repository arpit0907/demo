from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
# app.debug = True
                           

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'userid' or request.form['pswrd'] != '1234':
            error = 'Invalid Username/Password.'
        else:
            return redirect(url_for('home'))
    else:
        return render_template("login.html")

if __name__  == '__main__':
  app.run()
