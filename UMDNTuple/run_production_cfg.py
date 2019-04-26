import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
import re

process = cms.Process("UMDNTuple")

# setup 'analysis'  options
opt = VarParsing.VarParsing ('analysis')

opt.register('isMC', -1, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, 'Flag indicating if the input samples are from MC (1) or from the detector (0).')
opt.register('year', 2016, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, 'Flag indicating run year (2016-2018). Default to 2016. ')
opt.register('nEvents', 1000, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, 'Number of events to analyze')
opt.register('disableEventWeights', 0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, 'Set to 1 to disable event weights')

#input files. Can be changed on the command line with the option inputFiles=...
opt.inputFiles = [
    #'file:/data/users/jkunkle/Samples/aQGC_WWW_SingleLepton_LO/Job_0000/MakeMINIAOD/aQGC_WWW_SingleLepton_LO_MINIAOD.root',
    #'file:/data/users/jkunkle/Samples/WGamma/02FE572F-88DA-E611-8CAB-001E67792884.root',
    #'file:/data/users/jkunkle/Samples/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAOD/08F5FD50-23BC-E611-A4C2-00259073E3DA.root',
    #'file:/afs/cern.ch/work/y/yofeng/public/WGamma/SignalMiniAOD/FEAAD8B5-E7FC-E611-81C1-008CFA197B74.root'
    #'root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleMuon/MINIAOD/07Aug17_ver1-v1/70000/F8E02A2B-0E7F-E711-BC53-0CC47A4D761A.root', #rereco legacy16 @ Aug17
    #'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/90000/FE8A7852-66E4-E611-B5D0-002590E7E01A.root', # DY MC 2016

	#'/store/data/Run2016H/SingleElectron/MINIAOD/17Jul2018-v1/00000/582D84C6-EB8B-E811-8313-0025905B861C.root', ##SingleElectron2016H re-miniaod
	'file:/eos/cms/store/user/kawong/582D84C6-EB8B-E811-8313-0025905B861C.root', ##SingleElectron2016H re-miniaod

	#'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/100000/0C2AEF4D-1FBF-E811-A04F-B496910A80F4.root', ##2016 DY MC re-miniaod (v3)
	#'file:/eos/cms/store/user/kawong/0C2AEF4D-1FBF-E811-A04F-B496910A80F4.root', ##2016 DY MC re-miniaod (v3)

    #'/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/04F71189-4742-E811-AA48-008CFAC9157C.root',
    'file:/eos/cms/store/user/kawong/04F71189-4742-E811-AA48-008CFAC9157C.root',

	#'/store/data/Run2017B/SingleElectron/MINIAOD/31Mar2018-v1/30000/40BCA89D-2C38-E811-9682-008CFAC93CF8.root' 
    #'file:/eos/cms/store/user/kawong/40BCA89D-2C38-E811-9682-008CFAC93CF8.root', # 2017 SingleElectron

    #'/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/910000/ECC11159-F647-E811-A157-001E67792510.root', # DY MC 2017 Madgraph RecoSIM step
    #'root://cms-xrd-global.cern.ch//store/data/Run2016G/SingleElectron/MINIAOD/23Sep2016-v1/100000/004A7893-A990-E611-B29F-002590E7DE36.root'
    #'root://cms-xrd-global.cern.ch//store/data/Run2016G/SingleElectron/MINIAOD/03Feb2017-v1/50000/004A75AB-B2EA-E611-B000-24BE05CEFDF1.root',
]
opt.outputFile = "ntuple.root"


#defaults
#opt.nEvents = 1000
opt.disableEventWeights = 0
opt.parseArguments()

process.source = cms.Source("PoolSource",
                            fileNames =  cms.untracked.vstring(opt.inputFiles))

# try to determine if its data or MC based on the name
# otherwise request the user to provide isMC=
print "isMC: ", opt.isMC
if opt.isMC < 0 and len(process.source.fileNames) > 0:
  if re.match(r'.*/(MINI)?AODSIM/.*', process.source.fileNames[0]):
    print "MC dataset detected."
    opt.isMC = 1
  elif re.match(r'.*/(MINI)?AOD/.*', process.source.fileNames[0]):
    print "Real data dataset detected."
    opt.isMC = 0

