CREATE TABLE IF NOT EXISTS userdata (
    uid varchar(128) primary key,
    name varchar(128) CHARACTER SET utf8,
    age INTEGER(128)
    ) engine=InnoDB default charset utf8;
