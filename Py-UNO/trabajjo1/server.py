from flask import Flask, request, Response, send_from_directory
import requests
import os

# Nexus Infrastructure - Python Gateway v3.0
app = Flask(__name__, static_folder='.', static_url_path='')

TARGET_URL = "https://restful-booker.herokuapp.com"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/proxy/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def proxy(path):
    # Preflight handling
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()

    url = f"{TARGET_URL}/{path}"
    
    # Headers preparation
    headers = {k: v for k, v in request.headers if k.lower() != 'host'}
    
    # Auth Logic Tunneling
    auth_header = request.headers.get('Authorization')
    custom_token = request.headers.get('X-Auth-Token')
    
    if custom_token or (auth_header and 'Bearer' in auth_header):
        token = custom_token if custom_token else auth_header.replace('Bearer ', '')
        headers['Cookie'] = f"token={token}"
    elif auth_header and 'Basic' in auth_header:
        headers['Authorization'] = auth_header
    else:
        # QA Fallback Credentials
        headers['Authorization'] = 'Basic YWRtaW46cGFzc3dvcmQxMjM='

    # Mandatory format headers
    headers['Accept'] = 'application/json'
    if request.method in ['POST', 'PUT', 'PATCH']:
        headers['Content-Type'] = 'application/json'

    # Execute request
    try:
        resp = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        
        # Build response
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]
        
        response = Response(resp.content, resp.status_code, headers)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['X-Powered-By'] = 'Nexus-Python-Gateway'
        return response
    except Exception as e:
        return Response(str(e), 502)

def _build_cors_prelight_response():
    response = Response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Auth-Token, Accept'
    return response

if __name__ == '__main__':
    print("""
    \x1b[36m┌────────────────────────────────────────────────────────┐
    │  \x1b[1mNEXUS INFRASTRUCTURE - PYTHON CORE v3.0\x1b[0m\x1b[36m               │
    ├────────────────────────────────────────────────────────┤
    │  \x1b[32mSTATUS: CERTIFIED Python Environment\x1b[0m\x1b[36m                  │
    │  \x1b[34mPORT: 5000\x1b[0m\x1b[36m                                            │
    │  \x1b[34mPROXY: ENABLED (Flask Gateway)\x1b[0m\x1b[36m                       │
    │  \x1b[34mMODE: ACADEMIC OPTIMIZED\x1b[0m\x1b[36m                             │
    └────────────────────────────────────────────────────────┘\x1b[0m
    """)
    app.run(port=5000, debug=True)

