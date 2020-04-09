#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "UMDNTuple/UMDNTuple/interface/UMDNTuple.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

UMDNTuple::UMDNTuple( const edm::ParameterSet & iConfig ) :
    _produceEvent(true),
    _produceElecs(true),
    _produceMuons(true),
    _producePhots(true),
    _produceJets(true),
    _produceFJets(true),
    _produceMET(true),
    _produceMETFilter(true),
    _produceTrig(true),
    _produceGen(true),
    _produceDeepMET(false),
    _isMC( -1 )
{
    edm::Service<TFileService> fs;


    // Get config flags
    if( !iConfig.exists( "isMC" ) ) {
        throw cms::Exception("CorruptData")
        << "Must provide isMC flag so we can handle the data/MC properly";
    }

    _isMC = iConfig.getUntrackedParameter<int>("isMC");
    _doPref = iConfig.getUntrackedParameter<bool>("doPref");

    bool disableEventWeights = false;
    if( iConfig.exists("disableEventWeights" ) ) {
        disableEventWeights = iConfig.getUntrackedParameter<bool>("disableEventWeights");
    }

    _produceDeepMET = iConfig.getUntrackedParameter<bool>("doDeepMET");

    // Create tree to store event data
    _myTree = fs->make<TTree>( "EventTree", "EventTree" );
    // Create tree to store metadata
    _weightInfoTree = fs->make<TTree>( "WeightInfoTree", "WeightInfoTree" );
    // Create tree to store metadata
    _trigInfoTree = fs->make<TTree>( "TrigInfoTree", "TrigInfoTree" );
    _filterInfoTree = fs->make<TTree>( "FilterInfoTree", "FilterInfoTree" );

    // get the detail levels from the configuration
    int elecDetail = 99;
    int muonDetail = 99;
    int photDetail = 99;
    int jetDetail  = 99;
    if( iConfig.exists("electronDetailLevel") ) {  
        elecDetail = iConfig.getUntrackedParameter<int>("electronDetailLevel"); 
    }
    if( iConfig.exists("muonDetailLevel") ) {
        muonDetail   = iConfig.getUntrackedParameter<int>("muonDetailLevel"); 
    }
    if( iConfig.exists("photonDetailLevel") ) {
        photDetail = iConfig.getUntrackedParameter<int>("photonDetailLevel"); 
    }
    if( iConfig.exists("jetDetailLevel") ) {
        jetDetail    = iConfig.getUntrackedParameter<int>("jetDetailLevel"); 
    }

    // get pt cut from the configuration
    float elecMinPt = 0;
    float muonMinPt = 0;
    float photMinPt = 0;
    float jetMinPt  = 0;
    float fjetMinPt = 0;
    float genMinPt  = 0;
    std::vector<int> genVIP = {};

    if( iConfig.exists("electronMinPt") ) {
        elecMinPt = iConfig.getUntrackedParameter<double>("electronMinPt");
    }
    if( iConfig.exists("muonMinPt") ) {
        muonMinPt = iConfig.getUntrackedParameter<double>("muonMinPt");
    }
    if( iConfig.exists("photonMinPt") ) {
        photMinPt = iConfig.getUntrackedParameter<double>("photonMinPt");
    }
    if( iConfig.exists("jetMinPt") ) {
        jetMinPt  = iConfig.getUntrackedParameter<double>("jetMinPt");
    }
    std::cout<< iConfig.exists("jetMinPt")<< " minpt "<<iConfig.getUntrackedParameter<double>("jetMinPt")<<" "<<jetMinPt<<std::endl;
    if( iConfig.exists("fjetMinPt") ) {
        fjetMinPt = iConfig.getUntrackedParameter<double>("fjetMinPt");
    }
    if( iConfig.exists("genMinPt") ) {
        genMinPt  = iConfig.getUntrackedParameter<double>("genMinPt");
    }
    if( iConfig.exists("genVIP") ) {
        genVIP  = iConfig.getUntrackedParameter<std::vector<int>>("genVIP");
    }

    // prefix for object branches
    // defaults
    std::string prefix_el          = "el";
    std::string prefix_mu          = "mu";
    std::string prefix_ph          = "ph";
    std::string prefix_jet         = "jet";
    std::string prefix_fjet        = "fjet";
    std::string prefix_trig        = "passTrig";
    std::string prefix_gen         = "gen";
    std::string prefix_pref        = "pref";
    std::string prefix_met         = "met";
    std::string prefix_puppimet    = "puppimet";
    std::string prefix_deepmet     = "deepmet";
    std::string prefix_met_filter  = "metFilter";

    if( iConfig.exists("prefix_el") ) {
        prefix_el = iConfig.getUntrackedParameter<std::string>("prefix_el");
    }
    if( iConfig.exists("prefix_mu") ) {
        prefix_mu = iConfig.getUntrackedParameter<std::string>("prefix_mu");
    }
    if( iConfig.exists("prefix_ph") ) {
        prefix_ph = iConfig.getUntrackedParameter<std::string>("prefix_ph");
    }
    if( iConfig.exists("prefix_jet") ) {
        prefix_jet = iConfig.getUntrackedParameter<std::string>("prefix_jet");
    }
    if( iConfig.exists("prefix_fjet") ) {
        prefix_fjet = iConfig.getUntrackedParameter<std::string>("prefix_fjet");
    }
    if( iConfig.exists("prefix_trig") ) {
        prefix_trig = iConfig.getUntrackedParameter<std::string>("prefix_trig");
    }
    if( iConfig.exists("prefix_gen") ) {
        prefix_gen = iConfig.getUntrackedParameter<std::string>("prefix_gen");
    }
    if( iConfig.exists("prefix_pref") ) {
        prefix_pref = iConfig.getUntrackedParameter<std::string>("prefix_pref");
    }
    if( iConfig.exists("prefix_met") ) {
        prefix_met = iConfig.getUntrackedParameter<std::string>("prefix_met");
    }
    if( iConfig.exists("prefix_puppimet") ) {
        prefix_puppimet = iConfig.getUntrackedParameter<std::string>("prefix_puppimet");
    }
    if( iConfig.exists("prefix_deepmet") ) {
        prefix_deepmet = iConfig.getUntrackedParameter<std::string>("prefix_deepmet");
    }
    if( iConfig.exists("prefix_met_filter") ) {
        prefix_met_filter = iConfig.getUntrackedParameter<std::string>("prefix_met_filter");
    }


    edm::EDGetTokenT<reco::BeamSpot> beamSpotToken;
    edm::EDGetTokenT<reco::ConversionCollection> conversionsToken;
    edm::EDGetTokenT<std::vector<reco::Vertex> > verticesToken;
    edm::EDGetTokenT<std::vector<PileupSummaryInfo> > puToken;
    edm::EDGetTokenT<GenEventInfoProduct> generatorToken;
    edm::EDGetTokenT<GenLumiInfoHeader> genLumiInfoToken;
    edm::EDGetTokenT<double> prefToken;
    edm::EDGetTokenT<double> rhoToken;
    edm::EDGetTokenT<double> prefweight_token;
    edm::EDGetTokenT<double> prefweightup_token;
    edm::EDGetTokenT<double> prefweightdown_token;
    edm::EDGetTokenT<LHEEventProduct> lheEventToken;
    edm::EDGetTokenT<LHERunInfoProduct> lheRunToken;

    if( iConfig.exists("beamSpotTag" ) ) {
        beamSpotToken = consumes<reco::BeamSpot>(
                        iConfig.getUntrackedParameter<edm::InputTag>("beamSpotTag"));
    }
    if( iConfig.exists("conversionsTag") ) {
        conversionsToken = consumes<reco::ConversionCollection>(
                 iConfig.getUntrackedParameter<edm::InputTag>("conversionsTag"));
    }
    if( iConfig.exists("verticesTag") ) {
        verticesToken = consumes<std::vector<reco::Vertex> >(
                 iConfig.getUntrackedParameter<edm::InputTag>("verticesTag"));
    }
    if( iConfig.exists("puTag") ) {
        puToken = consumes<std::vector<PileupSummaryInfo> >(
                 iConfig.getUntrackedParameter<edm::InputTag>("puTag"));
    }
    if( iConfig.exists("generatorTag") ) {
        generatorToken = consumes<GenEventInfoProduct>(
                 iConfig.getUntrackedParameter<edm::InputTag>("generatorTag"));
    }
    if( iConfig.exists("genheaderTag") ) {
        genLumiInfoToken = consumes<GenLumiInfoHeader, edm::InLumi>(
                 iConfig.getUntrackedParameter<edm::InputTag>("genheaderTag"));
    }
    if( iConfig.exists("rhoTag") ) {
        rhoToken = consumes<double>(
                 iConfig.getUntrackedParameter<edm::InputTag>("rhoTag"));
    }
    if( iConfig.exists("prefTag") && _isMC) { 
	prefweight_token = consumes< double >(
		  iConfig.getUntrackedParameter<edm::InputTag>("prefTag")); 
	prefweightup_token = consumes< double >(
		  iConfig.getUntrackedParameter<edm::InputTag>("prefupTag")); 
	prefweightdown_token = consumes< double >(
		  iConfig.getUntrackedParameter<edm::InputTag>("prefdownTag")); 
    }
    if( iConfig.exists("lheEventTag") ) {
        lheEventToken = consumes<LHEEventProduct>(
                 iConfig.getUntrackedParameter<edm::InputTag>("lheEventTag"));
    }
    if( iConfig.exists("lheRunTag") ) {
        lheRunToken = consumes<LHERunInfoProduct, edm::InRun>(
                 iConfig.getUntrackedParameter<edm::InputTag>("lheRunTag"));
    }

    // flags to enable or disable production
    // of objects based on the provided tags
   // _produceJets      = iConfig.exists( "jetTag" );
   // _produceFJets     = iConfig.exists( "fatjetTag" );
   // _produceElecs     = iConfig.exists( "electronTag" );
   // _produceMuons     = iConfig.exists( "muonTag" );
   // _producePhots     = iConfig.exists( "photonTag" );
   // _produceMET       = iConfig.exists( "metTag" );
   // _produceMETFilter = iConfig.exists( "metFilterTag" );
   // _produceTrig      = iConfig.exists( "triggerTag" );
   // _produceGen       = iConfig.exists( "genParticleTag" );

    if( !_isMC ) _produceGen = false;

    // delcare object tokens
    edm::EDGetTokenT<edm::View<pat::Jet> >            jetToken;
    edm::EDGetTokenT<edm::View<pat::Jet> >            fjetToken;
    edm::EDGetTokenT<edm::View<pat::Electron> >       elecToken;
    //edm::EDGetTokenT<edm::View<pat::Electron> >       elecCalibToken;
    edm::EDGetTokenT<edm::View<pat::Muon> >           muonToken;
    edm::EDGetTokenT<edm::View<pat::Photon> >         photToken;
    edm::EDGetTokenT<edm::View<pat::Photon> >         photCalibToken;
    edm::EDGetTokenT<edm::View<pat::MET> >            metToken;
    edm::EDGetTokenT<edm::View<pat::MET> >            puppimetToken;
    edm::EDGetTokenT<edm::View<pat::MET> >            deepmetToken;
    edm::EDGetTokenT<edm::TriggerResults>             metFilterToken;
    edm::EDGetTokenT<edm::TriggerResults>             trigToken;
    edm::EDGetTokenT<std::vector<reco::GenParticle> > genToken;
    edm::EDGetTokenT<std::vector<reco::GenJet> >      genDressedLeptonToken;
    edm::EDGetTokenT<std::vector<reco::MET> >         genMetToken;

    std::cout << " _produceJets " << _produceJets << std::endl; 
    std::cout << " _produceFJets " << _produceFJets << std::endl;
    std::cout << " _produceElecs " << _produceElecs << std::endl;
    std::cout << " _produceMuons " << _produceMuons << std::endl;
    std::cout << " _producePhots " << _producePhots << std::endl;
    std::cout << " _produceMET " << _produceMET << std::endl;
    std::cout << " _produceMETFilter " << _produceMETFilter << std::endl;
    std::cout << " _produceTrig " << _produceTrig << std::endl;
    std::cout << " _produceGen " << _produceGen << std::endl;
    std::cout << " _produceDeepMET" << _produceDeepMET << std::endl;

    // Event information
    _eventProducer.initialize( verticesToken, puToken, 
                               generatorToken, genLumiInfoToken, lheEventToken, lheRunToken,
                               rhoToken, prefweight_token, prefweightup_token, prefweightdown_token,
 			       _myTree, _weightInfoTree, _isMC , _doPref);

    if(disableEventWeights ) {
        _eventProducer.disableEventWeights();
    }
    // Electrons
    if( _produceElecs ) {
        elecToken =  consumes<edm::View<pat::Electron> >(
                     iConfig.getUntrackedParameter<edm::InputTag>("electronTag"));

        _elecProducer.initialize( prefix_el  , elecToken, _myTree, elecMinPt, elecDetail );

        std::string elecIdVeryLoose = iConfig.getUntrackedParameter<std::string>("elecIdVeryLooseStr");
        std::string elecIdLoose     = iConfig.getUntrackedParameter<std::string>("elecIdLooseStr");
        std::string elecIdMedium    = iConfig.getUntrackedParameter<std::string>("elecIdMediumStr");
        std::string elecIdTight     = iConfig.getUntrackedParameter<std::string>("elecIdTightStr");
        std::string elecIdHEEP      = iConfig.getUntrackedParameter<std::string>("elecIdHEEPStr");

        _elecProducer.addUserString( ElectronIdVeryLoose , elecIdVeryLoose);
        _elecProducer.addUserString( ElectronIdLoose     , elecIdLoose);
        _elecProducer.addUserString( ElectronIdMedium    , elecIdMedium);
        _elecProducer.addUserString( ElectronIdTight     , elecIdTight);
        _elecProducer.addUserString( ElectronIdHEEP      , elecIdHEEP);

        _elecProducer.addConversionsToken( conversionsToken );
        _elecProducer.addBeamSpotToken( beamSpotToken );
        _elecProducer.addVertexToken( verticesToken );
        _elecProducer.addRhoToken( rhoToken );

        std::string elecEneCalib = iConfig.getUntrackedParameter<std::string>("elecEneCalibStr");
        _elecProducer.addEnergyCalib( elecEneCalib );
    }

    if( _produceMuons ) { 

        muonToken = consumes<edm::View<pat::Muon> >(
                    iConfig.getUntrackedParameter<edm::InputTag>("muonTag"));

        _muonProducer.initialize( prefix_mu       , muonToken, _myTree, muonMinPt, muonDetail );
        _muonProducer.addVertexToken( verticesToken );
        _muonProducer.addRhoToken( rhoToken );
    }

    if( _producePhots ) {

        photToken = consumes<edm::View<pat::Photon> >(
                    iConfig.getUntrackedParameter<edm::InputTag>("photonTag"));

        _photProducer.initialize( prefix_ph       , photToken, _myTree, photMinPt, photDetail );

        std::string phoChIso  = iConfig.getUntrackedParameter<std::string>("phoChIsoStr");
        std::string phoNeuIso = iConfig.getUntrackedParameter<std::string>("phoNeuIsoStr");
        std::string phoPhoIso = iConfig.getUntrackedParameter<std::string>("phoPhoIsoStr");
        std::string phoIdLoose  = iConfig.getUntrackedParameter<std::string>("phoIdLooseStr");
        std::string phoIdMedium = iConfig.getUntrackedParameter<std::string>("phoIdMediumStr");
        std::string phoIdTight  = iConfig.getUntrackedParameter<std::string>("phoIdTightStr");

        _photProducer.addUserString( PhotonChIso        , phoChIso  );
        _photProducer.addUserString( PhotonNeuIso       , phoNeuIso );
        _photProducer.addUserString( PhotonPhoIso       , phoPhoIso );
        _photProducer.addUserString( PhotonVIDLoose      , phoIdLoose  );
        _photProducer.addUserString( PhotonVIDMedium     , phoIdMedium );
        _photProducer.addUserString( PhotonVIDTight      , phoIdTight  );

        //_photProducer.addElectronsToken( elecToken );
        _photProducer.addConversionsToken( conversionsToken );
        _photProducer.addBeamSpotToken( beamSpotToken );
        _photProducer.addRhoToken( rhoToken );

        std::string phoEneCalib = iConfig.getUntrackedParameter<std::string>("phoEneCalibStr");
        _photProducer.addEnergyCalib( phoEneCalib );
    }

    if( _produceJets ) {
        jetToken = consumes<edm::View<pat::Jet> >(
                   iConfig.getUntrackedParameter<edm::InputTag>("jetTag"));
        _jetProducer .initialize( prefix_jet   , jetToken , _myTree, jetMinPt, jetDetail );
    }

    if( _produceFJets ) {

        fjetToken =  consumes<edm::View<pat::Jet> >(
                     iConfig.getUntrackedParameter<edm::InputTag>("fatjetTag"));

        _fjetProducer.initialize( prefix_fjet     , fjetToken, _myTree, fjetMinPt );
    }

    if( _produceMET ) {
        metToken  = consumes<edm::View<pat::MET> >(
                    iConfig.getUntrackedParameter<edm::InputTag>("metTag"));

        _metProducer .initialize( prefix_met      , metToken , _myTree );
        
        puppimetToken  = consumes<edm::View<pat::MET> >(
                    iConfig.getUntrackedParameter<edm::InputTag>("puppimetTag"));

        _puppimetProducer .initialize( prefix_puppimet , puppimetToken , _myTree );

        if(_produceDeepMET){
            deepmetToken  = consumes<edm::View<pat::MET> >(
                        iConfig.getUntrackedParameter<edm::InputTag>("deepmetTag"));
            _deepmetProducer .initialize( prefix_deepmet, deepmetToken, _myTree, 0);
        }
    }
    if( _produceMETFilter ) {
        metFilterToken = consumes<edm::TriggerResults>(
                    iConfig.getUntrackedParameter<edm::InputTag>("metFilterTag"));

        edm::EDGetTokenT<bool> BadChCandFilterToken = 
            consumes<bool>(iConfig.getUntrackedParameter<edm::InputTag>("BadChargedCandidateFilter"));

        edm::EDGetTokenT<bool> BadPFMuonFilterToken = 
            consumes<bool>(iConfig.getUntrackedParameter<edm::InputTag>("BadPFMuonFilter"));

        std::vector<std::string> filter_map = 
            iConfig.getUntrackedParameter<std::vector<std::string> >("metFilterMap");

        _metFilterProducer .initialize( prefix_met_filter , metFilterToken , 
                                        filter_map, _myTree, _filterInfoTree );

        _metFilterProducer.addBadChargedCandidateFilterToken( BadChCandFilterToken );
        _metFilterProducer.addBadPFMuonFilterToken( BadPFMuonFilterToken );
    }
    if( _produceTrig ) {
        trigToken = consumes<edm::TriggerResults>(
                    iConfig.getUntrackedParameter<edm::InputTag>("triggerTag"));

        std::vector<std::string> trigger_map = 
            iConfig.getUntrackedParameter<std::vector<std::string> >("triggerMap");

        edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> trigObjToken = 
                    consumes<pat::TriggerObjectStandAloneCollection> (
                    iConfig.getUntrackedParameter<edm::InputTag>("triggerObjTag"));

        _trigProducer.initialize( prefix_trig, trigToken, trigObjToken,
                                  trigger_map, _myTree, _trigInfoTree );

    }
    if( _produceGen ) {
        genToken = consumes<std::vector<reco::GenParticle> >(
                   iConfig.getUntrackedParameter<edm::InputTag>("genParticleTag"));
        genDressedLeptonToken = consumes<std::vector<reco::GenJet> >(
                    iConfig.getUntrackedParameter<edm::InputTag>("genDressedLeptonTag"));
        genMetToken = consumes<std::vector<reco::MET> >(
                    iConfig.getUntrackedParameter<edm::InputTag>("genMetTag"));

        _genProducer.initialize( prefix_gen, genToken, genDressedLeptonToken, genMetToken, _myTree, genMinPt, genVIP );
    }

}

