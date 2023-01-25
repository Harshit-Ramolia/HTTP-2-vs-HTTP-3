import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def parse_metrics(logs, metrics):
    temp = []
    for m in metrics:
        idx = logs.find(m)
        temp.append(logs[idx:].split("\"")[0])
    return temp

def write_metrics(metrics):
    temp = {}
    for m in metrics:
        temp[m.split(':')[0]] = float(m.split(': ')[1])
    return temp

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser':'INFO'}
driver = webdriver.Chrome(options=options, desired_capabilities=dc)

driver.get("http://localhost:3000/samples/dash-if-reference-player/index.html")

url = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/input")
url.clear()
url.send_keys("https://localhost:8000/testfiles/movie-dash.mpd")
time.sleep(3)

load = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/span/button[3]")
load.click()

print("HELLO")

json_str = []
while True:
    logs = str(driver.get_log('browser'))
    if 'FINAL METRICS' in logs:
        metrics = parse_metrics(logs, 
                    ['Stalls', 'Quality changes', 'Avg. bitrate', 'Avg. buffer length'])
        json_str.append(write_metrics(metrics))

        json_obj = json.dumps(json_str, indent=4)
        with open("metrics.json", "w") as outfile:
            outfile.write(json_obj)

        print("Metrics recorded")
        break

