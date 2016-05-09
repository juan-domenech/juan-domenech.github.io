# Please write a program that duplicates the Linux command 'ls' in your favored language.
# It should accept arguments and produce output in manner of GNU 'ls' command.
# Please write this in your production style code and use only the base install modules of the language you choose.
# Implement 5 commonly used switches as arguments.

# Usage:
# python juan_ls.py [Options] [File/Path]


import sys, os, re

# Print Debug messages
def print_DEBUG(message):
    if DEBUG:
        print 'DEBUG: '+message


# Print help message
def print_help():
    print 'Usage: python juan_ls.py [Options]... [File/Path]...'
    print
    print '-a, --all        do not ignore entries starting with .'
    print '-d, --directory  list directories themselves, not their contents'
    print '-f               do not sort'
    print '-r, --reverse    reverse order while sorting'
    print '-R, --recursive  list subdirectories recursively'
    print '--debug          enable debug mode'
    print '--help           print this message'
    print


# Check for valid arguments
def valid_arguments(arguments, allowed_switches):
    for item_argument in arguments:
        if item_argument not in allowed_switches:
            print "juan_ls: unrecognized option: '"+item_argument+"'"
            print "Try 'python juan_ls.py --help' for more information."
            return False
    return True


# Normalize arguments list -> look for concatenated single character switches and duplicates
def normalize_arguments(arguments):
    print_DEBUG('Normalize: Initial arguments'+str(arguments))

    # Single character switches can be concatenated
    new_arguments = []
    for argument in arguments:
        # Is this argument a '-' followed by something different and longer than 2?
        if argument[0] == '-' and argument[1] != '-' and len(argument) > 2 :
            # Then we have concatenated single character switch in our hands
            # Iterate over the characters and convert them into separated switches
            for item in range(1,len(argument)):
                new_arguments.append('-'+argument[item])
            print_DEBUG('Unpacked arguments'+str(new_arguments))
        else:
            new_arguments.append(argument)

    # Remove possible duplicated arguments
    new_arguments = sorted(new_arguments)
    arguments = [ new_arguments[item] for item in xrange(0,len(new_arguments)) if new_arguments[item:item+1] != new_arguments[item+1:item+2] ]

    print_DEBUG('Normalize: Final list of arguments'+str(arguments))

    return arguments


# Extract path and switches from argument list
def obtain_path_and_arguments(arguments):

    # Check for empty list of arguments and just return path='.' if that is the case
    if len(arguments) == 0:
        print_DEBUG('obtain_path: No arguments present. Returning: ".",[] ')
        return '.',[]

    # Is the last argument a switch ?
    if arguments[-1][0] != '-':
        # No -> Then is a path. Let's use it and remove it from the argument list
        path = arguments[-1]
        arguments.pop(-1)
        print_DEBUG('Introduced Path: "'+path+'"')
    else:
        # Yes -> No path present. Using '.'
        path = '.'
        print_DEBUG('No path introduced. Path set to "."')

    return path, arguments


