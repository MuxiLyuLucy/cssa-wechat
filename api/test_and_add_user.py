import psycopg2
def test_add_user(input_wechat_id,req_tag):
    if req_tag == "req_find_q":
        q_in_sql = ""
        find_or_not = False
        # connect to the postgresql
        db_host_id = "127.0.0.1"
        db_name = "jhu_cssa"
        db_pass = "12345"
        db_owner = "postgres"
        db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
        cursor = db_connection.cursor()
        # get data
        select_data = (
            """
                SELECT wechat_id,q_process FROM "usres";
            """)
        # create the table
        cursor.execute(select_data)
        sql_wechat_id_list_ori = cursor.fetchall()
        sql_wechat_id_list = [i[0] for i in sql_wechat_id_list_ori]

        if input_wechat_id in sql_wechat_id_list:
            find_or_not = True
            q_in_sql = sql_wechat_id_list_ori[sql_wechat_id_list.index(input_wechat_id)][1]
        else: 
            find_or_not = False
        id_add = len(sql_wechat_id_list) + 1
        if find_or_not == False:
            insert_list_item = [(str(id_add),
                                str(id_add),
                                str(input_wechat_id),
                                '',
                                '0_0','','','','')]

            # insert into postgre
            try:
                args =  ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8')
                                for i in insert_list_item)
                cursor.execute("INSERT INTO usres VALUES " + (args))
                db_connection.commit()
                
            except Exception as ex:
                print("errors:%s"%ex)
                db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
                cursor = db_connection.cursor()
            q_in_sql = '0_0'


        return q_in_sql

    return None
    
