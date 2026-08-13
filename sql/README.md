# SQL

## installation 

```
sudo apt install mysql-server -y
```

## verify server is running 

```
sudo systemctl status mysql
```

## login 
```
mysql -u <User name> -p  | mysql
```
-u : User
-p : Password



```
mysql> describe <table_name>; 
```
This will desplay the fields in the tables.

## createing table

## adding row to table 

```
 insert into Users values (1, "tlhongtshepiso2@gmail.com", "Tshepiso");
```

## showing info from table
```
select * from Users;
```

<*> this means every column 

## inserting values in tables

```
insert into Users values (1, "tlhongtshepiso2@gmail.com", "Tshepiso");
```

## Getting only rows
```
select <row_name> from <table_name>
```

## Filter out
Filter out information based the values
```
select * from <table> where <coloumn_name> = <value>
```
```
select * from Avengers where origin = "earth";
```
Now you can add logic such as or
```
select * from <table_name> where <column_name> = <value> or <column_name> = <value>
```

## Deleting from table 
```
 delete from Avengers where first_name = "jeff";
```

## Update Table

```
update Avengers  set last_name = NULL where first_name = "groot";
```


## displaying in order

```
select * from Avengers order by age asc;
```
```
select * from Avengers order by age desc;
```

## Altering tables
```
alter table Avengers add beard boolean;
```
