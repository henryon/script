#!/usr/bin/python

from esconfig.consul_es_config import ConsulEsConfig
import boto3
import collections
import os
import mechanize
import re


# Get proxy login crendential from esconfig
config = ConsulEsConfig.get_instance("prod", "common/proxy")
user=config.query("user")
password=config.query("password")

def simulate_login():
        # Get proxy login crendential from esconfig
        config = ConsulEsConfig.get_instance("prod", "common/proxy")
        user=config.query("user")
        password=config.query("password")

        #Initial environment and header etc
        br=mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

       	br.set_debug_http(True)
        br.set_debug_redirects(True)
        br.set_debug_responses(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        #open URL and login
        r=br.open('http://vip.squides.com/login.php')

        #set user/password for login
        br.select_form(nr=0)
        br.form['username']=user
        br.form['password']=password
        br.submit()

        #Open the authips pages
        #br.open('http://vip.squides.com/index.php?action=authip')

        #create regexp to filter result
        list=re.compile(r'\d+\.\d+\.\d+\.\d+.*',re.M)
        result=list.findall(br.response().read())
	return result

if __name__ == "__main__":
	proxylist=simulate_login()
	proxylist="\n".join(proxylist)
	print proxylist
