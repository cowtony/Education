# Manru Wang
# ITP 115
# Assignment 8
# 3/23/2018
# Description: Web Scraping Course Information

from bs4 import BeautifulSoup
import urllib.request


def filter(displayFilter):
    file = open("result.txt", 'w')
    file.write("Here are all of the ITP classes that are 3.0 units:\n")

    url = "http://classes.usc.edu/term-20181/classes/itp/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    courses = soup.find_all("div", class_="course-info expandable")
    for course in courses:
        courseUnits = course.find("span", class_="units").text
        if courseUnits == "(" + str(displayFilter) + ".0 units)":
            file.write(course.find("h3").text + '\n')
            for section in course.find_all("tr"):
                if section.text == "SectionSessionTypeTimeDaysRegisteredInstructorLocationSyllabusInfo":
                    continue
                info = section.find("td", class_="time").text + ", " + section.find("td",class_="registered").text + ", " + section.find("td", class_="instructor").text + '\n'

                file.write(info)
            file.write('\n')

    file.close()


def main():
    while True:
        displayFilter=int(input("Enter the number of units you wish to search for classes by (1-4):"))
        if displayFilter>=1 and displayFilter<=4:
            filter(displayFilter)
            print("See 'results.txt' for your results.")
            break
        else:
            print("Invalid Input, please try again.")


main()