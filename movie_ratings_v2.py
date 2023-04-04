# Movie rating program v2

def get_age():
    age_of_user = input("Could you please provide me your age?")
    return int(age_of_user)


def get_movie_rating(age):
    if age >= 118 or age == 0:
        return "Please provide the right age."
    elif age >= 18:
        return "You can watch any movie."
    elif age >= 13:
        return "You can watch U movies."
    elif age <= 12:
        return "You can watch PG movies"
    else:
        return "Wrong input."


age = get_age()
movie_rating = get_movie_rating(age)
print(movie_rating)
