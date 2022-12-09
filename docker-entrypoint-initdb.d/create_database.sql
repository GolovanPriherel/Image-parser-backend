DO
$do$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'image_info') THEN
     CREATE DATABASE IF NOT EXISTS "image_info";
    END IF;
END
$do$;