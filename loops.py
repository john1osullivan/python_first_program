def say_hello_to_people(people_names: list):
    # using for in
    for person in people_names:
        print("Hello " + person)

list_of_people_names: list = ["Alvaro", "John", "Random"]
say_hello_to_people(["Random", "Doe"])
say_hello_to_people(list_of_people_names)