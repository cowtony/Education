# Manru Wang
# ITP 115
# Assignment 7
# 3/18/2018
# Description: Music Library

import random
import MusicLibraryHelper

def displayMenu():
    print("Welcome to Your Music Library\n\tOptions:\n\t1) Display Display\n\t2) Display all artists\n\t3) Add an album\n\t4) Delete an album\n\t5) Delete an artist\n\t6) Search library\n\t7) Generate a random playlist\n\t8) Make your own playlist\n\t9) Exit")

def displayLibrary(musicLibDictionary):
    for artist in musicLibDictionary:
        print("Artist: " + artist)
        print("Albums:")
        for album in musicLibDictionary[artist]:
            print("\t- " + album)

def displayArtists(musicLibDictionary):
    print("Displaying all artists:")
    for artist in musicLibDictionary:
        print("-",artist)

def addAlbum(musicLibDictionary):
    newArtist=input("Enter artist:")
    newAlbum=input("Enter album:")
    if newArtist.title() in musicLibDictionary:
        musicLibDictionary[newArtist].append(newAlbum)
    else:
        musicLibDictionary[newArtist] = [newAlbum]

def deleteAlbum(musicLibDictionary):
    delArtist=input("Enter artist:")
    delAlbum=input("Enter album:")
    if delArtist.title() in musicLibDictionary:
        if delAlbum.title() in musicLibDictionary[delArtist]:
            musicLibDictionary[delArtist].remove(delAlbum)
            return True
        else:
            return False


def deleteArtist(musicLibDictionary):
    delArtistonly=input("Enter artist:")
    if delArtistonly.title() in musicLibDictionary:
        del musicLibDictionary[delArtistonly]
        return True
    else:
        return False

def searchLibrary(musicLibDictionary):
    term = input("Please enter a search term: ")

    print("Artists containing '" + term + "'")
    noResult = True
    for artist in musicLibDictionary:
        if artist.lower().find(term.lower()) != -1:
            print("- " + artist)
            noResult = False
    if noResult == True:
        print("\tNo results")

    print("Albums containing '" + term + "'")
    noResult = True
    for artist in musicLibDictionary:
        for album in musicLibDictionary[artist]:
            if album.lower().find(term.lower()) != -1:
                print("- " + album)
                noResult = False
    if noResult == True:
        print("\tNo results")

def generateRandomPlaylist(musicLibDictionary):
    print("Here is your random playlist:")
    for artist in musicLibDictionary:
        index = random.randint(0, len(musicLibDictionary[artist]) - 1)
        print("- " + musicLibDictionary[artist][index],"by",artist)


def main():
    library = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    while True:
        displayMenu()
        choise = input()
        if choise == '1':  # Display library
            displayLibrary(library)
        elif choise == '2':  # Display all artists
            displayArtists(library)
        elif choise == '3':  # Add an album
            addAlbum(library)
        elif choise == '4':  # Delete an album
            success = deleteAlbum(library)
            if success == True:
                print("Delete album success!")
            else:
                print("Delete album failed.")
        elif choise == '5':  # Delete an artist
            success = deleteArtist(library)
            if success == True:
                print("Delete artist success!")
            else:
                print("Delete artist failed.")
        elif choise == '6':  # Search library
            searchLibrary(library)
        elif choise == '7':  # Generate a random playlist
            generateRandomPlaylist(library)
        elif choise == '9':  # Exit
            print("Saving music library...")
            MusicLibraryHelper.saveLibrary("musicLibrary_test.dat", library)
            print("Goodbye!")
            break
        else:
            print("Invalid Input, please try again.")

main()