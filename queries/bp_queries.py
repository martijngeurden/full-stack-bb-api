all_reviews = "SELECT * FROM bakery.reviews;"
apply = "INSERT INTO bakery.applicants (name, mail, motivation, fileLocation) VALUES (%s, %s, %s, %s);"