if opt.isMC < 0:
  raise Exception("Failed to detect data type. Data type need to be specify with the isMC cmsRun command line option")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(opt.nEvents))
#process.source.skipEvents = cms.untracked.uint32(1000)
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck') 

process.TFileService = cms.Service("TFileService",
                                   #fileName = cms.string('ntuple.root' )
								  	fileName = cms.string(opt.outputFile)
)
			


#-----------------------------------------------------
# Configure message logger
#-----------------------------------------------------
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
#process.MessageLogger.suppressWarning = cms.untracked.vstring('ecalLaserCorrFilter','manystripclus53X','toomanystripclus53X')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
#process.options.allowUnscheduled = cms.untracked.bool(True)
#-----------------------------------------------------

# Load the standard set of configuration modules
# may not need this for MiniAOD v2
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

#-----------------------------------
# Load additional MET Filters
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#How_to_run_the_Bad_Charged_Hadro

process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
process.BadPFMuonFilter.taggingMode = cms.bool( True )

process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
process.BadChargedCandidateFilter.taggingMode = cms.bool( True )




#------------------------------------
#Condition DB tag
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if opt.year == 2016: 
	dataGlobalTag = '94X_dataRun2_v10'
	mcGlobalTag = '94X_mcRun2_asymptotic_v3'
	egamma_era='2016-Legacy'
	prefire_era="2016BtoH"
if opt.year == 2017:
	dataGlobalTag = '94X_dataRun2_v11'
	mcGlobalTag = '94X_mc2017_realistic_v17'
	egamma_era='2017-Nov17ReReco'
	prefire_era="2017BtoF"

if opt.isMC == 1:
  process.GlobalTag = GlobalTag(process.GlobalTag, mcGlobalTag, '')
else:
  process.GlobalTag = GlobalTag(process.GlobalTag, dataGlobalTag, '')


#------------------------------------
# load Egamma id
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
if opt.year == 2016:
	setupEgammaPostRecoSeq(process, 
						applyEnergyCorrections=False,
                       	era=egamma_era)  #era is new to select between 2016 / 2017,  it defaults to 2017
if opt.year == 2017:
	setupEgammaPostRecoSeq(process,
                       	runVID=False, ##saves CPU time by not needlessly re-running VID, if you want the Fall17V2 IDs, set this to True or remove (default is True)
                       	era=egamma_era)
#a sequence egammaPostRecoSeq has now been created and should be added to your path, eg process.p=cms.Path(process.egammaPostRecoSeq)

#--------------------------------------------

