import psycopg2
def create_table_user():
    db_host_id = "127.0.0.1"
    db_name = "jhu_cssa"
    db_pass = "12345"
    db_owner = "postgres"
    # connect to the postgresql
    db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
    cursor = db_connection.cursor()
    # create table
    try:
        create_table = (
            """
        CREATE TABLE "usres" (
                        "db_id"   VARCHAR(255),
                        "usr_id" VARCHAR(255),
                        "wechat_id" VARCHAR(255),
                        "wechat_name" VARCHAR(255),
                        "q_process" VARCHAR(255), 
                        "a_year" VARCHAR(255),
                        "a_baldc" VARCHAR(255),
                        "a_colg" VARCHAR(255),
                        "a_major" VARCHAR(255),
                        "a_bsphd" VARCHAR(255),
                        "b_group1" VARCHAR(255),
                        "b_group2" VARCHAR(255),
                        "ungra_or_gra" VARCHAR(255),
                        "ver_id" VARCHAR(255),
                        "ver_mail" VARCHAR(255),
                        "ver_torf" VARCHAR(255),
                        "tmp_store" VARCHAR(255),
                        PRIMARY KEY ("usr_id") 
                    )
            """)
        cursor.execute(create_table)
        db_connection.commit()
    except Exception as ex:
        print("errors:%s"%ex)
        db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
        cursor = db_connection.cursor()
        
create_table_user()
