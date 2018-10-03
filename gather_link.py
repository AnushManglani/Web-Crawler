from html.parser import HTMLParser
from urllib import parse


class GatherFiles(HTMLParser):

    # init is an initialization method
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        # saving every url in this set
        self.links = set()

    # handle_starttag is a method which will gather every data from an opening tag
    def handle_starttag(self, tag, attrs):
        # we take 'a' because all the links start from 'a href' in a web page
        if tag == 'a':
            for (attributes, value) in attrs:
                if attributes == 'href':
                    # urljoin is a function which joins the url with the base url if its an relative url
                    url = parse.urljoin(self.base_url, value)
                    # print('inside join method and the url is ' + url)
                    self.links.add(url)

    def return_link(self):
        return self.links

    # the error function check for any error while executing
    def error(self, message):
        print('Error')
        pass
