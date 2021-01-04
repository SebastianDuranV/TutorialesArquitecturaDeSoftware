import os
import mysql.connector

class NestorBot:

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
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
            return "ERR -"


    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self,command):
        return {
            "channel": self.channel,
            "blocks": [
                self._message(command),
            ],
        }