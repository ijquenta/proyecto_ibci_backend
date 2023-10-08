from flask_cors import CORS
from flask import Flask, session, jsonify, request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from logging.handlers import RotatingFileHandler
from core import configuration
import logging
import traceback
import os

from client.responses import clientResponses as messages
from client.routes import Routes as routes

import resources.resources as resources
import resources.BenSocial as BenSocial
import resources.Persona as Persona
import resources.Reportes as Report
import resources.Usuario as Usuario

from core.database import Base, session_db, engine
from web.wsrrhh_service import *


# Librerias para para JWT (Json Web Token)
# requests: acceder datos enviados del por el cliente en una solicitud http.
# jsonify: es una función para convertir objetvos de Python en repuestas JSON al cliente.
# make_responde: se utlizara para crear una respuesta HTTP personalizada.
# reder_template: se tuliza para renderizar planillas HTML.
# session: permite almacenar datos del usuario en una sesión persistente entre solicitudes HTTP.
# jwt. es una biblioteca para trabajnar con tokens JWT, permite crear firmar y verificar tokens JWT, que son utiles para la autenticación y autorización en aplicaciones web.
# datetime: se utilizan para trabajar con fecha y tiempos.
# wraps: es un decorador en Python, se utiliza para mantener infomación de metadatos de una función, como su nombre y su documentación.
from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps
# importar para JWT

LOG_FILENAME = 'aplication.log'
#logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=40000000, backupCount=40)
logger.addHandler(handler)


app = Flask(__name__) # Aplicación Flask
app.config['SECRET_KEY'] = '67fcaee1a58b4bc7a0ff30c9d0036b5e'


def token_required(func): # Esta es un función decoradora llamada "token_requerid". Toma una función func como argumentos.
	# decorator factory which invoks update_wrapper() method and passes decorated function as an argument
	@wraps(func) # Este decarorador sirve para preservar los metadatos de la función original 
	def decorated(*args, **kwargs): # esta fución anidad toma cualquier número de argumentos y palabras clave (*args y **kwargs)
		token = request.args.get('token') # se intenta obtener el token JWT de los argumentos de la solicitud HTTP.
		if not token: # Si no encuentra el token en los argumentso de la solicitud, retorna una alerta.
			return jsonify({'Alert!':'Token is missing!'}), 401 #Se retorna el http 401 (No autorizando)
		try: 
			payload = jwt.decode(token, app.config['SECRET_KEY']) # intenta decodificar el token JWT utlizando una calve sercrea almacenada en la configuración de la aplicación
															   # Si tien exito, la carga útil (payload) del token se malcenará en la variable payload
			# You can use the JWT errs in exception
		# except jwt.InvalidTokenError:
		# 	return 'Invalid token. Please log in again.'
		except: # Si ocurre una exception durante la decodifación del token (por ejemplo, si el oten es invalido)
			return jsonify({'Alert':'Invalid Token'}), 403 # Devuelve una respuesta JSON que idica que el token es invalido con el codigo de estado 403 (Prohibido)
		return func(*args, **kwargs) # Si el token es valido, la función decorada original (func) se llama conlos mismo argumnetos y palabras clave que recibio
	return decorated # La función deracdora devuelve la función anidad "decorated", que se encargará de la autenticación antes de llamar a la función original

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
    	 return 'Logged in currently'
	
@app.route('/public')
def public():
	return 'For Public'

@app.route('/auth')
@token_required
def auth():
	return 'JWT is verified. Welcome to your dashboard'
	


# Login
@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] =='ijquenta' and request.form['password'] == '123456':
        session['logged_in'] = True

        token = jwt.encode({
            'user': request.form['username'],
            # don't foget to wrap it in str function, otherwise it won't work [ i struggled with this one! ]
            'expiration': str(datetime.utcnow() + timedelta(seconds=60))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})


@app.route('/logout', methods=['POST'])
def logout():
    pass

CORS(app)

@app.errorhandler(404)
def page_not_found(error):
    return messages._404, 404

@app.errorhandler(500)
def page_not_found(error):
    return messages._500, 500
    
api = Api(app)

app.secret_key = configuration.APP_SECRET_KEY

api.add_resource(resources.Index, routes.index)
api.add_resource(resources.Protected, routes.protected)


# API Usuarios
api.add_resource(Persona.ListarUsuarios, routes.listaUsuarios)

# Reporte Prueba
api.add_resource(Report.rptTotalesSigma, routes.rptTotalesSigma)

# Roles
api.add_resource(Usuario.ListarRoles, routes.listarRoles)
api.add_resource(Usuario.CrearRol, routes.crearRol)
api.add_resource(Usuario.ModificarRol, routes.modificarRol)
api.add_resource(Usuario.EliminarRol, routes.eliminarRol)

# Ejemplos de API
# Obtener los datos de un docente
#api.add_resource(BenSocial.ObtenerDatosDocente, routes.obtenerDatosDocente)
# Listar beneficios sociales por CodDocente
#api.add_resource(BenSocial.ListarBeneficiosDocente, routes.listarBeneficiosDocente)
#api.add_resource(BenSocial.ListarTipoMotivo, routes.listarTipoMotivo)
# Obtener los datos para modificar
#api.add_resource(BenSocial.ObtenerDatosModificar, routes.obtenerDatosModificar)
#Listar los ultimos tres meses remunerados de un docente
#api.add_resource(BenSocial.ListarTresUltimosMesesRemuneraadosDocente, routes.listarTresUltimosMesesRemuneraadosDocente)
#api.add_resource(BenSocial.RegTresUltMesRemDoc, routes.regTresUltMesRemDoc)
#api.add_resource(BenSocial.RegistrarBeneficioNuevo, routes.registrarBeneficioNuevo)
#api.add_resource(BenSocial.EliminarBeneficio, routes.eliminarBeneficio)


if __name__ == '__main__':
	Base.metadata.create_all(engine)
	HOST = configuration.SERVER_HOST
	PORT = configuration.SERVER_PORT
	DEBUG = configuration.DEBUG
	print (HOST,PORT, ':3')
	app.run(host=HOST,port=PORT,debug=True)