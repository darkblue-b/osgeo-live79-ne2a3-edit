## tiny werkzeug data adaptor
##  12jan14 -dbb  GPLv2+


import os
import sys, pdb, time
import re, simplejson, psycopg2
import werkzeug
from textwrap import wrap
from werkzeug.wrappers import BaseRequest as Request, BaseResponse as Response
from werkzeug.utils import escape

##----------------------------------------------------------------------------
## add this line to your httpd.conf or equivalent
##  WSGIScriptAlias /ne2a3_werkzeug /path/to/wsgi_local_test/werkzeug_mini.wsgi
##

##  G L O B A L S

gDSN = "dbname=ne2_svn user=ne2_edit password=ne2_edit host=localhost"


##----------------------------------------------------------------------------
## example: a png werkzeug logo as data, wrapped in a Response object
##

logo = Response('''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
='''.decode('base64'), mimetype='image/png')


gVersStr = '''
    werkzeug_mini data adaptor for natural_earth2a3 - vers 0.1
'''

gInfoPage = '''
<html> <head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<title>werkzeug_mini data adaptor for natural_earth2a3</title>
</head>
<body>
<h3>werkzeug_mini data adaptor for natural_earth2a3</h3>
heck - use this service to get data, not web pages<br>
<br>
<b>POST EDITs:</b><br>
POST http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/1   { ... json data here ... } <br>
<br>
<br>
<b>GET Data</b> <br>
<br>
GET http://host/ne2a3_werkzeug/<em>dataset_name</em> <br>
<br>
&nbsp;&nbsp;ne2a3_jan14_admin1<br>
<br>
&nbsp;&nbsp;ne2a3_jan14_defs<br>
<br>
&nbsp;&nbsp;ne2a3_jan14_mainlist <br>
<br>
&nbsp;&nbsp;ne2a3_jan14_mlist_defs <br>
<br>
&nbsp;&nbsp;unc_compare_iso2 <br>
<br>
&nbsp;&nbsp;unc_compare_defs <br>
<br>
<b>Use Patterns</b><br>
GET host/ne2a3_werkzeug/ne2a3_jan14_mainlist<br>
A short index record for each admin1 <br>
<pre>[ adm1_code, name, admin, latitude, longitude, pkey ]</pre>
<br>
available as a complete set of 4000+, <br>
 or selected by one of six predefined regions<br>
<pre>[ north_america, south_america, eu_plus, au_plus, india_plus, africa_plus ]</pre>
<br>
display to the user, note pkey<br>
GET full record by appending /pkey to the full record URL<br>
<br>
<em> to get a record by index:</em> <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/1  <br>
<br>
<em>also available as CSV:</em> <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1.csv  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/1.csv  <br>
<br>
<em>get an index set by edit_area:</em> <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_mainlist/north_america  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_mainlist/south_america  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_mainlist/africa_plus  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_mainlist/eu_plus  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_mainlist/au_plus  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_mainlist/india_plus  <br>
<br>
<em>get a full record set by edit_area: (unused)</em> <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/north_america  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/south_america  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/africa_plus  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/eu_plus  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/au_plus  <br>
GET http://host/ne2a3_werkzeug/ne2a3_jan14_admin1/india_plus  <br>
<br>
<br>
<br>
</body>
</html>
'''

tInit_edits_table = '''
drop table if exists jan14_edits cascade;
create table jan14_edits as
select 
pkey as rec_pkey, name, name_alt, name_local, abbrev, type, type_en, latitude, longitude,
wikipedia, area_sqkm, note, code_local, code_hasc, postal, fips, fips_alt,
iso_3166_2, iso_a2, adm0_sr, provnum_ne, gadm_level, region_cod, region,
woe_id, woe_label, woe_name, sov_a3, adm0_a3, adm0_label, admin, adm1_code,
gns_id, gns_name, gns_level, gns_lang, gns_adm1, gns_region, geonunit, gu_a3,
gn_id, gn_name, gn_level, gn_region, gn_a1_code, region_sub, sub_code

from 
jan14_web ;
truncate jan14_edits;

alter table jan14_edits add column edit_time timestamp;
alter table jan14_edits add column ip_addr inet;
alter table jan14_edits add column primary_key serial;
alter table jan14_edits add PRIMARY KEY (primary_key);
'''

