#----------------------------------
#
#	Unititled Game
#	By: James Gubler
#	Darren Kent
#	Luke Hansen
#
#	Main.py
#	Handles Program Initialization
#
#----------------------------------

# Imports
import sys
sys.path.insert(0,'src/')
import application

''' Function: Main
	Creates an instance of the game and
	runs it.'''
def main():
    filname = "data/maps/mainmap.xml"
    app = application.Application(filname)
    app.run()

# Call Main
if( __name__ == '__main__'):
	main()