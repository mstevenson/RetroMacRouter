import datetime
from memento_client import MementoClient
import urlparse
 
def wayback(uri):
    #time = datetime.datetime(1997, 1, 1, 0, 0)
    #mc = MementoClient('https://web.archive.org/web/')
    #info = mc.get_memento_info(uri, time)
    #memento_uri = info.get("mementos").get("closest").get("uri")[0]

    #path = urlparse.urlparse(memento_uri).path
    #identifier = path.split('/')[2]
    #memento_uri = memento_uri.replace(identifier, identifier + 'id_')

    #return memento_uri

    wb_uri = 'https://web.archive.org/web/199701010000id_/' + uri
    return wb_uri



#if __name__ == '__main__':
    #import requests
    #html = requests.get('http://stackoverflow.com/questions/5598524/can-i-remove-script-tags-with-beautifulsoup').content
    #html = macify(html)
    #with open('macified.html', 'w') as fd:
    #    fd.write(html)

