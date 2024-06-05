"""
    WAIFUSLIDESHOW IS A LITTLE PYTHON APPLICATION THAT
    RUNS A SLIDESHOW OF DIFFERENT ASCII ART. WHETHER THAT
    IS HOT ANIME WAIFU'S OR CATS AND DOGS.

    THIS WAS MADE FOR ONLY FUN AND JOKES AND SHOULD
    NOT BE TAKEN SERIOUSLY

    THIS APPLICATION ALSO DOES NOT HAVE ANY
    WARRENTY AND THAT THE AUTHOR OF THIS SOFTWARE
    IS NOT RESPONSIBLE FOR ANY DAMAGES DONE TO YOUR COMPUTER
    FROM THIS SOFTWARE.

    YOU HAVE BEEN WARNED!
"""
# Here we are importing different libraries for use
import threading # Imports multi threading libraries
import os        # Imports the OS library which is to communciate and send syscalls to the OS
import time      # Imports the time library which allows us to specifiy a time interval between function calls

# This defines the main function at the top where all the code is ran
def main():
    WaifuAsciiFiles = ['NSFW.txt','SFW.txt','LEWD.txt']

# This calls main if the following is correct and or true
if __name__ == '__main__':
    try:
        main()

    except:
        exit()