themepark_query = "SELECT name FROM coasters.themepark"

parkDetails = "SELECT name,openingDate,city,website FROM coasters.themepark;"

parkOpening = "SELECT name,openingDate,city,website FROM coasters.themepark where year(openingDate) = %s;"

inversions = "SELECT name,height,length,maximumSpeed,inversions FROM coasters.rollercoaster where inversions>=%s  order by 5,1;"

coasters = "SELECT name,height,length,maximumSpeed,inversions FROM coasters.rollercoaster where rollercoasterID=%s order by 5,1;"