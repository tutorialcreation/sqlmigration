select top 20 count(endpoints_location.landmarks) as [c_landmarks],endpoints_location.landmarks,endpoints_location.id
from endpoints_trafficinfo 
inner join endpoints_location 
on endpoints_trafficinfo.location_id = endpoints_location.id
group by endpoints_location.landmarks,endpoints_location.id
having count(endpoints_location.landmarks) > 1
order by count(endpoints_location.landmarks) desc
