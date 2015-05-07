#! /usr/bin/python

import os
import json
import sys
import argparse
from datetime import datetime
from elasticsearch import Elasticsearch

def parse_date(utcTime,fmt):
    return datetime.strptime(utcTime, fmt)
def from_iso8601(utcTime):
    return parse_date(utcTime,fmt="%Y-%m-%dT%H:%M:%S.%fZ")
def from_epoch(epoch):
    return datetime.fromtimestamp(float(epoch))
def isodate(d):
    return d.isoformat('T')

parser = argparse.ArgumentParser(description='Import JSON docs into Elasticsearch')
parser.add_argument('--index',  help='Elastic Index to use')
parser.add_argument('--estype', help='Elastic type (_type)')
args = parser.parse_args()

es_index_name = args.index
es_doc_type   = args.estype

es = Elasticsearch()
c=0
print "Import starts.."
for json_str in sys.stdin:
    j = json.loads(json_str)

    ### Modify/Add to your JSON here
    ### For example ES is picky about dates - use the included routines to munge dates into correct format 
    ### From an epoch: isodate(from_epoch(doc["my_epoch_date"]))
    ### From a string formatted as DD-MM-YYYY try: isodate(parse_date("20-02-1997","%d-%m-%Y"))

    try:
        es.index(index=es_index_name, doc_type=es_doc_type, timeout=60, body=j)
    except Exception,e:
        print e
        pass
    finally:
        c=c+1
print "Import finished. ",c," records imported"
