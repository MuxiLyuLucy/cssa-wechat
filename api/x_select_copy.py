#-*- coding: utf-8 -*-

import psycopg2
import pandas as pd

def select():

    # connect to the postgresql
    db_host_id = "127.0.0.1"
    db_name = "jhu_cssa"
    db_pass = "12345"
    db_owner = "postgres"
    conn = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
    # Creating a cursor object using the cursor() 
    # method
    cursor = conn.cursor()
    
    # drop table accounts
    sql = """SELECT * FROM usres"""
    
    # Executing the query
    cursor.execute(sql)
    print("Table select !")
    result_1 = cursor.fetchall()
    # set dataframe
    df_1 = pd.DataFrame(result_1)
    print(df_1)
    df_1.to_csv("data/data_2.csv")
    # Closing the connection
    conn.close()



select()
