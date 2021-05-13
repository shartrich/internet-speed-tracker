from datetime import datetime
import speedtest

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

    return {
        'record_datetime': start_time.isoformat(timespec='seconds'), 
        'unit': unit, 
        'download': conversions_map.get(unit) * download,
        'upload': conversions_map.get(unit) * upload, 
        'ping': st.results.ping
    }
