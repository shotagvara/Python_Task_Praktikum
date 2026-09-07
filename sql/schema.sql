CREATE TABLE rooms (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    birthday TIMESTAMP NOT NULL,
    room INTEGER NOT NULL,
    sex CHAR(1),
    FOREIGN KEY (room) REFERENCES rooms(id)
);