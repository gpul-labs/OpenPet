INSERT INTO provinces (name) VALUES ('A Coruña');

INSERT INTO locations (name, url, phone, latitude, longitude, province_id) VALUES
    ('Perrera Municipal de Bens',
     'http://www.coruna.es/adopcion',
     '+34981263093',
      43.3638, -8.4433,
      (SELECT id FROM provinces WHERE name = 'A Coruña'));

INSERT INTO origins (name, url) VALUES ('coruna.es','http://www.coruna.es/adopcion');

INSERT INTO `species` VALUES (1,'Perro',NULL),(2,'Gato',NULL);

INSERT INTO `races` (specie_id, name) VALUES 
    (1,'American Staffordshire terrier'),
    (1,'Can de palleiro'),
    (1,'Pastor alemán'),
    (1,'Pastor belga'),    
    (1,'Perro genérico'),
    (2,'Persa'),
    (2,'Siamés'),
    (2,'Gato genérico');
