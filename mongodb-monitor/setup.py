try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup,find_packages

sdict = {
    'name' : 'mongodb-monitor',
    'version' : 2.0,
    'packages' : ['src'],
    'entry_points' : {
        'console_scripts' : [
            'monitor = src.com.tgl.monitor.collection.mongostat.read_mongo_stat:main',
            'iomonitor = src.com.tgl.monitor.collection.iostat.read_io_stat:main',
            'vismonitor = src.com.tgl.monitor.collection.mongovis.mongo_vis:main'],
    },

}

sdict['packages'] = find_packages()



setup(**sdict)