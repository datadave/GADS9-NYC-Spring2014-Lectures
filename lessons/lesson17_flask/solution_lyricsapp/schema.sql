DROP TABLE IF EXISTS predictions;
CREATE TABLE predictions (
  id integer primary key autoincrement,
  lyrics text not null,
  artist text not null
);
