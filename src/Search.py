import requests
from bs4 import BeautifulSoup
from typing import TextIO

class GoogleSearch:
    search_engine_url = "https://www.google.com/search?q="

    # element in result page showing link and website description
    result_html_attribs = {"class", "egMi0 kCrYT"}

    # attributes of <a> tag containing link to website in each result
    result_html_a_attribs = {"class", "BNeawe vvjwJb AP7Wnd"}

    def __init__(self, output_stream:TextIO):
        self.output_stream = output_stream
    

    def _fetch_results(self):
        self.response = requests.get(self._generate_query())
        self._parse_html()
        return self.response
        
    def _print_results(self):
        self._print_query_header()
        for tag in self.parser.find_all(attrs=self.result_html_attribs):
            self._print_tag(tag)

    def search(self, search_words:str):
        self.search_words = search_words
        self._fetch_results()
        self._print_results()

    def _generate_query(self) -> str:
        return self.search_engine_url + self.search_words.replace(' ', '+')
    
    def _parse_html(self):
        if self._is_parseable():
            self.parser = BeautifulSoup(self.response.content, 'html.parser')
    
    def _is_parseable(self):
        return True if self.response.status_code == 200 else False


    def _print_tag(self, tag):
        self.output_stream.writelines([
            "[" +
            tag.find(attrs=self.result_html_a_attribs).string +
            "](" +
            tag.a['href'].replace("/url?q=", "") +
            ")" +
            self._markdown_line_terminate()
        ])
        print(tag.find(attrs=self.result_html_a_attribs).string)
        print(tag.a['href'].replace("/url?q=", ""))

    def _markdown_line_terminate(self):
        return "  \n";
    
    def _print_query_header(self):
        self.output_stream.writelines([
            "### " + self.search_words + self._markdown_line_terminate()
        ])
if __name__ == '__main__':

    s = GoogleSearch()
    s.search("Boomerang")