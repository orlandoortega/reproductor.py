# ver en repl.it: https://repl.it/CDaf/1
# UNEFA Mérida
# Integrantes: orlandoortega, Gerardouz, mariacolmenares
# Profesor: javierri
# Calificación:

class reproductor:
      rep_encendido = False
      max_vol = 10
      volumen = 5
      cd_interno = False
      pos_cancion = 0
      canciones = 0 
      rep_cancion = False
      usb_interno = False
      frecuencia_fm = True

      def encender(self):
         if (self.rep_encendido == False):
             self.rep_encendido = True
             print ("bienvenido")
      def apagar(self):
         if (self.rep_encendido == True):
             self.rep_encendido = False
             print ("adios")
      #debe insertar el nro de canciones.
      def insertar_cd(self,m):
         self.canciones = m
         if (self.rep_encendido == True):
             if (self.usb_interno == True):
                 self.rep_cancion = False
             if (self.cd_interno == False):
                 self.cd_interno = True
                 self.pos_cancion = 1 
                 print ("reproduciendo cd")
             else:
                 print ("ya hay un cd en la unidad ")
         else:
              print ("error, enciende el reproductor")
                   
      def expulsar(self):
          if (self.rep_encendido == True):
              if (self.cd_interno == True):
                  self.cd_interno = False
                  print ("expulsando")
              else:
                  print (" no hay cd en la unidad")
          else:
              print ("error, enciende el reproductor")
                 
      def subir_vol(self,n):
          if (self.rep_encendido == True):
              for j in range(n):
                  if (self.volumen < self.max_vol):        
                      self.volumen = self.volumen + 1
                      print ("volumen:",self.volumen)
                  else:
                      print ("volumen maximo")
                      break
          else:
              print (" error, enciende el reproductor")
           
      def bajar_vol(self,n):
          if (self.rep_encendido == True):
              for j in range(n):
                  if (self.volumen > 0):
                      self.volumen = self.volumen - 1
                      print ("volumen:",self.volumen)
                  else:
                      print ("volumen al minimo")
                      break
          else:
              print ("error, enciende el reproductor")

      def adelante(self):
         if (self.rep_encendido == True):    
              if (self.pos_cancion < self.canciones):
                  self.pos_cancion = self.pos_cancion + 1 
                  print ("cancion nro:",self.pos_cancion)
              else:
                  print (" ultima cancion")
         else:
             print (" error, enciende el reproductor")
      def atras(self):
          if (self.rep_encendido == True):
              if (self.pos_cancion > 1):
                  self.pos_cancion = self.pos_cancion - 1
                  print ("cancion nro:",self.pos_cancion)
              else:
                  print (" primera cancion")
          else:
              print ("error, enciende el reproductor")

      def reproducir(self):
           if (self.rep_encendido == True):
               if (self.rep_cancion == False):
                   self.rep_cancion = True
               else:
                   print ("ya esta reproduciendo")
           else:
               print ("error, enciende el reproductor")

      def pausar(self):
            if (self.rep_encendido == True):
                if (self.rep_cancion == True):
                    self.rep_cancion = False
                    print ("pausado")
                else:
                    print (" esta en pausa")
            else:
                print ("error, enciende el reproductor")

      #debe insertar el nro de canciones.
      def insertar_usb(self,n):
              self.canciones = n
              if (self.rep_encendido == True):
                  if (self.cd_interno == True):
                      rep_cancion = False
                      
                  if (self.usb_interno == False):
                      self.rep_cancion = False
                      self.usb_interno = True
                      self.reproducir()
                      self.pos_cancion = 1
                      print ("reproduciendo usb")
                  else:
                      print ("usb en la unidad")
              else:
                  print ("error, enciende el reproductor")
                  
      #tiene que insertar una emisora cualquiera am o fm.
      def radio(self,n):
          if (self.rep_encendido == True):
              self.frecuencia = n
              if (type(n) == float):
                  self.rep_cancion = False
                  self.frecuencia = n
                  self.reproducir()
                  print ("reproduciendo radio su frecuencia es fm: ",n)
              else:
                  self.cambiar_frecuencia()
                  self.rep_cancion = False
                  self.reproducir()
                  print ("reproduciendo radio su frecuencia es am: ",n)
          else:
              print ("error, enciende el reproductor")
      
      def cambiar_frecuencia(self):
          if (self.rep_encendido == True):
              if (self.frecuencia_fm == True):
                  self.frecuencia_fm = False
              else:
                  self.frecuencia_fm = True
          else:
              print ("error, encienda el reproductor")

reproductor = reproductor()
reproductor.encender()
reproductor.radio(101.1)
reproductor.pausar()
reproductor.reproducir()
reproductor.radio(120)
reproductor.apagar()
reproductor.encender()
reproductor.radio(312)
reproductor.insertar_usb(8)
reproductor.adelante()
reproductor.insertar_cd(9)
reproductor.atras()
reproductor.adelante()
reproductor.adelante()
reproductor.subir_vol(2)
reproductor.bajar_vol(8)
reproductor.subir_vol(11)
reproductor.expulsar()
reproductor.expulsar()
reproductor.apagar()
reproductor.insertar_cd(9)
