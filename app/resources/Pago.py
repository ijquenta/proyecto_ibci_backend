from flask_restful import Resource, reqparse
from services.pago_service import * # Servicio de pago
# from core.auth import require_token
# from resources.Autenticacion import token_required

class GetPayments(Resource):
    def get(self):
        paymests_data = getPayments()
        # print("paymests_data:",paymests_data)
        return paymests_data

class ListarPago(Resource):
    # method_decorators = [token_required]  # Aplica el decorador a todos los métodos de la clase
    # @token_required
    def get(self):
        return listarPago()
        # return make_response(jsonify(listarUsuarios())), 200
      
parsePagoEstudiante = reqparse.RequestParser()
parsePagoEstudiante.add_argument('perid', type=int, help='Ingrese perid', required=True)
class ListarPagoEstudiante(Resource):
    # @token_required
    def post(self):
        data = parsePagoEstudiante.parse_args()
        return listarPagoEstudiante(data)

parsePagoEstudianteMateria = reqparse.RequestParser()
parsePagoEstudianteMateria.add_argument('perid', type=int, help='Ingrese perid', required=True)
parsePagoEstudianteMateria.add_argument('curid', type=int, help='Ingrese curid', required=True)
parsePagoEstudianteMateria.add_argument('matid', type=int, help='Ingrese matid', required=True)
class ListarPagoEstudianteMateria(Resource):
    # @token_required
    def post(self):
        data = parsePagoEstudianteMateria.parse_args()
        return listarPagoEstudianteMateria(data)
      
class ListarPagoCurso(Resource):
    def get(self):
        return listarPagoCurso()  
      
parsePagoEstudiantesMateria = reqparse.RequestParser()
parsePagoEstudiantesMateria.add_argument('curid', type=int, help='Ingrese curid', required=True)
parsePagoEstudiantesMateria.add_argument('matid', type=int, help='Ingrese matid', required=True)
class ListarPagoEstudiantesMateria(Resource):
    # @token_required
    def post(self):
        data = parsePagoEstudiantesMateria.parse_args()
        return listarPagoEstudiantesMateria(data)
      
      
parseGestionarPago = reqparse.RequestParser()
parseGestionarPago.add_argument('tipo', type=int, help='Ingrese tipo', required=True)
parseGestionarPago.add_argument('pagid', type=int, help='Ingrese pagid', required=True)
parseGestionarPago.add_argument('insid', type=int, help='Ingrese insid', required=True)
parseGestionarPago.add_argument('pagdescripcion', type=str, help='Ingrese pagdescripcion', required=True)
parseGestionarPago.add_argument('pagmonto', type=int, help='Ingrese pagmonto', required=True)
parseGestionarPago.add_argument('pagfecha', type=str, help='Ingrese pagfecha', required=True)
parseGestionarPago.add_argument('pagrusureg', type=str, help='Ingrese pagrusureg', required=True)
parseGestionarPago.add_argument('pagestadodescripcion', type=str, help='Ingrese pagestadodescripcion', required=True)
parseGestionarPago.add_argument('pagestado', type=int, help='Ingrese pagestado', required=True)
class GestionarPago(Resource):
    # @token_required
    def post(self):
        data = parseGestionarPago.parse_args()
        return gestionarPago(data)
    
class TipoPago(Resource):
    def get(self):
        return tipoPago()  

# Insertar Pago
parseInsertarPago = reqparse.RequestParser()
parseInsertarPago.add_argument('pagdescripcion', type=str, help='Ingrese pagdescripcion', required=True)
parseInsertarPago.add_argument('pagmonto', type=float, help='Ingrese pagmonto', required=True)
parseInsertarPago.add_argument('pagarchivo', type=str, help='Ingrese pagarchivo')
parseInsertarPago.add_argument('pagfecha', type=str, help='Ingrese pagfecha', required=True)
parseInsertarPago.add_argument('pagusureg', type=str, help='Ingrese pagusureg', required=True)
parseInsertarPago.add_argument('pagtipo', type=int, help='Ingrese pagtipo', required=True)
class InsertarPago(Resource):
    # @token_required
    def post(self):
        data = parseInsertarPago.parse_args()
        return insertarPago(data)

parseModificarPago = reqparse.RequestParser()
parseModificarPago.add_argument('pagid', type=int, help='Ingrese pagid', required=True)
parseModificarPago.add_argument('pagdescripcion', type=str, help='Ingrese pagdescripcion', required=True)
parseModificarPago.add_argument('pagmonto', type=float, help='Ingrese pagmonto', required=True)
parseModificarPago.add_argument('pagarchivo', type=str, help='Ingrese pagarchivo')
parseModificarPago.add_argument('pagfecha', type=str, help='Ingrese pagfecha', required=True)
parseModificarPago.add_argument('pagusumod', type=str, help='Ingrese pagusureg', required=True)
parseModificarPago.add_argument('pagtipo', type=int, help='Ingrese pagtipo', required=True)
parseModificarPago.add_argument('archivobol', type=int, help='Ingrese archivobol', required=True)
class ModificarPago(Resource):
    # @token_required
    def post(self):
        data = parseModificarPago.parse_args()
        return modificarPago(data)

# Asignar Pago a Inscripcion  
parseAsignarPagoInscripcion = reqparse.RequestParser()
parseAsignarPagoInscripcion.add_argument('insid', type=int, help='Ingrese insid', required=True)
parseAsignarPagoInscripcion.add_argument('pagid', type=int, help='Ingrese pagid', required=True)
parseAsignarPagoInscripcion.add_argument('pagusumod', type=str, help='Ingrese pagusureg', required=True)
class AsignarPagoInscripcion(Resource):
    # @token_required
    def post(self):
        data = parseAsignarPagoInscripcion.parse_args()
        return asignarPagoInscripcion(data)
    
# Asignar pago a matricula  
parseAsignarPagoMatricula = reqparse.RequestParser()
parseAsignarPagoMatricula.add_argument('matrid', type=int, help='Ingrese matrid', required=True)
parseAsignarPagoMatricula.add_argument('pagid', type=int, help='Ingrese pagid', required=True)
parseAsignarPagoMatricula.add_argument('matrusumod', type=str, help='Ingrese matrusumod', required=True)
class AsignarPagoMatricula(Resource):
    # @token_required
    def post(self):
        data = parseAsignarPagoMatricula.parse_args()
        return asignarPagoMatricula(data)
    
class ObtenerUltimoPago(Resource):
    def get(self):
        return obtenerUltimoPago()