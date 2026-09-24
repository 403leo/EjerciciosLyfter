import csv


def save_game_ranking(file_path, data):

    # Open the file in write mode ('w')

    # Use newline='' to prevent blank lines between records

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        # Get the column names from the keys of the first record

        headers = data[0].keys()

        # Initialize the writer with the destination file and headers

        writer = csv.DictWriter(file, fieldnames=headers)

        # Write the first row with the column names

        writer.writeheader()

        # Insert the complete list of games

        writer.writerows(data)


# Method to fill the game ranking with the information of each game

def add_games_to_ranking(number_of_games):

    # List of dictionaries containing the selected games

    top_10_ranking = []

    # Loop to add each game to the ranking

    for i in range(number_of_games):

        print(f"Adding game {i + 1} of {number_of_games}:")

        name = input("Enter the game name: ")
        genre = input("Enter the game genre: ")
        developer = input("Enter the game developer: ")
        esrb_rating = input("Enter the ESRB rating: ")

        game = {
            'nombre': name,
            'genero': genre,
            'desarrollador': developer,
            'clasificacion': esrb_rating
        }

        top_10_ranking.append(game)

    return top_10_ranking


def main():

    number_of_games = int(
        input("Enter the number of games you want to add to the ranking: ")
    )

    top_10_ranking = add_games_to_ranking(number_of_games)

    save_game_ranking('new_game_ranking.csv', top_10_ranking)


main()