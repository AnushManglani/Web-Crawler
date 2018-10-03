# Here we will extract the domain name of the website so that the crawler stays in the domain

# urlparse is a module for parsing the html links
from urllib.parse import urlparse


# getting the sub domain name (mail.thehindu.news.com)
def get_subdomain_name(url):
    try:
        # netloc extracts the subdomain
        return urlparse(url).netloc
    except:
        return ''


def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''



#print(get_domain_name('https://thenewboston.com/'))
