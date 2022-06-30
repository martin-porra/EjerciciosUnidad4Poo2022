from clasePaciente import Paciente

from claseManejadorPacientes import ManejadorPacientes

from claseObjectEncoder import ObjectEncoder

from vistaPacientes import PacientesView

from claseControladorPacientes import ControladorPacientes

from claseRepositorioPacientesJSON import RespositorioPacientes

def testPacientes(unManejadorPacientes):
    paciente1=Paciente('Rueda', 'Melisa', '(264)4777222','157', '67') #peso sup al normal
    paciente2=Paciente('López', 'Carlos', '(261)4888111','165', '70') #peso sup al normal
    paciente3=Paciente('Pérez', 'Maira', '(264)5111222','170', '65')  #peso normal
    paciente4=Paciente('Altamirano', 'Sandra', '(263)6478912','190', '80') #peso inf al normal
    paciente5=Paciente('Artime', 'Luis', '(264)4558699','157', '80') #obesidad
    unManejadorPacientes.agregarPaciente(paciente1)
    unManejadorPacientes.agregarPaciente(paciente2)
    unManejadorPacientes.agregarPaciente(paciente3)
    unManejadorPacientes.agregarPaciente(paciente4)
    unManejadorPacientes.agregarPaciente(paciente5)

def main():
    conn=ObjectEncoder('pacientes.json')
    repo=RespositorioPacientes(conn)
    vista=PacientesView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()


if __name__=='__main__':
    jF = ObjectEncoder('pacientes.json')
    manejador=ManejadorPacientes()
    
    #Para generar el archivo json con los datos de los pacientes usamos:
    #testPacientes(manejador)
    #diccionarioManejador=manejador.toJSON()
    #jF.guardarJSONArchivo(diccionarioManejador)

    #Cuando ya se encuentre cargado el json, usamos
    diccionario=jF.leerJSONArchivo()
    manejador=jF.decodificarDiccionario(diccionario)
    main()