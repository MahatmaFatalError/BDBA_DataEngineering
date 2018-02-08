-- Table: public.service_request

-- DROP TABLE public.service_request;

CREATE TABLE public.service_request
(
    unique_key character(255)  NOT NULL,
    created_date timestamp without time zone,
    agency_name character(255)  ,
    complaint_type character(255)  ,
    descriptor character(255)  ,
    longitude double precision,
    latitude double precision,
    agency character(255)  ,
    location_type character(255)  ,
    incident_zip character(10)  ,
    incident_address character(255)  ,
    street_name character(255)  ,
    cross_street_1 character(255)  ,
    cross_street_2 character(255)  ,
    address_type character(255)  ,
    city character(255)  ,
    status character(50)  ,
    due_date timestamp without time zone,
    borough character(100)  ,
    resolution_description text  ,
    closed_date timestamp without time zone,
    CONSTRAINT unique_key_primary PRIMARY KEY (unique_key)
)

ALTER TABLE public.service_request
    OWNER to postgres;