#--------------------------------------------
# define the triggers that we want to save
if opt.year == 2017:
	trigger_map = cms.untracked.vstring( 
    # Muon triggers
    '0:HLT_Mu8',
    '1:HLT_Mu17',
    '2:HLT_Mu19',
    '3:HLT_Mu20',
    '4:HLT_Mu27',
    '5:HLT_Mu50',
    '6:HLT_Mu55',
    '7:HLT_Mu8_TrkIsoVVL', 
    '8:HLT_IsoMu20', 
    '9:HLT_IsoMu24', # intended trigger
    '10:HLT_IsoMu27', # intended trigger
    '11:HLT_IsoMu30', 
    '12:HLT_IsoMu24_eta2p1', 
    '13:HLT_IsoMu27_LooseChargedIsoPFTau20_SingleL1',
    '14:HLT_IsoMu27_MediumChargedIsoPFTau20_SingleL1',
    '15:HLT_IsoMu27_TightChargedIsoPFTau20_SingleL1',
    # Electron triggers
    '20:HLT_Ele20_WPLoose_Gsf',
    '21:HLT_Ele20_WPTight_Gsf',
    '22:HLT_Ele20_eta2p1_WPLoose_Gsf',
    '23:HLT_Ele28_eta2p1_WPTight_Gsf_HT150',
    '24:HLT_Ele27_WPTight_Gsf',  
    '25:HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned',
    '26:HLT_Ele32_WPTight_Gsf',
    '27:HLT_Ele32_WPTight_Gsf_L1DoubleEG',
    '28:HLT_Ele35_WPTight_Gsf', # intended trigger
    '29:HLT_Ele35_WPTight_Gsf_L1EGMT',
    '30:HLT_Ele38_WPTight_Gsf',
    '31:HLT_Ele40_WPTight_Gsf',
    '32:HLT_Ele135_CaloIdVT_GsfTrkIdT',
    '33:HLT_Ele145_CaloIdVT_GsfTrkIdT',
    '34:HLT_Ele200_CaloIdVT_GsfTrkIdT',
    '35:HLT_Ele250_CaloIdVT_GsfTrkIdT',
    '36:HLT_Ele300_CaloIdVT_GsfTrkIdT',
    # Photon triggers
    '40:HLT_Photon25',
    '41:HLT_Photon33',
    '42:HLT_Photon50', 
    '43:HLT_Photon75', 
    '44:HLT_Photon90', 
    '45:HLT_Photon120', 
    '46:HLT_Photon150', 
    '47:HLT_Photon175', 
    '48:HLT_Photon200',  ## intended trigger
    '49:HLT_Photon300_noHE',
    '50:HLT_Photon50_R9Id90_HE10_IsoM',
    '51:HLT_Photon75_R9Id90_HE10_IsoM',
    '52:HLT_Photon90_R9Id90_HE10_IsoM',
    '53:HLT_Photon120_R9Id90_HE10_IsoM',
    '54:HLT_Photon165_R9Id90_HE10_IsoM',
    '55:HLT_Photon20_HoverELoose',
    '56:HLT_Photon30_HoverELoose',
    '57:HLT_Photon40_HoverELoose',
    '58:HLT_Photon50_HoverELoose',
    '59:HLT_Photon60_HoverELoose',
    '60:HLT_Photon120_R9Id90_HE10_IsoM',
    '61:HLT_Photon165_R9Id90_HE10_IsoM',
    '62:HLT_Photon50_R9Id90_HE10_IsoM',
    '63:HLT_Photon75_R9Id90_HE10_IsoM',
    '64:HLT_Photon90_R9Id90_HE10_IsoM',
    '65:HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL',
    '66:HLT_Photon60_R9Id90_CaloIdL_IsoL',
    '67:HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350MinPFJet15',
    '68:HLT_Photon50_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_PFMET50',
    '69:HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3',
    '70:HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ600DEta3',
    #DiMuon triggers
    '80:HLT_Mu18_Mu9',
    '81:HLT_Mu18_Mu9_DZ',
    '82:HLT_Mu18_Mu9_SameSign',
    '83:HLT_Mu18_Mu9_SameSign_DZ',
    '84:HLT_Mu20_Mu10',
    '85:HLT_Mu20_Mu10_DZ',
    '86:HLT_Mu20_Mu10_SameSign',
    '87:HLT_Mu20_Mu10_SameSign_DZ',
    '88:HLT_Mu23_Mu12',
    '89:HLT_Mu23_Mu12_DZ',
    '90:HLT_Mu23_Mu12_SameSign',
    '91:HLT_Mu23_Mu12_SameSign_DZ',
    '92:HLT_Mu37_TkMu27',
    '93:HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL',
    '94:HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 
    '95:HLT_Mu20_TkMu0_Phi',
    '96:HLT_Mu25_TkMu0_Onia',
    '97:HLT_Mu25_TkMu0_Phi',
    '98:HLT_Mu30_TkMu0_Onia',
    '99:HLT_DoubleIsoMu20_eta2p1',
    '100:HLT_DoubleIsoMu24_eta2p1',
    '101:HLT_DoubleL2Mu50',
    #DiElectron triggers
    '110:HLT_DoubleEle33_CaloIdL_MW',
    '111:HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 
    '112:HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL',
    '113:HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL', 
    '114:HLT_DoubleEle24_eta2p1_WPTight_Gsf',
    '115:HLT_DoubleEle25_CaloIdL_MW',
    '116:HLT_DoubleEle27_CaloIdL_MW',
    '117:HLT_Ele27_Ele37_CaloIdL_MW',
    # muon + egamma triggers
    '120:HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 
    '121:HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ',
    '122:HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL',
    '123:HLT_Mu24_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',
    '124:HLT_Mu17_Photon30_IsoCaloId',
    '125:HLT_Mu27_Ele37_CaloIdL_MW',
    '125:HLT_Mu37_Ele27_CaloIdL_MW',
    #DiPhoton triggers
    '130:HLT_DoublePhoton33_CaloIdL',
    '131:HLT_DoublePhoton70', 
    '132:HLT_DoublePhoton85',
    )

