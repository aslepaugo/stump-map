delete from stump;
delete from city;
delete from stump_type;


insert into city(name) values('Brno');
insert into city(name) values('Wroclaw');
insert into city(name) values('Minsk');

insert into stump_type(name, color) values('To Plant', 'lightgreen');
insert into stump_type(name, color) values('Stump', 'lightgray');
insert into stump_type(name, color) values('Dead Tree', 'darkred');
insert into stump_type(name, color) values('Dead Sapling', 'darkblue');


insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.211169,16.592006, 'img/to_plant_01.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='To Plant'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.205425,16.596822, 'img/stump_01.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.21535,16.579414 , 'img/stump_02.jpg', (select id from city where name = 'Brno'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.215519,16.579864, 'img/dead_tree_01.jpg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Tree'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.215572,16.580008, 'img/to_plant_02.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='To Plant'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.215769,16.580964, 'img/dead_tree_02.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Tree'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.215769,16.580978, 'img/dsapling_01.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.216014,16.581642, 'img/dsapling_02.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.216381,16.582911, 'img/stump_03.jpg', (select id from city where name = 'Brno'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.216514,16.583375, 'img/dsapling_01.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.216767,16.584767, 'img/stump_05.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.215722,16.588078, 'img/stump_06.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.217083,16.586206, 'img/dsapling_02.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.215736,16.586039, 'img/dead_tree_03.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Tree'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.212472,16.593444, 'img/dsapling_02.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.211767,16.591989, 'img/to_plant_01.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='To Plant'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.212008,16.592067, 'img/dsapling_01.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.211281,16.591147, 'img/stump_07.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.203772,16.6033  , 'img/dsapling_02.jpeg', (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.203769,16.603303, 'img/stump_03.jpg', (select id from city where name = 'Brno'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.214925,16.593111, null, (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.195647,16.571975, null, (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Tree'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.210378,16.611186, null, (select id from city where name = 'Brno'), (select id from stump_type where name='To Plant'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (49.210369,16.611181, null, (select id from city where name = 'Brno'), (select id from stump_type where name='Dead Tree'));


insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (53.897134, 27.518490, null, (select id from city where name = 'Minsk'), (select id from stump_type where name='Dead Tree'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (53.896873, 27.526413, null, (select id from city where name = 'Minsk'), (select id from stump_type where name='To Plant'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (53.922996, 27.619951, null, (select id from city where name = 'Minsk'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (53.892488, 27.657104, null, (select id from city where name = 'Minsk'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (53.927697, 27.569096, null, (select id from city where name = 'Minsk'), (select id from stump_type where name='Stump'));


insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.092123, 16.979293, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Dead Tree'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.094171, 16.983520, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='To Plant'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.099562, 16.984226, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.097278, 16.998463, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.097615, 16.998978, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.097649, 17.001263, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Dead Tree'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.099919, 17.005952, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='To Plant'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.098315, 17.011434, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Dead Sapling'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.098322, 17.010704, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Stump'));
insert into stump (latitude, longitude, image_url, city_id, stump_type_id) 
values (51.097224, 17.012828, null, (select id from city where name = 'Wroclaw'), (select id from stump_type where name='Stump'));