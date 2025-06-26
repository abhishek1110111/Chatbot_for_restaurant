-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: indian_eatery
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `order_id` int(11) NOT NULL,
  `street_address` varchar(255) NOT NULL,
  `city` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) NOT NULL,
  PRIMARY KEY (`order_id`),
  CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (67,'172 newport road','','CF24 1DL');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_items`
--

DROP TABLE IF EXISTS `food_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `food_items` (
  `item_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_items`
--

LOCK TABLES `food_items` WRITE;
/*!40000 ALTER TABLE `food_items` DISABLE KEYS */;
INSERT INTO `food_items` VALUES (1,'Pav Bhaji',6.00),(2,'Chole Bhature',7.00),(3,'Pizza',8.00),(4,'Mango Lassi',5.00),(5,'Masala Dosa',6.00),(6,'Biryani',9.00),(7,'Vada Pav',4.00),(8,'Rava Dosa',7.00),(9,'Samosa',5.00);
/*!40000 ALTER TABLE `food_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_tracking`
--

DROP TABLE IF EXISTS `order_tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_tracking` (
  `order_id` int(11) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_tracking`
--

LOCK TABLES `order_tracking` WRITE;
/*!40000 ALTER TABLE `order_tracking` DISABLE KEYS */;
INSERT INTO `order_tracking` VALUES (40,'delivered'),(41,'in transit'),(46,'Order Placed'),(47,'Order Placed'),(48,'Order Placed'),(49,'Order Placed'),(50,'Order Placed'),(51,'Order Placed'),(52,'Order Placed'),(53,'Order Placed'),(54,'Order Placed'),(55,'Order Placed'),(56,'Order Placed'),(57,'Order Placed'),(58,'Order Placed'),(59,'Order Placed'),(60,'Order Placed'),(61,'Order Placed'),(62,'Order Placed'),(67,'Preparing');
/*!40000 ALTER TABLE `order_tracking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`order_id`,`item_id`),
  KEY `orders_ibfk_1` (`item_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `food_items` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (40,1,2,12.00),(40,3,1,8.00),(41,4,3,15.00),(41,6,2,18.00),(41,9,4,20.00),(42,4,2,10.00),(42,5,1,6.00),(43,4,2,10.00),(43,5,1,6.00),(44,4,2,10.00),(44,5,1,6.00),(45,4,2,10.00),(45,5,1,6.00),(46,4,2,10.00),(46,5,1,6.00),(47,4,2,10.00),(47,5,1,6.00),(48,4,2,10.00),(48,5,1,6.00),(49,4,2,10.00),(49,5,1,6.00),(50,4,2,10.00),(50,5,1,6.00),(51,4,2,10.00),(51,5,1,6.00),(52,4,2,10.00),(52,5,1,6.00),(53,4,2,10.00),(53,5,1,6.00),(54,4,2,10.00),(54,5,1,6.00),(55,4,2,10.00),(55,5,1,6.00),(56,4,2,10.00),(56,5,1,6.00),(57,4,2,10.00),(57,5,1,6.00),(58,2,1,7.00),(58,3,1,8.00),(59,1,1,6.00),(59,2,1,7.00),(59,9,3,15.00),(60,3,1,8.00),(61,2,1,7.00),(61,4,1,5.00),(61,5,1,6.00),(61,9,2,10.00),(62,3,1,8.00),(62,4,1,5.00),(62,9,2,10.00),(63,2,1,7.00),(63,4,1,5.00),(63,5,2,12.00),(64,2,1,7.00),(64,4,1,5.00),(64,5,2,12.00),(65,2,1,7.00),(65,4,1,5.00),(65,5,2,12.00),(66,2,1,7.00),(66,4,1,5.00),(66,5,2,12.00),(67,2,1,7.00),(67,4,1,5.00),(67,5,2,12.00);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-26 14:37:51
