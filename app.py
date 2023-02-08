from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    provinces = {'p1': 'Tehran', 'p2': 'Yazd', 'p3': 'Semnan'}
    values = {'v1': 100, 'v2': 200, 'v3': 400}

    data = provinces | values
    print(data)
    return render_template('map.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
