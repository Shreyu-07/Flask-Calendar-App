from flask import Flask, render_template, request
import calendar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    cal = ''
    if request.method == 'POST':
        mm = int(request.form['month'])
        yy = int(request.form['year'])
        cal = calendar.HTMLCalendar().formatmonth(yy, mm)
    return render_template("index.html", calenders=cal)

if __name__ == '__main__':
    app.run(debug=True)
