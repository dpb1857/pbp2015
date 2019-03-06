;; Riders finishing between 90 and 91 hours;
select * FROM (select r.plaque, endtime.timestamp-start.timestamp elapsed, r.time
              FROM data_rider r JOIN data_timestamp start ON r.plaque=start.plaque AND start.control_id=1
                                JOIN data_timestamp endtime ON r.plaque=endtime.plaque AND endtime.control_id=17
                                WHERE endtime.timestamp-start.timestamp > 90) sub
         ORDER BY elapsed;
