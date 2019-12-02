import pandas as pd
from pandas.tseries.holiday import Holiday, sunday_to_monday, AbstractHolidayCalendar, Easter, Day
from pandas.tseries.offsets import CustomBusinessDay
from datetime import date, timedelta, datetime

class EsBusinessCalendar(AbstractHolidayCalendar):
   rules = [
     Holiday('Año Nuevo', month=1, day=1, observance=sunday_to_monday),
     Holiday('Epifanía del Señor', month=1, day=6, observance=sunday_to_monday),
     Holiday('Viernes Santo', month=1, day=1, offset=[Easter(), Day(-2)]),
     Holiday('Día del Trabajador', month=5, day=1, observance=sunday_to_monday),
     Holiday('Asunción de la Virgen', month=8, day=15, observance=sunday_to_monday),
     Holiday('Día de la Hispanidad', month=10, day=12, observance=sunday_to_monday),
     #Holiday('Todos los Santos', month=11, day=1, observance=sunday_to_monday),
     #Holiday('Día Constitución', month=12, day=6, observance=sunday_to_monday),
     Holiday('Inmaculada Concepción', month=12, day=8, observance=sunday_to_monday),
     Holiday('Navidad', month=12, day=25, observance=sunday_to_monday)
   ]
   def __init__(self, extra_rules):
       self.rules.extend(extra_rules)


class weekday(object):
      rules = []
      def __init__(self, inicio, fin):
            date_object = datetime.strptime(inicio, '%d/%m/%Y')
            inicio = date_object - timedelta(days=30)
            inicio = inicio.strftime('%Y-%m-%d')
            
            date_object = datetime.strptime(fin, '%d/%m/%Y')
            fin = date_object.strftime('%Y-%m-%d')
            self.inicio = inicio
            self.fin = fin

      def obtener_habiles(self, inhabiles):
            for inhabil in inhabiles:
                  fecha = inhabil.split('/')
                  self.rules.append(Holiday('Festivo', month=int(fecha[1]), day=int(fecha[0]), observance=sunday_to_monday))
            es_BD = CustomBusinessDay(calendar=EsBusinessCalendar(self.rules))
            s = pd.date_range(self.inicio, end=self.fin, freq=es_BD)
            s.strftime('%Y-%m-%d')
            return s.tolist()

class process_data(object):

      def __weekday(self, day):
            date_number = day.weekday()
            if date_number < 5:
                  return day
            else:
                  new_date = day - timedelta(days=1)
                  return self.__weekday(new_date)

      def date_assignament(self, date):
            if date == 'lunes':
                  return 0
            if date == 'martes':
                  return 1
            if date == 'miercoles':
                  return 2
            if date == 'jueves':
                  return 3
            if date == 'viernes':
                  return 4
      def get_dates(self, str_dates):
            dates = []
            index = 0
            for date in str_dates:
                  date_object = datetime.strptime(date, '%d/%m/%Y')
                  if index < 3:
                        quantity = 6
                  else:
                        quantity = 3
                  optimal_date = date_object - timedelta(days = quantity)
                  final_date = self.__weekday(optimal_date)
                  dates.append(final_date)
                  index += 1
            return dates