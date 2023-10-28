import requests
import json
import sys
import urllib.request

versionManifestUrl = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

def loadJson(url):
    response = requests.get(url)
    if (int(response.status_code) != 200):
        print("http error - " + str(response.status_code))
        exit(1)
    data = json.loads(response.content)
    return data

def main():
   versionManifestData = loadJson(versionManifestUrl)
   targetVersion = sys.argv[1]
   if (targetVersion == "latest") or (targetVersion == "latest-release"):
       targetVersion = versionManifestData['latest']['release']
   if (targetVersion == "latest-snapshot"):
       targetVersion = versionManifestData['latest']['snapshot']
   packageManifestUrl = None
   for versionEntry in versionManifestData['versions']:
       if (versionEntry['id'] == targetVersion):
           packageManifestUrl = versionEntry['url']
           break
   if (packageManifestUrl == None):
       print("Version not found")
       exit(1)
   packageManifestData = loadJson(packageManifestUrl)
   downloadUrl = packageManifestData['downloads']['server']['url']
   urllib.request.urlretrieve(downloadUrl, 'server.jar') 
   print(downloadUrl)
   return 0
   
if __name__ == "__main__":
    main()
