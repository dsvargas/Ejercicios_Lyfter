

create table SalesPerson(
    ID int primary key,
    Name varchar(50),
    age int,
    salary int
)
create table Customers(
    ID int primary key,
    Name varchar(50),
    city varchar(50),
    Industry varchar(50)
)
create table Orders(
    ID int primary key,
    OrderDate date,
    CustomerID int,
    SalesPersonID int,
    Amount decimal(10,2),
    foreign key (CustomerID) references Customers(ID),
    foreign key (SalesPersonID) references SalesPerson(ID)
)

select SalesPerson.name, SalesPerson.salary from SalesPerson 
inner join Orders on SalesPerson.ID = Orders.SalesPersonID 
inner join Customers on Orders.CustomerID = Customers.ID 
where Customers.Name like 'Samsonic%' order by SalesPerson.name desc;



select SalesPerson.name from SalesPerson
inner join Orders on SalesPerson.ID = Orders.SalesPersonID
where Orders.ID is null;

delete from SalesPerson where ID in (select SalesPersonID from Orders group by SalesPersonID having count(*) = 0);


