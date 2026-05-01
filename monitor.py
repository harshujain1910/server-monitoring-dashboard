import psutil
import time

def check_system():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    connections = psutil.net_connections()

    print("CPU:", cpu, "% | Memory:", memory, "% | Active Connections:", len(connections))

    if cpu > 80:
        print("⚠️ High CPU Usage!")

    if memory > 80:
        print("⚠️ High Memory Usage!")

    # Suspicious process check
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        if process.info['cpu_percent'] > 50:
            print("🚨 Suspicious Process:", process.info)


while True:
    check_system()
    time.sleep(2)


