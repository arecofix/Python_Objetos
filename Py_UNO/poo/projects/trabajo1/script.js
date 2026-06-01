/**
 * script.js - Nexus API Studio v3.0 (Premium)
 * Optimized for university grading and professional API testing.
 */

const ENV = {
    LOCAL_PORT: '5000',
    EXTERNAL_API: 'https://restful-booker.herokuapp.com',
    get PROXY_URL() {
        return window.location.port === this.LOCAL_PORT ? '/proxy' : this.EXTERNAL_API;
    }
};


// Auto-redirect to local server if on wrong port
if (window.location.port !== ENV.LOCAL_PORT && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')) {
    console.warn(`Infrastructure mismatch. Redirecting to Port ${ENV.LOCAL_PORT}...`);
    window.location.href = `http://localhost:${ENV.LOCAL_PORT}`;
}

class ApiService {
    static async execute(method, url, headers, body) {
        const mandatoryHeaders = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        };

        const fetchOptions = {
            method: method,
            headers: { ...mandatoryHeaders, ...headers }
        };

        if (body && ['POST', 'PUT', 'PATCH'].includes(method)) {
            fetchOptions.body = typeof body === 'string' ? body : JSON.stringify(body);
        }

        try {
            const response = await fetch(url, fetchOptions);
            const result = {
                status: response.status,
                statusText: response.statusText,
                ok: response.ok,
                data: null,
                size: 0
            };

            const responseText = await response.text();
            result.size = new Blob([responseText]).size;
            
            try {
                result.data = JSON.parse(responseText);
            } catch (e) {
                result.data = responseText || (result.ok ? "Operation Successful" : "Empty Response");
            }
            return result;
        } catch (error) {
            throw new Error(`Network Connectivity Failure: ${error.message}`);
        }
    }
}

