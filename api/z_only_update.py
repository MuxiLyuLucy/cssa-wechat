import psycopg2

# connect to the postgresql
db_host_id = "127.0.0.1"
db_name = "jhu_cssa"
db_pass = "12345"
db_owner = "postgres"
db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
cursor = db_connection.cursor()
# get data
select_data = (
            """ UPDATE usres
            SET q_process = %s
            WHERE wechat_id = %s""" )
# create the table
cursor.execute(select_data,(str("1_1"), str("wxid_aaaaaaa")))
db_connection.commit()