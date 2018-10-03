# This Class will grab a link from the waiting queue and then connect to that link and then
# execute the HTLMParser(gather_link file) on that page which in turn will gather all the links
# on that page and add them to the waiting queue and then lastly move it to the crawled file

# when we connect to the internet, the python returns the results not in human readable english but in bytes so
# before sending them off for parsing we need to convert them to human readable english

# just a module which allows us to connect to the web pages
from urllib.request import urlopen
from gather_link import GatherFiles
from first import *


class Spider:
    # we will create a class variable which will be shared among multiple instance(Spiders)

    # project_name is the name of the folder
    project_name = ''

    # base_url is for the Relative links
    base_url = ''
    domain_name = ''

    # the reason we are making the sets is that we don't want to write to
    # the file every time we find a link but write when the Spider is being shut down
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        # making the path name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', base_url)

    # Boot method is the method which will be executed the first time
    # that's why it has initializing capabilities
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # crawl_page function adds functionality to the different Spiders
    # which are nothing but different Threads
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Items Queued: ' + str(len(Spider.queue)) + ' | Items Crawled: ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.find_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def find_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                # utf-8 is a type of character encoding
                html_string = html_bytes.decode("utf-8")
            finder = GatherFiles(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Can not open url')
            return set()
        return finder.return_link()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue

                # we check the domain name because then there are high chances that our crawler will
                # go out of range and will begin crawling the entire web
            if Spider.domain_name not in url:
                continue
            if 'video' in url:
                Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
