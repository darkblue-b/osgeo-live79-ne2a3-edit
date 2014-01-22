--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: jan14_edits; Type: TABLE; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

CREATE TABLE jan14_edits (
    rec_pkey integer,
    name character varying(100),
    name_alt character varying(200),
    name_local character varying(200),
    abbrev character varying(10),
    type character varying(100),
    type_en character varying(100),
    latitude numeric,
    longitude numeric,
    wikipedia character varying(254),
    area_sqkm numeric,
    note character varying(254),
    code_local character varying(50),
    code_hasc character varying(10),
    postal character varying(10),
    fips character varying(5),
    fips_alt character varying(50),
    iso_3166_2 character varying(10),
    iso_a2 character varying(2),
    adm0_sr integer,
    provnum_ne double precision,
    gadm_level integer,
    region_cod character varying(50),
    region character varying(100),
    woe_id double precision,
    woe_label character varying(250),
    woe_name character varying(100),
    sov_a3 character varying(3),
    adm0_a3 character varying(3),
    adm0_label integer,
    admin character varying(200),
    adm1_code character varying(10),
    gns_id double precision,
    gns_name character varying(200),
    gns_level integer,
    gns_lang character varying(10),
    gns_adm1 character varying(10),
    gns_region character varying(10),
    geonunit character varying(200),
    gu_a3 character varying(3),
    gn_id double precision,
    gn_name character varying(200),
    gn_level integer,
    gn_region character varying(50),
    gn_a1_code character varying(10),
    region_sub character varying(250),
    sub_code character varying(10),
    edit_time timestamp without time zone,
    ip_addr inet,
    primary_key integer NOT NULL
);


ALTER TABLE public.jan14_edits OWNER TO ne2a3_editor;

--
-- Name: jan14_edits_primary_key_seq; Type: SEQUENCE; Schema: public; Owner: ne2a3_editor
--

CREATE SEQUENCE jan14_edits_primary_key_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.jan14_edits_primary_key_seq OWNER TO ne2a3_editor;

--
-- Name: jan14_edits_primary_key_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ne2a3_editor
--

ALTER SEQUENCE jan14_edits_primary_key_seq OWNED BY jan14_edits.primary_key;


--
-- Name: jan14_web; Type: TABLE; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

CREATE TABLE jan14_web (
    adm1_code character varying(10),
    shape_leng numeric,
    shape_area numeric,
    diss_me double precision,
    iso_3166_2 character varying(10),
    wikipedia character varying(254),
    iso_a2 character varying(2),
    adm0_sr integer,
    name character varying(100),
    name_alt character varying(200),
    name_local character varying(200),
    type character varying(100),
    type_en character varying(100),
    code_local character varying(50),
    code_hasc character varying(10),
    note character varying(254),
    hasc_maybe character varying(50),
    region character varying(100),
    region_cod character varying(50),
    provnum_ne double precision,
    gadm_level integer,
    check_me integer,
    scalerank integer,
    datarank integer,
    abbrev character varying(10),
    postal character varying(10),
    area_sqkm numeric,
    sameascity integer,
    labelrank integer,
    featurecla character varying(50),
    name_len double precision,
    mapcolor9 integer,
    mapcolor13 integer,
    fips character varying(5),
    fips_alt character varying(50),
    woe_id double precision,
    woe_label character varying(250),
    woe_name character varying(100),
    latitude numeric,
    longitude numeric,
    sov_a3 character varying(3),
    adm0_a3 character varying(3),
    adm0_label integer,
    admin character varying(200),
    geonunit character varying(200),
    gu_a3 character varying(3),
    gn_id double precision,
    gn_name character varying(200),
    gns_id double precision,
    gns_name character varying(200),
    gn_level integer,
    gn_region character varying(50),
    gn_a1_code character varying(10),
    region_sub character varying(250),
    sub_code character varying(10),
    gns_level integer,
    gns_lang character varying(10),
    gns_adm1 character varying(10),
    gns_region character varying(10),
    pkey integer NOT NULL
);


ALTER TABLE public.jan14_web OWNER TO ne2a3_editor;

--
-- Name: jan14_main_view; Type: VIEW; Schema: public; Owner: ne2a3_editor
--

CREATE VIEW jan14_main_view AS
    SELECT jan14_web.adm1_code, jan14_web.name, jan14_web.admin, jan14_web.latitude, jan14_web.longitude, jan14_web.pkey FROM jan14_web ORDER BY jan14_web.admin, jan14_web.name;


ALTER TABLE public.jan14_main_view OWNER TO ne2a3_editor;

--
-- Name: jan14_web_pkey_seq; Type: SEQUENCE; Schema: public; Owner: ne2a3_editor
--

CREATE SEQUENCE jan14_web_pkey_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.jan14_web_pkey_seq OWNER TO ne2a3_editor;

--
-- Name: jan14_web_pkey_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ne2a3_editor
--

ALTER SEQUENCE jan14_web_pkey_seq OWNED BY jan14_web.pkey;


--
-- Name: ne_10m_admin_1_states_provinces_shp; Type: TABLE; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

