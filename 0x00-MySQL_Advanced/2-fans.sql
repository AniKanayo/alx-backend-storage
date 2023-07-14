-- Group by origin and sum the number of fans
SELECT 
  origin, -- The 'origin' column showing the country of origin
  SUM(fans) AS nb_fans  -- The 'nb_fans' column representing the total number of (non-unique) fans
FROM 
  metal_bands
GROUP BY 
  origin
ORDER BY 
  nb_fans DESC -- Order the results by the number of fans in descending order
;
