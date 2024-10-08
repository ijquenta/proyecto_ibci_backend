from flask_restful import Resource, reqparse
from resources.Autenticacion import token_required
from services.curso_service import * # Servicio de curso

class ListarCursoMateria(Resource):
  @token_required
  def get(self):
      return getListCursoMateria()

parseEliminarCursoMateria = reqparse.RequestParser()
parseEliminarCursoMateria.add_argument('curmatid', type=int, help='Debe ingresar curmatid', required = True)
class EliminarCursoMateria(Resource):
  @token_required
  def post(self):
      data = parseEliminarCursoMateria.parse_args()
      return eliminarCursoMateria(data)

parseInsertarCursoMateria = reqparse.RequestParser()
parseInsertarCursoMateria.add_argument('curid', type=int, help='Debe ingresar curid', required = True)
parseInsertarCursoMateria.add_argument('matid', type=int, help='Debe ingresar matid', required = True)
parseInsertarCursoMateria.add_argument('periddocente', type=int, help='Debe ingresar periddocente', required = True)
parseInsertarCursoMateria.add_argument('curmatfecini', type=str, help='Debe insersar curmatfecini', required = True)
parseInsertarCursoMateria.add_argument('curmatfecfin', type=str, help='Debe insersar curmatfecfin', required = True)
parseInsertarCursoMateria.add_argument('curmatestado', type=str, help='Debe insersar curmatestado', required = True)
parseInsertarCursoMateria.add_argument('curmatestadodescripcion', type=str, help='Debe insersar curmatestadodescripcion', required = True)
parseInsertarCursoMateria.add_argument('curmatusureg', type=str, help='Debe insersar curmatusureg', required = True)
parseInsertarCursoMateria.add_argument('curmatidrol', type=int, help='Debe insersar curmatidrol', required = True)
parseInsertarCursoMateria.add_argument('curmatidroldes', type=str, help='Debe insersar curmatidroldes', required = True)
parseInsertarCursoMateria.add_argument('curmatcosto', type=int, help='Debe insersar curmatcosto', required = True)
class InsertarCursoMateria(Resource):
  @token_required
  def post(self):
      data = parseInsertarCursoMateria.parse_args()
      return insertarCursoMateria(data)
    
parseModificarCursoMateria = reqparse.RequestParser()
parseModificarCursoMateria.add_argument('curmatid', type=int, help='Debe ingresar curmatid', required = True)
parseModificarCursoMateria.add_argument('curid', type=int, help='Debe ingresar curid', required = True)
parseModificarCursoMateria.add_argument('matid', type=int, help='Debe ingresar matid', required = True)
parseModificarCursoMateria.add_argument('periddocente', type=int, help='Debe ingresar periddocente', required = True)
parseModificarCursoMateria.add_argument('curmatfecini', type=str, help='Debe insersar curmatfecini', required = True)
parseModificarCursoMateria.add_argument('curmatfecfin', type=str, help='Debe insersar curmatfecfin', required = True)
parseModificarCursoMateria.add_argument('curmatestado', type=str, help='Debe insersar curmatestado', required = True)
parseModificarCursoMateria.add_argument('curmatestadodescripcion', type=str, help='Debe insersar curmatestadodescripcion', required = True)
parseModificarCursoMateria.add_argument('curmatusumod', type=str, help='Debe insersar curmatusumod', required = True)
parseModificarCursoMateria.add_argument('curmatidrol', type=int, help='Debe insersar curmatidrol', required = True)
parseModificarCursoMateria.add_argument('curmatidroldes', type=str, help='Debe insersar curmatidroldes', required = True)
parseModificarCursoMateria.add_argument('curmatcosto', type=int, help='Debe insersar curmatcosto', required = True)
class ModificarCursoMateria(Resource):
  @token_required
  def post(self):
      data = parseModificarCursoMateria.parse_args()
      return modificarCursoMateria(data)

class ListaCursoCombo(Resource):
  @token_required
  def get(self):
      return listaCursoCombo()
       
parseListaPersonaDocenteCombo = reqparse.RequestParser()
parseListaPersonaDocenteCombo.add_argument('rolnombre', type=str, help='Debe ingresar el nombre del rol', required = True)
class ListaPersonaDocenteCombo(Resource):
  @token_required
  def post(self):
    data = parseListaPersonaDocenteCombo.parse_args()
    return listaPersonaDocenteCombo(data)
  
class TipoRol(Resource):
  @token_required
  def get(self):
    return tipoRol()
  
parseGestionarCursoMateriaEstado = reqparse.RequestParser()
parseGestionarCursoMateriaEstado.add_argument('tipo', type=int, help='Debe ingresar tipo', required = True)
parseGestionarCursoMateriaEstado.add_argument('curmatid', type=int, help='Debe ingresar curmatid', required = True)
parseGestionarCursoMateriaEstado.add_argument('curmatusumod', type=str, help='Debe insersar curmatusumod', required = True)
class GestionarCursoMateriaEstado(Resource):
  @token_required
  def post(self):
      data = parseGestionarCursoMateriaEstado.parse_args()
      return gestionarCursoMateriaEstado(data)
    
    
class GetCursoByIdResource(Resource):
    @token_required
    def get(self, curid):
        return getCursoById(curid)
    

class GetTipoCurso(Resource):
    @token_required
    def get(self):
        return getTipoCurso()
  
class GetTipoMateriaByCursoIdResource(Resource):
    @token_required
    def get(self, curid):
        return getTipoMateriaByCursoId(curid)
