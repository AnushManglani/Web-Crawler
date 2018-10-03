# creation of multi-spiders take place here
import threading
from queue import Queue
from Spider import Spider
from Domain import *
from first import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# check if there are items in the the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print('The items lest in queue are ' + str(len(queued_links)))
        create_jobs()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()


def creating_spiders():
    for x in range(NUMBER_OF_THREADS):
        # target specifies the work which the different spiders will do
        t = threading.Thread(target=Work)
        # daemon ensure that every thread will stop when the main exits
        t.daemon = True
        t.start()

def Work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


creating_spiders()
crawl()
