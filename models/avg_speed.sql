select avg(avg_speed) as [average_vehicle_speed],type from endpoints_trafficinfo group by type;
