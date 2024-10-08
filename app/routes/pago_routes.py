from flask_restful import Api
import resources.Pago_resource as Pago_resource
from client.routes import Routes as routes

def pago_routes(api: Api):
    api.add_resource(Pago_resource.ListarPago, routes.listarPago)
    api.add_resource(Pago_resource.ListarPagoEstudiante, routes.listarPagoEstudiante)
    api.add_resource(Pago_resource.ListarPagoEstudianteMateria, routes.listarPagoEstudianteMateria)
    api.add_resource(Pago_resource.ListarPagoEstudiantesMateria, routes.listarPagoEstudiantesMateria)
    api.add_resource(Pago_resource.ListarPagoCurso, routes.listarPagoCurso)
    api.add_resource(Pago_resource.ManagePayment, routes.managePayment)
    api.add_resource(Pago_resource.ManageAssignPayment, routes.manageAssignPayment)
    api.add_resource(Pago_resource.TipoPago, routes.tipoPago)
    api.add_resource(Pago_resource.GetPayments, routes.getPayments)
    api.add_resource(Pago_resource.RptPagoEstudianteMateria, routes.rptPagoEstudianteMateria)
    api.add_resource(Pago_resource.GenerarComprobantePagoEstudiante, routes.generarComprobantePagoEstudiante)
    api.add_resource(Pago_resource.GenerarComprobantePagoMatricula, routes.generarComprobantePagoMatricula)
    api.add_resource(Pago_resource.GetPagoByIdResource, routes.getPagoById)                                                                     