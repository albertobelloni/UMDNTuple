import os
import getpass
import socket
from argparse import ArgumentParser

HOST=socket.gethostname()
USER=getpass.getuser()

p = ArgumentParser(description = "USAGE: python submit_crab.py --year 2016 --version 20200520")

p.add_argument('--version', dest='version', required=True, help='version' )
p.add_argument('--year', dest='year', required=True,  help='year' )
p.add_argument('--outputPath', dest='outputPath', default='/store/user/%s/WGamma' %USER, help='output path on storage site, default=/store/user/%s/WGamma' %USER )
p.add_argument('--site', dest='site', default='T3_US_UMD', help='destination site, default=T3_US_UMD' )
p.add_argument('--dtype', default = 'All', help='process data type: All, MC, Data, Signal' )

options = p.parse_args()


assert any(w in options.dtype for w in ["All","MC","Data","Signal"]), "--dtype must be one of the following: All, MC, Data, Signal"


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
    '/EGamma/Run2018C-17Sep2018-v1/MINIAOD',
    '/EGamma/Run2018B-17Sep2018-v1/MINIAOD',
    '/EGamma/Run2018A-17Sep2018-v2/MINIAOD',
]

data_samples2018D = [
#2018 D
    #'/SingleMuon/Run2018D-PromptReco-v2/MINIAOD',
    #'/EGamma/Run2018D-PromptReco-v2/MINIAOD',
    '/SingleMuon/Run2018D-22Jan2019-v2/MINIAOD',
    '/EGamma/Run2018D-22Jan2019-v2/MINIAOD',
]


mc_samples2016 = [
    # list of MC sample
    # The first arugment is the DAS path for the dataset
    # The second argument controls if the EventWeights are saved (removing them saves disk space)
    '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM',
    #'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    #'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
    '/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    '/WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM',
    '/WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
    '/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
    '/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM',
    '/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM',
    '/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
    '/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
    '/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
    '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
    '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM',
    '/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
    '/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',


#     #QCD samples
#    '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#    '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#    '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
#    '/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
#    '/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
#    '/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#
#    '/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#    '/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    '/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
]


