import psycopg2
def delete():

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
    sql = '''DROP TABLE usres '''
    
    # Executing the query
    cursor.execute(sql)
    print("Table dropped !")
    
    # Commit your changes in the database
    conn.commit()
    
    # Closing the connection
    conn.close()

delete()
