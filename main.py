import time, logging, os
from datetime import datetime as dt

os.system("title NoMoreLogging (Bate)")
hosts_path=r'C:\\Windows\\System32\\drivers\\etc\\hosts'
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;63m[\x1b[0m%(asctime)s\x1b[38;5;63m]\x1b[0m %(message)s",
    datefmt="%H:%M:%S"
)
logging.info('This Is Very Shitty Ill Make It Better When I Feel Like It But Is Dose Block All The Sites')

def fetch_domains():
    os.system("C:\\Windows\\System32\\curl \
    https://raw.githubusercontent.com/Paradisx/NoMoreLogging/main/Sites.txt > domains.txt");

def file_read_write():
    with open("domains.txt", 'r', encoding='UTF-8') as f:
        text = [line.strip('\n') for line in f]
        logging.info(text)
    logging.info('Writing To File')
    with open(hosts_path, 'a') as h:
        h.write('\n'.join('127.0.0.1 ' + url for url in text))

def main():
    fetch_domains()
    file_read_write()


main()
