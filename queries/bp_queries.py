# bp = Brecht Proesmans

all_reviews = "SELECT * FROM bakery.reviews;"
apply = "INSERT INTO bakery.applicants (name, mail, motivation) VALUES (%s, %s, %s);"
people = 'SELECT * FROM bakery.people WHERE gender LIKE %s'