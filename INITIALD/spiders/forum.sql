DROP TABLE IF EXISTS `forum_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_info` (
  `forum_id` int not null primary key auto_increment,
  `url` varchar(200) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `img` varchar(200) DEFAULT NULL,
  `keyword` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE forum_info ADD UNIQUE(url);
