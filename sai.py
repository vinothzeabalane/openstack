from ConfigParser import SafeConfigParser
import glob
import codecs
import sys

parser = SafeConfigParser()
parser.optionxform=str

# candidates = ['dashboard.ini']
# 
# found = parser.read(candidates)
# 
# missing = set(candidates) - set(found)
# 
# print 'Found config files:', sorted(found)
# print 'Missing files     :', sorted(missing)


with codecs.open('dashboard.ini', 'r', encoding='utf-8') as f:
    parser.readfp(f)

fp = open('dashboard.ini', 'w')

parser.set('section', 'OPENSTACK_HOST', '10.161.113.177')
parser.write(fp)

