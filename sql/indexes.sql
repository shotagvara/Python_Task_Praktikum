-- General index for queries that join rooms with students.
-- Общий индекс для запросов, которые соединяют комнаты со студентами.
-- students.room is frequently used in JOIN conditions with rooms.id.
-- students.room часто используется в JOIN с rooms.id.
CREATE INDEX IF NOT EXISTS idx_students_room
ON students(room);


-- Composite index proposed for age-related queries.
-- Составной индекс, предложенный для запросов, связанных с возрастом.
-- room is used for joining/grouping, while birthday is used
-- for average-age and age-difference calculations.
-- room используется для JOIN/GROUP BY, а birthday —
-- для расчёта среднего возраста и разницы возрастов.

CREATE INDEX IF NOT EXISTS idx_students_room_birthday
ON students(room, birthday);


-- The (room, sex) ordering can help PostgreSQL with grouping
-- and filtering students by sex.
-- Порядок (room, sex) может помочь PostgreSQL при группировке
-- и проверке наличия студентов разных полов.
CREATE INDEX IF NOT EXISTS idx_students_room_sex
ON students(room, sex);