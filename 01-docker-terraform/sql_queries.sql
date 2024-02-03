-- Question 3. Count records
select count(*)
from data_taxi
where lpep_pickup_datetime >= '2019-09-18' and lpep_dropoff_datetime < '2019-09-19';
-- answer 15612


-- Question 4. Largest trip for each day
select lpep_pickup_datetime::date as trip_date, trip_distance
from data_taxi dt
order by trip_distance desc
limit 1;
-- answer 2019-09-26


--Question 5. Three biggest pick up Boroughs
select z."Borough", sum(total_amount) as total
from data_taxi t
left join zones z on
	t."PULocationID" = z."LocationID"
where t.lpep_pickup_datetime >= '2019-09-18' and t.lpep_pickup_datetime < '2019-09-19' and z."Borough" != 'Unknown'
group by z."Borough"
having sum(total_amount) >= 50000
order by sum(total_amount) desc
limit 3;
--answer "Brooklyn" "Manhattan" "Queens"


--Question 6. Largest tip
select z."Zone" as pick_up_zone, z2."Zone" as drop_off_zone, tip_amount
from data_taxi d
left join zones z on
    d."PULocationID" = z."LocationID"
left join zones z2 on
    d."DOLocationID" = z2."LocationID"
where d.lpep_pickup_datetime::date >= '2019-09-01' and d.lpep_pickup_datetime::date < '2019-10-01' and z."Zone" = 'Astoria'
order by tip_amount desc
limit 1;
-- answer JFK Airport

