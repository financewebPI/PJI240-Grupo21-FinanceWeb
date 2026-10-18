import os
import psycopg2


def conectar():

    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "financeweb"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv(
            "DB_PASSWORD",
            "FinanceWeb2026"
        ),
        port=os.getenv("DB_PORT", "5432")
    )

    return conexao