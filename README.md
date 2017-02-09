# trello_conky
Script to show me list of stuff I need to do today in conky. 

Example conkyrc:

```
Trello
$hr
${execpi 300 python3 ~/p/trello_conky/main.py}

```