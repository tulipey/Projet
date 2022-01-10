# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 03:14:00 2022

@author: uplay
"""

import webbrowser

f = open('helloworld.html','w')

message = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <img src="/Users/uplay/Desktop/projet/tests/test_web/camember.png" alt="ok">
  <img src="/Users/uplay/Desktop/projet/tests/test_web/camembermini.png" alt="ok">
  <img src="/Users/uplay/Desktop/projet/tests/test_web/diag_but.png" alt="ok">
</body>
</html>
"""

f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///Users/username/Desktop/projet/tests/test_web/' + 'camenbert.html'
webbrowser.open_new_tab("helloworld.html")