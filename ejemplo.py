class Paciente:
    def __init__(self):
        self.__nombre =''
        self.__cedula = 0
        self.__genero = ''
        self.__servicio = ''

    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula

    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarCedula(self,c):
        self.__cedula = c 
class Sistema():
    def __init__(self):
        self.__lista_pacientes = []
    def verificarPaciente(self,cedula):
        encontrado= False
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                encontrado = True
                break
        return encontrado
    def ingresarPacientes(self):
        nombre= input('Ingrese el nombre: ')
        cedula= int(input('Ingrese la cedula: '))
        genero= input('Ingrese el genero: ')
        servicio= input('Ingrese el servicio: ')
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p)
        self.__numero_pacientes = len(self.__lista_pacientes)
    def verNumeroPacientes(self):
        return self.__numero_pacientes
    def verDatosPaciente(self):
        cedula = int(input('Ingrese cedula a buscar:  '))
        for paciente in self.__lista_pacientes:
            if cedula ==paciente.verCedula():
                print(f'Nombre: {paciente.verNombre()}')
                print(f'Cedula: {str(paciente.verCedula())}')
                print(f'Genero: {paciente.verGenero()}')
                print(f'Servicio: {paciente.verServicio()}')
mi_sistema=Sistema()
while True:
    opcion= int(input('1. Nuevo paciente\n2. Numero de pacientes\n3. Datos paciente\n4. Salir\n'))
    if opcion == 1:
        mi_sistema.ingresarPacientes()
    elif opcion== 2:
        print(f'Ahora hay {str(mi_sistema.verNumeroPacientes())} pacientes')
    elif opcion== 3:
        mi_sistema.verDatosPaciente()
    elif opcion== 4:
        break 

    else:
        print('Opcion invalida')

def suma(a,b):
    return a+b

    
