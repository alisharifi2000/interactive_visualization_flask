from flask import Flask
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    data = [['Tehran', 728], ['Qom', 121], ['North Khorasan', 10], ['East Azerbaijan', 1000], ['West Azerbaijan', 660]]

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('map.html')
    output_from_parsed_template = template.render(data=data)
    # to save the results
    with open("my_new_file.html", "w") as fh:
        fh.write(output_from_parsed_template)
    return output_from_parsed_template


if __name__ == '__main__':
    app.run()