if opt.year == 2016: 
	trigger_map2016 = cms.untracked.vstring( 
    # Muon triggers
    '0:HLT_Mu8',
    '1:HLT_Mu17',
    '2:HLT_Mu20',
    '3:HLT_Mu24',
    '4:HLT_Mu27',
    '5:HLT_Mu34',
    '6:HLT_Mu50',
    '7:HLT_Mu55',
    '8:HLT_Mu300',
    '9:HLT_Mu350',
    '10:HLT_Mu24_eta2p1',
    '11:HLT_Mu45_eta2p1',
    '12:HLT_Mu50_eta2p1',
    '13:HLT_Mu8_TrkIsoVVL',
    '14:HLT_Mu17_TrkIsoVVL',
    '15:HLT_Mu24_TrkIsoVVL',
    '16:HLT_Mu34_TrkIsoVVL',
    '17:HLT_TkMu20',
    '18:HLT_TkMu27',
    '19:HLT_TkMu24_eta2p1',
    '20:HLT_IsoMu18',
    '21:HLT_IsoMu20',
    '22:HLT_IsoMu22',
    '23:HLT_IsoMu24',
    '24:HLT_IsoMu27',
    '25:HLT_IsoMu17_eta2p1',
    '26:HLT_IsoMu20_eta2p1',
    '27:HLT_IsoMu24_eta2p1',
    '28:HLT_IsoTkMu18',
    '29:HLT_IsoTkMu20',
    '30:HLT_IsoTkMu22',
    '31:HLT_IsoTkMu24',
    '32:HLT_IsoTkMu27',
    '33:HLT_IsoTkMu20_eta2p1',
    '34:HLT_IsoTkMu24_eta2p1',
    '35:HLT_Mu16_eta2p1_CaloMET30',
    '36:HLT_IsoMu16_eta2p1_CaloMET30',
    # Electron triggers
    '50:HLT_Ele22_eta2p1_WPLoose_Gsf',
    '51:HLT_Ele22_eta2p1_WPTight_Gsf',
    '52:HLT_Ele23_WPLoose_Gsf',
    '53:HLT_Ele24_eta2p1_WPLoose_Gsf',
    '54:HLT_Ele25_WPTight_Gsf',
    '55:HLT_Ele25_eta2p1_WPLoose_Gsf',
    '56:HLT_Ele25_eta2p1_WPTight_Gsf',
    '57:HLT_Ele27_WPLoose_Gsf',
    '58:HLT_Ele27_WPTight_Gsf',
    '59:HLT_Ele27_eta2p1_WPLoose_Gsf',
    '60:HLT_Ele27_eta2p1_WPTight_Gsf',
    '61:HLT_Ele32_eta2p1_WPLoose_Gsf',
    '62:HLT_Ele32_eta2p1_WPTight_Gsf',
    '63:HLT_Ele35_WPLoose_Gsf',
    '64:HLT_Ele45_WPLoose_Gsf',
    '65:HLT_Ele105_CaloIdVT_GsfTrkIdT',
    '66:HLT_Ele115_CaloIdVT_GsfTrkIdT',
    '67:HLT_Ele12_CaloIdL_TrackIdL_IsoVL',
    '68:HLT_Ele17_CaloIdL_GsfTrkIdVL',
    '69:HLT_Ele17_CaloIdL_TrackIdL_IsoVL',
    '70:HLT_Ele23_CaloIdL_TrackIdL_IsoVL',
    # Photon triggers
    '100:HLT_Photon250_NoHE',
    '101:HLT_Photon300_NoHE',
    '102:HLT_Photon22',
    '103:HLT_Photon30',
    '104:HLT_Photon36',
    '105:HLT_Photon50',
    '106:HLT_Photon75',
    '107:HLT_Photon90',
    '108:HLT_Photon120',
    '109:HLT_Photon175',
    '110:HLT_Photon500',
    '111:HLT_Photon600',
    '112:HLT_Photon165_HE10',
    '113:HLT_Photon22_R9Id90_HE10_IsoM',
    '114:HLT_Photon30_R9Id90_HE10_IsoM',
    '115:HLT_Photon36_R9Id90_HE10_IsoM',
    '116:HLT_Photon50_R9Id90_HE10_IsoM',
    '117:HLT_Photon75_R9Id90_HE10_IsoM',
    '118:HLT_Photon90_R9Id90_HE10_IsoM',
    '119:HLT_Photon120_R9Id90_HE10_IsoM',
    '120:HLT_Photon165_R9Id90_HE10_IsoM',
    '121:HLT_Photon22_R9Id90_HE10_Iso40_EBOnly',
    '122:HLT_Photon36_R9Id90_HE10_Iso40_EBOnly',
    '123:HLT_Photon50_R9Id90_HE10_Iso40_EBOnly',
    '124:HLT_Photon75_R9Id90_HE10_Iso40_EBOnly',
    '125:HLT_Photon90_R9Id90_HE10_Iso40_EBOnly',
    '126:HLT_Photon120_R9Id90_HE10_Iso40_EBOnly',
    #DiMuon triggers
    '150:HLT_Mu17_Mu8',
    '151:HLT_Mu17_Mu8_DZ',
    '152:HLT_Mu17_Mu8_SameSign_DZ',
    '153:HLT_Mu20_Mu10',
    '154:HLT_Mu20_Mu10_DZ',
    '155:HLT_Mu20_Mu10_SameSign_DZ',
    '156:HLT_Mu17_TkMu8_DZ',
    '157:HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL',
    '158:HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ',
    '159:HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL',
    '160:HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ',
    '161:HLT_Mu27_TkMu8',
    '162:HLT_Mu30_TkMu11',
    '163:HLT_Mu40_TkMu11',
    '164:HLT_DoubleIsoMu17_eta2p1',
    '165:HLT_DoubleIsoMu17_eta2p1_noDzCut',
    #DiElectron triggers
    '200:HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf',
    '201:HLT_DoubleEle25_CaloIdL_GsfTrkIdVL',
    '202:HLT_DoubleEle33_CaloIdL',
    '203:HLT_DoubleEle33_CaloIdL_MW',
    '204:HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW',
    '205:HLT_DoubleEle33_CaloIdL_GsfTrkIdVL',
    '206:HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL',
    '207:HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',
    '208:HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',
    '209:HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL',
    '210:HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL',
    '211:HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL',
    # muon + egamma triggers
    '212:HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL',
    '213:HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL',
    '214:HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL',
    '215:HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL',
    '216:HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL',
    '217:HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL',
    '218:HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL',
    '219:HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL',
    '220:HLT_Mu17_Photon30_CaloIdL_L1ISO',
    #DiPhoton triggers
    '250:HLT_DoublePhoton40',
    '251:HLT_DoublePhoton50',
    '252:HLT_DoublePhoton60',
    '253:HLT_DoublePhoton85',
    '254:HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60',
    '255:HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15',
    '256:HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90',
    '257:HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelSeedMatch_Mass70',
    '258:HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55',
    '259:HLT_Diphoton30_18_Solid_R9Id_AND_IsoCaloId_AND_HE_R9Id_Mass55',
    '260:HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95',
    '261:HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55',
    '262:HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15',
    )
