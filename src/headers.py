from . import app


@app.after_request
def add_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'origin'
    response.headers['Content-Security-Policy'] = "script-src 'self'; img-src 'self' data:;"
    if app.debug:
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        response.headers['Access-Control-Allow-Headers'] = 'content-type'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response
