zabbix-import
=============

CLI tool for importing Zabbix XML configuration files using Zabbix API

## Usage :

    ./zabbix-import.py [Options]

## Options :

     -u, --user : Username to be used to connect to Zabbix API. Defaults to *Admin*
     -p, --password : Password to be used to connect to Zabbix API. Defaults to *zabbix*
     -s, --server : Server API URL. Defaults to *http://127.0.0.1/zabbix*
     -f, --file : XML configuration file to be uploaded. Defaults to *hosts.xml*
