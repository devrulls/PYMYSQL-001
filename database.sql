CREATE DATABASE IF NO EXISTS master_python;
USE master_python;

CREATE TABLE user(
    id INT(25) AUTO_INCREMENT NOT NULL,
    name VARCHAR(100),
    last_name VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    CONSTRAINT pk_user PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notes(
    id INT(25) AUTO_INCREMENT NOT NULL,
    user_id INT(25) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description MEDIUMTEXT,
    date_note DATE NOT NULL,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_note_user FOREIGN KEY(user_id) REFERENCES user(id)
)ENGINE=InnoDb;