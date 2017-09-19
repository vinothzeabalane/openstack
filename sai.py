from configparser import SafeConfigParser
import codecs

parser = SafeConfigParser()
parser.optionxform=str


with codecs.open('dashboard.ini', 'r', encoding='utf-8') as f:
    parser.readfp(f)

fp = open('dashboard.ini', 'w')

parser.set('section', 'OPENSTACK_HOST', '10.161.113.177')
parser.set('section','CACHES',"{ 'default': { 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', 'LOCATION': 10.161.113.177:11211  } }'")
parser.write(fp)