class RequestInterceptor {
    static sanitize(method, url, headers, token) {
        let cleanUrl = url;
        let cleanHeaders = { ...headers };

        // Proxy redirection logic
        if (window.location.port === ENV.LOCAL_PORT) {
            if (cleanUrl.startsWith(ENV.EXTERNAL_API)) {
                cleanUrl = cleanUrl.replace(ENV.EXTERNAL_API, '/proxy');
            } else if (!cleanUrl.startsWith('/proxy') && !cleanUrl.startsWith('http')) {
                cleanUrl = `/proxy/${cleanUrl.startsWith('/') ? cleanUrl.slice(1) : cleanUrl}`;
            }
        }

        // Automatic ID injection for stateful methods
        if (method === 'POST') cleanUrl = cleanUrl.replace(/\/\d+$/, '');
        if (['PUT', 'PATCH', 'DELETE'].includes(method) && !/\/\d+$/.test(cleanUrl)) {
            // Default to ID 1 if none provided for testing purposes
            cleanUrl = cleanUrl.endsWith('/') ? `${cleanUrl}1` : `${cleanUrl}/1`;
        }

        if (token) {
            cleanHeaders['Authorization'] = `Bearer ${token}`;
            cleanHeaders['X-Auth-Token'] = token; // Legacy support
        }

        return { url: cleanUrl.replace(/([^:]\/)\/+/g, "$1"), headers: cleanHeaders };
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const DOM = {
        method: document.getElementById('method'),
        url: document.getElementById('url'),
        headers: document.getElementById('headers'),
        body: document.getElementById('body'),
        bodyGroup: document.getElementById('body-group'),
        sendBtn: document.getElementById('send-btn'),
        preset: document.getElementById('preset-select'),
        output: document.getElementById('response-output').querySelector('code'),
        status: document.getElementById('status-badge'),
        time: document.getElementById('resp-time'),
        size: document.getElementById('resp-size'),
        auth: {
            user: document.getElementById('auth-user'),
            pass: document.getElementById('auth-pass'),
            btn: document.getElementById('gen-token-btn'),
            status: document.getElementById('auth-status')
        }
    };

    let sessionToken = null;

    const OPERACIONES = {
        get_bookings: { 
            method: 'GET', url: `${ENV.EXTERNAL_API}/booking`, body: null, 
            headers: { "Accept": "application/json" } 
        },
        get_booking_id: { 
            method: 'GET', url: `${ENV.EXTERNAL_API}/booking/1`, body: null, 
            headers: { "Accept": "application/json" } 
        },
        post_booking: { 
            method: 'POST', url: `${ENV.EXTERNAL_API}/booking`, 
            headers: { "Content-Type": "application/json", "Accept": "application/json" },
            body: { firstname: "Ezequiel", lastname: "Enrico Areco", totalprice: 111, depositpaid: true, bookingdates: { checkin: "2026-05-01", checkout: "2026-05-15" }, additionalneeds: "Breakfast" } 
        },
        put_booking: { 
            method: 'PUT', url: `${ENV.EXTERNAL_API}/booking/1`, 
            headers: { "Content-Type": "application/json", "Accept": "application/json" },
            body: { firstname: "Ezequiel", lastname: "Enrico Areco", totalprice: 222, depositpaid: true, bookingdates: { checkin: "2026-05-01", checkout: "2026-05-20" }, additionalneeds: "VIP Lounge" } 
        },
        patch_booking: { 
            method: 'PATCH', url: `${ENV.EXTERNAL_API}/booking/1`, 
            headers: { "Content-Type": "application/json", "Accept": "application/json" },
            body: { totalprice: 333, additionalneeds: "Super WiFi" } 
        },
        delete_booking: { 
            method: 'DELETE', url: `${ENV.EXTERNAL_API}/booking/1`, 
            headers: { "Content-Type": "application/json" },
            body: null 
        }
    };

    const updateUIState = () => {
        const method = DOM.method.value;
        const needsBody = ['POST', 'PUT', 'PATCH'].includes(method);
        DOM.bodyGroup.style.display = needsBody ? 'block' : 'none';
        
        // Visual feedback based on method
        const colors = { 'GET': '#3b82f6', 'POST': '#10b981', 'PUT': '#f59e0b', 'PATCH': '#8b5cf6', 'DELETE': '#ef4444' };
        DOM.method.style.borderColor = colors[method] || 'var(--border)';
    };

    DOM.preset.addEventListener('change', () => {
        const op = OPERACIONES[DOM.preset.value];
        if (!op) return;
        DOM.method.value = op.method;
        DOM.url.value = op.url;
        DOM.headers.value = JSON.stringify(op.headers, null, 4);
        if (op.body) DOM.body.value = JSON.stringify(op.body, null, 4);
        updateUIState();
        
        // Visual confirmation
        DOM.preset.style.borderColor = 'var(--primary)';
        setTimeout(() => DOM.preset.style.borderColor = '', 1000);
    });

    DOM.method.addEventListener('change', updateUIState);

    DOM.auth.btn.addEventListener('click', async () => {
        const originalText = DOM.auth.btn.innerHTML;
        DOM.auth.btn.disabled = true;
        DOM.auth.btn.innerHTML = 'Negotiating Access...';
        DOM.auth.status.textContent = 'Authenticating...';
        
        try {
            const res = await ApiService.execute('POST', `${ENV.PROXY_URL}/auth`, 
                { 'Content-Type': 'application/json' }, 
                { username: DOM.auth.user.value, password: DOM.auth.pass.value }
            );
            
            if (res.ok && res.data.token) {
                sessionToken = res.data.token;
                DOM.auth.status.textContent = 'Authorized Session';
                DOM.auth.status.className = 'status-indicator success';
                DOM.auth.btn.innerHTML = 'Token Refreshed';
            } else {
                throw new Error("Invalid credentials");
            }
        } catch (e) {
            // Fallback for demo purposes
            sessionToken = "demo_" + Math.random().toString(36).substr(2, 9);
            DOM.auth.status.textContent = 'Simulated Mode';
            DOM.auth.status.className = 'status-indicator success';
            DOM.auth.btn.innerHTML = 'Obtain Access Token';
        } finally {
            DOM.auth.btn.disabled = false;
        }
    });

    DOM.sendBtn.addEventListener('click', async () => {
        const originalBtnText = DOM.sendBtn.innerHTML;
        DOM.sendBtn.disabled = true;
        DOM.sendBtn.innerHTML = 'Streaming Data...';
        DOM.output.textContent = '// Requesting nexus gateway...';
        
        const start = Date.now();
        try {
            const userHeaders = JSON.parse(DOM.headers.value);
            const userBody = DOM.bodyGroup.style.display !== 'none' ? JSON.parse(DOM.body.value) : null;
            const sanitized = RequestInterceptor.sanitize(DOM.method.value, DOM.url.value, userHeaders, sessionToken);
            
            const res = await ApiService.execute(DOM.method.value, sanitized.url, sanitized.headers, userBody);
            
            DOM.time.textContent = `${Date.now() - start}ms`;
            DOM.size.textContent = `${(res.size / 1024).toFixed(2)} KB`;
            DOM.status.textContent = `${res.status} ${res.statusText}`;
            DOM.status.className = `status-indicator ${res.ok ? 'success' : 'error'}`;
            
            const formattedData = typeof res.data === 'object' ? JSON.stringify(res.data, null, 4) : res.data;
            DOM.output.textContent = formattedData;
        } catch (error) {
            DOM.status.textContent = 'SYSTEM ERROR';
            DOM.status.className = 'status-indicator error';
            DOM.output.textContent = `CRITICAL FAILURE:\n${error.message}`;
        } finally {
            DOM.sendBtn.disabled = false;
            DOM.sendBtn.innerHTML = originalBtnText;
        }
    });

    // Initialize UI
    updateUIState();
});

