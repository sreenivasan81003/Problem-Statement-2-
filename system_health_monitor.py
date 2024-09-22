import psutil
import logging

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    else:
        logging.info(f'CPU usage is normal: {cpu_usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory.percent}%')
    else:
        logging.info(f'Memory usage is normal: {memory.percent}%')

def check_disk_usage():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f'Low Disk space detected: {disk.percent}% used')
    else:
        logging.info(f'Disk space usage is normal: {disk.percent}% used')

def check_running_processes():
    processes = len(psutil.pids())
    logging.info(f'Number of running processes: {processes}')

if __name__ == '__main__':
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