signal_samples2016 = [
    '/MadGraphChargedResonance_WGToLNu_M900_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M900_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M800_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M800_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M700_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M700_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M600_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M600_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M500_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M500_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M450_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M450_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M400_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M400_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M4000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M4000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M350_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M350_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M3500_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M3500_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M300_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M300_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M3000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M3000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2800_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2800_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2600_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2600_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M250_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M250_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2400_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2400_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2200_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2200_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M200_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M200_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M2000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1800_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1800_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1600_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1600_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1400_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1400_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1200_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1200_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1000_width5/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNu_M1000_width0p01/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',

    ## FIXME: missing reminiaod pythia samples
    ## only older re-reco available: cannot be run out of the box now, at least because some of the tags are different.
    #'/PythiaChargedResonance_WGToLNu_M900_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M900_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M700_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M700_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M500_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M500_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M450_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M450_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M4000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M4000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M350_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M350_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M3500_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M3500_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M300_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M300_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M3000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M3000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M250_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M250_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M2000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    #'/PythiaChargedResonance_WGToLNu_M1000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    ]

mc_samples2017 = [
    ## 2017
    '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM', #newpmx
    '/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM', #newpmx
    '/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM', #newpmx
    '/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM', #newpmx
    '/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
    '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
    '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
    '/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM',
    '/WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WGToLNuG_PtG-500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
    '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM',
    '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
    '/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
    '/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
    '/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM',
    ]


signal_samples2017=[
    # ###   2017 signal samples
    "/MadGraphChargedResonance_WGToLNuG_M1000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1600_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M1800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M250_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M250_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2600_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M2800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M3000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M3000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M300_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M300_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M3500_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M3500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
   "/MadGraphChargedResonance_WGToLNuG_M350_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M350_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M4000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M4000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M450_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M450_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M500_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M600_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M700_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M700_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M900_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/MadGraphChargedResonance_WGToLNuG_M900_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    # ### 2017 signal pythia
    "/PythiaChargedResonance_WGToLNuG_M1800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1600_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M1000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2200_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2200_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M250_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M250_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2600_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M2800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M3000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M3000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M300_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M300_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M3500_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M3500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M350_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M350_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M4000_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M4000_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M400_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M400_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M450_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M450_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M500_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M500_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M600_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M600_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M700_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M700_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M800_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M800_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M900_width0p01/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    "/PythiaChargedResonance_WGToLNuG_M900_width5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
]

mc_samples2018 = [
    # list of MC sample
    # The first arugment is the DAS path for the dataset
    # The second argument controls if the EventWeights are saved (removing them saves disk space)
    '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM', ## more statistics
    '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-4cores5k_102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',
    '/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',
    '/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2/MINIAODSIM',
    '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM',
    '/WGToLNuG_PtG-500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
    '/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',
    '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',
    '/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',
    '/DiPhotonJets_MGG-80toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    ]

signal_samples2018=[
    ###   2018 signal samples
    '/MadGraphChargedResonance_WGToLNuG_M900_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M900_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M700_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M700_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M450_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M450_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M4000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M4000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M350_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M350_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M3500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M3500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M300_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M300_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M3000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M3000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M250_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M250_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M2000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/MadGraphChargedResonance_WGToLNuG_M1000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',

    '/PythiaChargedResonance_WGToLNuG_M1800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M1000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M900_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M900_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M700_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M700_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M450_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M450_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M4000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M4000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M350_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M350_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M3500_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M3500_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M300_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M300_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M3000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M3000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2800_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2800_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2600_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2600_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M250_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M250_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2400_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2400_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M200_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M200_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2000_width5/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
    '/PythiaChargedResonance_WGToLNuG_M2000_width0p01/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',
]


if options.year == "2016":  
    data_samples = data_samples2016
    mc_samples = mc_samples2016
    signal_samples = signal_samples2016
    json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

if options.year == "2017":
    data_samples = data_samples2017
    mc_samples = mc_samples2017
    signal_samples= signal_samples2017
    json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'

if options.year == "2018":
    data_samples = data_samples2018
    mc_samples = mc_samples2018
    signal_samples= signal_samples2018
    json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
if options.year == "2018D":
    data_samples = data_samples2018D
    mc_samples = []
    json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
    options.year = "2018" ## NOTE for tag on output name

config_dir = 'crab_configs'

if not os.path.isdir( config_dir ) :
    os.mkdir(config_dir )

submit_commands = []

if "All" in options.dtype or "Data" in options.dtype:

    for path in data_samples :

        base_name = path.split('/')[1]+'_'+path.split('/')[2]

        fname = '%s/%s.py'%(config_dir, base_name)

        ofile = open(fname, 'w' )

        file_entries = []

        file_entries.append( 'from CRABClient.UserUtilities import config' )
        file_entries.append( 'config = config()' )
        file_entries.append( '' )
        file_entries.append( 'config.General.requestName = "production_data_%s_%s"' %( options.version, base_name ) )
        file_entries.append( 'config.General.workArea = "crab_projects" ' )
        file_entries.append( 'config.General.transferOutputs = True' )
        file_entries.append( 'config.General.transferLogs = False' )
        file_entries.append( '' )
        file_entries.append( 'config.JobType.pluginName = "Analysis"' )
        file_entries.append( 'config.JobType.psetName = "src/UMDNTuple/UMDNTuple/run_production_cfg.py"' )
        file_entries.append( 'config.JobType.pyCfgParams = ["isMC=0", "year=%s"]' %options.year )
        file_entries.append( '' )
        file_entries.append( 'config.Data.inputDataset = "%s"' %path )
        file_entries.append( 'config.Data.splitting = "LumiBased"' )
        file_entries.append( 'config.Data.unitsPerJob = 100' )
        file_entries.append( 'config.Data.outLFNDirBase = "%s"' %options.outputPath)
        file_entries.append( 'config.Data.publication = False' )
        file_entries.append( 'config.Data.outputDatasetTag = "UMDNTuple_%s_%s"' %(options.version, options.year) )
        file_entries.append( 'config.Data.lumiMask = "%s"' %json_path)
        file_entries.append( '' )
        file_entries.append( 'config.Site.storageSite = "%s"' %options.site )
        file_entries.append('config.JobType.allowUndistributedCMSSW = True')

        for line in file_entries :
            ofile.write( line + '\n' )

        ofile.close()

        submit_commands.append( 'crab submit --config %s' %( fname ) )



if "All" in options.dtype or "Signal" in options.dtype:
    for path in signal_samples:

        processed = path.split('/')[2]
        if '_ext' in processed:
            ext = 'ext' + processed.rsplit('_ext', 1)[1]
        else:
            ext = processed.rsplit('-', 1)[1]
        base_name = path.split('/')[1] + '_' + ext

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
        file_entries.append('config.Data.outputDatasetTag= "UMDNTuple_%s_%s"' %(options.version,options.year))
        file_entries.append('config.JobType.pyCfgParams = ["isMC=1","year=%s"]' %(options.year))
        file_entries.append('config.General.requestName = "production_signal_%s_%s_%s"' %(options.version, base_name, options.year))
        file_entries.append('config.Data.inputDataset = "%s"' %path)
        file_entries.append('config.JobType.allowUndistributedCMSSW = True')
        file_entries.append('config.Data.splitting = "FileBased"')
        file_entries.append('config.Data.unitsPerJob = 100') ##no. files per job

        for line in file_entries : 
            ofile.write( line + '\n' )

        ofile.close()

        submit_commands.append( 'crab submit --config %s' %( fname ) )


if "All" in options.dtype or "MC" in options.dtype:
    for path in mc_samples:

        processed = path.split('/')[2]
        if '_ext' in processed:
            ext = 'ext' + processed.rsplit('_ext', 1)[1]
        else:
            ext = processed.rsplit('-', 1)[1]
        base_name = path.split('/')[1] + '_' + ext

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
        file_entries.append('config.Data.outputDatasetTag= "UMDNTuple_%s_%s"' %(options.version,options.year))
        file_entries.append('config.JobType.pyCfgParams = ["isMC=1","year=%s"]' %(options.year))
        file_entries.append('config.General.requestName = "production_mc_%s_%s_%s"' %(options.version, base_name, options.year))
        file_entries.append('config.Data.inputDataset = "%s"' %path)
        file_entries.append('config.JobType.allowUndistributedCMSSW = True')
        if "DY" in path:
            file_entries.append('config.Data.splitting = "FileBased"')
            file_entries.append('config.Data.unitsPerJob = 5') ##no. files per job
            file_entries.append('config.JobType.maxJobRuntimeMin = 2500')
        else:
            file_entries.append('config.Data.splitting = "Automatic"')
            file_entries.append('config.Data.unitsPerJob = 1500')

        for line in file_entries : 
            ofile.write( line + '\n' )

        ofile.close()

        submit_commands.append( 'crab submit --config %s' %( fname ) )


submit_file = open('submit_crab.sh', 'w' )
submit_file.write( '#!/bin/bash\n' )

for cmd in submit_commands :
    submit_file.write(cmd + '\n' )


submit_file.close()


