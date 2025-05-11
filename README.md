# Exposed-Server-Finder
This repository used censys to find exposed stremio streaming server on the internet, and returns the address of the stremio server and if it's online and functional.
# Method
The contents of the below url was saved as the txt file, and can be read by the python file and the urls of the available server are extracted and a gui from within the program can be used to check if the urls are online.
**https://search.censys.io/search?resource=hosts&virtual_hosts=EXCLUDE&q=%28services.http.response.headers%3A+%28key%3A+%60location%60+and+value.headers%3A+%60https%3A%2F%2Fapp.strem.io%2Fshell-v4.4%2F%3FstreamingServer%3Dhttp%2A%60%29%29+and+services.port%3D%6011470%60**

