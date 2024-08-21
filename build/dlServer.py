import requests
import json
import sys
import urllib.request

versionmanifesturl = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

def loadjson(url):
    response = requests.get(url)
    if (int(response.status_code) != 200):
        print("http error - " + str(response.status_code))
        exit(1)
    data = json.loads(response.content)
    return data

def main():
   versionmanifestdata = loadjson(versionmanifesturl)
   targetversion = sys.argv[1]
   if (targetversion == "latest") or (targetversion == "latest-release"):
       targetversion = versionmanifestdata['latest']['release']
   if (targetversion == "latest-snapshot"):
       targetversion = versionmanifestdata['latest']['snapshot']
   packagemanifesturl = None
   for versionentry in versionmanifestdata['versions']:
       if (versionentry['id'] == targetversion):
           packagemanifesturl = versionentry['url']
           break
   if (packagemanifesturl == None):
       print("version not found")
       exit(1)
   packagemanifestdata = loadjson(packagemanifesturl)
   downloadurl = packagemanifestdata['downloads']['server']['url']
   urllib.request.urlretrieve(downloadurl, 'server.jar')
   print(downloadurl)
   return 0
   
if __name__ == "__main__":
    main()
