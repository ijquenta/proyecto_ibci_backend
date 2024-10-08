from . import configuration
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_migrate import Migrate
from core import configuration
from psycopg2 import sql
import psycopg2
from datetime import datetime
from re import sub
import pandas as pd
import json
from http import HTTPStatus
from client.responses import clientResponses as messages
from sqlalchemy.exc import SQLAlchemyError  # Importa las excepciones de SQLAlchemy

engine = create_engine(configuration.SQLALCHEMY_DATABASE_URL, pool_size=40,
                       max_overflow=8,
                       pool_recycle=600,
                       pool_pre_ping=True,
                       pool_use_lifo=True)
Base = declarative_base()
Session = sessionmaker(engine)
session_db = Session()
db = SQLAlchemy()


def as_string(composable, encoding="utf-8"):
    if isinstance(composable, sql.Composed):
        return ''.join([as_string(x, encoding) for x in composable])
    elif isinstance(composable, sql.SQL):
        return composable.string
    else:
        rv = sql.ext.adapt(composable._wrapped)
        if isinstance(rv, psycopg2.extensions.QuotedString):
            rv.encoding = encoding
        rv = rv.getquoted()
        return rv.decode(encoding) if isinstance(rv, bytes) else rv


def camel_case(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


def rename_cols(cols):
    new_cols = []
    for col in cols:
        new_cols.append(camel_case(col))
    return new_cols


def select(query):
    try:
        df = pd.read_sql_query(query, engine)
        df.columns = rename_cols(df.columns)
        jsonData = df.to_json(orient='records', date_format='iso')
        return json.loads(jsonData)
        # return json.loads(jsonData), HTTPStatus.OK
    except SQLAlchemyError as err:
        # Maneja errores específicos de SQLAlchemy
        session_db.rollback()
        print(err)
        return {"code": 0, "message": f"Error: {err}"}, HTTPStatus.NOT_FOUND

def execute(query):
    try:
        session_db.execute(text(query))
        session_db.commit()
        return {"code": 1, "message": "Operación exitosa"}, HTTPStatus.OK
    except SQLAlchemyError as err:
        session_db.rollback()
        print(err)
        return {"code": 0, "message": f"Error en la base de datos: {err}"}, HTTPStatus.INTERNAL_SERVER_ERROR
    
def execute_response(query):
    try:
        result = session_db.execute(text(query))
        session_db.commit()
        row = result.fetchone()
        print("execute_response: ", row)
        return {"valor": row[0]}, HTTPStatus.OK
    except SQLAlchemyError as err:
        # Maneja errores específicos de SQLAlchemy
        session_db.rollback()
        print(err)
        return {"code": 0, "message": f"Error: {err}"}, HTTPStatus.NOT_FOUND

def execute_function(query):
    try:
        result = session_db.execute(query)
        session_db.commit()
        row = result.fetchone()
        if row is not None:
            return {"valor": row["valor"]}, HTTPStatus.OK
        else:
            return {"code": 0, "message": "La función no devolvió ningún resultado."}, HTTPStatus.NOT_FOUND

    except Exception as err:
        session_db.rollback()
        print(err)
        return {"code": 0, "message": f"Error: {err}"}, HTTPStatus.NOT_FOUND
    
def execute_function_multiple(query):
    try:
        if not session_db.transaction:
            with session_db.begin() as connection:
                result = connection.execute(query)
                row = result.fetchone()
                if row is not None:
                    return {"valor": row["valor"]}, HTTPStatus.OK
                else:
                    return {"code": 0, "message": "La función no devolvió ningún resultado."}, HTTPStatus.NOT_FOUND
        else:
            result = session_db.execute(query)
            row = result.fetchone()
            if row is not None:
                return {"valor": row["valor"]}, HTTPStatus.OK
            else:
                return {"code": 0, "message": "La función no devolvió ningún resultado."}, HTTPStatus.NOT_FOUND

    except Exception as err:
        print(err)
        return {"code": 0, "message": f"Error: {err}"}, HTTPStatus.INTERNAL_SERVER_ERROR
