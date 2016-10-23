-- MySQL dump 10.15  Distrib 10.0.22-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: openpet
-- ------------------------------------------------------
-- Server version	10.0.22-MariaDB

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
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `latitude` decimal(7,4) DEFAULT NULL,
  `longitude` decimal(7,4) DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `province_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_17E64ABAE946114A` (`province_id`),
  CONSTRAINT `FK_17E64ABAE946114A` FOREIGN KEY (`province_id`) REFERENCES `provinces` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'Perrera Municipal de Bens','http://www.coruna.es/adopcion','+34981263093',43.3638,-8.4433,NULL,1);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `origins`
--

DROP TABLE IF EXISTS `origins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `origins` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `origins`
--

LOCK TABLES `origins` WRITE;
/*!40000 ALTER TABLE `origins` DISABLE KEYS */;
INSERT INTO `origins` VALUES (1,'coruna.es','http://www.coruna.es/adopcion',NULL);
/*!40000 ALTER TABLE `origins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provinces`
--

DROP TABLE IF EXISTS `provinces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provinces` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provinces`
--

LOCK TABLES `provinces` WRITE;
/*!40000 ALTER TABLE `provinces` DISABLE KEYS */;
INSERT INTO `provinces` VALUES (1,'A Coruña',NULL);
/*!40000 ALTER TABLE `provinces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `races`
--

DROP TABLE IF EXISTS `races`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `races` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `specie_id` int(11) DEFAULT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_5DBD1EC9D5436AB7` (`specie_id`),
  CONSTRAINT `FK_5DBD1EC9D5436AB7` FOREIGN KEY (`specie_id`) REFERENCES `species` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `races`
--

LOCK TABLES `races` WRITE;
/*!40000 ALTER TABLE `races` DISABLE KEYS */;
INSERT INTO `races` VALUES (1,1,'American Staffordshire terrier',NULL),(2,1,'Can de palleiro',NULL),(3,1,'Pastor alemán',NULL),(4,1,'Pastor belga',NULL),(5,1,'Perro genérico',NULL),(6,2,'Persa',NULL),(7,2,'Siamés',NULL),(8,2,'Gato genérico',NULL);
/*!40000 ALTER TABLE `races` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `species`
--

DROP TABLE IF EXISTS `species`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `species` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `species`
--

LOCK TABLES `species` WRITE;
/*!40000 ALTER TABLE `species` DISABLE KEYS */;
INSERT INTO `species` VALUES (1,'Perro',NULL),(2,'Gato',NULL);
/*!40000 ALTER TABLE `species` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specimens`
--

DROP TABLE IF EXISTS `specimens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `specimens` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `origin_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `race_id` int(11) DEFAULT NULL,
  `origin_identification` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` longtext COLLATE utf8_unicode_ci,
  `summary` longtext COLLATE utf8_unicode_ci,
  `sex` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `entrydate` date DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_F599311E56A273CC` (`origin_id`),
  KEY `IDX_F599311E64D218E` (`location_id`),
  KEY `IDX_F599311E6E59D40D` (`race_id`),
  CONSTRAINT `FK_F599311E56A273CC` FOREIGN KEY (`origin_id`) REFERENCES `origins` (`id`),
  CONSTRAINT `FK_F599311E64D218E` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`),
  CONSTRAINT `FK_F599311E6E59D40D` FOREIGN KEY (`race_id`) REFERENCES `races` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specimens`
--

LOCK TABLES `specimens` WRITE;
/*!40000 ALTER TABLE `specimens` DISABLE KEYS */;
INSERT INTO `specimens` VALUES (25,1,1,5,'1421115268371','Wendy','http://www.coruna.es//IMG/P_Contenido_1442845170005_860_1000_U_e1e6af8c47705f93ec03b1d3aa576c.jpg','Wendy fue recogida por uno de nuestros laceros en la zapateira. Es una perra muy asustadiza pero su comportamiento es bueno. La persona que la adopte necesitará darle un tiempo para ganarse su confianza.','Hembra, color marrón y blanca, tamaño mediano.','f','2013-12-28','2014-12-28',NULL),(26,1,1,NULL,'1453604015123','LUA','http://www.coruna.es//IMG/P_Contenido_1442848262344_860_1000_U_de3625f9c4194e53c3750a5ba7df1ef.jpg','Lua fue entregada por su propietario por motivos personales. Desde su llegada ha mostrado buen carácter y es muy tranquila.\n','Hembra, negra y marrón, tamaño grande.\n','f','2011-11-15','2016-09-29',NULL),(27,1,1,5,'1414118881130','Pou','http://www.coruna.es//IMG/P_Contenido_1442845169941_860_1000_U_50756788b49e5ccc875f6baa5c66c78f.jpg','Pou fue abandonado delante de la puerta de nuestras instalaciones. Es un perro muy jugueton, con mucha energia, cariñoso y muy bueno.','Macho, color blanco y marrón, tamaño mediano.','m','2013-10-01','2014-10-12',NULL),(28,1,1,5,'1453604015847','Pancho','http://www.coruna.es//IMG/P_Contenido_1442848262761_860_1000_U_a223817c68ca252d7e17adf4bb37c68a.jpg','Pancho es un precioso cachorrito al que le estamos buscando un nuevo hogar. Nadie lo ha reclamado desde que está con nosotros y es un perro inquieto y muy juguetón.\n','Macho, negro y blanco, cachorro.\n','m','2016-06-30','2016-09-30',NULL),(29,1,1,5,'1453604020009','Dana','http://www.coruna.es//IMG/P_Contenido_1442848262890_860_1000_U_49cc55bb1bb3d78224a8897cf1c5f90.jpg','Dana fue entregada por su propietario por motivos personales. Está acostumbrada a vivir en un piso y es muy tranquila y cariñosa cuando tiene confianza.\n','Hembra, marrón y blanca, tamaño mediano.\n','f','2015-03-26','2016-09-26',NULL),(30,1,1,5,'1453596712957','Pequi','http://www.coruna.es//IMG/P_Contenido_1442846926090_860_1000_U_a5bd35197992e650e25c571196ffb7c8.jpg','Pequi fue recogida por uno de nuestros laceros estando preñada y ya ha dado luz a varios cachorritos. Ahora le estamos buscando un nuevo hogar donde pueda comenzar una nueva etapa de su vida donde le brinden todo el cariño que se merece.\n','Hembra, color negra y marrón, tamaño pequeño.\n','f','2015-01-03','2016-05-03',NULL),(31,1,1,5,'1453585425212','Rubia','http://www.coruna.es//IMG/P_Contenido_1442845219812_860_1000_U_2bd95efddbd4cf8acd9858eddfec6b8.jpg','Rubia fue entregada por su propietario por motivos personales. Muestra buen comportamiento, es un poco asustadiza y se lleva bien con otros animales.\n','Hembra, color canela, tamaño mediano.\n','f','2013-03-18','2016-03-18',NULL),(32,1,1,5,'1453589882090','Naira','http://www.coruna.es//IMG/P_Contenido_1442845686940_860_1000_U_824ce393b131facc7fc525345cc144e.jpg','Naira es una cachorrita inquieta y muy juguetona. Para su adopción es necesario disponer de licencia de animales potencialmente peligrosos.\n','Hembra, color marrón y blanca, tamaño grande.\n','f','2016-01-22','2016-03-22',NULL),(33,1,1,5,'1453587995880','Cloe','http://www.coruna.es//IMG/P_Contenido_1442845428830_860_1000_U_b73a70fcda7939196c4c4f69a169839.jpg','Cloe es una perra muy cariñosa, activa y que muestra buen comportamiento con otros perros.\n','Mestiza, color negra y marrón, tamaño grande.\n','f','2014-03-23','2016-03-23',NULL),(34,1,1,5,'1453600859448','Tibi','http://www.coruna.es//IMG/P_Contenido_1442847630033_860_1000_U_14b16d6f888710801dca8939d64c96.jpg','Tibi es un perro con mucha fuerza y energía que necesita de una nueva familia que le pueda dedicar tiempo para compartir grandes caminatas y que le den mucho cariño.\n','Macho, tricolor, tamaño grande.\n','m','2013-08-25','2016-08-25',NULL),(35,1,1,5,'1453594992544','Gala','http://www.coruna.es//IMG/P_Contenido_1442846735518_860_1000_U_a9e81b95d3707ace384a0c3e995bb18.jpg','Gala es muy tranquila y se lleva bien con otros animales. Esperamos que pronto tengamos un nuevo hogar para ella.\n','Hembra, color negra, marrón y blanca, tamaño grande.\n','f','2016-04-15','2016-05-30',NULL),(36,1,1,8,'1453596927552','Gatitos','http://www.coruna.es//IMG/P_Contenido_1442846973210_860_1000_U_db85d6eee3f733f69df7cf57a213ac1.jpg','Gatitos de aproximadamente 30 dias, varios colores. Machos y hembras.\n','Gatitos de aproximadamente 1 mes\n','f','2016-06-01','2016-07-11',NULL),(37,1,1,8,'1453583972135','Nancy','http://www.coruna.es//IMG/P_Contenido_1442845051079_860_1000_U_65e936c898ca843219eca5bd66fea9c.jpg','Nancy es una gatita muy tranquila a la que esperamos encontrarle pronto una familia\n','Gata común, atigrada con reflejos dorados.\n','f','2014-08-31','2015-08-31',NULL),(38,1,1,5,'1453598590549','Dani','http://www.coruna.es//IMG/P_Contenido_1442847320925_860_1000_U_554797304353ad24b9703b99ceae28f8.jpg','Dani fue encontrado en la zona del parque de Vioño y nadie lo ha reclamado hasta la fecha. Es un perro que muestra buen comportamiento y se lleva bien con otros perros. Es un tanto desconfiado por lo que necesita de tiempo para ganarse su cariño.\n','Macho, color marrón, tamaño pequeño.\n','m','2013-07-29','2016-07-29',NULL),(39,1,1,5,'1453586769687','Neo','http://www.coruna.es//IMG/P_Contenido_1442845332541_860_1000_U_4df6b246492152bdd0d4825e927f65dc.jpg','Neo fue recogido por uno de nuestros laceros cuando corria desorientado. Es un perro muy bueno y un poco asustadizo hasta que tiene la suficiente confianza.\n','Mestizo, color marrón, tamaño mediano.\n','m','2014-10-01','2016-04-01',NULL),(40,1,1,8,'1438219205364','Tiniebla','http://www.coruna.es//IMG/P_Contenido_1442841616562_860_1000_U_7884a816718596d326d3c8ac3e32d80.jpg','Tiniebla fue encontrada por nuestros laceros hace ya varios meses y de momento nadie se ha interesado por ella. Esperamos que pronto tenga una nueva familia.','Gata común negra.','f','2008-01-05','2015-01-05',NULL),(41,1,1,5,'1453602517484','Tula','http://www.coruna.es//IMG/P_Contenido_1442848025963_860_1000_U_c1c428f8f8c4e4a885c9cfe2244d90.jpg','Tula es una perrita que fue entregada por su propietario por motivos personales. Su comportamiento es bueno y sólo necesita cariño y tiempo para adaptarse a un nuevo hogar.\n','Hembra, marrón y blanca, tamaño mediano.\n','f','2011-05-01','2016-09-21',NULL),(42,1,1,NULL,'1437700564812','Tigresa','http://www.coruna.es//IMG/P_Contenido_1442845170203_860_1000_U_d1fcd1f2b8643c46861f751c917ea59.jpg','Tigresa fue recogida por uno de nuestros laceros y lleva con nosotros un par de meses. De momento nadie se ha interesado por ella. Es necesaria licencia de animales potencialmente peligrosos para su adopción.','Hembra, atigrada y blanca, tamaño grande.','f','2014-05-03','2015-05-03',NULL),(43,1,1,5,'1453604462232','Meireles','http://www.coruna.es//IMG/P_Contenido_1442848332046_860_1000_U_ec792ffbda2769897446e28d994ab7.jpg','Meireles es un precioso cachorro al que le estamos buscando un nuevo hogar. Es juguetón e inquieto y le encantan los mimos.\n','Macho, color marrón y blanco, tamaño mediano.\n','m','2016-07-13','2016-09-13',NULL),(44,1,1,5,'1445476364319','Nock','http://www.coruna.es//IMG/P_Contenido_1442847988580_860_1000_U_5a768bcbf884066d1a0679710e683d6.jpg','Nock es un perro tranquilo, obediente y que se lleva bien con otros perros. De momento no hemos conseguido encontrarle un nuevo hogar pero esperamos conseguirle pronto una nueva familia.','Macho, color negro, tamaño mediano.','m','2013-08-01','2015-08-01',NULL),(45,1,1,5,'1453596787335','Nelson','http://www.coruna.es//IMG/P_Contenido_1442846937450_860_1000_U_4f9a5c7a98918831e8b0eae06c9628.jpg','Nelson es un perro muy tranquilo que muestra buen comportamiento con otros perros. Es un compañero ideal para aquellas personas que puedan brindarle un nuevo hogar.\n','Macho, color negro y marrón, tamaño mediano.\n','m','2012-06-20','2016-06-20',NULL),(46,1,1,5,'1453602518123','Yumi','http://www.coruna.es//IMG/P_Contenido_1442848026097_860_1000_U_d1218e10a6e34dd6544245cc5613089.jpg','Yumi fue entregada por su propietario por motivos personales. Al principio es un poco desconfiada pero pronto se encariña con uno cuando le das un poco de mimos.\n','Hembra, marrón, tamaño mediano.\n','f','2015-03-17','2016-09-17',NULL),(47,1,1,5,'1453597678571','Rex','http://www.coruna.es//IMG/P_Contenido_1442847087231_860_1000_U_3afd138fc1b854cf4fff34e423867c.jpg','Rex es un perro que cuando lo recogimos no tenía movilidad en las patas traseras debido probablemente a un posible atropello. Después de ser tratado en nuestras instalaciones está ya disponible para salir en adopción y totalmente recuperado aunque tiene una muy leve cojera.\n','Mestizo, color blanco negro y marrón.\n','m','2016-01-24','2016-06-24',NULL),(48,1,1,1,'1453604457933','Kita','http://www.coruna.es//IMG/P_Contenido_1442848331426_860_1000_U_2fcfadb768825890b2b3b89cd6fb0.jpg','Kita es una joven perrita a la que le estamos buscando una nueva familia. Para este tipo de razas es necesario licencia de animales potencialmente peligrosos. Su comportamiento es muy bueno y es muy tranquila.\n','Hembra, marrón y blanca, tamaño mediano.\n','f','2016-01-09','2016-08-09',NULL);
/*!40000 ALTER TABLE `specimens` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-23 12:34:38
