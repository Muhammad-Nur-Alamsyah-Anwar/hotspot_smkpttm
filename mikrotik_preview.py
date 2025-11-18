import http.server
import socketserver
import os
import urllib.parse

PORT = 8000

# Konfigurasi Data Palsu (Sisa kuota dihapus)
MOCK_DATA = {
    # Action URL simulasi
    '$(link-login-only)': '/action_login', 
    '$(link-logout)': '/action_logout',
    
    # Link navigasi
    '$(link-login)': '/login.html',
    '$(link-orig)': 'http://google.com',
    '$(link-status)': '/status.html',
    
    # Data User
    '$(username)': 'Siswa_SMK_Penerbangan',
    '$(ip)': '192.168.88.101',
    '$(bytes-in-nice)': '150 MiB',   # Upload
    '$(bytes-out-nice)': '1.2 GiB',  # Download
    '$(uptime)': '2j 30m 15d',
    '$(error)': '', 
}

class MikrotikHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(303)
            self.send_header('Location', '/login.html')
            self.end_headers()
            return

        clean_path = self.path.split('?')[0]

        if clean_path.endswith('.html'):
            try:
                file_path_on_disk = clean_path[1:] 
                
                if not os.path.exists(file_path_on_disk):
                    super().do_GET()
                    return

                with open(file_path_on_disk, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace Variabel
                for key, value in MOCK_DATA.items():
                    content = content.replace(key, value)
                
                # Bersihkan IF/ELSE MikroTik
                import re
                if not MOCK_DATA['$(error)']:
                    content = re.sub(r'\$\(if error\)([\s\S]*?)\$\(endif\)', '', content)
                else:
                    content = content.replace('$(if error)', '').replace('$(endif)', '')
                
                # Hapus sisa tag if
                content = re.sub(r'\$\(if [\w-]+\)', '', content, flags=re.IGNORECASE)
                content = re.sub(r'\$\(endif\)', '', content, flags=re.IGNORECASE)

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
                return

            except Exception as e:
                print(f"Error: {e}")
                super().do_GET()
        else:
            super().do_GET()

    def do_POST(self):
        # Handler Form Login & Logout
        if self.path == '/action_login':
            print("-> Login Sukses. Redirect ke alogin.")
            self.send_response(303)
            self.send_header('Location', '/alogin.html')
            self.end_headers()
            
        elif self.path == '/action_logout':
            print("-> Logout Sukses.")
            self.send_response(303)
            self.send_header('Location', '/logout.html')
            self.end_headers()
            
        else:
            self.send_response(303)
            self.send_header('Location', '/login.html')
            self.end_headers()

print(f"Server Simulasi Berjalan di http://localhost:{PORT}")
print("Akses di browser. Tekan Ctrl+C untuk berhenti.")

with socketserver.TCPServer(("", PORT), MikrotikHandler) as httpd:
    httpd.serve_forever()