gGetMainTable_SQL = '''
SELECT 
pkey, name, name_alt, name_local, abbrev, type, type_en, latitude, longitude,
wikipedia, area_sqkm, note, code_local, code_hasc, postal, fips, fips_alt,
iso_3166_2, iso_a2, adm0_sr, provnum_ne, gadm_level, region_cod, region,
woe_id, woe_label, woe_name, sov_a3, adm0_a3, adm0_label, admin, adm1_code,
gns_id, gns_name, gns_level, gns_lang, gns_adm1, gns_region, geonunit, gu_a3,
gn_id, gn_name, gn_level, gn_region, gn_a1_code, region_sub, sub_code

FROM jan14_web
WHERE {0}
ORDER BY pkey
'''


tUnc_compare_defs = '''
                         View "public.unc_compare_iso2"
      Column       |          Type          | Modifiers 
-------------------+------------------------+-----------
 iso_a2            | character varying(2)   | 
 ne2a3_name        | character varying(100) | 
 iso_3166_2        | character varying(10)  | 
 adm1_code         | character varying(10)  | 
 unc_iso_2         | text                   | 
 unc_iso_3         | text                   | 
 unc_iana_internet | text                   | 
 ne2a3_admin       | character varying(200) | 

'''


tMainlist_pg_defs = '''
         View "public.jan14_main_view"
   Column  |         Type           | Modifiers 
-----------+------------------------+-----------
 adm1_code | character varying(10)  | 
 name      | character varying(100) | 
 admin     | character varying(200) | 
 latitude  | numeric                | 
 longitude | numeric                | 
 pkey      | integer                | 
'''


tAdmin1_pg_defs = '''
Table "public.jan14_web"

   Column   |          Type          |    Modifiers     
------------+------------------------+-----------------
 adm1_code  | character varying(10)  | 
 shape_leng | numeric                | 
 shape_area | numeric                | 
 diss_me    | double precision       | 
 iso_3166_2 | character varying(10)  | 
 wikipedia  | character varying(254) | 
 iso_a2     | character varying(2)   | 
 adm0_sr    | integer                | 
 name       | character varying(100) | 
 name_alt   | character varying(200) | 
 name_local | character varying(200) | 
 type       | character varying(100) | 
 type_en    | character varying(100) | 
 code_local | character varying(50)  | 
 code_hasc  | character varying(10)  | 
 note       | character varying(254) | 
 hasc_maybe | character varying(50)  | 
 region     | character varying(100) | 
 region_cod | character varying(50)  | 
 provnum_ne | double precision       | 
 gadm_level | integer                | 
 check_me   | integer                | 
 scalerank  | integer                | 
 datarank   | integer                | 
 abbrev     | character varying(10)  | 
 postal     | character varying(10)  | 
 area_sqkm  | numeric                | 
 sameascity | integer                | 
 labelrank  | integer                | 
 featurecla | character varying(50)  | 
 name_len   | double precision       | 
 mapcolor9  | integer                | 
 mapcolor13 | integer                | 
 fips       | character varying(5)   |
 fips_alt   | character varying(50)  | 
 woe_id     | double precision       | 
 woe_label  | character varying(250) | 
 woe_name   | character varying(100) | 
 latitude   | numeric                | 
 longitude  | numeric                | 
 sov_a3     | character varying(3)   | 
 adm0_a3    | character varying(3)   | 
 adm0_label | integer                | 
 admin      | character varying(200) | 
 geonunit   | character varying(200) | 
 gu_a3      | character varying(3)   | 
 gn_id      | double precision       | 
 gn_name    | character varying(200) | 
 gns_id     | double precision       | 
 gns_name   | character varying(200) | 
 gn_level   | integer                | 
 gn_region  | character varying(50)  | 
 gn_a1_code | character varying(10)  | 
 region_sub | character varying(250) | 
 sub_code   | character varying(10)  | 
 gns_level  | integer                | 
 gns_lang   | character varying(10)  | 
 gns_adm1   | character varying(10)  | 
 gns_region | character varying(10)  | 
 pkey       | integer                |
'''