CREATE TABLE ne_10m_admin_1_states_provinces_shp (
    gid integer NOT NULL,
    adm1_code character varying(10),
    shape_leng numeric,
    shape_area numeric,
    diss_me integer,
    adm1_code_ character varying(10),
    iso_3166_2 character varying(10),
    wikipedia character varying(254),
    sr_sov_a3 character varying(3),
    sr_adm0_a3 character varying(3),
    iso_a2 character varying(2),
    adm0_sr smallint,
    admin0_lab smallint,
    name character varying(100),
    name_alt character varying(200),
    name_local character varying(200),
    type character varying(100),
    type_en character varying(100),
    code_local character varying(50),
    code_hasc character varying(10),
    note character varying(254),
    hasc_maybe character varying(50),
    region character varying(100),
    region_cod character varying(50),
    region_big character varying(200),
    big_code character varying(50),
    provnum_ne integer,
    gadm_level smallint,
    check_me smallint,
    scalerank smallint,
    datarank smallint,
    abbrev character varying(10),
    postal character varying(10),
    area_sqkm double precision,
    sameascity smallint,
    labelrank smallint,
    featurecla character varying(50),
    admin character varying(200),
    name_len integer,
    mapcolor9 smallint,
    mapcolor13 smallint,
    the_geom geometry(MultiPolygon,4326)
);


ALTER TABLE public.ne_10m_admin_1_states_provinces_shp OWNER TO ne2a3_editor;

--
-- Name: ne_10m_admin_1_states_provinces_shp_gid_seq; Type: SEQUENCE; Schema: public; Owner: ne2a3_editor
--

CREATE SEQUENCE ne_10m_admin_1_states_provinces_shp_gid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ne_10m_admin_1_states_provinces_shp_gid_seq OWNER TO ne2a3_editor;

--
-- Name: ne_10m_admin_1_states_provinces_shp_gid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ne2a3_editor
--

ALTER SEQUENCE ne_10m_admin_1_states_provinces_shp_gid_seq OWNED BY ne_10m_admin_1_states_provinces_shp.gid;


--
-- Name: prov_admin1_ne; Type: TABLE; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

CREATE TABLE prov_admin1_ne (
    gid integer NOT NULL,
    adm1_code character varying(10),
    shape_leng numeric,
    shape_area numeric,
    diss_me double precision,
    iso_3166_2 character varying(10),
    wikipedia character varying(254),
    iso_a2 character varying(2),
    adm0_sr integer,
    name character varying(100),
    name_alt character varying(200),
    name_local character varying(200),
    type character varying(100),
    type_en character varying(100),
    code_local character varying(50),
    code_hasc character varying(10),
    note character varying(254),
    hasc_maybe character varying(50),
    region character varying(100),
    region_cod character varying(50),
    provnum_ne double precision,
    gadm_level integer,
    check_me integer,
    scalerank integer,
    datarank integer,
    abbrev character varying(10),
    postal character varying(10),
    area_sqkm numeric,
    sameascity integer,
    labelrank integer,
    featurecla character varying(50),
    name_len double precision,
    mapcolor9 integer,
    mapcolor13 integer,
    fips character varying(5),
    fips_alt character varying(50),
    woe_id double precision,
    woe_label character varying(250),
    woe_name character varying(100),
    latitude numeric,
    longitude numeric,
    sov_a3 character varying(3),
    adm0_a3 character varying(3),
    adm0_label integer,
    admin character varying(200),
    geonunit character varying(200),
    gu_a3 character varying(3),
    gn_id double precision,
    gn_name character varying(200),
    gns_id double precision,
    gns_name character varying(200),
    gn_level integer,
    gn_region character varying(50),
    gn_a1_code character varying(10),
    region_sub character varying(250),
    sub_code character varying(10),
    gns_level integer,
    gns_lang character varying(10),
    gns_adm1 character varying(10),
    gns_region character varying(10),
    geom geometry(MultiPolygon,4326)
);


ALTER TABLE public.prov_admin1_ne OWNER TO ne2a3_editor;

--
-- Name: TABLE prov_admin1_ne; Type: COMMENT; Schema: public; Owner: ne2a3_editor
--

COMMENT ON TABLE prov_admin1_ne IS '/home/shared/ne2_work/ne3_misc/ne_10m_admin_1_states_provinces/ne_10m_admin_1_states_provinces';


--
-- Name: prov_admin1_ne_gid_seq; Type: SEQUENCE; Schema: public; Owner: ne2a3_editor
--

CREATE SEQUENCE prov_admin1_ne_gid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prov_admin1_ne_gid_seq OWNER TO ne2a3_editor;

--
-- Name: prov_admin1_ne_gid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ne2a3_editor
--

ALTER SEQUENCE prov_admin1_ne_gid_seq OWNED BY prov_admin1_ne.gid;


--
-- Name: primary_key; Type: DEFAULT; Schema: public; Owner: ne2a3_editor
--

ALTER TABLE ONLY jan14_edits ALTER COLUMN primary_key SET DEFAULT nextval('jan14_edits_primary_key_seq'::regclass);


