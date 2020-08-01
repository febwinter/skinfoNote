SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema car_test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema car_test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `car_test` DEFAULT CHARACTER SET utf8 ;
USE `car_test` ;

-- -----------------------------------------------------
-- Table `car_test`.`seller`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Seller` (
  `seller_id` INT NOT NULL auto_increment,
  `name` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`seller_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_test`.`car_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`car_list` (
  `serial_no` INT NOT NULL auto_increment,
  `seller_id` INT NOT NULL,
  `car_model` VARCHAR(45) NULL,
  `used` TINYINT NULL,
  `price` INT NULL,
  PRIMARY KEY (`serial_no`),
  INDEX `fk_sell_list_seller_idx` (`seller_id` ASC) ,
  CONSTRAINT `fk_sell_list_seller`
    FOREIGN KEY (`seller_id`)
    REFERENCES `car_test`.`Seller` (`seller_id`)
    ON DELETE cascade
    ON UPDATE cascade)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_test`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Customer` (
  `customer_id` INT NOT NULL auto_increment,
  `name` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `e_mail` VARCHAR(45) NULL,
  PRIMARY KEY (`customer_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_test`.`mechanic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Mechanic` (
  `mechanic_id` INT NOT NULL auto_increment,
  `name` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `major` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`mechanic_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_test`.`Invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Invoice` (
  `car_serial_no` INT NOT NULL,
  `customer_id` INT NULL,
  `purchase_date` DATE NULL,
  PRIMARY KEY (`car_serial_no`),
  INDEX `fk_Invoice_customer1_idx` (`customer_id` ASC) ,
  INDEX `fk_Invoice_sell_list1_idx` (`car_serial_no` ASC) ,
  CONSTRAINT `fk_Invoice_customer1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `car_test`.`Customer` (`customer_id`)
    ON DELETE cascade
    ON UPDATE cascade,
  CONSTRAINT `fk_Invoice_sell_list1`
    FOREIGN KEY (`car_serial_no`)
    REFERENCES `car_test`.`car_list` (`serial_no`)
    ON DELETE cascade
    ON UPDATE cascade)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_test`.`service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Service` (
  `service_no` INT NOT NULL auto_increment,
  `car_serial_no` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `service_date` DATE NULL,
  PRIMARY KEY (`service_no`, `car_serial_no`),
  INDEX `fk_repair_service_customer1_idx` (`customer_id` ASC) ,
  INDEX `fk_service_Invoice1_idx` (`car_serial_no` ASC) ,
  CONSTRAINT `fk_repair_service_customer1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `car_test`.`Customer` (`customer_id`)
    ON DELETE cascade
    ON UPDATE cascade,
  CONSTRAINT `fk_service_Invoice1`
    FOREIGN KEY (`car_serial_no`)
    REFERENCES `car_test`.`Invoice` (`car_serial_no`)
    ON DELETE cascade
    ON UPDATE cascade)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_test`.`Parts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Parts` (
  `parts_no` INT NOT NULL auto_increment, 
  `price` VARCHAR(45) NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`parts_no`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_test`.`Parts_requirment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Parts_requirement` (
  `require_no` INT NOT NULL auto_increment,
  `service_no` INT NOT NULL ,
  `car_serial_no` INT NOT NULL,
  `parts_no` INT NOT NULL,
  INDEX `fk_Parts_requirment_Parts1_idx` (`Parts_no` ASC) ,
  primary key (`require_no`),
  CONSTRAINT `fk_Parts_requirment_Parts1`
    FOREIGN KEY (`parts_no`)
    REFERENCES `car_test`.`Parts` (`parts_no`)
    ON DELETE cascade
    ON UPDATE cascade,
  CONSTRAINT `fk_Parts_requirment_service1`
    FOREIGN KEY (`service_no` , `car_serial_no`)
    REFERENCES `car_test`.`Service` (`service_no` , `car_serial_no`)
    ON DELETE cascade
    ON UPDATE cascade)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `car_test`.`mechanic_allocation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_test`.`Mechanic_Allocation` (
  `allocation_no` INT NOT NULL auto_increment,
  `service_no` INT NOT NULL, 
  `car_serial_no` INT NOT NULL,
  `mechanic_id` INT NOT NULL,
  PRIMARY KEY (`allocation_no`),
  INDEX `fk_mechanic_allocation_mechanic1_idx` (`mechanic_id` ASC) ,
  CONSTRAINT `fk_mechanic_allocation_service1`
    FOREIGN KEY (`service_no` , `car_serial_no`)
    REFERENCES `car_test`.`Service` (`service_no` , `car_serial_no`)
    ON DELETE cascade
    ON UPDATE cascade,
  CONSTRAINT `fk_mechanic_allocation_mechanic1`
    FOREIGN KEY (`mechanic_id`)
    REFERENCES `car_test`.`Mechanic` (`mechanic_id`)
    ON DELETE cascade
    ON UPDATE cascade)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


# Customer Data
insert into Customer (name, phone, address, e_mail) values('Arron', '010-0000-0000', 'seoul', 'arron@abc.com');
insert into Customer (name, phone, address, e_mail) values('Ben', '010-0000-1111', 'Busan', 'ben@abc.com');
insert into Customer (name, phone, address, e_mail) values('Danny', '010-0000-3333', 'wabu', 'danny@abc.com');
insert into Customer (name, phone, address, e_mail) values('chris', '010-0000-2222', 'Junju', 'chris@abc.com');
insert into Customer (name, phone, address, e_mail) values('Danny', '010-0000-4444', 'jeju', 'danny@abc.com');
insert into Customer (name, phone, address, e_mail) values('Elly', '010-0000-5555', 'daegu', 'elly@abc.com');
insert into Customer (name, phone, address, e_mail) values('Gavi', '010-0000-6666', 'chungju', 'gavi@abc.com');
insert into Customer (name, phone, address, e_mail) values('Hong', '010-0000-7777', 'goyang', 'hong@abc.com');
insert into Customer (name, phone, address, e_mail) values('Eva', '010-0000-8888', 'hanam', 'eva@abc.com');
insert into Customer (name, phone, address, e_mail) values('Kobe', '010-0000-9999', 'yeoju', 'kobe@abc.com');
insert into Customer (name, phone, address, e_mail) values('Jenny', '010-0000-1010', 'jamsil', 'jenny@abc.com');

#Mechanic Data
insert into Mechanic (name, phone, major, store) values('Lyon', '010-1111-0000', 'Computer Science', 'Jamsil');
insert into Mechanic (name, phone, major, store) values('Willan', '010-1111-1111', 'Motor Electornic', 'Boramae');
insert into Mechanic (name, phone, major, store) values('Mount', '010-1111-3333', 'Mechanical Engineering', 'Jamsil');
insert into Mechanic (name, phone, major, store) values('James', '010-1111-2222', 'Mechanical Engineering', 'Jamsil');
insert into Mechanic (name, phone, major, store) values('Alex', '010-1111-4444', 'Computer Science', 'Boramae');
insert into Mechanic (name, phone, major, store) values('Caroline', '010-1111-5555', 'Motor Electornic', 'Boramae');
insert into Mechanic (name, phone, major, store) values('Vince', '010-1111-6666', 'Computer Science', 'Jamsil');
insert into Mechanic (name, phone, major, store) values('Brian', '010-1111-7777', 'Motor Electornic', 'Jamsil');
insert into Mechanic (name, phone, major, store) values('Nathan', '010-1111-8888', 'Motor Electornic', 'Boramae');
insert into Mechanic (name, phone, major, store) values('Jay', '010-1111-9999', 'Mechanical Engineering', 'Jamsil');
insert into Mechanic (name, phone, major, store) values('Jina', '010-1111-1010', 'Mechanical Engineering', 'Boramae');

#Seller Data
insert into Seller (name, phone, store) values('Whang', '010-2222-0000', 'Boramae');
insert into Seller (name, phone, store) values('Curry', '010-2222-1111','Jamsil');
insert into Seller (name, phone, store) values('Irving', '010-2222-3333','Boramae');
insert into Seller (name, phone, store) values('Green', '010-2222-2222', 'Boramae');
insert into Seller (name, phone, store) values('Mathal', '010-2222-4444', 'Boramae');
insert into Seller (name, phone, store) values('Wood', '010-2222-5555', 'Boramae');
insert into Seller (name, phone, store) values('Sergio', '010-2222-6666', 'Jamsil');
insert into Seller (name, phone, store) values('Roberto', '010-2222-7777', 'Jamsil');
insert into Seller (name, phone, store) values('John', '010-2222-8888', 'Jamsil');
insert into Seller (name, phone, store) values('Jony', '010-2222-9999', 'Jamsil');
insert into Seller (name, phone, store) values('Alice', '010-2222-1010', 'Boramae');

#car_list Data
insert into car_list values(1000231,1,'Sorento',False, 40000 );
insert into car_list(seller_id, car_model, used, price) values(1,'Santafe', False, 42000 );
insert into car_list(seller_id, car_model, used, price) values(2,'Santafe', False, 42000 );
insert into car_list(seller_id, car_model, used, price) values(3,'Sorento',False, 40000 );
insert into car_list(seller_id, car_model, used, price) values(4,'Santafe', False, 42000 );
insert into car_list(seller_id, car_model, used, price) values(5,'Santafe', False, 42000 );
insert into car_list(seller_id, car_model, used, price) values(3,'Sorento',False, 40000 );
insert into car_list(seller_id, car_model, used, price) values(2,'Granduer', False, 42000 );
insert into car_list(seller_id, car_model, used, price) values(8,'Santafe', False, 42000 );
insert into car_list(seller_id, car_model, used, price) values(3,'Sorento',False, 40000 );
insert into car_list(seller_id, car_model, used, price) values(11,'Granduer', False, 42000 );
insert into car_list(seller_id, car_model, used, price) values(10,'Santafe', False, 32000 );
insert into car_list(seller_id, car_model, used, price) values(8,'K7',True, 20000 );
insert into car_list(seller_id, car_model, used, price) values(9,'k5', True, 12000 );
insert into car_list(seller_id, car_model, used, price) values(1,'Santafe', False, 52000 );
insert into car_list(seller_id, car_model, used, price) values(4,'XC90',False, 47000 );
insert into car_list(seller_id, car_model, used, price) values(8,'SM6', False, 22000 );
insert into car_list(seller_id, car_model, used, price) values(2,'Avante', False, 32000 );
insert into car_list(seller_id, car_model, used, price) values(3,'GV80',False, 70000 );
insert into car_list(seller_id, car_model, used, price) values(1,'Avante', True, 12000 );
insert into car_list(seller_id, car_model, used, price) values(1,'k3', False, 22000 );
insert into car_list(seller_id, car_model, used, price) values(11,'QM6',False, 25000 );

# Invoice Data
insert into Invoice values (1000231, 1,'2017-08-25');
insert into Invoice values (1000233, 3, '2018-03-21');
insert into Invoice values (1000237, 7,'2018-12-02');
insert into Invoice values (1000232, 9,'2017-09-25');
insert into Invoice values (1000238, 2,'2018-01-17');
insert into Invoice values (1000234, 3,'2017-02-08');
insert into Invoice values (1000235, 6,'2017-03-15');
insert into Invoice values (1000236, 4,'2019-05-25');
insert into Invoice values (1000239, 10,'2017-07-12');
insert into Invoice values (1000240, 7, '2018-03-25');
insert into Invoice values (1000241, 2,'2019-08-09');
insert into Invoice values (1000242, 3,'2017-01-02');
insert into Invoice values (1000243, 1,'2017-08-23');
insert into Invoice values (1000244, 5,'2019-12-14');
insert into Invoice values (1000245, 5,'2017-11-21');
insert into Invoice values (1000247, 6,'2018-02-27');
insert into Invoice values (1000249, 1,'2019-04-14');
insert into Invoice values (1000250, 1,'2019-07-07');
insert into Invoice values (1000246, 1,'2020-06-01');
insert into Invoice values (1000248, 1,'2019-08-13');

# Service Data (service_no, car_serail_no, customer_id, service_date)
insert into Service values (1, 1000231, 1,'2018-08-25');
insert into Service(car_serial_no, customer_id, service_date) values (1000233, 3, '2019-03-21');
insert into Service(car_serial_no, customer_id, service_date) values (1000237, 7,'2019-03-02');
insert into Service(car_serial_no, customer_id, service_date) values (1000232, 9,'2020-03-13');
insert into Service(car_serial_no, customer_id, service_date) values (1000238, 2,'2019-07-17');
insert into Service(car_serial_no, customer_id, service_date) values (1000238, 2,'2019-07-18');
insert into Service(car_serial_no, customer_id, service_date) values (1000241, 2,'2020-03-09');
insert into Service(car_serial_no, customer_id, service_date) values (1000242, 3,'2017-01-02');
insert into Service(car_serial_no, customer_id, service_date) values (1000243, 1,'2017-08-23');
insert into Service(car_serial_no, customer_id, service_date) values (1000244, 5,'2020-12-14');
insert into Service(car_serial_no, customer_id, service_date) values (1000245, 5,'2018-12-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000247, 6,'2018-02-27');
insert into Service(car_serial_no, customer_id, service_date) values (1000249, 1,'2019-04-14');
insert into Service(car_serial_no, customer_id, service_date) values (1000250, 1,'2019-07-17');
insert into Service(car_serial_no, customer_id, service_date) values (1000235, 6,'2017-09-15');
insert into Service(car_serial_no, customer_id, service_date) values (1000236, 4,'2019-05-25');
insert into Service(car_serial_no, customer_id, service_date) values (1000236, 4,'2019-05-27');
insert into Service(car_serial_no, customer_id, service_date) values (1000239, 10,'2019-08-13');
insert into Service(car_serial_no, customer_id, service_date) values (1000240, 7,'2018-09-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000241, 2,'2019-10-18');
insert into Service(car_serial_no, customer_id, service_date) values (1000242, 3,'2017-09-06');
insert into Service(car_serial_no, customer_id, service_date) values (1000243, 1,'2017-08-29');
insert into Service(car_serial_no, customer_id, service_date) values (1000244, 5,'2019-12-14');
insert into Service(car_serial_no, customer_id, service_date) values (1000245, 5,'2019-02-13');
insert into Service(car_serial_no, customer_id, service_date) values (1000247, 6,'2018-06-11');
insert into Service(car_serial_no, customer_id, service_date) values (1000249, 1,'2020-01-07');
insert into Service(car_serial_no, customer_id, service_date) values (1000250, 1,'2019-07-07');
insert into Service(car_serial_no, customer_id, service_date) values (1000248, 1,'2019-12-13');
insert into Service(car_serial_no, customer_id, service_date) values (1000240, 7,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000236, 4,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000249, 1,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000241, 2,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000242, 3,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000243, 1,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000244, 5,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000245, 5,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000247, 6,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000248, 1,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000235, 6,'2020-08-12');
insert into Service(car_serial_no, customer_id, service_date) values (1000242, 3,'2020-08-13');
select * from Service;
# Mechanic Allocation Data (service_no, car_serial_no, mechanic_id)
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (1, 1000231, 1);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (2, 1000233, 2);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (3, 1000237, 3);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (4, 1000232, 4);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (5, 1000238, 11);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (6, 1000238, 4);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (7, 1000241, 9);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (8, 1000242, 2);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (9, 1000243,5);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (10, 1000244,6);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (11, 1000245,7);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values(12, 1000247,9);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (13, 1000249,10);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (14, 1000250,4);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (15, 1000235,2);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (16, 1000236,4);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (17, 1000236,5);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (18, 1000239,6);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (19, 1000240,8);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (20, 1000241,7);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (21, 1000242,1);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (22, 1000243,4);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (23, 1000244,5);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (24, 1000245,8);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (25, 1000247,7);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (26, 1000249,2);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (27, 1000250,3);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id) values (28, 1000248,5);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (29, 1000240,1);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (30, 1000236,2);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (31, 1000249,3);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (32, 1000241,4);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (33, 1000242,5);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (34, 1000243,6);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (35, 1000244,7);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (36, 1000245,8);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (37, 1000247,9);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (38, 1000248,10);
insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values (39, 1000235,11);


# Parts Data
insert into Parts(price, name) values (200, 'Air Filter');
insert into Parts(price, name)   values (260, 'Alternator');
insert into Parts(price, name)   values (720, 'Axle');
insert into Parts(price, name)   values (50, 'Joint');
insert into Parts(price, name)   values (70, 'Carbin Filter');
insert into Parts(price, name)   values (700, 'Handle');
insert into Parts(price, name)   values (400, 'Mount');
insert into Parts(price, name)   values (90, 'Headlight');
insert into Parts(price, name)   values (170, 'Muffler');
insert into Parts(price, name)   values (130, 'Radiator');
insert into Parts(price, name)  values (90, 'Starter');
insert into Parts(price, name)   values (110, 'Mirror');
insert into Parts(price, name)   values (310, 'Switch');
insert into Parts(price, name)   values (60, 'Wheel');

# Parts_requirement Data 
insert into Parts_requirement values (1, 28, 1000248, 3);
insert into Parts_requirement(service_no, car_serial_no, parts_no) values (28, 1000248, 7);
insert into Parts_requirement(service_no, car_serial_no, parts_no) values (28, 1000248, 11);
insert into Parts_requirement(service_no, car_serial_no, parts_no) values (14, 1000250, 9);
insert into Parts_requirement(service_no, car_serial_no, parts_no) values (14, 1000250, 14);
insert into Parts_requirement(service_no, car_serial_no, parts_no) values (8, 1000242, 9);
insert into Parts_requirement(service_no, car_serial_no, parts_no) values (8, 1000242, 10);



