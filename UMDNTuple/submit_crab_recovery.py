from __future__ import print_function
import os
import re
from argparse import ArgumentParser

'''
Usage example to resubmit missing 2017 data jobs:
for f in crab_configs/Single*2017.py; do echo $f; python src/UMDNTuple/UMDNTuple/submit_crab_recovery.py --config $f; done
for f in crab_configs/Single*2017_recovery.py; do echo $f; crab submit --config $f; done
'''

p = ArgumentParser(description = "USAGE: python submit_crab_recovery.py --config crab_configs/SingleElectron_Run2017F-31Mar2018-v1_2017.py")

p.add_argument('--config', required=True, help='path to original config' )
p.add_argument('--splitting', default = 'Automatic', help='job splitting type' )
p.add_argument('--units', default = 300, help='depending on splitting type: lumis or runtime in minutes' )
p.add_argument('--skipreport', action='store_true', help='skip crab report (retrieves the notFinishedLumis.json)' )

options = p.parse_args()

assert os.path.isfile(options.config), "--config must point to a valid CRAB configuration file"

ifile = open(options.config, 'r' )
path, ext = os.path.splitext(options.config)
opath = path + '_recovery' + ext
ofile = open(opath, 'w' )
print('new config file = %s' % opath)

requestName = ''
workArea = ''
crab_project_path = ''
for iline in ifile:
    oline = iline
    
    # detect work area, update request name
    m = re.match('(.*requestName) = \"(.*)\"', iline)
    if m:
        requestName = m.group(2)
        oline = m.group(1) + ' = "' + m.group(2) + '_recovery' + '"\n'
    m = re.match('(.*workArea) = \"(.*)\"', iline)
    if m:
        workArea = m.group(2)
    
    # update job splitting
    m = re.match('(.*splitting) = (.*)', iline)
    if m:
        oline = m.group(1) + ' = "' + str(options.splitting) + '"\n'
    m = re.match('(.*unitsPerJob) = (.*)', iline)
    if m:
        oline = m.group(1) + ' = ' + str(options.units) + '\n'
    
    # update lumimask
    m = re.match('(.*lumiMask) = \"(.*)\"', iline)
    if m:
        crab_project_path = os.path.join(workArea, 'crab_' + requestName)
        assert os.path.isdir(crab_project_path), 'could not find crab directory'
        if not options.skipreport:
            cmd = 'crab report -d %s' % crab_project_path
            os.system(cmd)
        notFinishedLumisJson = os.path.abspath(crab_project_path + '/results/notFinishedLumis.json')
        assert os.path.isfile(notFinishedLumisJson), 'notFinishedLumis.json does not exist, run with --report'
        oline = m.group(1) + ' = "' + notFinishedLumisJson + '"\n'
    
    print(oline, end='')
    ofile.write(oline)

ifile.close()
ofile.close()


