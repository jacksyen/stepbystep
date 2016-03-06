drop table if exits entries;
create table entries(
  id INTEGER primary key autoincrement,
  title string not null,
  text string not NULL
);