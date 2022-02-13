import user.connectDB as connDB

connect = connDB.connect()  # conn database
database = connect[0]  # database
cursor = connect[1]  # cursor


class Note:

    def __init__(self, user_id, title, description):
        self.user_id = user_id
        self.title = title
        self.description = description

    def store(self):
        sql = "INSERT INTO notes VALUES(NULL, %s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.description)

        cursor.execute(sql, note)
        database.commit()

        return [cursor.rowcount, self]

    def readByUserId(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"

        cursor.execute(sql);
        result = cursor.fetchall();

        return result

    def remove(self):
        sql = f"DELETE  FROM notes WHERE user_id = {self.user_id} AND title LIKE '%{self.title}%'"

        cursor.execute(sql);
        database.commit();

        return [cursor.rowcount, self]


