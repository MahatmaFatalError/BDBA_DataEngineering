-- Table: public.service_request

-- DROP TABLE public.service_request;

CREATE TABLE public.service_request
(
    id bigserial NOT NULL,    
	created_date timestamp with time zone,
    agency_name character(255) COLLATE pg_catalog."default",
    complaint_type character(255) COLLATE pg_catalog."default",
    descriptor character(255) COLLATE pg_catalog."default",
    longitude double precision,
    latitude double precision,
    agency character(255) COLLATE pg_catalog."default",
    location_type character(255) COLLATE pg_catalog."default",
    incident_zip character(10) COLLATE pg_catalog."default",
    incident_address character(255) COLLATE pg_catalog."default",
    street_name character(255) COLLATE pg_catalog."default",
    cross_street_1 character(255) COLLATE pg_catalog."default",
    cross_street_2 character(255) COLLATE pg_catalog."default",
    address_type character(255) COLLATE pg_catalog."default",
    city character(255) COLLATE pg_catalog."default",
    status character(50) COLLATE pg_catalog."default",
    due_date timestamp with time zone,
    borough character(100) COLLATE pg_catalog."default",
    resolution_description text COLLATE pg_catalog."default",
    CONSTRAINT pk_id PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.service_request
    OWNER to postgres;