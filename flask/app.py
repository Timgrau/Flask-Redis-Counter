import redis
from flask import Flask, request, render_template
from wtforms import StringField, validators, SubmitField
from flask_wtf import FlaskForm
import datetime as dt




### Redis ###
client = redis.Redis(host=host, port=6379)
q = ["dummy"]
#############

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = "..."


class RegistrationForm(FlaskForm):
   username = StringField("Username", validators=[validators.DataRequired()])
   submit = SubmitField("Sumbit")


@app.route('/', methods=["GET", "POST"])
def hello():
   q.append(str(dt.datetime.now().replace(microsecond=0)))
   form = RegistrationForm()
   user = None

   if form.validate_on_submit():
      user = form.username.data

      if client.exists(user) == 0:
         client.set(user, "0")
         return "Welcome {}".format(user)
      else:
         client.incr(user)
         client.save()
         q.pop(0)
      return "User: {} logged in the {}. time. " \
             "Last time you used the application {}".format(user,
                                                            client.get(user).decode("utf-8"),
                                                            q[0])
   return render_template("hello.html", form=form)

if __name__ == '__main__':
   app.run()