void UMDNTuple::beginJob() {


}

void UMDNTuple::analyze(const edm::Event &iEvent, const edm::EventSetup &iSetup) {
    _eventProducer.produce( iEvent );
    if( _produceElecs )         _elecProducer      .produce( iEvent );
    if( _produceMuons )         _muonProducer      .produce( iEvent );
    if( _producePhots )         _photProducer      .produce( iEvent );
    if( _produceJets  )         _jetProducer       .produce( iEvent );
    if( _produceFJets )         _fjetProducer      .produce( iEvent );
    if( _produceMET   ) {
                                _metProducer       .produce( iEvent );
                                _puppimetProducer  .produce( iEvent );
                                if( _produceDeepMET ){
                                        _deepmetProducer.produce( iEvent );
                                }
    }
    if( _produceMETFilter  )    _metFilterProducer .produce( iEvent );
    if( _produceTrig  )         _trigProducer      .produce( iEvent );
    if( _produceGen && _isMC  ) _genProducer       .produce( iEvent );

    _myTree->Fill();
}

void UMDNTuple::endJob() {

}

void UMDNTuple::beginLuminosityBlock( edm::LuminosityBlock const& iLumi, edm::EventSetup const&) {

  _eventProducer.beginLuminosityBlock( iLumi );

}

void UMDNTuple::endRun( edm::Run const& iRun, edm::EventSetup const&) {

  _eventProducer.endRun( iRun );
  if( _produceMETFilter ) _metFilterProducer.endRun();
  if( _produceTrig ) _trigProducer.endRun();


}

UMDNTuple::~UMDNTuple() {

};


DEFINE_FWK_MODULE(UMDNTuple);
