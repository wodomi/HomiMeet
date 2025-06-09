CREATE DATABASE homimeet_db;
USE homimeet_db;

-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    bio TEXT,
    avatar_url TEXT
);

-- Meetups Table
CREATE TABLE meetups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    location TEXT NOT NULL,
    datetime DATETIME NOT NULL,
    created_by INT,
    status ENUM('scheduled', 'canceled', 'done') DEFAULT 'scheduled',
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- Meetup Participants Table
CREATE TABLE meetup_participants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    meetup_id INT,
    transport_mode VARCHAR(50) NOT NULL,
    join_time DATETIME NOT NULL,
    arrival_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (meetup_id) REFERENCES meetups(id)
);

-- Scores Table
CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    meetup_id INT,
    punctuality ENUM('early', 'on_time', 'late', 'missed') NOT NULL,
    score_change INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (meetup_id) REFERENCES meetups(id)
);