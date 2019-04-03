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