# We will use the native os.walk method to scan the file system using path as starting point
# Reference: https://docs.python.org/2/library/os.html#os.walk
def walk(arguments, path):

    references = []

    # When --recursive we iterate on all the available items (let's call them 'references')
    if ('-R' in arguments) or ('--recursive' in arguments):
        for current_folder in os.walk(path):
            # !
            # Local and parent folder not present on os.walk(). Requires investigation.
            # Workaround: Alter the second position of the 3-tuple and add them
            temp = current_folder[1][:]
            temp.append('.')
            temp.append('..')
            references.append( ( current_folder[0] , temp , current_folder[2] ) )
            print_DEBUG('os.walk: recursive'+str(current_folder))
            # !

    # When not --recursive a single next() is executed to get the first item
    else:
        current_folder = next(os.walk(path))
        # !
        # Local and parent folder not present on os.walk(). Requires investigation.
        # Workaround: Alter the second position of the 3-tuple and add them
        temp = current_folder[1]
        temp.append('.')
        temp.append('..')
        references.append( ( current_folder[0] , temp , current_folder[2] ) )
        print_DEBUG('os.walk: not recursive'+str(references))
        # !

    print_DEBUG('os.walk references: '+str(references))

    # Remove files/folders with '.' as first character in their name when --all is not selected
    if ('-a' not in arguments) and ('--all' not in arguments):
        total = []

        # Iterate over all the references obtained by os.walk (there are more than one when we are in --recursive)
        for reference in references:
            result_directories = []
            result_files = []

            # Detect hidden folders when --recursive and ignore the rest of information in that reference
            if re.match(r'.*?/\..*?',reference[0] ):
                print_DEBUG('Hidden folder'+str(reference[0]))
                continue

            # Iterate over all the directory names that might exits in the current reference
            # ( Second position of the 3-tuple)
            for item_directory in range(0,len(reference[1])):
                # Only append when has a no '.' as first character
                if reference[1][item_directory][0] != '.':
                    result_directories.append(reference[1][item_directory])

            # Iterate over all the file names that might exits in the current reference
            # ( Third position of the 3-tuple)
            for item_file in range(0,len(reference[2])):
                # Only append when has a no '.' as first character
                if reference[2][item_file][0] != '.':
                    result_files.append(reference[2][item_file])

            # Survivors added to reference list as 3-tuple (its original format)
            total.append( (reference[0],result_directories,result_files) )
    else:
        # When no --all present the final list of references doesn't need to be filtered. We'll use everything.
        total = references

    print_DEBUG('walk_not_recursive'+str(total))

    return total


# Print on console the final output
def print_references(arguments, references):

    for item in references:

        # When more than a reference is received it means that we are in --recursive mode. Let's print each folder name.
        if len(references) > 1 and item[0] != '.' :
            #print
            print item[0]+':'

        # With --directory present we care only for second position of the 3-tuple (directories)
        if ('-d' in arguments) or ('--directory' in arguments):
            files = item[1]
            print_DEBUG('--directory called.')
        # Without --directory present we use both directories and file names
        else:
            files = item[1]+item[2]
            print_DEBUG('--directory NOT called.')

        # Sorting requested
        if '-f' not in arguments:
            print_DEBUG('-f not called. Sorting.')

            # Sorting requested in reverse
            if ('-r' in arguments) or ('--reverse' in arguments):
                files.sort(reverse=True)
                print_DEBUG('Sorting in reverse.')
            # Sorting
            else:
                files.sort(reverse=False)
                print_DEBUG('Sorting.')

        # Iterate over files when there is something to print (it might be an empty folder)
        if len(files) > 0 :
            for item in files:
                print item+'\t ',
            print
            print
        else:
            print


### Main

# List of allowed switches
allowed_switches = ['--help','--debug','-R','--recursive','-a','--all','-r','--reverse','-f','-d','--directory']

# Obtaining argument list form command line
arguments = sys.argv

# Discarding first elements of the list (is our program name)
arguments = arguments[1:]

# Set DEBUG mode
if '--debug' in arguments:
    DEBUG = True
    print_DEBUG('Running juan_ls.py')
    print_DEBUG('Debug enabled')
else:
    DEBUG = False

# Is '--help' prensent? The print Help and exit(0)
if '--help' in arguments:
    print_DEBUG('Help called')
    print_help()
    exit(0)


print_DEBUG('Total number of arguments:'+str(len(arguments)) )
print_DEBUG('Complete arguments list:'+str(arguments) )

# Extract path and arguments from command line
path, arguments = obtain_path_and_arguments(arguments)

# Normalize switches
arguments = normalize_arguments(arguments)

print_DEBUG('This is the list of arguments to work with:'+str(arguments))
print_DEBUG('This is the path to work with: "'+str(path)+'"')

if not valid_arguments(arguments,allowed_switches):
    # Exit
    print_DEBUG('Exit with errors due invalid arguments')
    sys.exit(2)

print_references( arguments, walk(arguments, path) )

print_DEBUG('Exit with no errors')

exit(0)