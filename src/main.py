#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

import constants as c
import ejercicio_1_utils as u


def main():
    df = pd.read_csv(c.PRICES_CATALOG_PATH, names=c.PRICES_COLUMN_HEADERS)
    u.get_number_of_records(df)
    u.get_list_of_categories(df)
    u.get_store_chains(df)
    u.get_most_frequently_monitored_products(df)
    u.get_store_chain_product_variety(df)
    u.get_interesting_fact(df)


if __name__ == "__main__":
    main()
