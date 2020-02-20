import            time
import           winsound
class alarma:

 def __init__(self, f, d):
          self.d=d
          self.f=f

 def detect(self):

    print(" Bienvenido a APITRONICS \n Los horarios de servicio son : \n Lunes - Viernes : 9:00  a 20:00 hrs. \n Sábado : 9:00 a 15:00 hrs. \n Domingo: cerrado \n ")
    d  = str(input(" Escriba en minúsculas \n Ingrese con letras el día que es hoy: "))
    h = float(input(" Ingrese con número la hora actual (horario 24 hrs.) ejem. 21.11: "))

    if (((d != "domingo" or d!="sabado" ) and (h >= 9 and h <= 20)) or  (d == "sabado" and (h >= 9 and h <= 15))) :
         print(" BIENVENIDO, hoy ", d)

    else:
        print(" Hoy " , d,  " a las", h, "no se puede entrar")
        f = self.f
        d = self.d
        t = 0

        while (t != 3):
             winsound.Beep(f, d)
             time.sleep(0.15)
             winsound.Beep(f, d)
             time.sleep(0.15)
             t = t + 1

O = alarma(2500, 900)
O.detect()
