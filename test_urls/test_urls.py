import fileinput
from urllib import request, error
from sys import stderr

#file_name = "pool_urls.txt"

def test_urls(filename):

    line_number = 1
    error_count = 0

    for web_address in fileinput.input(filename):
        #print(f"{line_number}: {web_address}")
        request_url = request.Request(url = web_address, headers={'User-Agent': 'Mozilla/6.0'})
        try:
            web_content = request.urlopen(request_url)
            if web_content.status != 200: # https://docs.python.org/3/library/http.html#http-status-codes
                error_count += 1
                print(f"ERROR {web_content.getcode()} {web_content.reason} ACCESSING URL #{line_number}: {web_address}")
            else:
                print(f"{web_content.getcode()} {web_content.reason} ACCESSING URL #{line_number}: {web_address}")
        except error.HTTPError as web_error:
            error_count += 1
            print(f"FATAL ERROR {web_error.getcode()} {web_error.reason}) while accessing {web_address}", file=stderr)
        line_number += 1

    return error_count
