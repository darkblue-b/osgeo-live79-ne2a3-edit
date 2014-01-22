

def application(environ, start_response):
    status = '200 OK'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', '51200' )]
    start_response(status, response_headers)
    outStr = ''
    return [ outStr.zfill(50*1024) ]

