from selenium import webdriver
import requests
from sys import argv
from os import getcwd

def proxyAyarla(ip,port,site):
    # Firefox proxy ayarlarını değiştirdik
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1) 
    profile.set_preference("network.proxy.http", ip) 
    profile.set_preference("network.proxy.http_port", int(port))
    profile.set_preference("network.proxy.ssl", ip) 
    profile.set_preference("network.proxy.ssl_port", int(port))
    profile.set_preference("javascript.enabled", True)
    profile.update_preferences() 

    # GeckoDriver konumuna göre siteye girdik
    myPath = getcwd()
    driver = webdriver.Firefox(executable_path=myPath+"/geckodriver", firefox_profile=profile) 
    driver.get(site)

if __name__ == "__main__":
    # Proxyyi siteden çektik, ip ve portu aldık
    # 1 https://gimmeproxy.com/api/getProxy
    # 2 https://api.getproxylist.com/proxy
    proxyCek = requests.get("https://gimmeproxy.com/api/getProxy")
    ip,port = proxyCek.json()['ip'], proxyCek.json()['port']

    proxyAyarla(ip,port,argv[1])