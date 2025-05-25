archivo_sin_leer = open ("archivos\\texto_de_dalto.txt",encoding="UTF-8")
#una vez que un archivo se lee, no se puede volver a leer. Habría que cerrarlo

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer línea por línea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()


#con archivos muy grandes de texto, cuidado con el readlines() porque te consume toda la RAM

#cerrar el archivo
archivo_sin_leer.close()

#si queremos leerlo deberíamos abrirlo de nuevo
print(linea)
