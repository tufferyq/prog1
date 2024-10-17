"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    :param filename: name of the file that contains the data
    :return genre_data: dictionary linking series and genres
    """

    genre_data = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            genre_data[name] = genres


        file.close()
        return genre_data

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None

def reverse_search_from_dictionary(dictionary, genre):
    """
    Searches for TV shows in the dictionary that belong to the specified genre.

    :param dictionary: dict, where keys are TV show names and values are lists of genres.
    :param genre: str, the genre to search for.
    :return: list, the names of TV shows that are associated with the specified genre.
    """
    found_shows = []

    # Iterate through the dictionary where key is show name and value is a list of genres.
    for show, genres in dictionary.items():
        # Check if the genre exists in the list of genres for the current show.
        if genre in genres:
            found_shows.append(show)
    return found_shows

def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    genre_list = list(genre_data.values())
    distinct_genres_list = []
    for i in range (0,len(genre_list)):
        for j in range (0, len(genre_list[i])):
            if genre_list[i][j] not in distinct_genres_list:
                distinct_genres_list.append(genre_list[i][j])
    print(f"Available genres are: {', '.join(sorted(distinct_genres_list))}")

    while True:
        genre = input("> ")
        

        if genre == "exit":
            return

        found_shows = reverse_search_from_dictionary(genre_data, genre)
        if found_shows:
            print("\n".join(sorted(found_shows)))



if __name__ == "__main__":
    main()
