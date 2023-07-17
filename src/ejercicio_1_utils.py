#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pandasql import sqldf

import constants as c


def get_number_of_records(df):
    """Determines count of records from the incoming dataset for question 1.1:

    ¿Cuántos registros hay?

    Args:
        df: Pandas dataframe
    """
    print("\n-------------------BULLET 1.1-------------------")
    row_count = df.shape[0]
    print(f"There are {row_count} records in the file")


def get_list_of_categories(df):
    """Retrieves list of categories for question 1.2:

    ¿Cuántas categorías?

    Args:
        df: Pandas dataframe
    """

    print("\n-------------------BULLET 1.2-------------------")
    list_of_categories = df["categoria"].sort_values(ascending=True).unique()
    category_count = list_of_categories.size
    print(f"Category count: {category_count}")
    print(f"List of categories: {list_of_categories}")


def get_store_chains(df):
    """Retrieves store chain information for question 1.3:

    ¿Cuántas cadenas comerciales están siendo monitoreadas (y, por lo tanto, reportadas
    en esa base de datos)?

    Args:
        df: Pandas dataframe
    """

    print("\n-------------------BULLET 1.3-------------------")
    store_chain_count = df["cadenacomercial"].sort_values(ascending=True).unique().size
    print(f"There are : {store_chain_count} store chains being reported and monitored")


def get_most_frequently_monitored_products(df):
    """Calculates most frequent monitored products for question 1.4:

    ¿Cuáles son los productos más monitoreados en cada estado de la república?

    Args:
        df: Pandas dataframe
    """

    print("\n-------------------BULLET 1.4-------------------")
    df_products = df.groupby(["estado", "producto"])
    most_frequent_product_per_state = (
        df_products.producto.count()
        .sort_values(ascending=False)
        .groupby(level=0)
        .head(1)
        .sort_values()
        .to_frame()
    )
    print(
        f"Most frequently monitored products per state: {most_frequent_product_per_state}"
    )


def get_store_chain_product_variety(df):
    """Retrieves store chain product variety for question 1.5:

    ¿Cuál es la cadena comercial con mayor variedad de productos monitoreados?

    Args:
        df: Pandas dataframe
    """

    print("\n-------------------BULLET 1.5-------------------")
    df_store_chains = (
        df.groupby("cadenacomercial")
        .agg({"producto": pd.Series.nunique})
        .sort_values(by="producto", ascending=False)
        .head(1)
    )
    print(
        f"Store chain with the most variety of monitored products: {df_store_chains['producto'].index[0]} - Unique monitored products: {df_store_chains['producto'][0]}"
    )


def get_interesting_fact(df):
    """Determines fun facts for question 1.6:

    Encuentra algún dato curioso en los datos y comunícalo en un slide de powerpoint (see attached pptx file).

    Args:
        df: Pandas dataframe
    """
    print("\n-------------------BULLET 1.6-------------------")
    print(f"Interesting facts:")
    print("Top 10 of most monitored medicine products across the country:")
    df_sql = sqldf(c.NATIONAL_MEDICINE_COUNT_SQL)
    df_sql.index += 1
    print(df_sql)
    print("Most monitored medicine products per state:")
    df_sql_2 = sqldf(c.STATE_MEDICINE_COUNT_SQL)
    df_sql_2.reset_index(drop=True, inplace=True)
    print(df_sql_2)
