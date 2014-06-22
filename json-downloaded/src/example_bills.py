#!/usr/bin/python

import json
import os


if __name__=="__main__":
    root_dir="/home/aanchan/open_parliament/OpenParliamentAnalyses/json-downloaded/data/bills"
    for direc,cvs,members in os.walk(root_dir):
        for bill_file in members:
            with open("%s/%s"%(direc,bill_file)) as data_file:
                try:
                    data=json.load(data_file)

        #####################################
        # Notes on the data object for bills#
        #####################################
        #data is a dictionary with keys [u'pagination', u'objects']
        
        #A. data.[u'pagination'] is a dictionary that looks like this:
             # {u'next_url': u'/bills/?offset=20&limit=20&politican=eve-adams&format=json', u'offset': 0, u'limit': 20, u'previous_url': None}
        #B. data.[u'objects'] is a list of dictionaries. E.g. for eve-adams.json, the list had 20 elements with each 
            #dictionary with identical keys looking like this:
            #[u'name', u'url', u'number', u'session', u'introduced', u'legisinfo_id']
        

        #####################################
        # End of note                       #
        #####################################
                    name=(bill_file.split('.')[0].split('-'))
                    print "Bills introduced by:%s %s"%(name[0].title(),name[1].title())
                    for item in data[u'objects']:
                        print item[u'name'][u'en']
                except:
                    print "Error in loading JSON file:%s"%(bill_file)

             
