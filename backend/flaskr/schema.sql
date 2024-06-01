DROP TABLE IF EXISTS guests;
DROP TABLE IF EXISTS admins;

CREATE TABLE guests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    familyGroup INTEGER NOT NULL,
    friday INTEGER,
    accommodation TEXT,
    attendance INTEGER,
    email TEXT,
    plusone INTEGER,
    plusoneName TEXT
);

CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);