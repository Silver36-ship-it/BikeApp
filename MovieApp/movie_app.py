movie_dict = {}

def get_movie():
    return list(movie_dict.keys())
def add_movie(movie):
    if movie not in movie_dict:
        movie_dict[movie] = []
    return get_movie()
def add_movie_rating(movie,rating):
    if(movie in movie_dict):
        try:
            rating = float(rating)
            movie_dict[movie].append(rating)
        except ValueError:
            return "Rating is not a number"
    else:
        return "Movie doesn't exist,please go and add the movie"
    return movie_dict
def get_movie_average_rating():
    if not movie_dict:
        return "No movies have been added yet,please go and add the movie"
    result = ""
    for movie,rating in movie_dict.items():
        if rating:
            average_rating = sum(rating) / len(rating)
            result += f"Movie: {movie} - Average Rating: {average_rating}\n"
        else:
            result += f"{movie} has no rating! Go and add a rating\n"
    return result.strip()

def display_main_menu():
    display = """
        Welcome to the Movie App!
    [][][][][][][][][][][][][][][][][]    
        1. Add a movie
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        2. Rate a movie
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        3. View Average Ratings
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        4. Exit
    [][][][][][][][][][][][][][][][][]
        """
    return display
def main():
    userInput = None
    print(display_main_menu())
    while(userInput != 4):
        userInput = input("Enter an option:")
        match userInput:
            case "1":
                while True:
                    add_input = input("Enter a movie name:").strip()
                    print("<<<<<<<Movie added successfully!!!>>>>>")
                    print(add_movie(add_input))
                    while True:
                        continue_input = input("Wish to enter another movie? press yes or no to exit:").strip().lower()
                        if continue_input == "yes":
                            break
                        elif continue_input == "no":
                            break
                        else:
                            print("Invalid input, please try again")
                            continue
                    if continue_input == "no":
                        break
                print(display_main_menu())
            case "2":
                while True:
                    movie_input = input("Enter a movie name:")
                    rate_input = input("Enter a movie rating:")
                    print("<<<<<<<<Movie and rating added successfully!!!>>>>>")
                    print(add_movie_rating(movie_input,rate_input))
                    while True:
                        continue_input = input("Wish to enter another movie? press yes or no to exit:").strip().lower()
                        if continue_input == "yes":
                            break
                        elif continue_input == "no":
                            break
                        else:
                            print("Invalid input, please try again")
                            continue
                    if continue_input == "no":
                        break
                print(display_main_menu())
            case "3":
                print(get_movie_average_rating())
                print(display_main_menu())
            case "4":
                print("Thank you for using Movie App.Bye!")
                break
            case _:
                print("Invalid input")
main()
