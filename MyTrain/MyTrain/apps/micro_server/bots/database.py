import simplePostgrConnector as Connector
import MyTrain.local_settings as ls

DB = Connector.PostgrDB(
    database_name=ls.NAME,
    user=ls.USER,
    user_password=ls.PASSWORD,
    host=ls.HOST,
    port=ls.PORT
)
