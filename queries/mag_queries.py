# mag = Martijn Geurden

sub_all = "SELECT * FROM bakery.subscriptions;"
sub_push = "INSERT INTO bakery.subscriptions (email, firstName, lastName, subscriptionType, address, address2, zipCode, city, additionalInformation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
sub_check_mail = "SELECT email FROM bakery.subscriptions;"

pastries = "SELECT * FROM bakery.pastries WHERE score >= %s ORDER BY price;"
pastriesDesc = "SELECT * FROM bakery.pastries WHERE score >= %s ORDER BY price DESC;"

post_order = "INSERT INTO bakery.orders (name, orderDate, orderDetails) VALUES (%s, %s, %s);"