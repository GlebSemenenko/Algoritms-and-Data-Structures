def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth

    if age == 0:
        return "You were born this very year!"
    elif age == 1:
        return "You are 1 year old."
    elif age == -1:
        return "You will be born in 1 year."
    elif age > 1:
        return f"You are {age} years old."
    else:
        return f"You will be born in {-age} years."