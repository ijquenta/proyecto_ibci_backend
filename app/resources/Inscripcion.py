from flask_restful import Resource, reqparse
from services.inscripcion_service import *

class ListarInscripcion(Resource):
  def get(self):
      return listarInscripcion()
    
class ListarComboCursoMateria(Resource):
  def get(self):
      return listarComboCursoMateria()
    
class ListarComboMatricula(Resource):
  def get(self):
      return listarComboMatricula()

parseInsertarInscripcion = reqparse.RequestParser()
parseInsertarInscripcion.add_argument('matrid', type=int, help = 'Debe elegir matrid', required = True)
parseInsertarInscripcion.add_argument('peridestudiante', type=int, help = 'Debe elegir peridestudiante', required = True)
parseInsertarInscripcion.add_argument('pagid', type=int, help = 'Debe elegir pagid', required = True)
parseInsertarInscripcion.add_argument('insusureg', type=str, help = 'Debe elegir insusureg', required = True)
parseInsertarInscripcion.add_argument('curmatid', type=int, help = 'Debe elegir numero curmatid', required = True)
parseInsertarInscripcion.add_argument('insestado', type=int, help = 'Debe elegir insestado', required = True)
parseInsertarInscripcion.add_argument('insestadodescripcion', type=str, help = 'Debe elegir insestadodescripcion', required = True)
class InsertarInscripcion(Resource):
  def post(self):
    data = parseInsertarInscripcion.parse_args()
    return insertarInscripcion(data)
  
parseModificarInscripcion = reqparse.RequestParser()
parseModificarInscripcion.add_argument('insid', type=int, help = 'Debe elegir insid', required = True)
parseModificarInscripcion.add_argument('matrid', type=int, help = 'Debe elegir matrid', required = True)
parseModificarInscripcion.add_argument('peridestudiante', type=int, help = 'Debe elegir peridestudiante', required = True)
parseModificarInscripcion.add_argument('pagid', type=int, help = 'Debe elegir pagid', required = True)
parseModificarInscripcion.add_argument('insusumod', type=str, help = 'Debe elegir insusureg', required = True)
parseModificarInscripcion.add_argument('curmatid', type=int, help = 'Debe elegir numero curmatid', required = True)
parseModificarInscripcion.add_argument('insestado', type=int, help = 'Debe elegir insestado', required = True)
parseModificarInscripcion.add_argument('insestadodescripcion', type=str, help = 'Debe elegir insestadodescripcion', required = True)
class ModificarInscripcion(Resource):
  def post(self):
    data = parseModificarInscripcion.parse_args()
    return modificarInscripcion(data)
  

parseObtenerCursoMateria = reqparse.RequestParser()
parseObtenerCursoMateria.add_argument('curid', type=int, help = 'Debe elegir curid', required = True)
parseObtenerCursoMateria.add_argument('matid', type=int, help = 'Debe elegir matid', required = True)
class ObtenerCursoMateria(Resource):
  def post(self):
    data = parseObtenerCursoMateria.parse_args()
    return obtenerCursoMateria(data)
  
parseEliminarInscripcion = reqparse.RequestParser()
parseEliminarInscripcion.add_argument('insid', type=int, help = 'Debe elegir insid', required = True)
class EliminarInscripcion(Resource):
  def post(self):
    data = parseEliminarInscripcion.parse_args()
    return eliminarInscripcion(data)
  
  
  