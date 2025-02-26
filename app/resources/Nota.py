from flask_restful import Resource, reqparse
from resources.Autenticacion import token_required
from services.nota_service import *
from resources.Autenticacion import token_required

class ListarNota(Resource):
    @token_required
    def get(self):
        return listarNota()

class ListarNotaCurso(Resource):
    @token_required
    def get(self):
        return listarNotaCurso() 

parseGestionarNota = reqparse.RequestParser()
parseGestionarNota.add_argument('tipo', type=int, help='Ingrese tipo', required=True)
parseGestionarNota.add_argument('notid', type=int, help='Ingrese notid', required=True)
parseGestionarNota.add_argument('insid', type=int, help='Ingrese insid', required=True)
parseGestionarNota.add_argument('not1', type=float, help='Ingrese not1', required=True)  # Cambiar a float
parseGestionarNota.add_argument('not2', type=float, help='Ingrese not2', required=True)  # Cambiar a float
parseGestionarNota.add_argument('not3', type=float, help='Ingrese not3', required=True)  # Cambiar a float
parseGestionarNota.add_argument('notfinal', type=float, help='Ingrese notfinal', required=True)  # Cambiar a float
parseGestionarNota.add_argument('notusureg', type=str, help='Ingrese notusureg', required=True)
parseGestionarNota.add_argument('notusumod', type=str, help='Ingrese notusumod', required=True)
parseGestionarNota.add_argument('notestado', type=int, help='Ingrese notestado', required=True)
class GestionarNota(Resource):
    @token_required
    def post(self):
        data = parseGestionarNota.parse_args()
        return manage_nota(data)    
  
parseNotaEstudiante = reqparse.RequestParser()
parseNotaEstudiante.add_argument('perid', type=int, help='Ingrese perid', required=True)
class ListarNotaEstudiante(Resource):
    @token_required
    def post(self):
        data = parseNotaEstudiante.parse_args()
        return listarNotaEstudiante(data)

parseNotaDocente = reqparse.RequestParser()
parseNotaDocente.add_argument('perid', type=int, help='Ingrese perid', required=True)
class ListarNotaDocente(Resource):
    @token_required
    def post(self):
        data = parseNotaDocente.parse_args()
        return listarNotaDocente(data)  
    
parseNotaEstudianteMateria = reqparse.RequestParser()
parseNotaEstudianteMateria.add_argument('perid', type=int, help='Ingrese perid', required=True)
parseNotaEstudianteMateria.add_argument('curid', type=int, help='Ingrese curid', required=True)
parseNotaEstudianteMateria.add_argument('matid', type=int, help='Ingrese matid', required=True)
class ListarNotaEstudianteMateria(Resource):
    @token_required
    def post(self):
        data = parseNotaEstudianteMateria.parse_args()
        return listarNotaEstudianteMateria(data)

parseNotaEstudianteCurso = reqparse.RequestParser()
parseNotaEstudianteCurso.add_argument('curmatid', type=int, help='Ingrese curmatid', required=True)
class ListarNotaEstudianteCurso(Resource):
    @token_required
    def post(self):
        data = parseNotaEstudianteCurso.parse_args()
        return listarNotaEstudianteCurso(data)
    
    
parseRptNotaEstudianteMateria = reqparse.RequestParser()
parseRptNotaEstudianteMateria.add_argument('perid', type=int, help='Ingrese perid', required=True)
parseRptNotaEstudianteMateria.add_argument('usuname', type=str, help='Ingrese usuname', required=True)
class RptNotaEstudianteMateria(Resource):
    def post(self):
        data = parseRptNotaEstudianteMateria.parse_args()
        return rptNotaEstudianteMateria(data)
    
parseRptNotaCursoMateria = reqparse.RequestParser()
parseRptNotaCursoMateria.add_argument('curmatid', type=int, help='Ingrese curmatid', required=True)
parseRptNotaCursoMateria.add_argument('usuname', type=str, help='Ingrese usuname', required=True)
class RptNotaCursoMateria(Resource):
    def post(self):
        data = parseRptNotaCursoMateria.parse_args()
        return rptNotaCursoMateria(data)
    
parseRptNotaCursoMateriaGeneral = reqparse.RequestParser()
parseRptNotaCursoMateriaGeneral.add_argument('usuname', type=str, help='Ingresar nombre del usuario', required=True)
class RptNotaCursoMateriaGeneral(Resource):
    def post(self):
        data = parseRptNotaCursoMateriaGeneral.parse_args()
        return rptNotaCursoMateriaGeneral(data)
    
parseRptNotaCursoMateriaDocente = reqparse.RequestParser()
parseRptNotaCursoMateriaDocente.add_argument('periddocente', type=int, help='Ingrese periddocente', required=True)
parseRptNotaCursoMateriaDocente.add_argument('usuname', type=str, help='Ingresar nombre del usuario', required=True)
class RptNotaCursoMateriaDocente(Resource):
    def post(self):
        data = parseRptNotaCursoMateriaDocente.parse_args()
        return rptNotaCursoMateriaDocente(data)
    
