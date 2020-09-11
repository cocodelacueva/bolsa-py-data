from datetime import datetime
import pytz

tz_BA = pytz.timezone('America/buenos_aires') 
datetime_BA = datetime.now(tz_BA)
hora = datetime_BA.strftime("%H:%M:%S")
print(hora)