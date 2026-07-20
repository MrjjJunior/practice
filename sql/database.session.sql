
-- @block 
CREATE TABLE Users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE, 
    bio TEXT, 
    country VARCHAR(2)
);

-- @block
 create table Users(
    id INT auto_increment primary key,
    email varchar(255) not null unique,
    name varchar(255)
    );

-- @block
insert into Users values (
    1, "tlhongtshepiso2@gmail.com", "Tshepiso"
    );


-- @block
select * from Users;

-- @block
insert into Users values (
    1,
    "tlhongtshepiso2@gmail.com",
    "Tshepiso");
