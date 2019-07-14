# -*- coding: utf-8 -*-
import sys
import webpkg.helper
import webpkg.getURLpath
import webpkg.htmlparser
import webpkg.regex

if(len(sys.argv)!=2):
    usage = "check-directorylisting url"
    webpkg.helper.help(usage)

url = str(sys.argv[1])
domain, middle = webpkg.getURLpath.getDomainandMiddle(url)
current_page, path = webpkg.getURLpath.getCurrentPage(url)

html = webpkg.htmlparser.returnhtml(path)
m = webpkg.regex.findSearchstr('페이지를 표시할 수 없습니다|[F|f]orbidden', html)
if m:
    print("\n***** This website is \"SAFE\" from Directory listing")
else:
    print("***** This website is \"RISK\" from Directory listing")