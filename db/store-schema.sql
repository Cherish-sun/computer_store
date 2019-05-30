
drop table if exists Customers;

drop table if exists OrderLineItems;

drop table if exists Goods;

drop table if exists Orders;

/*==============================================================*/
/* Table: Customers                                             */
/*==============================================================*/
create table Customers
(
   id                  varchar(20) primary key,
   name                 varchar(50) not null,
   password             varchar(20) not null,
   address              varchar(100),
   phone                varchar(20),
   birthday             varchar(20)
);

/*==============================================================*/
/* Table: Goods                                                 */
/*==============================================================*/
create table Goods
(
   id                  integer  primary key autoincrement,
   name                varchar(100) not null,
   price                float,
   description          varchar(200),
   brand                varchar(30),
   cpu_brand            varchar(30),
   cpu_type             varchar(30),
   memory_capacity      varchar(30),
   hd_capacity          varchar(30),
   card_model           varchar(30),
   displaysize          varchar(30),
   image                varchar(100)
);

/*==============================================================*/
/* Table: Orders                                                */
/*==============================================================*/
create table Orders
(
   id                   varchar(20) primary key,
   order_date           varchar(20),
   status               integer default 1,
   total                float
);


/*==============================================================*/
/* Table: OrderLineItems                                        */
/*==============================================================*/
create table OrderLineItems
(
   id                   integer primary key autoincrement,
   goodsid              integer not null references Goods(id),
   orderid              integer not null references Orders(id) ,
   quantity             integer,
   sub_total            float
);
