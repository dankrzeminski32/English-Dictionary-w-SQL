import mysql.connector
from difflib import SequenceMatcher, get_close_matches


con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    query2 = cursor.execute("SELECT Expression FROM Dictionary")
    expressions = [b[0] for b in cursor.fetchall()]

    matches = get_close_matches(word, expressions)
    print(matches)
    #print("did you mean %s instead? (Y/N)" % )