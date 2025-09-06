# Just testing my understanding of writing, reading and appending to files in Python

f= open("log.txt","a")
f.write("My Name is Emmanuel\n")
f.close()

with open("log_1.txt","a") as f:
    f.write("when using the 'with' you do not need to close the file, its automatically does it for you\n")