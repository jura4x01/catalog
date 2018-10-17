ALTER USER postgres WITH PASSWORD 'postgres';
CREATE USER catalog WITH PASSWORD 'catalog' SUPERUSER;
CREATE DATABASE catalog OWNER catalog;
GRANT ALL PRIVILEGES ON DATABASE catalog TO postgres;
CREATE EXTENSION postgis;
ALTER TABLE geometry_columns OWNER TO catalog;
ALTER TABLE geography_columns OWNER TO catalog;
ALTER TABLE raster_columns OWNER TO catalog;
ALTER TABLE raster_overviews OWNER TO catalog;
ALTER TABLE spatial_ref_sys OWNER TO catalog;