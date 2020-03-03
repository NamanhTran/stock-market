CREATE database if not exists STOCK_TRADER;
use STOCK_TRADER;

CREATE table if not exists CUSTOMER(user_ID int NOT NULL, user_name varchar(20) NOT NULL, 
first_name varchar(30) NOT NULL, last_name varchar(30) NOT NULL,
suffix varchar(5), ssn varchar(9) NOT NULL, address1 varchar(60), address2 varchar(60),
city varchar(45), state varchar(30), country varchar(45), zipcode varchar(5),
date_of_birth datetime,
primary key(user_ID, user_name, ssn));

CREATE table if not exists STOCK(user_ID int NOT NULL, stock_ID int NOT NULL,
quantity int NOT NULL, market_value float NOT NULL,
primary key(user_ID, stock_ID), index(stock_ID),
foreign key(user_ID) references CUSTOMER(user_ID));

CREATE table if not exists STOCK_ORDER(order_num int NOT NULL, stock_ID int NOT NULL,
date_of_transaction datetime NOT NULL, num_of_shares int NOT NULL, total_cost float NOT NULL, 
cost_of_share float NOT NULL,
primary key(order_num),
foreign key(stock_ID) references STOCK(stock_ID));

CREATE table if not exists BALANCE(user_ID int NOT NULL, net_account_value float,
net_cash float, transaction_type varchar(10), date_of_deposit datetime, deposit_amount float,
date_of_withdrawal datetime, withdrawal_amount float,
primary key(user_ID),
foreign key(user_ID) references CUSTOMER(user_ID));

CREATE table if not exists BANK_INFO(user_ID int NOT NULL, bank_num int, 
bank_name varchar(45), account_num int, paper_routing_num int, wire_routing_num int,
bank_address1 varchar(60), bank_address2 varchar(60), city varchar(45),
state varchar(30), country varchar(45), zip varchar(5), date_added datetime,
date_removed datetime, status_of_account varchar(20),
primary key(user_ID, bank_num),
foreign key(user_ID) references CUSTOMER(user_ID));
