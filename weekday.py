import pandas as pd
from pandas.tseries.holiday import Holiday, sunday_to_monday, AbstractHolidayCalendar, Easter, Day
from pandas.tseries.offsets import CustomBusinessDay

class EsBusinessCalendar(AbstractHolidayCalendar):
   rules = [
     Holiday('Año Nuevo', month=1, day=1, observance=sunday_to_monday),
     Holiday('Epifanía del Señor', month=1, day=6, observance=sunday_to_monday),
     Holiday('Viernes Santo', month=1, day=1, offset=[Easter(), Day(-2)]),
     Holiday('Día del Trabajador', month=5, day=1, observance=sunday_to_monday),
     Holiday('Asunción de la Virgen', month=8, day=15, observance=sunday_to_monday),
     Holiday('Día de la Hispanidad', month=10, day=12, observance=sunday_to_monday),
     #Holiday('Todos los Santos', month=11, day=1, observance=sunday_to_monday),
     Holiday('Día Constitución', month=12, day=6, observance=sunday_to_monday),
     Holiday('Inmaculada Concepción', month=12, day=8, observance=sunday_to_monday),
     Holiday('Navidad', month=12, day=25, observance=sunday_to_monday)
   ]
   def __init__(self, extra_rules):
       self.rules.extend(extra_rules)

rules = [
    #Holiday('Todos los Santos', month=11, day=1, observance=sunday_to_monday),
    Holiday('Todos los Santos', month=11, day=4, observance=sunday_to_monday)
    ]

es_BD = CustomBusinessDay(calendar=EsBusinessCalendar(rules))
inicio = '2019-11-01'
fin = '2019-11-15'
s = pd.date_range(inicio, end=fin, freq=es_BD)
df = pd.DataFrame(s, columns=['Fecha'])
print(df)