--
-- Name: pkey; Type: DEFAULT; Schema: public; Owner: ne2a3_editor
--

ALTER TABLE ONLY jan14_web ALTER COLUMN pkey SET DEFAULT nextval('jan14_web_pkey_seq'::regclass);


--
-- Name: gid; Type: DEFAULT; Schema: public; Owner: ne2a3_editor
--

ALTER TABLE ONLY ne_10m_admin_1_states_provinces_shp ALTER COLUMN gid SET DEFAULT nextval('ne_10m_admin_1_states_provinces_shp_gid_seq'::regclass);


--
-- Name: gid; Type: DEFAULT; Schema: public; Owner: ne2a3_editor
--

ALTER TABLE ONLY prov_admin1_ne ALTER COLUMN gid SET DEFAULT nextval('prov_admin1_ne_gid_seq'::regclass);


--
-- Name: jan14_edits_pkey; Type: CONSTRAINT; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

ALTER TABLE ONLY jan14_edits
    ADD CONSTRAINT jan14_edits_pkey PRIMARY KEY (primary_key);


--
-- Name: ne_10m_admin_1_states_provinces_shp_pkey; Type: CONSTRAINT; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

ALTER TABLE ONLY ne_10m_admin_1_states_provinces_shp
    ADD CONSTRAINT ne_10m_admin_1_states_provinces_shp_pkey PRIMARY KEY (gid);


--
-- Name: prov_admin1_ne_pkey; Type: CONSTRAINT; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

ALTER TABLE ONLY prov_admin1_ne
    ADD CONSTRAINT prov_admin1_ne_pkey PRIMARY KEY (gid);


--
-- Name: ne_10m_admin_1_states_provinces_shp_the_geom_gist; Type: INDEX; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

CREATE INDEX ne_10m_admin_1_states_provinces_shp_the_geom_gist ON ne_10m_admin_1_states_provinces_shp USING gist (the_geom);


--
-- Name: prov_admin1_ne_geom_gist; Type: INDEX; Schema: public; Owner: ne2a3_editor; Tablespace: 
--

CREATE INDEX prov_admin1_ne_geom_gist ON prov_admin1_ne USING gist (geom);


--
-- Name: jan14_edits; Type: ACL; Schema: public; Owner: ne2a3_editor
--

REVOKE ALL ON TABLE jan14_edits FROM PUBLIC;
REVOKE ALL ON TABLE jan14_edits FROM ne2a3_editor;
GRANT ALL ON TABLE jan14_edits TO ne2a3_editor;
GRANT INSERT ON TABLE jan14_edits TO ne2_edit;


--
-- Name: jan14_edits_primary_key_seq; Type: ACL; Schema: public; Owner: ne2a3_editor
--

REVOKE ALL ON SEQUENCE jan14_edits_primary_key_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE jan14_edits_primary_key_seq FROM ne2a3_editor;
GRANT ALL ON SEQUENCE jan14_edits_primary_key_seq TO ne2a3_editor;
GRANT USAGE ON SEQUENCE jan14_edits_primary_key_seq TO ne2_edit;


--
-- Name: jan14_web; Type: ACL; Schema: public; Owner: ne2a3_editor
--

REVOKE ALL ON TABLE jan14_web FROM PUBLIC;
REVOKE ALL ON TABLE jan14_web FROM ne2a3_editor;
GRANT ALL ON TABLE jan14_web TO ne2a3_editor;
GRANT SELECT ON TABLE jan14_web TO ne2_edit;


--
-- Name: jan14_main_view; Type: ACL; Schema: public; Owner: ne2a3_editor
--

REVOKE ALL ON TABLE jan14_main_view FROM PUBLIC;
REVOKE ALL ON TABLE jan14_main_view FROM ne2a3_editor;
GRANT ALL ON TABLE jan14_main_view TO ne2a3_editor;
GRANT SELECT ON TABLE jan14_main_view TO ne2_edit;


--
-- Name: ne_10m_admin_1_states_provinces_shp; Type: ACL; Schema: public; Owner: ne2a3_editor
--

REVOKE ALL ON TABLE ne_10m_admin_1_states_provinces_shp FROM PUBLIC;
REVOKE ALL ON TABLE ne_10m_admin_1_states_provinces_shp FROM ne2a3_editor;
GRANT ALL ON TABLE ne_10m_admin_1_states_provinces_shp TO ne2a3_editor;
GRANT SELECT ON TABLE ne_10m_admin_1_states_provinces_shp TO ne2_edit;


--
-- Name: prov_admin1_ne; Type: ACL; Schema: public; Owner: ne2a3_editor
--

REVOKE ALL ON TABLE prov_admin1_ne FROM PUBLIC;
REVOKE ALL ON TABLE prov_admin1_ne FROM ne2a3_editor;
GRANT ALL ON TABLE prov_admin1_ne TO ne2a3_editor;
GRANT SELECT ON TABLE prov_admin1_ne TO ne2_edit;


--
-- PostgreSQL database dump complete
--

