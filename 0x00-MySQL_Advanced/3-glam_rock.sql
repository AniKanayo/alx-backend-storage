-- The SQL query selects band names and computes their lifespan, filtering for bands with Glam rock as main style
SELECT 
  band_name, -- 'band_name' column for the name of the band
  IF(split IS NOT NULL, split, 2022) - formed AS lifespan -- 'lifespan' column, lifespan of the band in years
FROM 
  metal_bands
WHERE 
  style = 'Glam rock'  -- We only want bands with Glam rock as their main style
ORDER BY 
  lifespan DESC -- We want the bands ranked by their longevity, in descending order
;
