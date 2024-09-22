import requests
import logging

# Setup logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# URL of the application
APP_URL = 'http://your-application-url.com'

def check_app_health():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            logging.info(f'Application is UP: Status code {response.status_code}')
        else:
            logging.error(f'Application is DOWN: Status code {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to reach application: {e}')

if __name__ == '__main__':
    check_app_health()
