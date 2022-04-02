from weatherdata import WeatherData
from currentconditions import DisplayCurrentConditions

wd = WeatherData()
cc=DisplayCurrentConditions(wd)

wd.measurements_changed("15 derece","50%","3N")
wd.measurements_changed("16 derece","90%","3N")



