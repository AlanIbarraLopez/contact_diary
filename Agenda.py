"""
    Agenda de contactos con Archivo
    Contact Diary with File
    Author: Alan Ibarra
    Python 3.6
"""
class Agenda:
    def __init__(self):
        self.db = "agenda.txt"

    def agregar(self,nombre,telefono):
        id = self.consultar()
        contacto = str(id + 1) + "," + str(nombre) + "," + str(telefono) + "\n"
        regs = self.contactos() + contacto
        data = open(self.db , 'w')
        data.write(regs)
        data.close()
        return True

    def eliminar(self,id):
        num = self.consultar()
        out = True
        if(num > 0):
            registros = ""
            with open(self.db) as f:
                for contacto in f:
                    conct = contacto.split(',')
                    num = conct[0]
                    if(num != id):  
                        registros +=contacto
            f.close()
            f  = open(self.db,'w')
            f.write(registros)
            f.close()
        else:
            out = False
        return out

    def modificar(self,id,nombre,telefono):
        out = True
        if(self.consultar() == 0):
            out = False
            
        with open(self.db) as f:
            registros = ""
            for contacto in f:
                conct = contacto.split(',')
                num = conct[0]
                if(num == id):
                    nombre = conct[1] if nombre == "" else nombre
                    telefono = conct[2] if telefono == "" else telefono + "\n"
                    registros += str(id) + "," + str(nombre) + "," + str(telefono)
                else:
                    registros += contacto
            f.close()
            f = open(self.db ,"w")
            f.write(registros)
            f.close()
        return out
        
    def consultar(self):
        num = 0
        registros = ""
        with open(self.db) as f:
            for contacto in f:
                reg = contacto.split(',')
                num = int(reg[0])
                registros += contacto
            f.close()
        return num

    def contactos(self):
        registros = ""
        with open(self.db) as f:
            for contacto in f:
                registros +=contacto
            f.close()
        return registros

    def main(self):
        opcion = '0'
        while(opcion != '5'):
            print("#######-CONTACTOS-#######")
            print("# 1. Ver Contactos      #")
            print("# 2. Nuevo Contacto     #")
            print("# 3. Eliminar Contacto  #")
            print("# 4. Modificar Contacto #")
            print("# 5. Salir              #")
            print("#########################")
            opcion = input("Capture una opción: ")

            if(opcion == '1'):
                print(self.contactos())
            elif(opcion == '2'):
                nombre = input("Nombre: ")
                tel = input("Telefono: ")
                if(self.agregar(nombre , tel)):
                    print("Guardado con exito")
                else:
                    print("No se pudo guardar")
            elif(opcion == '3'):
                id = input("Capture el ID del contacto: ")
                if(self.eliminar(id)):
                    print("Contacto eliminado")
                else:
                    print("No se elimino, puede que no exista el contacto")
            elif(opcion == '4'):
                id = input("Capture el ID del contacto: ")
                nombre = input("Capture el nuevo nombre: ")
                telefono = input("Capture el nuevo telefono: ")
                if(self.modificar(id,nombre,telefono)):
                    print("Contacto actualizado")
                else:
                    print("No se actualizo, es posible que no exista")
            else:
                pass


if __name__ == "__main__":
    a = Agenda()
    a.main()
        


