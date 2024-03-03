"""
Tiffany Truong
Beautiful Soup Example Code
Parsing a modified version of the Hacker News Website
"""

from bs4 import BeautifulSoup
import urllib.request


def main():
    # PART 1: SETUP
    # URL of the website we want to parse
    # url = "http://goo.gl/vy9dzM"
    url = "http://bcf.usc.edu/~parke/py/news.html"

    # request the page from the url
    page = urllib.request.urlopen(url)

    # Make soup from the page using the HTML parser
    # This returns to you a soup object
    soup = BeautifulSoup(page.read(), "html.parser")

    # PART 2: print the soup (aka the html tag soup)
    print(soup)
    # print all of the html in a nice format (w/indentation)
    print(soup.prettify())

    # PART 3: navigating the tags with a for loop
    for tag in soup:
        print("A tag from the page:", tag)

    # PART 4: Accessing tags by tag name
    print("The first \'a\' tag found on the page:", soup.a)  # ex: first link tag
    print("The title tag on the page:", soup.title)  # ex: title tag

    # Part 5: tag more info
    for tag in soup:
        print(tag.name)  # only print the tag's name
    # Get the table tag
    tableTag = soup.table
    print("Here is the table tag:", tableTag)
    print("The name of the tag is:", tableTag.name)  # Get the tag's name ("table")
    print("The table tag's attributes are:", tableTag.attrs)  # Get a dictionary of the tags attributes and their values
    # Get the tag's "bgcolor" attribute's value (use bracket notation like a dictionary)
    print("The table tag's bgcolor attribute's value is:", tableTag["bgcolor"])

    # PART 6: Using find functions
    found = soup.find("table")  # search for 1 tag by name
    print("Found a table tag:", found)
    # find all table rows that have the class attribute equal to "athing"
    found = soup.find_all("tr", class_="athing")
    for foundTableRow in found:
        print("Found table row w/ class \'athing\':", foundTableRow)

    # this gets all of the article titles!!
    # Grab all of the td tags of the title class
    foundDataTags = soup.find_all("td", class_="title")
    for data in foundDataTags:
        # Check if the data contains an "a" tag
        linkTag = data.find("a")
        if linkTag:
            # print(linkTag)  # test that we got the right link tag
            # print the string that is displayed by the link tag (text between the 'a' start and end tags)
            print(linkTag.string)


main()
