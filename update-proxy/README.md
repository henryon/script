This script used for update squidproxy automatically, It will update authorized IP list with latest IP's. If you have any special needs, please modify script.

First, We need mechanize,boto3,ec2 ,esconfig python module.Please install them firstly
	pip install -r requirements.txt

Then, RUN below command:
	export CONSUL_TOKEN=<PROD-TOKEN-FROM-OPS>

RUN Script:
	python  main.py
