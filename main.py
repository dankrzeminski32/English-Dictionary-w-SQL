import mysql.connector
from difflib import SequenceMatcher, get_close_matches

# SQL server connection
con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

run_again = True
print("---WELCOME TO SQL ENGLISH DICTIONARY---\n")


while run_again:

    # define SQL cursor
    cursor = con.cursor()
    i = 0
    word = input("Enter a word that you would like the definition to: ")
    print("\n")


    # Fetches expressiion and definition of word variable from SQL server
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    results = cursor.fetchall()
    query2 = cursor.execute("SELECT Expression FROM Dictionary")
    expressions = [b[0] for b in cursor.fetchall()]

    if results:  # if spelling is accurate then returns back value of dictionary
        for result in results:
            print(result[1])
    # otherwise checks for similar words and prompts user
    elif len(get_close_matches(word, expressions)) > 0:
        matches = get_close_matches(word, expressions)
        close_word = matches[0]
        error_check = input(("did you mean %s instead? (Y/N): " % close_word))
        if error_check == 'y' or error_check == 'Y':
            close_word_query = cursor.execute(
                "SELECT * FROM Dictionary WHERE Expression = '%s' " % close_word)
            close_word_definition = cursor.fetchall()
            for definition in close_word_definition:
                each_def = close_word_definition[i]
                print(each_def[1])
                i = i + 1
        else:
            print("Sorry, then that word does not exist in our database")
    else:
        print("Sorry we do not have a definition for that word\n")
    print("\n")
    
    answer = input("Would you like to search for another word? (Y/N): ")
    print("\n")
    if answer == 'y' or answer == 'Y':
        run_again = True
    else:
        print("ENDING SERVER")
        run_again = False
