from flask_restful import Api
import resources.Matricula as Matricula
from client.routes import Routes as routes

def matricula_routes(api: Api):
    api.add_resource(Matricula.ListarMatricula, routes.listarMatricula)
    api.add_resource(Matricula.ListarMatriculaEstudiante, routes.listarMatriculaEstudiante)
    api.add_resource(Matricula.InsertarMatricula, routes.insertarMatricula)
    api.add_resource(Matricula.ModificarMatricula, routes.modificarMatricula)
    api.add_resource(Matricula.EliminarMatricula, routes.eliminarMatricula)
    api.add_resource(Matricula.GestionarMatriculaEstado, routes.gestionarMatriculaEstado)   
    api.add_resource(Matricula.ListarTipoMatricula, routes.listarTipoMatricula)
    api.add_resource(Matricula.InsertarTipoMatricula, routes.insertarTipoMatricula)
    api.add_resource(Matricula.ModificarTipoMatricula, routes.modificarTipoMatricula)
    api.add_resource(Matricula.GestionarTipoMatriculaEstado, routes.gestionarTipoMatriculaEstado)
    api.add_resource(Matricula.ListarTipoMatriculaCombo, routes.listarTipoMatriculaCombo)
    api.add_resource(Matricula.ListarTipoPersonaEstudiante, routes.listarTipoPersonaEstudiante)
    