def great(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather today is good {name}?")


# function with more than one input
def great_with_location(name, location):
    print(f"Hello {name}")
    print(f"Good to see you in {location}")


name_input = input("Please input your name: ")
location_input = input("Please input your location: ")

# call with the keyword arguments instead of using positional arguments
great_with_location(location=location_input, name=name_input)
