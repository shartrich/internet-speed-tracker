import socket
from datetime import datetime
import speedtest
from src.configs.settings import DEBUG_MODE

conversions_map = {
    'KBps': 1 / 1024,
    'MBps': 1 / 1024 / 1024,
    'GBps': 1 / 1024 / 1024 / 1024,
}

def run_test(unit='MBps', servernames=[]):
    start_time = datetime.utcnow()
    st = speedtest.Speedtest()
    download = st.download()
    upload = st.upload()
    servernames = []
    st.get_servers(servernames)

    if DEBUG_MODE:
        print(st.results)

    return {
        'record_datetime': start_time.isoformat(timespec='seconds'), 
        'device': socket.gethostname(),
        'unit': unit, 
        'download': conversions_map.get(unit) * download,
        'upload': conversions_map.get(unit) * upload, 
        'ping': st.results.ping
    }