##-------------------------------------
def get_ne2a3_jan14_mainlist_TA( inSel ):
  ''' handle any request for fixed data set ne2a3_jan14_admin1
       be sure to ORDER BY, because the web retrieval is index based
  '''

  try:
    tConn = psycopg2.connect( gDSN )
    tCurs = tConn.cursor()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, tCurs)
  except Exception, E:
    return u''

  ##-- Hack - clean up later
  tSelSQL = 'true '
  if ( re.match( 'north_america', inSel ) ):
        tSelSQL = 'latitude > 12 and latitude < 90 and longitude > -160 and longitude < -56 '
  elif ( re.match( 'south_america', inSel ) ):
        tSelSQL = 'latitude <= 12 and latitude > -90 and longitude > -160 and longitude < -26 '
  elif ( re.match( 'africa_plus', inSel ) ):
        tSelSQL = 'latitude < 37 and latitude < 90 and longitude >= -26 and longitude < 60 '
  elif ( re.match( 'eu_plus', inSel ) ):
        tSelSQL = 'latitude >= 37 and latitude < 90 and longitude >= -26 and longitude < 60 '
  elif ( re.match( 'au_plus', inSel ) ):
        tSelSQL = 'latitude < 5 and latitude > -90 and longitude >= 60 and longitude < 180 '
  elif ( re.match( 'india_plus', inSel ) ):
        tSelSQL = 'latitude >= 5 and latitude < 90 and longitude >= 60 and longitude < 180 '
  else:
        tSelSQL = 'true '

  ##-- the VIEW supplies the ORDER BY
  tSQL = 'select * from jan14_main_view WHERE {0}'
  tRes = tCurs.execute( tSQL.format( tSelSQL ) )
  tResTA = tCurs.fetchall()
  tConn.close()

  return tResTA


##-------------------------------------
def get_ne2a3_jan14_admin1_TA( inSel ):
  ''' handle any request for fixed data set ne2a3_jan14_admin1
       be sure to ORDER BY, because the web retrieval is index based
      the jan14_web database is the reference that wont change
      the jan14_edits is the changing one..
  '''

  ##--
  ##  grant insert on table jan14_edits to ne2_edit;
  ##  grant select on table jan14_web to ne2_edit;
  ##  grant select on all tables in schema public to ne2_edit;
  ##  grant USAGE on jan14_edits_primary_key_seq to ne2_edit ;
  ##
  #from dbgp.client import brk
  #brk( host="salvia.local", port=62170 )

  try:
    tConn = psycopg2.connect( gDSN )
    tCurs = tConn.cursor()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, tCurs)
  except Exception, E:
    return u''

  ##-- Hack - clean up later
  if ( re.match( 'north_america', inSel ) ):
        tSelSQL = 'latitude > 12 and latitude < 90 and longitude > -160 and longitude < -56 '
  elif ( re.match( 'south_america', inSel ) ):
        tSelSQL = 'latitude <= 12 and latitude > -90 and longitude > -160 and longitude < -26 '
  elif ( re.match( 'africa_plus', inSel ) ):
        tSelSQL = 'latitude < 37 and latitude < 90 and longitude >= -26 and longitude < 60 '
  elif ( re.match( 'eu_plus', inSel ) ):
        tSelSQL = 'latitude >= 37 and latitude < 90 and longitude >= -26 and longitude < 60 '
  elif ( re.match( 'au_plus', inSel ) ):
        tSelSQL = 'latitude < 5 and latitude > -90 and longitude >= 60 and longitude < 180 '
  elif ( re.match( 'india_plus', inSel ) ):
        tSelSQL = 'latitude >= 5 and latitude < 90 and longitude >= 60 and longitude < 180 '
  else:
        tSelSQL = 'true '
  tRes = tCurs.execute( gGetMainTable_SQL.format(tSelSQL)  )
  tResTA = tCurs.fetchall()
  
  ##-- the real set of column names returned is in
  ##      curs.description[n].name
  ##-- a tuple of Column objects with attribute name

  tConn.close()

  return tResTA


