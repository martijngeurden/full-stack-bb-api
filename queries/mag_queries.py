sub_all = "SELECT * FROM bakery.subscriptions;"

sub_push = "INSERT INTO bakery.subscriptions (email, firstName, lastName, subscriptionType, address, address2, zipCode, city, additionalInformation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

pastries = "SELECT * FROM bakery.pastries WHERE score >= %s ORDER BY price %s;"