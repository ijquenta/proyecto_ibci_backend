from core.database import select, execute
from web.wsrrhh_service import *
    
def obtenerDatosDocente(nroCi, nomCompleto):
    return getDatosDocente(nroCi, nomCompleto)

def listarBeneficiosDocente(codDoc):
    return select(f'''
    select b.cod_docente,b.ano,b.mes,b.nombre_completo,b.nro_ci,b.nro_dictamen,b.hoja_ruta, 
        b.fec_liquidacion, b.fec_ingrec,
        b.fec_conclusion,b.fec_retiro,b.observaciones, b.ts_ano,
        b.ts_mes, b.ts_dia, m.cod_tipo_motivo||'-'||m.des_tipo_motivo as motivo,
        b.fec_mod,b.usu_mod,
        sum(monto_tindemnizacion) as total_tindemnizacion
                        FROM  p_bsocial.t_beneficios b
                        JOIN p_bsocial.t_tipos_motivos m USING(cod_tipo_motivo)
                        WHERE b.cod_docente=\'{codDoc}\'
                        and b.estado_pla=1
                        GROUP BY b.cod_docente, b.nombre_completo,b.nro_ci, b.ano,b.mes,b.nro_dictamen, b.hoja_ruta,
                        b.fec_liquidacion, b.fec_ingrec,b.fec_conclusion, b.fec_retiro,b.observaciones, b.ts_ano,
                                b.ts_mes, b.ts_dia, motivo,b.fec_mod,b.usu_mod
    ''')
def listarBeneficiosDocenteGrilla2(data):
    return select(f''' 
                SELECT b.nro_liquidacion,
                (select distinct substr(cod_ape_pro,1,2)||'-'||(case when facultad is null then '' else facultad end)
                from p_bsocial.t_beneficios_designaciones_meses  where  cod_docente=b.cod_docente and nro_liquidacion= b.nro_liquidacion)  as apepro_fac,
                  b.cod_docente,b.nombre_completo,b.nro_ci,b.ano,b.mes,b.nro_dictamen, b.hoja_ruta, b.fec_liquidacion, b.fec_ingrec,
                  b.fec_conclusion,b.fec_retiro,b.observaciones, b.ts_ano,
                        b.ts_mes, b.ts_dia, m.cod_tipo_motivo||'-'||m.des_tipo_motivo as motivo,b.fec_mod,b.usu_mod,sum(b.monto_tindemnizacion) as total_tindemnizacion
                   FROM  p_bsocial.t_beneficios b
                   JOIN p_bsocial.t_tipos_motivos m USING(cod_tipo_motivo)
                   WHERE b.cod_docente=\'{data['cod_docente']}\'
                   and b.estado_pla=1
                   AND b.ano={data['ano']}
                   AND b.mes={data['mes']}
                   GROUP BY b.cod_docente, b.nombre_completo,b.nro_ci, b.ano,b.mes,b.nro_dictamen, b.hoja_ruta,
                   b.fec_liquidacion, b.fec_ingrec,b.fec_conclusion, b.fec_retiro,b.observaciones, b.ts_ano,
                          b.ts_mes, b.ts_dia, motivo,b.fec_mod,b.usu_mod,b.nro_liquidacion,apepro_fac
    ''')

def listarTipoMotivo():
    return select(f'''select cod_tipo_motivo, des_tipo_motivo  from bd_bsocialdocente.p_bsocial.t_tipos_motivos order by cod_tipo_motivo ''')

def listarTresUltimosMesesRemuneraadosDocente(cod_docente, ano, mes):
    return listarTresUltimosMeses(cod_docente, ano, mes)   

def registrarTresMesesDoc(data):
    return getTresUltimosMesesDoc(data['cod_docente'], data['ano'], data['mes'])


def obtenerDatosModificar(data):
    return select(f''' 
    SELECT b.cod_docente, b.nro_liquidacion, b.nro_dictamen, b.hoja_ruta, b.fec_liquidacion, b.fec_ingrec, b.fec_conclusion,b.fec_retiro,b.observaciones, b.ts_ano,
      b.ts_mes, b.ts_dia, SUM(i.sp_ano) as sp_ano, SUM(i.sp_mes) as sp_mes, SUM(i.sp_dia) as sp_dia, m.cod_tipo_motivo||'-'||m.des_tipo_motivo as motivo
    FROM p_bsocial.t_beneficios_designaciones i JOIN p_bsocial.t_beneficios b USING(ano, mes, cod_docente)
    JOIN p_bsocial.t_tipos_motivos m USING(cod_tipo_motivo)
    WHERE b.cod_docente= \'{data['cod_docente']}\' AND b.ano={data['ano']} AND b.mes={data['mes']}
    GROUP BY b.cod_docente, b.nro_liquidacion, b.nro_dictamen, b.hoja_ruta, b.fec_liquidacion, b.fec_ingrec,b.fec_conclusion, b.fec_retiro,b.observaciones, b.ts_ano,
      b.ts_mes, b.ts_dia, motivo
    ''')

def registrarBeneficioNuevo(data):
    return select(f'''
    select * from p_bsocial.bs08_aplicar_beneficios_docente_form2({data['ano']}, {data['mes']},\'{data['codDocente']}\', {data['codTipoMotivo']}, \'{data['nroDictamen']}\', \'{data['hojaRuta']}\', \'{data['fecLiquidacion']}\', \'{data['fecIngrec']}\', \'{data['fecConclusion']}\', \'{data['fecRetiro']}\', {data['tsAno']}, {data['tsMes']}, {data['tsDia']}, \'{data['observaciones']}\', \'{data['usuarioReg']}\')
    ''')

def eliminarBeneficio(data):
    return select(f'''
    select * from p_bsocial.bs06_eliminar_liquidacion_docente({data['ano']}, {data['mes']}, \'{data['codDocente']} \', \'{data['observacion']} \' , \'{data['usuarioReg']} \' )
    ''')