##-------------------------------------
def get_unc_compare_iso2_TA():
  ''' handle any request for fixed data set unc_compare_iso2
       be sure to ORDER BY, because the web retrieval is index based
  '''

  try:
    tConn = psycopg2.connect( gDSN )
    tCurs = tConn.cursor()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, tCurs)
  except Exception, E:
    return u''
  
  tSQL = 'select * from unc_compare_iso2 order by iso_a2,ne2a3_name'
  tRes = tCurs.execute( tSQL )
  tResTA = tCurs.fetchall()
  tConn.close()

  return tResTA


##-------------------------------------
def do_TA_to_json( inTA ):

  tResData = u''
  if inTA == '' or inTA is None:
    return tResData

  ##-- json level  
  try:
      tResData = simplejson.dumps( inTA, ensure_ascii=False)
  except Exception, E:
      tResData = u''  

  return tResData


##-------------------------------------
def do_TA_to_csv( inTA ):

  #pdb.set_trace()

  tFormat = 'JSON'
  tResData = u''
  if inTA == '' or inTA is None:
    return tResData

  for tRow in inTA:
      for tCol in tRow:
        tResData += unicode(tCol)
        tResData += u'\t'
        tResData += u'\t'

  ##-- done
  return tResData


##------------------------------------------------------------------------------
##-- HACK the same list of fields as occurs in the client.. 
##--   (must match)
##
gFldsA = ["pkey", "name", "name_alt", "name_local", "abbrev", "type", "type_en", 
"latitude", "longitude", "wikipedia", "area_sqkm", "note", "code_local", 
"code_hasc", "postal", "fips", "fips_alt", "iso_3166_2", "iso_a2", "adm0_sr", 
"provnum_ne", "gadm_level", "region_cod", "region", 
"woe_id", "woe_label", "woe_name", "sov_a3", "adm0_a3", "adm0_label", "admin", "adm1_code", 
"gns_id", "gns_name", "gns_level", "gns_lang", "gns_adm1", "gns_region", 
"geonunit", "gu_a3", "gn_id", "gn_name", "gn_level", "gn_region", "gn_a1_code", 
"region_sub", "sub_code" ]

gInsertSQL = '''
INSERT into jan14_edits (
  rec_{0},
edit_time, ip_addr  )
VALUES 
( {1}  %s,%s );
'''

