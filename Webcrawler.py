import requests #Library used to send HTTP requests using python, Http request either retrieves data or push data to a URL or server
import re #A regular expression(regex) is a special sequence of characters that uses a search pattern to find string or its set
#Python provides re module that supports the use of regex. It searches by taking a regular exp and a string and returns first match or None

class WebCrawler:
    def __init__(self):
        #to avoid revisiting same website
        self.discovered_websites=[]

    #BFS implementation
    def crawl(self,start_url):
        queue=[start_url]
        self.discovered_websites.append(start_url)

        while queue:
            actual_url=queue.pop(0)
            print(actual_url)

            #Raw html representation of given website
            actual_url_html=self.read_raw_html(actual_url)

            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)


    def get_links_from_html(self,raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",raw_html)
    #Regex with string starting from https followed by ://, followed by www.
    #\used to drop special meaning to char following it, []represents char class, {} indicates no. of occurences of a preceding regex to match
    #? check if string before ? occurs at least once or not at all, + matches one or more occurences of string preceeding, | means OR
    #findall() returns a list containing all matches

    def read_raw_html(self,url):
        raw_html=""

        try:
            raw_html=requests.get(url).text #get() used to retrieve info. from given server using URL, response.text()returns response in unicode 
        except Exception as e:
            pass

        return raw_html
    

crawler=WebCrawler()
link=input("Enter the link-")
crawler.crawl(link)
