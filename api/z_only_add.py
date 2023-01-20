import psycopg2
def add():

    # connect to the postgresql
    db_host_id = "127.0.0.1"
    db_name = "jhu_cssa"
    db_pass = "12345"
    db_owner = "postgres"
    db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
    cursor = db_connection.cursor()

    insert_list_item = [('99',
                        '99',
                        'wx123',
                        'aa测试',
                        '1_3')]

    # insert into postgre
    try:
        args =  ','.join(cursor.mogrify("(%s,%s,%s,%s,%s)", i).decode('utf-8')
                        for i in insert_list_item)
        cursor.execute("INSERT INTO usres VALUES " + (args))
        db_connection.commit()
        
    except Exception as ex:
        print("errors:%s"%ex)
        db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
        cursor = db_connection.cursor()

    return None

add()