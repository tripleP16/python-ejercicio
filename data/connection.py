from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class Connection: 

    SQLITE                  = 'sqlite'
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
    }

    # Main DB Connection Ref Obj
    db_engine = None
    def __init__(self):
        dbtype = "sqlite"
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB="products")

            self.db_engine = create_engine(engine_url)
            print(self.db_engine)

        else:
            print("DBType is not found in DB_ENGINE")
        
    def create_db_tables(self):
        metadata = MetaData()
        products = Table("products", metadata,
                      Column('id', Integer, primary_key=True),
                      Column('productId', Integer),
                      Column('name', String),
                       Column('stars', Integer)
                      )

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)
    
    def execute_query(self, query=''):
        if query == '' : return

        print (query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print("\n")
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row) # print(row[0], row[1], row[2])
                result.close()

        print("\n")

    def insert(self, name, stars, id):
        # Insert Data
        query = "INSERT INTO {}(name, stars, productId) " \
                "VALUES ('{}', {}, {});".format('products', name, stars, id)
        self.execute_query(query)