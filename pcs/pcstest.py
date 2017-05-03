from baidupcsapi import PCS

pcs = PCS('lpbirdueng','lupeng')
#pcs.info(verify=False)
print pcs.quota().content
print pcs.list_files('/').content