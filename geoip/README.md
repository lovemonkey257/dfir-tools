# dfir-tools
## geoip

geoip is an IP address command line enrichment tool. It uses the Maxmind GeoIP databases IPv4 City and ASN. 

It will except an ip from the command line itself (--ip) or from stdin. As long as the text on stdin looks like it contains an IP address (or addresses), based on a simple regex, it will do the lookup. It can also do a lookup against TOR node lists, downloaded from torstatus.blutmagie.de.

The output is by default tab separated which makes it command line friendly for things such as cut and sort as well as Spreadsheet/Database friendly

It has been used extensivily from investigations when you end up with lists of IP addresses and wish to make sense of them. Here are some of the use-cases and incantations I have used in the past:

### Testing it
nmap -sL -iR 10 | geoip

### Assuming you have a list of ips in a file
geoip < victims.txt

### Ordered By country
geoip < victims.txt | sort -k2

### Enrich list of victims with Geoip data
geoip --append < victims.txt > victims-geo.txt

### JSON output for all your NoSQL needs
#### MongoDB
geoip --json < victims.txt | mongoimport --collection victims

#### ElasticSearch
geoip --json < victims.txt | json-to-elastic --index=victim --type=geoip

