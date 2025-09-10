
-- Extended Blog + User Dashboard Schema
-- MySQL 8.0+ (InnoDB, utf8mb4). Import this file in Workbench: File > Open SQL Script, then run.
-- If you want a schema name other than 'dashboard_blog', change it below.
DROP DATABASE IF EXISTS dashboard_blog;
CREATE DATABASE dashboard_blog CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE dashboard_blog;

-- ------------------------------------------------------
-- Helper: standard timestamps default
-- ------------------------------------------------------
-- MySQL doesn't have a global default, so we set per column as needed.

-- ------------------------------------------------------
-- USERS
-- ------------------------------------------------------
CREATE TABLE users (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  email         VARCHAR(255) NOT NULL UNIQUE,
  username      VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

-- Optional roles table (per-user global role); we kept per-blog roles separately in blog_administrators
CREATE TABLE roles (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  name        VARCHAR(64) NOT NULL UNIQUE,
  description VARCHAR(255),
  PRIMARY KEY (id)
) ENGINE=InnoDB;

ALTER TABLE users
  ADD COLUMN role_id BIGINT UNSIGNED NULL,
  ADD CONSTRAINT fk_users_roles
    FOREIGN KEY (role_id) REFERENCES roles(id)
    ON DELETE SET NULL ON UPDATE CASCADE;

-- ------------------------------------------------------
-- BLOGS
-- ------------------------------------------------------
CREATE TABLE blogs (
  id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  blog_name       VARCHAR(255) NOT NULL,
  blog_description VARCHAR(500),
  created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  owner_user_id   BIGINT UNSIGNED NULL,
  PRIMARY KEY (id),
  INDEX idx_blogs_owner (owner_user_id),
  CONSTRAINT fk_blogs_owner
    FOREIGN KEY (owner_user_id) REFERENCES users(id)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Per-blog administrators / roles (Admin, Editor, Author, etc.)
CREATE TABLE blog_administrators (
  blogs_id  BIGINT UNSIGNED NOT NULL,
  users_id  BIGINT UNSIGNED NOT NULL,
  role      VARCHAR(45) NOT NULL, -- e.g., 'owner','admin','editor','author'
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (blogs_id, users_id),
  INDEX idx_blog_admin_user (users_id),
  CONSTRAINT fk_blog_admin_blog FOREIGN KEY (blogs_id) REFERENCES blogs(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_blog_admin_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------
-- POSTS
-- ------------------------------------------------------
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
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------
-- COMMENTS
-- ------------------------------------------------------
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
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------
-- FILES (attachments to posts)
-- ------------------------------------------------------
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

-- ------------------------------------------------------
-- USER ACTIVITY (page analytics)
-- ------------------------------------------------------
CREATE TABLE user_activity (
  id             BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  users_id       BIGINT UNSIGNED NULL,
  page_visited   VARCHAR(255) NOT NULL,
  ip_address     VARCHAR(45) NULL,
  time_on_page   FLOAT NULL,
  visit_timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_activity_user (users_id),
  INDEX idx_activity_visit_ts (visit_timestamp),
  CONSTRAINT fk_activity_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------
-- NOTIFICATIONS
-- ------------------------------------------------------
CREATE TABLE notifications (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  users_id   BIGINT UNSIGNED NOT NULL,
  message    VARCHAR(500) NOT NULL,
  is_read    BOOLEAN NOT NULL DEFAULT FALSE,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_notifications_user (users_id),
  CONSTRAINT fk_notifications_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------
-- LIKES / REACTIONS (on posts or comments)
-- ------------------------------------------------------
CREATE TABLE likes (
  id           BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  users_id     BIGINT UNSIGNED NOT NULL,
  posts_id     BIGINT UNSIGNED NULL,
  comments_id  BIGINT UNSIGNED NULL,
  reaction_type ENUM('like','love','clap','laugh','sad','angry') NOT NULL DEFAULT 'like',
  created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_like_post_user (users_id, posts_id),
  UNIQUE KEY uq_like_comment_user (users_id, comments_id),
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

-- ------------------------------------------------------
-- CATEGORIES & TAGS
-- ------------------------------------------------------
CREATE TABLE categories (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  name        VARCHAR(100) NOT NULL UNIQUE,
  description VARCHAR(255),
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE post_categories (
  post_id     BIGINT UNSIGNED NOT NULL,
  category_id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (post_id, category_id),
  INDEX idx_pc_category (category_id),
  CONSTRAINT fk_pc_post FOREIGN KEY (post_id) REFERENCES posts(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_pc_category FOREIGN KEY (category_id) REFERENCES categories(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE tags (
  id   BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE post_tags (
  post_id BIGINT UNSIGNED NOT NULL,
  tag_id  BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (post_id, tag_id),
  INDEX idx_pt_tag (tag_id),
  CONSTRAINT fk_pt_post FOREIGN KEY (post_id) REFERENCES posts(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_pt_tag FOREIGN KEY (tag_id) REFERENCES tags(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------
-- USER PROFILES
-- ------------------------------------------------------
CREATE TABLE user_profiles (
  id           BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  users_id     BIGINT UNSIGNED NOT NULL,
  bio          TEXT NULL,
  profile_pic  VARCHAR(255) NULL,
  social_links JSON NULL,
  preferences  JSON NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_profile_user (users_id),
  CONSTRAINT fk_profiles_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------
-- DIRECT MESSAGES
-- ------------------------------------------------------
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

-- ------------------------------------------------------
-- AUDIT LOGS
-- ------------------------------------------------------
CREATE TABLE audit_logs (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  users_id    BIGINT UNSIGNED NULL,
  action      VARCHAR(100) NOT NULL, -- e.g., 'login','update_post','delete_comment'
  target_type ENUM('post','comment','blog','file','user','other') NOT NULL DEFAULT 'other',
  target_id   BIGINT UNSIGNED NULL,
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX idx_audit_user (users_id),
  INDEX idx_audit_target (target_type, target_id),
  CONSTRAINT fk_audit_user FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;