def do_main_POST( req, environ ):

    from dbgp.client import brk
    #brk( host="salvia.local", port=53385 )
    
    #tReq = req
    #tEnv = environ
    
    respD = {}
    insA = []
    insA2 = []

    for tName in gFldsA:
      tVal = req.values.get( tName )
      if tVal is None:
        continue
      respD[ tName ] = tVal

    if len(respD) == 0:
      response = Response( 'POST failed for ne2a3_jan14_admin1: no defined fields', mimetype='text/plain;charset=utf-8' )
      return response
    
    try:
      tConn = psycopg2.connect( gDSN )
      tCurs = tConn.cursor()
      psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, tCurs)
    except Exception, E:
      tStr = str(E)
      response = Response( 'POST failed for ne2a3_jan14_admin1: '+tStr, mimetype='text/plain;charset=utf-8' )
      return response
  
    tF1 = ','.join( respD )
    tF2 = '%s, '*len(respD)
    
    #tRecord_pkey = 2000  ## FIXME get the record pkey
    #insA.append(  tRecord_pkey )
    
    [ insA.append( tVal ) for tVal in respD.values() ]
    insA.append( time.asctime() )
    insA.append(  environ.get( 'REMOTE_ADDR' ) )
    
    ## *sigh* handle pkey as special
    ##-- bug, this can crash ?!

    try:
        insA2.append( int(insA[0] ))
        
    except Exception, E:
        brk( host="salvia.local", port=53385 )
        response = Response( 'POST failed for ne2a3_jan14_admin1: bad pkey {0}'.format(insA[0]), mimetype='text/plain;charset=utf-8' )
        return response


    for tInd in range( len( insA ) - 1 ):
        insA2.append( insA[ tInd+1 ] )

    tSQL = gInsertSQL.format( tF1, tF2 )
    
    try:
      tRes = tCurs.execute( tSQL, insA2 )
      tConn.commit()
      tConn.close()
    except Exception, E:
      tStr = str(E)
      response = Response( 'POST failed for ne2a3_jan14_admin1: '+tStr, mimetype='text/plain;charset=utf-8' )
      return response

    
    ##-----------------------------
    response = Response( 'POST received for ne2a3_jan14_admin1 from '+ str(environ.get( 'REMOTE_ADDR' )), mimetype='text/plain;charset=utf-8' )
    return response


