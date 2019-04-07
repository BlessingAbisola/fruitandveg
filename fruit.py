a_fruit = {
	"name": "apple",
	"altitude": 5
}

another_fruit = {
	"name": "apple",
	"altitude": 8
}

yet_another_fruit = {
	"name": "banana",
	"altitude": 3
}

fruit_list = [a_fruit, another_fruit, yet_another_fruit]
print fruit_list
only_apples = list(filter(lambda next_fruit: next_fruit["name"] == 'apple', fruit_list))
print only_apples

def sortbyname(fruit): 
    return fruit["altitude"]

def sortByLengthOfName(fruit):
	return len(fruit["name"])

fruit_list.sort(reverse = True, key = lambda fruit: len(fruit["name"]))
fruit_list.sort(reverse = True, key = sortByLengthOfName)

print fruit_list

def form_input(name):
	only_named = list(filter(lambda next_fruit: next_fruit["name"] == name, fruit_list))
	only_named.sort(reverse = True, key = sortByLengthOfName)
	return json.dumps(only_named)

from flask import Flask, render_template
import logging

flask_app = Flask(__name__)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('application_logs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

@flask_app.route('/')
def homepage():
    return "Hello World"

@flask_app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())


logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)

