import humps


def convert_strings():
    print("convert_strings")
    # Convert snake_case to camelCase
    camel = humps.camelize('user_name')
    print(camel)  # Output: userName
    # Convert camelCase to snake_case
    snake = humps.decamelize('userName')
    print(snake)  # Output: user_name

def convert_dictionaries():
    print("convert_dictionaries")
    data = {'user_name': 'Alice', 'user_age': 30}
    # Convert all keys to camelCase
    camel_data = humps.camelize(data)
    print(camel_data)  # Output: {'userName': 'Alice', 'userAge': 30}
    # Convert all keys to snake_case
    snake_data = humps.decamelize(camel_data)
    print(snake_data)  # Output: {'user_name': 'Alice', 'user_age': 30}


convert_strings()
convert_dictionaries()
