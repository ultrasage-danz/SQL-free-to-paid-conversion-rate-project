SELECT 
    i.student_id,
    i.date_registered,
    MIN(e.date_watched) AS first_date_watched,
    MIN(p.date_purchased) AS first_date_purchased,
    DATEDIFF(MIN(e.date_watched), i.date_registered) AS date_diff_reg_watch,
    DATEDIFF(MIN(p.date_purchased), MIN(e.date_watched)) AS date_diff_watch_purch
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/yourfiles.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM
    student_info i
LEFT JOIN
    student_engagement e ON i.student_id = e.student_id
LEFT JOIN
    student_purchases p ON i.student_id = p.student_id
GROUP BY
    i.student_id, i.date_registered
HAVING
    first_date_watched <= first_date_purchased OR first_date_purchased IS NULL
ORDER BY
    i.student_id;
