#!/usr/bin/env python3
import cgitb
import random

excusefile = 'excuses'
header = 'header.html'
footer = 'footer.html'

cgitb.enable()
print("Content-Type: text/html;charset=utf-8\r\n\r\n")

def main():

    excuses = []
    with open(excusefile, encoding="utf-8") as infile:
        excuses = infile.readlines()
    excuse = random.choice(excuses)

    with open(header, 'r') as head:
        print(head.read())
    print("<h1>" + str(excuse) +"</h1>")
    with open(footer, 'r') as foot:
        print(foot.read())


if __name__ == "__main__":
    main()