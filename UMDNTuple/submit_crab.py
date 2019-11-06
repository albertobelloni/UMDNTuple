
import os
import getpass
USER=getpass.getuser()
import socket
HOST=socket.gethostname()
from argparse import ArgumentParser

p = ArgumentParser()

p.add_argument('--version', dest='version', required=True, help='version' )
p.add_argument('--year', dest='year', required=True,  help='year' )
p.add_argument('--outputPath', dest='outputPath', default='/store/user/%s/WGamma' %USER, help='output path on storage site, default=/store/user/%s/WGamma' %USER )
p.add_argument('--site', dest='site', default='T3_US_UMD', help='destination site, default=T3_US_UMD' )

options = p.parse_args()




data_samples2016 = [ 
	# 94X re-miniAOD
	'/SingleElectron/Run2016H-17Jul2018-v1/MINIAOD',
	'/SingleElectron/Run2016G-17Jul2018-v1/MINIAOD',
	'/SingleElectron/Run2016F-17Jul2018-v1/MINIAOD',
	'/SingleElectron/Run2016E-17Jul2018-v1/MINIAOD',
	'/SingleElectron/Run2016D-17Jul2018-v1/MINIAOD',
	'/SingleElectron/Run2016C-17Jul2018-v1/MINIAOD',
	'/SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD',
	##'/SingleElectron/Run2016B-17Jul2018_ver1-v1/MINIAOD', ## can be skipped
	'/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD',
	'/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD',
	'/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD',
	'/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD',
	'/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD',
	'/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD',
	'/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD',
	#'/SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD', ## can be skipped
	]

data_samples2017 = [ 
    # 2017
    '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD',
]

data_samples2018 = [
#2018
	'/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD',
	'/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD',
	'/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD',
	'/SingleMuon/Run2018D-PromptReco-v2/MINIAOD',
	'/EGamma/Run2018C-17Sep2018-v1/MINIAOD',
	'/EGamma/Run2018B-17Sep2018-v1/MINIAOD',
	'/EGamma/Run2018A-17Sep2018-v2/MINIAOD',
	'/EGamma/Run2018D-PromptReco-v2/MINIAOD',
]

data_samples2018D = [
#2018 D
	'/SingleMuon/Run2018D-PromptReco-v2/MINIAOD',
	'/EGamma/Run2018D-PromptReco-v2/MINIAOD',
]


