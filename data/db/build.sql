CREATE TABLE IF NOT EXISTS dukes (
    UserName STRING PRIMARY KEY,
    Score integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS earls (
    UserName STRING PRIMARY KEY,
    Score integer DEFAULT 0
);