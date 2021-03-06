DROP TABLE IF EXISTS `Company`;
DROP TABLE IF EXISTS `Plane`;
DROP TABLE IF EXISTS `Flight`;
DROP TABLE IF EXISTS `Controller`;
DROP TABLE IF EXISTS `Gate`;
DROP TABLE IF EXISTS `Terminal`;
DROP TABLE IF EXISTS `Engineer`;
DROP TABLE IF EXISTS `Services`;
DROP TABLE IF EXISTS `ParkingSpot`;
DROP TABLE IF EXISTS `Airstrip`;
DROP TABLE IF EXISTS `Freighter`;
DROP TABLE IF EXISTS `Loads`;

CREATE TABLE `Company` (
	`Name` varchar(255) NOT NULL,
	`Phone` varchar(255) NOT NULL,
	PRIMARY KEY (`Name`)
);

CREATE TABLE `Plane` (
	`ID` varchar(255) NOT NULL,
	`Owner` varchar(255) NOT NULL,
	`Maker` varchar(255) NOT NULL,
	`Model` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Flight` (
	`FlightID` varchar(255) NOT NULL,
	`PlaneID` varchar(255) NOT NULL,
	`Departure` varchar(255) NOT NULL,
	`Destination` varchar(255) NOT NULL,
	`DepartTime` DATETIME NOT NULL,
	`ArrivalTime` DATETIME NOT NULL,
	`RealDepartTime` DATETIME,
	`Controller` varchar(255) NOT NULL,
	`Status` varchar(255) NOT NULL,
	`GateID` varchar(255) NOT NULL,
	`AirstripID` varchar(255) NOT NULL,
	`ParkingSpotID` varchar(255),
	`ParkingStart` DATETIME,
	`ParkingEnd` DATETIME,
	PRIMARY KEY (`FlightID`)
);

CREATE TABLE `Controller` (
	`ID` varchar(255) NOT NULL,
	`Name` varchar(255) NOT NULL,
	`Surname` varchar(255) NOT NULL,
	`Phone` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Gate` (
	`GateID` varchar(255) NOT NULL,
	`TerminalID` varchar(255) NOT NULL,
	PRIMARY KEY (`GateID`)
);

CREATE TABLE `Terminal` (
	`ID` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Engineer` (
	`EngineerID` varchar(255) NOT NULL,
	`Name` varchar(255) NOT NULL,
	`Surname` varchar(255) NOT NULL,
	`Phone` varchar(255) NOT NULL,
	PRIMARY KEY (`EngineerID`)
);

CREATE TABLE `Services` (
	`FlightID` varchar(255) NOT NULL,
	`EngineerID` varchar(255) NOT NULL,
	PRIMARY KEY (`FlightID`,`EngineerID`)
);

CREATE TABLE `ParkingSpot` (
	`ID` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Airstrip` (
	`AirstripID` varchar(255) NOT NULL,
	PRIMARY KEY (`AirstripID`)
);

CREATE TABLE `Freighter` (
	`FreighterID` varchar(255) NOT NULL,
	`Name` varchar(255) NOT NULL,
	`Surname` varchar(255) NOT NULL,
	`Phone` varchar(255) NOT NULL,
	PRIMARY KEY (`FreighterID`)
);

CREATE TABLE `Loads` (
	`FlightID` varchar(255) NOT NULL,
	`FreighterID` varchar(255) NOT NULL,
	PRIMARY KEY (`FlightID`,`FreighterID`)
);

ALTER TABLE `Plane` ADD CONSTRAINT `Plane_fk0` FOREIGN KEY (`Owner`) REFERENCES `Company`(`Name`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Flight` ADD CONSTRAINT `Flight_fk0` FOREIGN KEY (`PlaneID`) REFERENCES `Plane`(`ID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Flight` ADD CONSTRAINT `Flight_fk1` FOREIGN KEY (`Controller`) REFERENCES `Controller`(`ID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Flight` ADD CONSTRAINT `Flight_fk2` FOREIGN KEY (`GateID`) REFERENCES `Gate`(`GateID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Flight` ADD CONSTRAINT `Flight_fk3` FOREIGN KEY (`AirstripID`) REFERENCES `Airstrip`(`AirstripID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Flight` ADD CONSTRAINT `Flight_fk4` FOREIGN KEY (`ParkingSpotID`) REFERENCES `ParkingSpot`(`ID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Gate` ADD CONSTRAINT `Gate_fk0` FOREIGN KEY (`TerminalID`) REFERENCES `Terminal`(`ID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Services` ADD CONSTRAINT `Services_fk0` FOREIGN KEY (`FlightID`) REFERENCES `Flight`(`FlightID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Services` ADD CONSTRAINT `Services_fk1` FOREIGN KEY (`EngineerID`) REFERENCES `Engineer`(`EngineerID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Loads` ADD CONSTRAINT `Loads_fk0` FOREIGN KEY (`FlightID`) REFERENCES `Flight`(`FlightID`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `Loads` ADD CONSTRAINT `Loads_fk1` FOREIGN KEY (`FreighterID`) REFERENCES `Freighter`(`FreighterID`) ON UPDATE CASCADE ON DELETE CASCADE;