filter_map = cms.untracked.vstring( 
    '1:Flag_HBHENoiseFilter',
    '2:Flag_HBHENoiseIsoFilter',
    '3:Flag_CSCTightHaloFilter',
    '4:Flag_CSCTightHaloTrkMuUnvetoFilter',
    '5:Flag_CSCTightHalo2015Filter',
    '6:Flag_globalTightHalo2016Filter',
    '7:Flag_globalSuperTightHalo2016Filter',
    '8:Flag_HcalStripHaloFilter',
    '9:Flag_hcalLaserEventFilter',
    '10:Flag_EcalDeadCellTriggerPrimitiveFilter',
    '11:Flag_EcalDeadCellBoundaryEnergyFilter',
    '12:Flag_goodVertices',
    '13:Flag_eeBadScFilter',
    '14:Flag_ecalLaserCorrFilter',
    '15:Flag_trkPOGFilters',
    '16:Flag_chargedHadronTrackResolutionFilter',
    '17:Flag_muonBadTrackFilter',
    '18:Flag_trkPOG_manystripclus53X',
    '19:Flag_trkPOG_toomanystripclus53X',
    '20:Flag_trkPOG_logErrorTooManyClusters',
    # these are added 'manually' because they are not availbe in the miniAOD
    '100:Flag_BadChargedCandidateFilter',
    '101:Flag_BadPFMuonFilter',
)


