import os
import random
import datetime
import uuid

def generate_access_log():
    # Sample IP addresses
    ips = [
        '127.0.0.1', '192.168.0.1', '10.0.0.1', '172.16.0.1',
        '192.168.1.1', '10.0.0.2', '172.16.0.2', '192.168.1.2',
        '10.0.0.3', '172.16.0.3', '192.168.1.3', '10.0.0.4',
        '172.16.0.4', '192.168.1.4', '10.0.0.5'
    ]
    
    # Sample HTTP methods
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    
    # Sample HTTP status codes
    status_codes = [200, 301, 404, 500]
    
    # Sample user agents
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.3',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    ]
    
    # Generate a random log entry
    ip = random.choice(ips)
    timestamp = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S %z')
    method = random.choice(methods)
    url = '/' + str(uuid.uuid4())[:8]  # Generate a random URL
    status = random.choice(status_codes)
    user_agent = random.choice(user_agents)
    
    # Assemble the log entry
    log_entry = '{ip} - - [{timestamp}] "{method} {url} HTTP/1.1" {status} - "{user_agent}"\n'.format(
        ip=ip, timestamp=timestamp, method=method, url=url, status=status, user_agent=user_agent
    )
    
    return log_entry

log_directory = '/var/log/httpd/'

# Ensure the log directory exists
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Run the script indefinitely
try:
    while True:
        log_entry = generate_access_log()
        with open(os.path.join(log_directory, 'access.log'), 'a') as log_file:
            log_file.write(log_entry)
except KeyboardInterrupt:
    print("Script stopped by user.")
