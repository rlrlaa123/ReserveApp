-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: reservation
-- ------------------------------------------------------
-- Server version	5.7.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add auth group',7,'add_authgroup'),(20,'Can change auth group',7,'change_authgroup'),(21,'Can delete auth group',7,'delete_authgroup'),(22,'Can add auth group permissions',8,'add_authgrouppermissions'),(23,'Can change auth group permissions',8,'change_authgrouppermissions'),(24,'Can delete auth group permissions',8,'delete_authgrouppermissions'),(25,'Can add auth permission',9,'add_authpermission'),(26,'Can change auth permission',9,'change_authpermission'),(27,'Can delete auth permission',9,'delete_authpermission'),(28,'Can add auth user',10,'add_authuser'),(29,'Can change auth user',10,'change_authuser'),(30,'Can delete auth user',10,'delete_authuser'),(31,'Can add auth user groups',11,'add_authusergroups'),(32,'Can change auth user groups',11,'change_authusergroups'),(33,'Can delete auth user groups',11,'delete_authusergroups'),(34,'Can add auth user user permissions',12,'add_authuseruserpermissions'),(35,'Can change auth user user permissions',12,'change_authuseruserpermissions'),(36,'Can delete auth user user permissions',12,'delete_authuseruserpermissions'),(37,'Can add django admin log',13,'add_djangoadminlog'),(38,'Can change django admin log',13,'change_djangoadminlog'),(39,'Can delete django admin log',13,'delete_djangoadminlog'),(40,'Can add django content type',14,'add_djangocontenttype'),(41,'Can change django content type',14,'change_djangocontenttype'),(42,'Can delete django content type',14,'delete_djangocontenttype'),(43,'Can add django migrations',15,'add_djangomigrations'),(44,'Can change django migrations',15,'change_djangomigrations'),(45,'Can delete django migrations',15,'delete_djangomigrations'),(46,'Can add django session',16,'add_djangosession'),(47,'Can change django session',16,'change_djangosession'),(48,'Can delete django session',16,'delete_djangosession'),(49,'Can add inquire',17,'add_inquire'),(50,'Can change inquire',17,'change_inquire'),(51,'Can delete inquire',17,'delete_inquire'),(52,'Can add notice',18,'add_notice'),(53,'Can change notice',18,'change_notice'),(54,'Can delete notice',18,'delete_notice'),(55,'Can add reservation',19,'add_reservation'),(56,'Can change reservation',19,'change_reservation'),(57,'Can delete reservation',19,'delete_reservation'),(58,'Can add user',20,'add_user'),(59,'Can change user',20,'change_user'),(60,'Can delete user',20,'delete_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$X98TrrN8nvEl$tpoKp+o4u7FwOAkko74ap/54gkVjvB3SZ8swEaDfrJ4=','2017-10-08 06:39:56.883945',1,'admin','','','',1,1,'2017-10-07 11:31:33.286586');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-10-07 11:35:50.917852','testid','User object',1,'[{\"added\": {}}]',20,1),(2,'2017-10-08 04:52:17.683930','1','Notice object',1,'[{\"added\": {}}]',18,1),(3,'2017-10-08 04:52:47.401944','1','Notice object',1,'[{\"added\": {}}]',18,1),(4,'2017-10-08 04:58:17.209324','2','Notice object',1,'[{\"added\": {}}]',18,1),(5,'2017-10-08 07:05:08.821078','2','Reservation object',3,'',19,1),(6,'2017-10-08 07:05:08.830047','1','Reservation object',3,'',19,1),(7,'2017-10-08 07:24:39.213966','4','Reservation object',2,'[{\"changed\": {\"fields\": [\"date\", \"state\"]}}]',19,1),(8,'2017-10-08 08:43:03.083772','5','Reservation object',2,'[{\"changed\": {\"fields\": [\"day\"]}}]',19,1),(9,'2017-10-08 08:43:24.092440','4','Reservation object',2,'[{\"changed\": {\"fields\": [\"classroom\", \"day\", \"purpose\"]}}]',19,1),(10,'2017-10-08 08:43:33.798419','5','Reservation object',2,'[{\"changed\": {\"fields\": [\"classroom\", \"purpose\"]}}]',19,1),(11,'2017-10-08 08:43:44.731171','5','Reservation object',2,'[{\"changed\": {\"fields\": [\"period\"]}}]',19,1),(12,'2017-10-08 08:43:55.937891','4','Reservation object',2,'[{\"changed\": {\"fields\": [\"period\"]}}]',19,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'reservation','authgroup'),(8,'reservation','authgrouppermissions'),(9,'reservation','authpermission'),(10,'reservation','authuser'),(11,'reservation','authusergroups'),(12,'reservation','authuseruserpermissions'),(13,'reservation','djangoadminlog'),(14,'reservation','djangocontenttype'),(15,'reservation','djangomigrations'),(16,'reservation','djangosession'),(17,'reservation','inquire'),(18,'reservation','notice'),(19,'reservation','reservation'),(20,'reservation','user'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-10-07 11:30:56.167760'),(2,'auth','0001_initial','2017-10-07 11:30:57.107951'),(3,'admin','0001_initial','2017-10-07 11:30:57.272338'),(4,'admin','0002_logentry_remove_auto_add','2017-10-07 11:30:57.312244'),(5,'contenttypes','0002_remove_content_type_name','2017-10-07 11:30:57.459894'),(6,'auth','0002_alter_permission_name_max_length','2017-10-07 11:30:57.520207'),(7,'auth','0003_alter_user_email_max_length','2017-10-07 11:30:57.624591'),(8,'auth','0004_alter_user_username_opts','2017-10-07 11:30:57.653266'),(9,'auth','0005_alter_user_last_login_null','2017-10-07 11:30:57.718319'),(10,'auth','0006_require_contenttypes_0002','2017-10-07 11:30:57.729283'),(11,'auth','0007_alter_validators_add_error_messages','2017-10-07 11:30:57.761635'),(12,'auth','0008_alter_user_username_max_length','2017-10-07 11:30:57.848395'),(13,'sessions','0001_initial','2017-10-07 11:30:57.908197'),(14,'reservation','0001_initial','2017-10-07 11:34:59.884279');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5ist3iosbrdr5g9avl5qtzp9f6g0yd96','ZGNhZjY1MTcxYjAxMTQwMDI4ODEzOTExOTVhMWUyZWVhZmMxNjRkNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjMzNjE3NDMxYzYxNTkwYWYwMTk2MDM3MzRiMTJmZWRkMGIxZjk0ZTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-10-22 06:39:56.909514');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `inquire`
--

LOCK TABLES `inquire` WRITE;
/*!40000 ALTER TABLE `inquire` DISABLE KEYS */;
/*!40000 ALTER TABLE `inquire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `notice`
--

LOCK TABLES `notice` WRITE;
/*!40000 ALTER TABLE `notice` DISABLE KEYS */;
INSERT INTO `notice` VALUES (1,'2017-10-08 04:52:36','admin','hello world2','hello hello hello <3'),(2,'2017-10-08 04:58:08','admin','hello world','hello hello hello <3');
/*!40000 ALTER TABLE `notice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (4,'test','철수','2017-10-08','1교시','301',3,'월요일','안녕'),(5,'test','철수','2017-10-08','1교시','305',2,'월요일','안녕');
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('test','12312','test','010','test','test','123'),('test1','12312','test','010','test','test','1234'),('testid','123123','donghyun','01071144543','hello@gmail.com','information','123123123');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-08 19:25:34
