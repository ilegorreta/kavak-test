PRICES_CATALOG_PATH = "/app/data/precios_profeco_2022.csv"

PRICES_COLUMN_HEADERS = [
    "producto",
    "presentacion",
    "marca",
    "categoria",
    "catalogo",
    "precio",
    "fecharegistro",
    "cadenacomercial",
    "giro",
    "nombrecomercial",
    "direccion",
    "estado",
    "municipio",
    "latitud",
    "longitud",
]

NATIONAL_MEDICINE_COUNT_SQL = """
                SELECT distinct producto, count(producto) as cuenta_de_productos
                FROM df
                where catalogo = 'MEDICAMENTOS'
                group by producto
                order by count(producto) DESC
                limit 10
            """
STATE_MEDICINE_COUNT_SQL = """
                with
                    medicine_per_state_cte as (
                        select
                            estado,
                            producto,
                            count(producto) as cuenta_producto,
                            row_number() over (partition by estado order by count(producto) desc) as rn
                        from df
                        where catalogo = 'MEDICAMENTOS'
                        group by estado, producto
                    )
                    select
                        estado,
                        producto,
                        cuenta_producto
                    from medicine_per_state_cte where rn = 1
            """
