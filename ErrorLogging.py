errorLogFile = "ErrorLog.txt"

#Handle errors and print the errors to a log
def LogError(err, fileName):
    with open(errorLogFile, 'a') as logf:
        logf.write("Failed to load {0}: {1}\n".format(str(fileName), str(err)))