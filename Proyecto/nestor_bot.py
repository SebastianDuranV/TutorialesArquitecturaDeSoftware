import os
import mysql.connector

class NestorBot:

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel, user):
        self.user = user
        self.channel = channel

    def _message(self,command):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="slackdatabase"
        )

        try:
            cur = mydb.cursor()
            cur.execute(command)
            try: #En caso de leer la base de datos
                ips = cur.fetchall()
                return ips
            except: # En caso de escribir en la base de datos
                print()
            mydb.commit()
            cur.close()
            return "OK +"
        except:
            cur = mydb.cursor()
            
            # Canales 
            cur.execute("select nombrecanal from canal")
            ips = cur.fetchall()
            if (self.channel,) not in ips:
                cur.execute("insert into canal(nombrecanal) values('" + self.channel +"')")
                mydb.commit()
                cur.execute("select idcanal from canal where nombrecanal = '" + self.channel + "'" )
                idChannel = cur.fetchall()
            else:
                cur.execute("select idcanal from canal where nombrecanal = '" + self.channel + "'" )
                idChannel = cur.fetchall()

            # Usuarios
            cur.execute("select nombreusuario from usuario")
            ips = cur.fetchall()
            if (self.user,) not in ips:
                cur.execute("insert into usuario(nombreusuario) values('" + self.user +"')")
                mydb.commit()
                cur.execute("select idusuario from usuario where nombreusuario = '" + self.user + "'" )
                idUser = cur.fetchall()
            else:
                cur.execute("select idusuario from usuario where nombreusuario = '" + self.user + "'" )
                idUser = cur.fetchall()

            idChannel = str(idChannel[0][0])
            idUser = str(idUser[0][0])
            print(command,idChannel,idUser)
            cur.execute("insert into mensaje (contenido,data,idusuario,idcanal) values('" + command +"',NOW(),'" + idChannel +"','" + idUser +"')")
            mydb.commit()
            cur.close()
            return "OK ++"


    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self,command):
        return self._message(command)