from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
    DataEra = cms.string(prefire_era),
    UseJetEMPt = cms.bool(False),
    PrefiringRateSystematicUncty = cms.double(0.2),
    SkipWarnings = False)

if opt.year == 2016:
        elecIdVeryLooseStr = cms.untracked.string("cutBasedElectronID-Summer16-80X-V1-veto")
        elecIdLooseStr     = cms.untracked.string("cutBasedElectronID-Summer16-80X-V1-loose")
        elecIdMediumStr    = cms.untracked.string("cutBasedElectronID-Summer16-80X-V1-medium")
        elecIdTightStr     = cms.untracked.string("cutBasedElectronID-Summer16-80X-V1-tight")
        phoIdLooseStr  = cms.untracked.string("cutBasedPhotonID-Spring16-V2p2-loose")
        phoIdMediumStr = cms.untracked.string("cutBasedPhotonID-Spring16-V2p2-medium")
        phoIdTightStr  = cms.untracked.string("cutBasedPhotonID-Spring16-V2p2-tight")
if opt.year == 2017:
        elecIdVeryLooseStr = cms.untracked.string("cutBasedElectronID-Fall17-94X-V1-veto")
        elecIdLooseStr     = cms.untracked.string("cutBasedElectronID-Fall17-94X-V1-loose")
        elecIdMediumStr    = cms.untracked.string("cutBasedElectronID-Fall17-94X-V1-medium")
        elecIdTightStr     = cms.untracked.string("cutBasedElectronID-Fall17-94X-V1-tight")
        phoIdLooseStr  = cms.untracked.string("cutBasedPhotonID-Fall17-94X-V1-loose")
        phoIdMediumStr = cms.untracked.string("cutBasedPhotonID-Fall17-94X-V1-medium")
        phoIdTightStr  = cms.untracked.string("cutBasedPhotonID-Fall17-94X-V1-tight")

