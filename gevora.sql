-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 08, 2022 at 05:02 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gevora`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `id_cli` bigint(12) NOT NULL,
  `nom1_cli` varchar(25) NOT NULL,
  `nom2_cli` varchar(25) NOT NULL,
  `ape1_cli` varchar(25) NOT NULL,
  `ape2_cli` varchar(25) NOT NULL,
  `f_nac_cli` date NOT NULL,
  `email_cli` varchar(60) NOT NULL,
  `movil_cli` bigint(12) NOT NULL,
  `estado_cli` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`id_cli`, `nom1_cli`, `nom2_cli`, `ape1_cli`, `ape2_cli`, `f_nac_cli`, `email_cli`, `movil_cli`, `estado_cli`) VALUES
(45464544, 'Jose', 'Juan', 'Perez', 'Perez', '1986-03-05', 'josej@gmail.com', 3012322123, 'Activo'),
(65146546, 'Juan', 'Jose', 'Perez', 'Perez', '1975-05-10', 'jj@gmail.com', 3015121211, 'Activo');

-- --------------------------------------------------------

--
-- Table structure for table `habitaciones`
--

CREATE TABLE `habitaciones` (
  `codhab` int(4) NOT NULL,
  `descriphab` varchar(100) NOT NULL,
  `preciohab` bigint(100) NOT NULL,
  `estadohab` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `habitaciones`
--

INSERT INTO `habitaciones` (`codhab`, `descriphab`, `preciohab`, `estadohab`) VALUES
(0, 'deluxe', 770000, 'Disponible'),
(2, 'sencilla', 70000, 'No Disponible'),
(408, 'Suite', 230000, 'Disponible'),
(1001, 'General', 120000, 'Disponible'),
(1002, 'General', 120000, 'No Dispnible');

-- --------------------------------------------------------

--
-- Table structure for table `reservas`
--

CREATE TABLE `reservas` (
  `num_reserva` int(12) NOT NULL,
  `f_ingreso_reserva` datetime NOT NULL,
  `f_salida_reserva` datetime NOT NULL,
  `id_cli` bigint(12) NOT NULL,
  `cod_hab` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reservas`
--

INSERT INTO `reservas` (`num_reserva`, `f_ingreso_reserva`, `f_salida_reserva`, `id_cli`, `cod_hab`) VALUES
(250106001, '2022-09-15 13:00:00', '2022-09-16 13:00:00', 9168172222, 2),
(250106002, '2022-09-15 00:34:06', '2022-09-15 00:34:06', 916817222, 3);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `tipo_doc_usu` varchar(20) NOT NULL COMMENT 'tipo de documento del usuario',
  `id_usu` bigint(12) NOT NULL COMMENT 'num ident usuario',
  `nom_ape_usu` varchar(60) NOT NULL COMMENT 'nombres y apellidos del usuario',
  `dir_usu` varchar(60) NOT NULL,
  `movil_usu` int(15) NOT NULL,
  `user_usu` varchar(15) NOT NULL COMMENT 'nombre de usuario -Max 15 caracteres,\r\n',
  `pasw_usu` varchar(8) NOT NULL COMMENT 'contraseña - maximo 8 caracteres',
  `tipo_usu` varchar(20) NOT NULL,
  `estado_usu` tinyint(1) NOT NULL COMMENT '0-Inactivo               \r\n\r\n\r\n1- Activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`tipo_doc_usu`, `id_usu`, `nom_ape_usu`, `dir_usu`, `movil_usu`, `user_usu`, `pasw_usu`, `tipo_usu`, `estado_usu`) VALUES
('Cédula de ciudadania', 555555, 'diana', 'cali', 333300022, 'dianatest', 'dianates', '', 0),
('Cédula de ciudadania', 123456789, 'fanery ospina', 'cali', 2147483647, 'faneryo', '123456', '', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cli`),
  ADD KEY `id_cli` (`id_cli`);

--
-- Indexes for table `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`codhab`),
  ADD KEY `cod_hab` (`codhab`);

--
-- Indexes for table `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`num_reserva`),
  ADD KEY `id_cli` (`id_cli`),
  ADD KEY `cod_hab` (`cod_hab`),
  ADD KEY `num_reserva` (`num_reserva`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usu`),
  ADD KEY `tipo_usu` (`tipo_usu`),
  ADD KEY `id_usu` (`id_usu`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `reservas`
--
ALTER TABLE `reservas`
  MODIFY `num_reserva` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=250106003;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
