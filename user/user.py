import datetime
import hashlib  # encrypt password
import user.connectDB as connDB

connect = connDB.connect()  # conn database
database = connect[0]       # database
cursor = connect[1]         # cursor


class User:

    def __init__(self, name, last_name, email, password):
        self.name = name;
        self.last_name = last_name;
        self.email = email;
        self.password = password;

    def register(self):
        date = datetime.datetime.now();
        # Encrypt - password

        encrypt_passwd = hashlib.sha256();
        encrypt_passwd.update(self.password.encode('utf8'));
        sql = "INSERT INTO user VALUES(NULL,%s,%s,%s,%s,%s)"
        user = (self.name, self.last_name, self.email, encrypt_passwd.hexdigest(), date)
        try:
            cursor.execute(sql, user)
            database.commit();
            result = [cursor.rowcount, self];
        except:
            result = [0, self];  # register[0] = 0  condition dans main.py -> else "error"
        return result;

    def login(self):
        # Query
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        # Encrypt - password
        encrypt_passwd = hashlib.sha256();
        encrypt_passwd.update(self.password.encode('utf8'));
        # Information by query (email, password)
        user = (self.email, encrypt_passwd.hexdigest())

        cursor.execute(sql, user);
        database.commit();
        result = cursor.fetchone()  # only one user

        return result