process.UMDNTuple = cms.EDAnalyzer("UMDNTuple",
    electronTag = cms.untracked.InputTag('slimmedElectrons'),
        elecIdVeryLooseStr = elecIdVeryLooseStr ,
        elecIdLooseStr     = elecIdLooseStr     , 
        elecIdMediumStr    = elecIdMediumStr    ,
        elecIdTightStr     = elecIdTightStr     ,
        #elecIdHLTStr       = cms.untracked.string("cutBasedElectronHLTPreselection-Summer16-V1"),
        elecIdHEEPStr      = cms.untracked.string("heepElectronID-HEEPV70"),
        # electron energy scale and smearings
        elecEneCalibStr    = cms.untracked.string('ecalTrkEnergyPostCorr'),
    muonTag     = cms.untracked.InputTag('slimmedMuons'),
    photonTag   = cms.untracked.InputTag('slimmedPhotons'),
        phoChIsoStr    = cms.untracked.string("phoChargedIsolation"),
        phoNeuIsoStr   = cms.untracked.string("phoNeutralHadronIsolation"),
        phoPhoIsoStr   = cms.untracked.string("phoPhotonIsolation"),
        phoIdLooseStr  = phoIdLooseStr  ,
        phoIdMediumStr = phoIdMediumStr ,
        phoIdTightStr  = phoIdTightStr  ,
        # photon energy scale and smearings
        phoEneCalibStr = cms.untracked.string("ecalEnergyPostCorr"),
    jetTag     = cms.untracked.InputTag('slimmedJets'),
    fatjetTag     = cms.untracked.InputTag('slimmedJetsAK8'),
    metTag     = cms.untracked.InputTag('slimmedMETs'),
    triggerTag  = cms.untracked.InputTag('TriggerResults', '', 'HLT'),
    triggerObjTag = cms.untracked.InputTag('selectedPatTrigger'),
    #triggerObjTag = cms.untracked.InputTag('slimmedPatTrigger'), # 2017
    triggerMap = trigger_map,
    metFilterTag  = cms.untracked.InputTag('TriggerResults', '', 'RECO'),
    BadChargedCandidateFilter = cms.untracked.InputTag('BadChargedCandidateFilter'),
    BadPFMuonFilter = cms.untracked.InputTag('BadPFMuonFilter'),
    metFilterMap = filter_map,

    beamSpotTag = cms.untracked.InputTag('offlineBeamSpot'),
    conversionsTag = cms.untracked.InputTag('reducedEgamma', 'reducedConversions' ),
    #conversionsTag = cms.untracked.InputTag('allConversions' ),
    verticesTag  = cms.untracked.InputTag('offlineSlimmedPrimaryVertices'),
    rhoTag  = cms.untracked.InputTag('fixedGridRhoFastjetAll'),
    prefTag = cms.untracked.InputTag('prefiringweight:NonPrefiringProb'),
    prefupTag = cms.untracked.InputTag('prefiringweight:NonPrefiringProbUp'),
    prefdownTag = cms.untracked.InputTag('prefiringweight:NonPrefiringProbDown'),
    puTag   = cms.untracked.InputTag('slimmedAddPileupInfo'),
    lheEventTag  = cms.untracked.InputTag('externalLHEProducer'),
    lheRunTag  = cms.untracked.InputTag('externalLHEProducer'),
    generatorTag = cms.untracked.InputTag('generator'),
    genParticleTag = cms.untracked.InputTag('prunedGenParticles'),

    electronDetailLevel = cms.untracked.int32( 1 ),
    photonDetailLevel = cms.untracked.int32( 1 ),
    muonDetailLevel = cms.untracked.int32( 1 ),
    jetDetailLevel = cms.untracked.int32( 1 ),
    isMC = cms.untracked.int32( opt.isMC ),
    disableEventWeights = cms.untracked.bool( opt.disableEventWeights ),
    prefix_el   = cms.untracked.string("el"),
    prefix_mu   = cms.untracked.string("mu"),
    prefix_ph   = cms.untracked.string("ph"),
    prefix_jet  = cms.untracked.string("jet"),
    prefix_fjet = cms.untracked.string("fjet"),
    prefix_trig = cms.untracked.string("passTrig"),
    prefix_gen  = cms.untracked.string("gen"),
    prefix_met  = cms.untracked.string("met"),
                                   
    electronMinPt = cms.untracked.double( 10 ),
    muonMinPt = cms.untracked.double( 10 ),
    photonMinPt = cms.untracked.double( 20 ),
    jetMinPt = cms.untracked.double( 30 ),
    fjetMinPt = cms.untracked.double( 200 ),
    genMinPt = cms.untracked.double( 5 ),


)


process.p = cms.Path()

process.p += process.egammaPostRecoSeq
# run additional MET filters
process.p += process.BadPFMuonFilter
process.p += process.BadChargedCandidateFilter
if opt.isMC: process.p += process.prefiringweight

process.p += process.UMDNTuple

