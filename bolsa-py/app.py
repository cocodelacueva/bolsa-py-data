from insert_simbolos import insert_simbolos
import schedule
import time 

timeout = time.time() + 60*5
valores = "'YPD', '49.5'"

#insert_simbolos(valores)
    
schedule.every(30).seconds.do(insert_simbolos, valores)

while True:
    schedule.run_pending()
    time.sleep(1)

    if time.time() > timeout:
        break