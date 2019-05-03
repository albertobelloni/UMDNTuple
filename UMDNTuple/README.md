# Setup for 2016 and 2017 data analysis

This configuration is harmonized for the latest version of 94X miniAOD dataset for 2016 and 2017

Current architecture: SL6 gcc630

2018 remains separate as it uses 102X

## Setup CMSSW
```
cmsrel CMSSW_9_4_13
cd CMSSW_9_4_13/src
cmsenv
```

Merge the EgammaPostRecoTools for photon and electron objects 

https://twiki.cern.ch/twiki/bin/viewauth/CMS/Egamma2016DataRecommendations
https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPostRecoRecipes
https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaMiniAODV2#2017_MiniAOD_V2
```
git cms-init
git cms-merge-topic cms-egamma:EgammaPostRecoTools
git clone https://github.com/albertobelloni/UMDNTuple
cd UMDNTuple
git checkout legacy2016
cd UMDNTuple
scram b -j8
```

## Test code locally
```
cd ${CMSSW_BASE}
cmsRun src/UMDNTuple/UMDNTuple/run_production_cfg.py  isMC=1
```
this will produce the ntuple.root under the current directory

(Note the default input file is no lxplus. You need to change it if on a different site.)

## Submit with crab
edit the datasets in `data_samples` and `mc_samples`, under `submit_crab.py` 

Also note that there exist two separate lists for 2016 and 2017

```
python src/UMDNTuple/UMDNTuple/submit_crab.py --version 0228 
chmod 744 submit_crab.sh #only needs to be done once
./submit_crab.sh
```
