from __future__ import print_function
import os
import re
from argparse import ArgumentParser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

'''
Usage example to resubmit missing 2017 data jobs:
for f in crab_configs/Single*2017.py; do echo $f; python src/UMDNTuple/UMDNTuple/submit_crab_recovery.py --config $f; done
for f in crab_configs_recX/Single*2017.py; do echo $f; crab submit --config $f; done
'''

p = ArgumentParser(description = "USAGE: python submit_crab_recovery.py --config crab_configs/SingleElectron_Run2017F-31Mar2018-v1_2017.py")

p.add_argument('--config', required=True, help='path to original config' )
p.add_argument('--splitting', default = 'EventAwareLumiBased', help='job splitting type: Automatic, FileBased, LumiBased, or EventAwareLumiBased' )
p.add_argument('--units', default = 50000, help='depending on splitting type: runtime in minutes, files, lumis, or events' )
p.add_argument('--skipreport', action='store_true', help='skip crab report (retrieves the notFinishedLumis.json)' )
p.add_argument('--force', action='store_true', help='force recovery job even if that exists already' )
p.add_argument('--dryrun', action='store_true', help='do not write new config files' )
p.add_argument('--tag', default = '4', help='tag for recovery jobs' )

options = p.parse_args()

assert os.path.isfile(options.config), "--config must point to a valid CRAB configuration file"

ifile = open(options.config, 'r' )
odir = 'crab_configs_rec' + options.tag
if not os.path.isdir(odir):
    os.mkdir(odir)
opath = odir + '/' + os.path.basename(options.config).replace('_recovery', '')
print(bcolors.HEADER + bcolors.BOLD + 'old config file = %s' % options.config + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.BOLD + 'new config file = %s' % opath + bcolors.ENDC)

oldRequestName = ''
newRequestName = ''
workArea = ''
crab_project_path = ''
success = True
olines = []
for iline in ifile:
    oline = iline
    
    # detect work area, update request name
    m = re.match('(.*requestName) = \"(.*)\"', iline)
    if m:
        oldRequestName = m.group(2)
        newRequestName = oldRequestName.split('_rec')[0] + '_rec' + options.tag
        if len(newRequestName) > 100:
            print(bcolors.WARNING + bcolors.BOLD + 'warning: new requestName too long (>100), please change before submission' + bcolors.ENDC)
        oline = m.group(1) + ' = "' + newRequestName + '"\n'
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
    
    # update lumimask later
    m = re.match('(.*lumiMask) = \"(.*)\"', iline)
    if m:
        oline = ''

    print(oline, end='')
    olines.append(oline)

crab_project_path = os.path.join(workArea, 'crab_' + oldRequestName)
if not os.path.isdir(crab_project_path):
    print(bcolors.FAIL + bcolors.BOLD + 'fail: could not find original crab directory' + bcolors.ENDC)
    success = False
crab_project_path_recovery = os.path.join(workArea, 'crab_' + newRequestName)
if os.path.isdir(crab_project_path_recovery):
    print(bcolors.WARNING + bcolors.BOLD + 'warning: recovery directory already exists' + bcolors.ENDC)
    if not options.force:
        print(bcolors.WARNING + 'skipping...' + bcolors.ENDC)
        success = False
if success and not (options.skipreport or options.dryrun):
    cmd = 'crab report -d %s' % crab_project_path
    os.system(cmd)
notFinishedLumisJson = os.path.abspath(crab_project_path + '/results/notFinishedLumis.json')
if not os.path.isfile(notFinishedLumisJson):
    print(bcolors.FAIL + bcolors.BOLD + 'fail: notFinishedLumis.json does not exist' + bcolors.ENDC)
    success = False
oline = 'config.Data.lumiMask = "' + notFinishedLumisJson + '"\n'
print(oline, end='')
olines.append(oline)

ifile.close()

if (success or options.force) and not options.dryrun:
    ofile = open(opath, 'w' )
    for oline in olines:
        ofile.write(oline)
    ofile.close()
