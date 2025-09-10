
-- Simplified Blog Dashboard Schema (with admins, likes, messages)
-- MySQL 8.0+ (InnoDB, utf8mb4)

DROP DATABASE IF EXISTS simple_blog_dashboard;
CREATE DATABASE simple_blog_dashboard CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE simple_blog_dashboard;

-- USERS
CREATE TABLE users (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  email         VARCHAR(255) NOT NULL UNIQUE,
  username      VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

-- BLOGS
CREATE TABLE blogs (
  id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  blog_name       VARCHAR(255) NOT NULL,
  blog_description VARCHAR(500),
  created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  owner_user_id   BIGINT UNSIGNED NULL,
  PRIMARY KEY (id),
  INDEX idx_blogs_owner (owner_user_id),
  CONSTRAINT fk_blogs_owner FOREIGN KEY (owner_user_id) REFERENCES users(id)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- BLOG ADMINISTRATORS
CREATE TABLE blog_administrators (
  blogs_id   BIGINT UNSIGNED NOT NULL,
  users_id   BIGINT UNSIGNED NOT NULL,
  role       VARCHAR(45) NOT NULL, -- e.g., 'owner','admin','editor','author'
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (blogs_id, users_id),
  INDEX idx_blog_admin_user (users_id),
  CONSTRAINT fk_blog_admin_blog FOREIGN KEY (blogs_id) REFERENCES blogs(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_blog_admin_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- POSTS
CREATE TABLE posts (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  blogs_id   BIGINT UNSIGNED NOT NULL,
  author_id  BIGINT UNSIGNED NOT NULL,
  title      VARCHAR(255) NOT NULL,
  content    LONGTEXT NOT NULL,
  status     ENUM('draft','published','archived') NOT NULL DEFAULT 'draft',
  published_at DATETIME NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_posts_blog (blogs_id),
  INDEX idx_posts_author (author_id),
  FULLTEXT INDEX ft_posts_content (title, content),
  CONSTRAINT fk_posts_blog FOREIGN KEY (blogs_id) REFERENCES blogs(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_posts_author FOREIGN KEY (author_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- COMMENTS
CREATE TABLE comments (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  posts_id   BIGINT UNSIGNED NOT NULL,
  users_id   BIGINT UNSIGNED NOT NULL,
  content    TEXT NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_comments_post (posts_id),
  INDEX idx_comments_user (users_id),
  CONSTRAINT fk_comments_post FOREIGN KEY (posts_id) REFERENCES posts(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_comments_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- FILES (attachments to posts)
CREATE TABLE files (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  posts_id   BIGINT UNSIGNED NOT NULL,
  file_name  VARCHAR(255) NOT NULL,
  file_path  VARCHAR(255) NOT NULL,
  mime_type  VARCHAR(100) NOT NULL,
  file_size  INT UNSIGNED NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_files_post (posts_id),
  CONSTRAINT fk_files_post FOREIGN KEY (posts_id) REFERENCES posts(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- LIKES (on posts or comments)
CREATE TABLE likes (
  id           BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  users_id     BIGINT UNSIGNED NOT NULL,
  posts_id     BIGINT UNSIGNED NULL,
  comments_id  BIGINT UNSIGNED NULL,
  reaction_type ENUM('like','love','clap','laugh','sad','angry') NOT NULL DEFAULT 'like',
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_likes_user (users_id),
  INDEX idx_likes_post (posts_id),
  INDEX idx_likes_comment (comments_id),
  CONSTRAINT fk_likes_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_likes_post FOREIGN KEY (posts_id) REFERENCES posts(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_likes_comment FOREIGN KEY (comments_id) REFERENCES comments(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT chk_like_target CHECK (
    (posts_id IS NOT NULL AND comments_id IS NULL) OR
    (posts_id IS NULL AND comments_id IS NOT NULL)
  )
) ENGINE=InnoDB;

-- MESSAGES (direct user-to-user)
CREATE TABLE messages (
  id           BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  sender_id    BIGINT UNSIGNED NOT NULL,
  receiver_id  BIGINT UNSIGNED NOT NULL,
  content      TEXT NOT NULL,
  is_read      BOOLEAN NOT NULL DEFAULT FALSE,
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_messages_sender (sender_id),
  INDEX idx_messages_receiver (receiver_id),
  CONSTRAINT fk_messages_sender FOREIGN KEY (sender_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_messages_receiver FOREIGN KEY (receiver_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;
