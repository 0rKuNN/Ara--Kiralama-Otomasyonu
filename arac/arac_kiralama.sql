-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 20 Ara 2023, 19:58:28
-- Sunucu sürümü: 8.0.31
-- PHP Sürümü: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `arac_kiralama`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `araclar`
--

DROP TABLE IF EXISTS `araclar`;
CREATE TABLE IF NOT EXISTS `araclar` (
  `arac_id` int NOT NULL AUTO_INCREMENT,
  `marka` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `plaka` varchar(255) DEFAULT NULL,
  `durum` varchar(255) DEFAULT NULL,
  `fiyat` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`arac_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Tablo döküm verisi `araclar`
--

INSERT INTO `araclar` (`arac_id`, `marka`, `model`, `plaka`, `durum`, `fiyat`) VALUES
(3, 'Renault', 'Clio', '34ABC123', 'Kiralandı', '750.00'),
(4, 'Ford', 'Focus', '35XYZ456', 'Kiralandı', '750.00'),
(5, 'Toyota', 'Corolla', '06DEF789', 'Müsait', '850.00'),
(6, 'Hyundai', 'i20', '07GHI123', 'Müsait', '800.00'),
(7, 'Volkswagen', 'Golf', '34JKL567', 'Müsait', '1300.00'),
(8, 'Honda', 'Civic', '06MNO890', 'Müsait', '1000.00'),
(9, 'Mercedes', 'A-Class', '06PQR123', 'Müsait', '4500.00'),
(10, 'Fiat', 'Egea', '35STU456', 'Müsait', '750.00'),
(11, 'Chevrolet', 'Spark', '07VWX789', 'Müsait', '750.00'),
(12, 'Nissan', 'Micra', '34YZA123', 'Kiralandı', '700.00'),
(13, 'Peugeot', '208', '35BCD456', 'Müsait', '700.00'),
(14, 'Opel', 'Corsa', '06EFG789', 'Kiralandı', '750.00'),
(15, 'BMW', '3 Series', '34HIJ123', 'Müsait', '3500.00'),
(16, 'Audi', 'A3', '35KLM456', 'Müsait', '4000.00'),
(17, 'Kia', 'Rio', '07NOP789', 'Müsait', '750.00');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kiralama_gecmisi`
--

DROP TABLE IF EXISTS `kiralama_gecmisi`;
CREATE TABLE IF NOT EXISTS `kiralama_gecmisi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `arac_id` int NOT NULL,
  `kullanici_id` int NOT NULL,
  `kira_tarihi` date NOT NULL,
  `iade_tarihi` date NOT NULL,
  `kullanici_ad` varchar(255) NOT NULL,
  `fiyat` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `arac_id` (`arac_id`),
  KEY `kullanici_id` (`kullanici_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Tablo döküm verisi `kiralama_gecmisi`
--

INSERT INTO `kiralama_gecmisi` (`id`, `arac_id`, `kullanici_id`, `kira_tarihi`, `iade_tarihi`, `kullanici_ad`, `fiyat`) VALUES
(1, 4, 3, '2023-12-18', '2023-12-18', '', NULL),
(2, 10, 4, '2023-12-19', '2023-12-19', '', NULL),
(3, 10, 3, '2023-12-19', '2023-12-20', '', NULL),
(4, 13, 3, '2023-12-19', '2023-12-19', 'Orkun', NULL),
(5, 6, 3, '2023-12-19', '2023-12-19', 'Orkun', NULL),
(6, 10, 3, '2023-12-19', '2023-12-20', '', '750.00'),
(7, 4, 3, '2023-12-19', '2023-12-23', '', '750.00'),
(8, 3, 3, '2023-12-19', '2023-12-21', '', '750.00'),
(9, 10, 3, '2023-12-19', '2023-12-20', '', '750.00'),
(10, 15, 3, '2023-12-20', '2023-12-20', '', '3500.00'),
(11, 10, 3, '2023-12-20', '2023-12-20', '', '750.00');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanici_giris`
--

DROP TABLE IF EXISTS `kullanici_giris`;
CREATE TABLE IF NOT EXISTS `kullanici_giris` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kullanici_ad` varchar(50) NOT NULL,
  `kullanici_sifre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Tablo döküm verisi `kullanici_giris`
--

INSERT INTO `kullanici_giris` (`id`, `kullanici_ad`, `kullanici_sifre`) VALUES
(1, 'kullanici_adi', 'sifre'),
(2, '', ''),
(3, 'Orkun', '1234');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
