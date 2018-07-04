import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }



from flaskapp import app as application
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    #host_name = os.environ['OPENSHIFT_GEAR_DNS']
    httpd = make_server(ip, 8000, application)
    #httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
    #httpd.serve_forever()