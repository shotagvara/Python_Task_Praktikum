from src.database.connection import get_connection
from psycopg.rows import dict_row

#   allows to get answer not as list of tuple: [(),(),()]
#   but as list of dict: [{},{},{}] 

class StudentsRoomsRepository:
    def __init__(self):
        self.connection=get_connection()


    def insert_rooms(self, rooms):
        cursor=self.connection.cursor()

        for room in rooms:
            room_id = room["id"] 
            room_name = room["name"]
            
            cursor.execute(
                """
                INSERT INTO rooms (id, name)
                VALUES (%s, %s)
                ON CONFLICT (id) DO NOTHING
                """,
                (room_id, room_name)
            )

        self.connection.commit()
        cursor.close()
        


    def insert_students(self, students):

        cursor = self.connection.cursor()

        for student in students:

            birthday = student["birthday"]
            student_id = student["id"]
            name = student["name"]
            room = student["room"]
            sex = student["sex"]

            cursor.execute(
                """
                INSERT INTO students (birthday, id, name, room, sex)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
                """,
                (birthday, student_id, name, room, sex)
            )

        self.connection.commit()
        cursor.close()


# Task #1: List of rooms and the number of students in each of them
# Returns list of dict: [{},{},{}], because we use row_factory=dict_row
# Otherwise would be list of tuples [(),(),()] becasue we use psycopg-3.3.5

    def get_rooms_with_student_count(self):

        cursor = self.connection.cursor(row_factory=dict_row)
        # we use row_factory=dict_row, that is why our output from cursor.fetchall()
        # will be [{},{},{}]

        cursor.execute(
            """
            SELECT
                r.id,
                r.name,
                COUNT(s.id) AS student_count
            FROM rooms r
            LEFT JOIN students s
                ON r.id = s.room
            GROUP BY r.id, r.name
            """
        )

        # Fetches the query result from PostgreSQL.
        # The calculations are performed in the database.
        result = cursor.fetchall() 

        cursor.close()

        return result


    #Task #2: 5 rooms with the smallest average age of students
    def get_5_rooms_with_smallest_average_age(self):
        cursor = self.connection.cursor(row_factory=dict_row)
        # we use row_factory=dict_row, that is why our output from cursor.fetchall()
        # will be [{},{},{}]

        cursor.execute(
            """
            SELECT
                r.id,
                r.name,
                ROUND(
                    AVG(
                        EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - s.birthday))
                        / 31557600.0
                    ),
                    2
                ) AS avg_age
            FROM rooms r
            JOIN students s
            ON r.id = s.room
            GROUP BY r.id, r.name
            ORDER BY avg_age
            LIMIT 5
            """
        )

        result = cursor.fetchall()

        cursor.close()

        return result

    #Task #3: 5 rooms with the largest difference in the age of students
    def get_5_rooms_with_largest_age_difference(self):
        cursor = self.connection.cursor(row_factory=dict_row)
            # we use row_factory=dict_row, that is why our output from cursor.fetchall()
            # will be [{},{},{}]



        cursor.execute(
            """SELECT
                r.id,
                r.name,
                ROUND(
                    EXTRACT(EPOCH FROM (MAX(s.birthday) - MIN(s.birthday)))
                    / 31557600.0,
                    2
                ) AS age_difference
            FROM rooms r
            JOIN students s
                ON r.id = s.room
            GROUP BY r.id, r.name
            ORDER BY age_difference DESC
            LIMIT 5;"""
        )

        result = cursor.fetchall()
        cursor.close()

        return result


    #Task 4: List of rooms where different-sex students live
    def rooms_with_different_sex_students(self):

        cursor = self.connection.cursor(row_factory=dict_row)
        # we use row_factory=dict_row, that is why our output from cursor.fetchall()
        # will be [{},{},{}]

        cursor.execute(
            """
            SELECT 
                r.id
            FROM rooms r 
            LEFT JOIN students s
            ON r.id=s.room
            Group by (r.id)
            HAVING 
            COUNT(CASE WHEN s.sex = 'M' THEN 1 END) > 0 
            AND 
            COUNT(CASE WHEN s.sex = 'F' THEN 1 END) > 0;
            """
        )

        result = cursor.fetchall()

        cursor.close()

        return result


    def create_indexes(self):
        
        cursor = self.connection.cursor()

        with open("sql/indexes.sql", "r", encoding="utf-8") as f:
            message = f.read()

        cursor.execute(message)
        self.connection.commit()

        cursor.close()

    def close_connection(self):
        self.connection.close()