mc_samples2016 = [
    # list of MC sample
    # The first arugment is the DAS path for the dataset
    # The second argument controls if the EventWeights are saved (removing them saves disk space)
    ('/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM', True  ),
	('/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM', False),
	('/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', True),
	('/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', True),
	('/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', True),
	('/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', True),
	('/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', False),
	('/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM', True),
	('/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM', True),
	('/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM', True),
	('/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', False),
	('/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', False),
	('/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM', False),
	('/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', True),
	('/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM', True),
	('/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', False),
	('/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM', True),
	('/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', True),
	('/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', True),
	('/MadGraphChargedResonance_WGToLNu_M1600_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', False),
	('/MadGraphChargedResonance_WGToLNu_M250_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', False),

    #('/WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True), ## in production
    ## tW samples
    ('/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', True),
    ('/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', True),

     ##new TT samples
     ('/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',False),       #77081156

    ('/MadGraphChargedResonance_WGToLNu_M900_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M900_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M800_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M800_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M700_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M700_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M600_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M600_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M500_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M500_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M450_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M450_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M400_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M400_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M4000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M4000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M350_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M350_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M3500_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M3500_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M300_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M300_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M3000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M3000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2800_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2800_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2600_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2600_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M250_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M250_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2400_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2400_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2200_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2200_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M200_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M200_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M2000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1800_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1800_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1600_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1600_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1400_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1400_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1200_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1200_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ('/MadGraphChargedResonance_WGToLNu_M1000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',False),
    ## FIXME: missing reminiaod pythia samples
	]

mc_samples2017 = [
	## 2017
    ('/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True),
    ('/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM/',False), #newpmx
    ('/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True),
    ('/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',False), #newpmx
    ('/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',False), #newpmx
    ('/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM', False),
    ('/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM',False), #newpmx 4754796
    ('/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM', False),
    ('/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True),
    ('/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM', True),
    #('/WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True), ## in production
    #('/WGToLNuG_PtG-500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True), ## in production
    ('/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM', False),
    ('/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM', False),
    ('/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM', False),
    ('/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True),
    ('/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', False),
    ('/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM', True),
    ('/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True),
    ('/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM', True),
    ('/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM', True),

    # tW samples
    ('/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', True),
    ('/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM', True),
/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM
/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM

    # new TT samples
     ('/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),           #9000000
     ('/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),    #43732445
     ##('/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',False),                 #960752
     ##('/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),                 #8705576
     ##('/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM',False),     #197670000
     ##('/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',False),          #41221873


     ###   2017 signal samples
     ('/MadGraphChargedResonance_WGToLNuG_M1000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M1200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M1400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M1400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M1800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M2000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M2000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M2200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M2200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M250_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M2600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M2800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M300_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M3500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M350_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M350_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M4000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M450_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M700_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M900_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),
     ('/MadGraphChargedResonance_WGToLNuG_M900_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',True ),

     ### 2017 signal pythia
     ('/PythiaChargedResonance_WGToLNuG_M1000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M1200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M1400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M1800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M1800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M2000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M2200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M2400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M250_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M2600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M300_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M300_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M3500_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M3500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M350_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M4000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M450_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M450_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M500_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M600_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
     ('/PythiaChargedResonance_WGToLNuG_M800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',False),
]

mc_samples2018 = [
    # list of MC sample
    # The first arugment is the DAS path for the dataset
    # The second argument controls if the EventWeights are saved (removing them saves disk space)
	#('/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
	('/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-4cores5k_102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',False),
	('/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
	('/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',True),
	('/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM',True),
	('/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',False),
	('/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',True),
	('/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
	('/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',True),
	('/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',True),
    ## Diphoton missing
	('/DiPhotonJets_MGG-80toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', True),
    ## new TT samples
     ('/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2/MINIAODSIM',False),                  #199925998
     ('/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),                       #101550000
     ('/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),                              #64310000


    ###   2018 signal samples
    ('/MadGraphChargedResonance_WGToLNuG_M900_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M900_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M700_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M700_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M450_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M450_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M4000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M4000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M350_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M350_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M3500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M3500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M300_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M300_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M3000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M3000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M250_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M250_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M2000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/MadGraphChargedResonance_WGToLNuG_M1000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',True),
    ('/PythiaChargedResonance_WGToLNuG_M2000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),

    ('/PythiaChargedResonance_WGToLNuG_M1800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M1000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M900_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M900_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M700_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M700_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M450_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M450_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M4000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M4000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M350_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M350_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M3500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M3500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M300_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M300_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M3000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M3000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M250_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M250_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),
    ('/PythiaChargedResonance_WGToLNuG_M2000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',False),



]

if options.year == "2016":	
	data_samples = data_samples2016
	mc_samples = mc_samples2016
	json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

if options.year == "2017":	
	data_samples = data_samples2017
	mc_samples = mc_samples2017
	json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'

if options.year == "2018":	
	data_samples = data_samples2018
	mc_samples = mc_samples2018
    json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-324420_13TeV_PromptReco_Collisions18_JSON.txt'
if options.year == "2018D":	
	data_samples = data_samples2018D
	mc_samples = []
    json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-324420_13TeV_PromptReco_Collisions18_JSON.txt'

config_dir = 'crab_configs'

if not os.path.isdir( config_dir ) :
    os.mkdir(config_dir ) 

submit_commands = []

for path in data_samples : 

    base_name = path.split('/')[1]+'_'+path.split('/')[2]

    fname = '%s/%s.py'%(config_dir, base_name)

    ofile = open(fname, 'w' )

    file_entries = []

    file_entries.append( 'from CRABClient.UserUtilities import config' )
    file_entries.append( 'config = config()' )
    file_entries.append( '' )
    file_entries.append( 'config.General.requestName = "production_%s_%s"' %( options.version, base_name ) )
    file_entries.append( 'config.General.workArea = "crab_projects" ' )
    file_entries.append( 'config.General.transferOutputs = True' )
    file_entries.append( 'config.General.transferLogs = False' )
    file_entries.append( '' )
    file_entries.append( 'config.JobType.pluginName = "Analysis"' )
    file_entries.append( 'config.JobType.psetName = "src/UMDNTuple/UMDNTuple/run_production_cfg.py"' )
    file_entries.append( 'config.JobType.pyCfgParams = ["isMC=0", "year=%i"]' %options.year )
    file_entries.append( '' )
    file_entries.append( 'config.Data.inputDataset = "%s"' %path )
    file_entries.append( 'config.Data.splitting = "LumiBased"' )
    file_entries.append( 'config.Data.unitsPerJob = 100' )
    file_entries.append( 'config.Data.outLFNDirBase = "%s"' %options.outputPath)
    file_entries.append( 'config.Data.publication = False' )
    file_entries.append( 'config.Data.outputDatasetTag = "UMDNTuple_%s"' %options.version )
    file_entries.append( 'config.Data.lumiMask = "%s"' %json_path)
    file_entries.append( '' )
    file_entries.append( 'config.Site.storageSite = "%s"' %options.site )

    for line in file_entries : 
        ofile.write( line + '\n' )

    ofile.close()

    submit_commands.append( 'crab submit --config %s' %( fname ) )





for path, useEventWeights in mc_samples: 

    base_name = path.split('/')[1]

    fname = '%s/%s.py'%(config_dir, base_name)

    ofile = open(fname, 'w' )

    file_entries = []

    file_entries.append('from CRABClient.UserUtilities import config')
    file_entries.append('config = config()')
    file_entries.append('config.General.workArea = "crab_projects"')
    file_entries.append('config.General.transferOutputs = True')
    file_entries.append('config.General.transferLogs = False')
    file_entries.append('config.JobType.pluginName = "Analysis"')
    file_entries.append('config.JobType.psetName = "src/UMDNTuple/UMDNTuple/run_production_cfg.py"')
    file_entries.append('config.Data.outLFNDirBase = "%s"' %options.outputPath)
    file_entries.append('config.Data.publication = False')
    file_entries.append('config.Site.storageSite = "%s"' %options.site)
    file_entries.append('config.Data.outputDatasetTag= "UMDNTuple_%s"' %options.version)
    file_entries.append('config.JobType.pyCfgParams = ["isMC=1","disableEventWeights=%d","year=%i"]' %(not useEventWeights,options.year))
    file_entries.append('config.General.requestName = "production_%s_%s"' %(options.version, base_name))
    file_entries.append('config.Data.inputDataset = "%s"' %path)
    if "DY" in path:
        file_entries.append('config.Data.splitting = "FileBased"')
        file_entries.append('config.Data.unitsPerJob = 10') ##no. files per job
    else:
        file_entries.append('config.Data.splitting = "Automatic"')
        file_entries.append('config.Data.unitsPerJob = 200')

    for line in file_entries : 
        ofile.write( line + '\n' )

    ofile.close()

    submit_commands.append( 'crab submit --config %s' %( fname ) )


submit_file = open('submit_crab.sh', 'w' )
submit_file.write( '#!/bin/bash\n' )

for cmd in submit_commands :
    submit_file.write(cmd + '\n' )


submit_file.close()


