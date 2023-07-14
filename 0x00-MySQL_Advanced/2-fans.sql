-- Creating the view 'band_ranking' that contains the ranking of countries by the number of (non-unique) fans
CREATE OR REPLACE VIEW band_ranking AS
SELECT 
    origin,  -- The 'origin' column containing the country of origin
    SUM(fans) AS nb_fans  -- The 'nb_fans' column containing the total number of (non-unique) fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