##---------------------------------------
def application(environ, start_response):
    """ WSGI application 
          interface to ne2_svn postgres database
    """
    req = Request(environ, populate_request=False)
    path_info = environ.get('PATH_INFO')

    ##-- standard Array-of-Tuple (TA) as content
    ##-- its name is tDataTag (could make an object, no big deal)
    tResTA = None
    tDataTag = None    

    #from dbgp.client import brk
    #brk( host="salvia.local", port=62170 )
    
    ##-- POST verbs here -------------------------
    ##-----------------------------------------------    
    tHttpVerb = environ.get( 'REQUEST_METHOD' ) 
    if tHttpVerb == 'POST':
        ##-- currently, POST only supported for one dataset
        if re.match( '^/ne2a3_jan14_admin1', path_info ) is None:
            response = Response( 'POST only supported for ne2a3_jan14_admin1', mimetype='text/plain;charset=utf-8' )
            return response(environ, start_response)
        
        ##-- handle POST to main edit set
        #tStream = req.stream
        response = do_main_POST( req, environ )
        return response(environ, start_response)


    ##-- GET verbs here -------------------------
    ##-----------------------------------------------    
    ##-- http://localhost/ne2a3_werkzeug/?resource=logo
    if req.args.get('resource') == 'logo':
        response = logo
        return response(environ, start_response)

    elif ( re.match( '^/version', path_info )):

        response = Response( gVersStr, mimetype='text/plain;charset=utf-8' )
        return response(environ, start_response)

    elif ( re.match( '^/ne2a3_jan14_admin1', path_info )):

      #pdb.set_trace()
      tSel = 'all'
      ## hack - clean up later
      if ( re.match( '^/ne2a3_jan14_admin1/north_america', path_info ) ):
        tSel = 'north_america'
      elif ( re.match( '^/ne2a3_jan14_admin1/south_america', path_info ) ):
        tSel = 'south_america'
      elif ( re.match( '^/ne2a3_jan14_admin1/africa_plus', path_info ) ):
        tSel = 'africa_plus'
      elif ( re.match( '^/ne2a3_jan14_admin1/eu_plus', path_info ) ):
        tSel = 'eu_plus'
      elif ( re.match( '^/ne2a3_jan14_admin1/au_plus', path_info ) ):
        tSel = 'au_plus'
      elif ( re.match( '^/ne2a3_jan14_admin1/india_plus', path_info ) ):
        tSel = 'india_plus'
      
      tResTA = get_ne2a3_jan14_admin1_TA( tSel )
      tDataTag = 'ne2a3_jan14_admin1'


    elif ( re.match( '^/ne2a3_jan14_defs', path_info )):
        ##-- defs
        response = Response( tAdmin1_pg_defs, mimetype='text/plain;charset=utf-8')
        return response(environ, start_response)
 

    elif ( re.match( '^/ne2a3_jan14_mainlist', path_info )):

      #pdb.set_trace()
      tSel = 'all'
      ## hack - clean up later
      if ( re.match( '^/ne2a3_jan14_mainlist/north_america', path_info ) ):
        tSel = 'north_america'
      elif ( re.match( '^/ne2a3_jan14_mainlist/south_america', path_info ) ):
        tSel = 'south_america'
      elif ( re.match( '^/ne2a3_jan14_mainlist/africa_plus', path_info ) ):
        tSel = 'africa_plus'
      elif ( re.match( '^/ne2a3_jan14_mainlist/eu_plus', path_info ) ):
        tSel = 'eu_plus'
      elif ( re.match( '^/ne2a3_jan14_mainlist/au_plus', path_info ) ):
        tSel = 'au_plus'
      elif ( re.match( '^/ne2a3_jan14_mainlist/india_plus', path_info ) ):
        tSel = 'india_plus'
      
      tResTA = get_ne2a3_jan14_mainlist_TA( tSel )
      tDataTag = 'ne2a3_jan14_mainlist'


    elif ( re.match( '^/ne2a3_jan14_mlist_defs', path_info )):
        ##-- defs
        response = Response( tMainlist_pg_defs, mimetype='text/plain;charset=utf-8')
        return response(environ, start_response)
 
 
    elif ( re.match( '^/unc_compare_iso2', path_info )):

      #pdb.set_trace()
      tResTA = get_unc_compare_iso2_TA()
      tDataTag = 'unc_compare_iso2'


    elif ( re.match( '^/unc_compare_defs', path_info )):
        ##-- defs
        response = Response( tUnc_compare_defs, mimetype='text/plain;charset=utf-8')
        return response(environ, start_response)
 

    else:
        ##-- serve a --help page if nothing else matches...
        #response = Response( gInfoPage.format(gVersStr), mimetype='text/html')
        response = Response( gInfoPage, mimetype='text/html')
        return response(environ, start_response)


    ##== is this an ask for one record?
    #pdb.set_trace()
    tMatch = re.search( tDataTag + r'/([0-9]+)', path_info)
    if tMatch is not None:
      tInd = tMatch.groups()[0]
      tInd = int(tInd)
      try:
        tRes2 = tResTA[ tInd-1 ]
        tResTA = [ tRes2 ]
      except:
        tResTA = None    

    ##=== now, take a suffix for return type, encode and send

    ## path_info.endswith('csv')  might be simpler
    ## re.match only looks at the START of a STRING :-/
    if re.search( 'csv$', path_info) is not None:

      tResData = do_TA_to_csv( tResTA )
      response = Response( tResData, mimetype='text/csv' )

    elif re.search( 'xml$', path_info) is not None:
      ## lxml FAQ http://lxml.de/FAQ.html#why-can-t-lxml-parse-my-xml-from-unicode-strings
      tResData = u''
      response = Response( tResData, mimetype='application/xml' )

    else:
      #pdb.set_trace()
      tResData = do_TA_to_json( tResTA )
      response = Response( tResData, mimetype='application/json; charset=utf-8' )

    ##-- all done 
    return response(environ, start_response)


if __name__ == '__main__':
    
    gHost = 'localhost'
    if len(sys.argv) > 1:
      if sys.argv[1] is not None and re.match( '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', sys.argv[1] ):
        gHost = sys.argv[1]
    from werkzeug.serving import run_simple
    run_simple( gHost, 5000, test_app, use_reloader=True)

