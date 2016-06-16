#!/usr/bin/env python3
import cgitb, random

excusefile = '../excuses'
total = 16
width = 4

header = ("<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01//EN' 'http://www.w3.org/TR/html4/strict.dtd'>\n"
        "<html lang='en'>\n<head>\n"
        "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>\n"
        "<title>IPv6 Excuse Bingo</title>\n"
        "<link rel='stylesheet' type='text/css' href='css/style.css'>\n"
        "</head>\n<body>\n"
        "\t<center>\n\t\t<h1><a href='https://twitter.com/ipv6excuses'><img src='http://ipv6excuses.com/ipv6excuses.png' height='50' width='50'/></a>IPv6 Excuse Bingo</h1>\n\t</center>")

footer = ("Made with excuses from <a href='http://ipv6excuses.com'>ipv6excuses.com</a>"
        "<br />Suggest a new excuse: "
        "<a href='https://twitter.com/intent/tweet?screen_name=ipv6excuses' class='twitter-mention-button' data-related='ipv6excuses'>Tweet to @ipv6excuses</a><script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>"
        "\t</body>\n</html>")

# Generates an HTML table representation of the bingo card for terms
def generateTable(ts):
    res = "<table>\n"
    for i, term in enumerate(ts):
        if i % width == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term.strip('\n') + "</td>\n"

        if i % width == width - 1:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res

def main():
    cgitb.enable()
    print("Content-Type: text/html;charset=utf-8\r\n\r\n")
    with open(excusefile, encoding="utf-8") as infile:
        terms = infile.readlines()
    print(header)
    random.shuffle(terms)
    print(generateTable(terms[:total]))
    print(footer)

if __name__ == "__main__":
    main()
