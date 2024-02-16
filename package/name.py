def print_name(name:str,
               time:int):
    result = (name + ", ") * time
    return result

# Example of using the function
if __name__ == "__main__":
    # Replace "John" and 3 with the desired values
    result_value = print_name("John", 3)
    print(result_value)