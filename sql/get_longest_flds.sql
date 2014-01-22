SELECT 

(select adm1_code from jan14_web where adm1_code is not Null order by length(adm1_code) desc limit 1) as adm1_code,

(select iso_3166_2 from jan14_web where iso_3166_2 is not Null order by length(iso_3166_2) desc limit 1) as iso_3166_2,
(select wikipedia from jan14_web where wikipedia is not Null order by length(wikipedia) desc limit 1) as wikipedia,
(select iso_a2 from jan14_web where iso_a2 is not Null order by length(iso_a2) desc limit 1) as iso_a2,

(select name from jan14_web where name is not Null order by length(name) desc limit 1) as name,
(select name_alt from jan14_web where name_alt is not Null order by length(name_alt) desc limit 1) as name_alt,
(select name_local from jan14_web where name_local is not Null order by length(name_local) desc limit 1) as name_local,
(select type from jan14_web where type is not Null order by length(type) desc limit 1) as type,
(select type_en from jan14_web where type_en is not Null order by length(type_en) desc limit 1) as type_en,
(select code_local from jan14_web where code_local is not Null order by length(code_local) desc limit 1) as code_local,
(select code_hasc from jan14_web where code_hasc is not Null order by length(code_hasc) desc limit 1) as code_hasc,
(select note from jan14_web where note is not Null order by length(note) desc limit 1) as note,
(select hasc_maybe from jan14_web where hasc_maybe is not Null order by length(hasc_maybe) desc limit 1) as hasc_maybe,
(select region from jan14_web where region is not Null order by length(region) desc limit 1) as region,
(select region_cod from jan14_web where region_cod is not Null order by length(region_cod) desc limit 1) as region_cod,

(select abbrev from jan14_web where abbrev is not Null order by length(abbrev) desc limit 1) as abbrev,
(select postal from jan14_web where postal is not Null order by length(postal) desc limit 1) as postal,

(select featurecla from jan14_web where featurecla is not Null order by length(featurecla) desc limit 1) as featurecla,

(select fips from jan14_web where fips is not Null order by length(fips) desc limit 1) as fips,
(select fips_alt from jan14_web where fips_alt is not Null order by length(fips_alt) desc limit 1) as fips_alt,

(select woe_label from jan14_web where woe_label is not Null order by length(woe_label) desc limit 1) as woe_label,
(select woe_name from jan14_web where woe_name is not Null order by length(woe_name) desc limit 1) as woe_name,

(select sov_a3 from jan14_web where sov_a3 is not Null order by length(sov_a3) desc limit 1) as sov_a3,
(select adm0_a3 from jan14_web where adm0_a3 is not Null order by length(adm0_a3) desc limit 1) as adm0_a3,

(select admin from jan14_web where admin is not Null order by length(admin) desc limit 1) as admin,
(select geonunit from jan14_web where geonunit is not Null order by length(geonunit) desc limit 1) as geonunit,
(select gu_a3 from jan14_web where gu_a3 is not Null order by length(gu_a3) desc limit 1) as gu_a3,

(select gn_name from jan14_web where gn_name is not Null order by length(gn_name) desc limit 1) as gn_name,

(select gns_name from jan14_web where gns_name is not Null order by length(gns_name) desc limit 1) as gns_name,

(select gn_region from jan14_web where gn_region is not Null order by length(gn_region) desc limit 1) as gn_region,
(select gn_a1_code from jan14_web where gn_a1_code is not Null order by length(gn_a1_code) desc limit 1) as gn_a1_code,
(select region_sub from jan14_web where region_sub is not Null order by length(region_sub) desc limit 1) as region_sub,
(select sub_code from jan14_web where sub_code is not Null order by length(sub_code) desc limit 1) as sub_code,

(select gns_lang from jan14_web where gns_lang is not Null order by length(gns_lang) desc limit 1) as gns_lang,
(select gns_adm1 from jan14_web where gns_adm1 is not Null order by length(gns_adm1) desc limit 1) as gns_adm1,
(select gns_adm1 from jan14_web where gns_region is not Null order by length(gns_region) desc limit 1) as gns_region


FROM 
  jan14_web

LIMIT 1;
