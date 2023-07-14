-- Select bands where style is 'Glam rock' and calculate their lifespan
SELECT 
  band_name, -- The 'band_name' column
  IF(split IS NOT NULL, split, 2022) - formed AS lifespan -- The 'lifespan' column representing the lifespan of the band
FROM 
  metal_bands
WHERE 
  style = 'Glam rock'  -- Filter the bands where style is 'Glam rock'
ORDER BY 
  lifespan DESC -- Order the results by the lifespan in descending order
;
