import test_urls
from sys import stderr
from pathlib import Path

filename=input("=== Let's test your pool of URLs ===\nGive me a filename where you have the URLs you want to test: ")

if Path(filename).is_file():
    # STEP 3 - Call the function from the external python file
    test_urls.test_urls(filename)

else:
    print("ERROR: The filename introduce is not valid or is a directory", file=stderr)