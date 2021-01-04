import mysql.connector

# Conectando a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

#Creando la base de datos
#Debe ser ejecutado solamente una vez de lo contrario se reinicia
try:
    mycursor.execute("DROP DATABASE slackdatabase")
    mycursor.execute("CREATE DATABASE slackdatabase")
except:
    mycursor.execute("CREATE DATABASE slackdatabase")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="slackdatabase"
)

mycursor = mydb.cursor()

# USUARIO
mycursor.execute('CREATE TABLE usuario (idusuario INT  AUTO_INCREMENT , PRIMARY KEY (idusuario), nombreUsuario VARCHAR(80));')

# CANAL
mycursor.execute('CREATE TABLE canal (idcanal INT  AUTO_INCREMENT , PRIMARY KEY (idcanal), nombreCanal VARCHAR(30));')

# MENSAJE
mycursor.execute('CREATE TABLE mensaje (idmensaje INT  AUTO_INCREMENT , PRIMARY KEY (idmensaje), contenido VARCHAR(30)'
                +',data DATETIME'
                +',idusuario int, FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)'
                +',idcanal int, FOREIGN KEY (idcanal) REFERENCES canal(idcanal));')



mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x[0])

mycursor.close()
print()
print("listo..")