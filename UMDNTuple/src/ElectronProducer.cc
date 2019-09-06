#include "UMDNTuple/UMDNTuple/interface/ElectronProducer.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/Event.h"

ElectronProducer::ElectronProducer(  ) : 
    el_n(0),
    el_pt(0),
    el_eta(0),
    el_phi(0),
    el_e(0),
    el_ptOrig(0),
    el_etaOrig(0),
    el_phiOrig(0),
    el_eOrig(0),
    el_passVIDVeryLoose(0),
    el_passVIDLoose(0),
    el_passVIDMedium(0),
    el_passVIDTight(0),
    el_passVIDHEEP(0),
    el_passVIDHLT(0),
    el_hOverE(0),
    el_sigmaIEIE(0),
    el_sigmaIEIEfull5x5(0),
    el_dEtaIn(0),
    el_dPhiIn(0),
    el_ooEmooP(0),
    el_d0(0),
    el_dz(0),
    el_passConvVeto(0),
    el_expectedMissingInnerHits(0),
    el_charge(0),
    el_sc_eta(0),
    el_dEtaClusterTrack (0),
    el_dPhiClusterTrack (0),
    el_sc_rawE(0),
    el_sc_e(0),
    el_ecalIso(0),
    el_ecalPfIso(0),
    el_aeff(0),
    el_chIso(0),
    el_neuIso(0),
    el_phoIso(0),
    el_puChIso(0),
    el_pfIsoRaw(0),
    el_pfIsoDbeta(0),
    el_pfIsoRho(0),
    el_trkSumPt(0),
    el_ecalRecHitSumEt(0),
    el_hcalTowerSumEt(0),
    //_effectiveAreas("data/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt"),
    _effectiveAreas( "src/UMDNTuple/UMDNTuple/data/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt" ),
    _detail(99)
{

}

void ElectronProducer::initialize( const std::string &prefix,
                                    const edm::EDGetTokenT<edm::View<pat::Electron> >&elecTok,
                                    TTree *tree, float minPt, int detail) {

    _prefix = prefix;
    _elecToken = elecTok;
    _detail = detail;
    _minPt = minPt;

    tree->Branch( (prefix + "_n" ).c_str(), &el_n, (prefix + "_n/I" ).c_str() );

    tree->Branch( (prefix + "_pt" ).c_str(), &el_pt );
    tree->Branch( (prefix + "_eta").c_str(), &el_eta );
    tree->Branch( (prefix + "_phi").c_str(), &el_phi );
    tree->Branch( (prefix + "_e"  ).c_str(), &el_e );
    tree->Branch( (prefix + "_ptOrig" ).c_str(), &el_ptOrig );
    tree->Branch( (prefix + "_etaOrig").c_str(), &el_etaOrig );
    tree->Branch( (prefix + "_phiOrig").c_str(), &el_phiOrig );
    tree->Branch( (prefix + "_eOrig"  ).c_str(), &el_eOrig );

    if( detail > 0 ) {

        tree->Branch( (prefix + "_passVIDVeryLoose").c_str(), &el_passVIDVeryLoose );
        tree->Branch( (prefix + "_passVIDLoose").c_str(), &el_passVIDLoose );
        tree->Branch( (prefix + "_passVIDMedium").c_str(), &el_passVIDMedium );
        tree->Branch( (prefix + "_passVIDTight").c_str(), &el_passVIDTight );
        tree->Branch( (prefix + "_passVIDHEEP").c_str(), &el_passVIDHEEP );
        tree->Branch( (prefix + "_passVIDHLT").c_str(), &el_passVIDHLT );


        tree->Branch( (prefix + "_hOverE").c_str(), &el_hOverE );
        tree->Branch( (prefix + "_sigmaIEIE").c_str(), &el_sigmaIEIE );
        tree->Branch( (prefix + "_sigmaIEIEfull5x5").c_str(), &el_sigmaIEIEfull5x5 );
        tree->Branch( (prefix + "_dEtaIn").c_str(), &el_dEtaIn );
        tree->Branch( (prefix + "_dPhiIn").c_str(), &el_dPhiIn );
        tree->Branch( (prefix + "_ooEmooP").c_str(), &el_ooEmooP );

        tree->Branch( (prefix + "_chIso").c_str(), &el_chIso );
        tree->Branch( (prefix + "_neuIso").c_str(), &el_neuIso );
        tree->Branch( (prefix + "_phoIso").c_str(), &el_phoIso );
        tree->Branch( (prefix + "_aeff").c_str(), &el_aeff );
        tree->Branch( (prefix + "_pfIsoRho").c_str(), &el_pfIsoRho );

        tree->Branch( (prefix + "_d0").c_str(), &el_d0);
        tree->Branch( (prefix + "_dz").c_str(), &el_dz);

        tree->Branch( (prefix + "_passConvVeto").c_str(), &el_passConvVeto );
        tree->Branch( (prefix + "_expectedMissingInnerHits").c_str(), &el_expectedMissingInnerHits );
        tree->Branch( (prefix + "_charge").c_str(), &el_charge );
        tree->Branch( (prefix + "_sc_eta").c_str(), &el_sc_eta );
        tree->Branch( (prefix + "_sc_e").c_str(), &el_sc_e );


        if( detail > 1 ) {

            tree->Branch( (prefix + "_dEtaClusterTrack").c_str(), &el_dEtaClusterTrack );
            tree->Branch( (prefix + "_dPhiClusterTrack").c_str(), &el_dPhiClusterTrack );
            tree->Branch( (prefix + "_puChIso").c_str(), &el_puChIso );
            tree->Branch( (prefix + "_sc_rawE").c_str(), &el_sc_rawE );
            tree->Branch( (prefix + "_ecalIso").c_str(), &el_ecalIso );
            tree->Branch( (prefix + "_ecalPfIso").c_str(), &el_ecalPfIso );
            tree->Branch( (prefix + "_pfIsoRaw").c_str(), &el_pfIsoRaw );
            tree->Branch( (prefix + "_pfIsoDbeta").c_str(), &el_pfIsoDbeta );
            tree->Branch( (prefix + "_trkSumPt").c_str(), &el_trkSumPt );
            tree->Branch( (prefix + "_ecalRecHitSumEt").c_str(), &el_ecalRecHitSumEt );
            tree->Branch( (prefix + "_hcalTowerSumEt").c_str(), &el_hcalTowerSumEt );
        }
    }
}

void ElectronProducer::addUserString( ElectronUserVar type, const std::string userString) {

    if( type == ElectronIdVeryLoose ) {
        _IdVeryLoose  = userString;
    }
    if( type == ElectronIdLoose ) {
        _IdLoose  = userString;
    }
    if( type == ElectronIdMedium ) {
        _IdMedium  = userString;
    }
    if( type == ElectronIdTight ) {
        _IdTight  = userString;
    }
    if( type == ElectronIdHLT ) {
        _IdHLT  = userString;
    }
    if( type == ElectronIdHEEP ) {
        _IdHEEP  = userString;
    }

}

void ElectronProducer::addConversionsToken( const edm::EDGetTokenT< reco::ConversionCollection> & tok)  { 
    _conversionsToken = tok;
}
void ElectronProducer::addBeamSpotToken( const edm::EDGetTokenT< reco::BeamSpot> & tok) {
    _beamSpotToken = tok;
}
void ElectronProducer::addVertexToken( const edm::EDGetTokenT<std::vector<reco::Vertex> > & tok) {
    _vertexToken = tok;
}
void ElectronProducer::addRhoToken( const edm::EDGetTokenT<double> & tok) {
    _rhoToken = tok;
}

void ElectronProducer::addEnergyCalib( const std::string eneCalib) {
   // electron energy scale and smearing corrections
   _eneCalib = eneCalib;
}
        

void ElectronProducer::produce(const edm::Event &iEvent ) {

    el_n = 0;

    el_pt->clear();
    el_eta->clear();
    el_phi->clear();
    el_e->clear();
    el_ptOrig->clear();
    el_etaOrig->clear();
    el_phiOrig->clear();
    el_eOrig->clear();

    if( _detail > 0 ) {
        el_passVIDVeryLoose->clear(); 
        el_passVIDLoose->clear();
        el_passVIDMedium->clear();
        el_passVIDTight->clear();
        el_passVIDHEEP->clear();
        el_passVIDHLT->clear();

        el_hOverE->clear();
        el_sigmaIEIE->clear();
        el_sigmaIEIEfull5x5->clear();
        el_dEtaIn->clear();
        el_dPhiIn->clear();
        el_ooEmooP->clear();

        el_chIso->clear();
        el_neuIso->clear();
        el_phoIso->clear();
        el_aeff->clear();
        el_pfIsoRho->clear();

        el_d0->clear();
        el_dz->clear();

        el_passConvVeto -> clear();

        el_expectedMissingInnerHits->clear();
        el_charge ->clear();
        el_sc_eta->clear();
        el_sc_e->clear();

        if( _detail > 1 ) {

            el_dEtaClusterTrack ->clear();
            el_dPhiClusterTrack ->clear();
            el_sc_rawE->clear();
            el_ecalIso->clear();
            el_ecalPfIso->clear();
            el_puChIso->clear();
            el_pfIsoRaw->clear();
            el_pfIsoDbeta->clear();
            el_trkSumPt->clear();
            el_ecalRecHitSumEt->clear();
            el_hcalTowerSumEt->clear();
        }
    }

    edm::Handle<edm::View<pat::Electron> > electrons;
    iEvent.getByToken(_elecToken,electrons);

    const std::string elecIdVeryLoose_str = _IdVeryLoose;
    const std::string elecIdLoose_str     = _IdLoose;
    const std::string elecIdMedium_str    = _IdMedium;
    const std::string elecIdTight_str     = _IdTight;
    const std::string elecIdHEEP_str      = _IdHEEP;

    const std::string eleEneCalib_str     = _eneCalib;

    edm::Handle<reco::BeamSpot> beamSpot_h;
    edm::Handle<reco::ConversionCollection> conversions_h;

    iEvent.getByToken(_conversionsToken, conversions_h);
    iEvent.getByToken(_beamSpotToken, beamSpot_h);

    edm::Handle<std::vector<reco::Vertex> > vertices_h;
    iEvent.getByToken( _vertexToken, vertices_h );

    edm::Handle<double> rho_h;
    iEvent.getByToken( _rhoToken, rho_h );

    for (unsigned int j=0; j < electrons->size();++j){
        edm::Ptr<pat::Electron> el = electrons->ptrAt(j);
 
        if( el->pt() < _minPt ) continue;
       
        el_n += 1;

        // kinematics
        el_ptOrig -> push_back( el->pt() );
        el_etaOrig -> push_back( el->eta() ); 
        el_phiOrig -> push_back( el->phi() );
        el_eOrig -> push_back( el->energy() );

        auto calibp4 = el->p4() * el->userFloat( eleEneCalib_str )/el->energy() ;
        el_pt ->push_back( calibp4.Pt() );
        el_eta -> push_back( calibp4.Eta() );
        el_phi -> push_back( calibp4.phi() );
        el_e -> push_back( calibp4.E() );

        if(_detail > 0 ) {

            // VID
            el_passVIDVeryLoose->push_back( el->electronID( elecIdVeryLoose_str ) );
            el_passVIDLoose->push_back(     el->electronID( elecIdLoose_str     ) );
            el_passVIDMedium->push_back(    el->electronID( elecIdMedium_str    ) );
            el_passVIDTight->push_back(     el->electronID( elecIdTight_str     ) );
            el_passVIDHEEP->push_back(      el->electronID( elecIdHEEP_str      ) );

            // shower shape quantities
            el_hOverE -> push_back( el->hcalOverEcal() );
            el_sigmaIEIE -> push_back(  el->sigmaIetaIeta() );
            el_sigmaIEIEfull5x5 -> push_back( el->full5x5_sigmaIetaIeta() );

            // Update the dEtaIn calculate according to 
            // https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Recipe80X 
            // https://github.com/ikrav/cmssw/blob/egm_id_80X_v1/RecoEgamma/ElectronIdentification/plugins/cuts/GsfEleDEtaInSeedCut.cc#L30-L33
            el_dEtaIn ->push_back( el->superCluster().isNonnull() && el->superCluster()->seed().isNonnull() ? el->deltaEtaSuperClusterTrackAtVtx() - el->superCluster()->eta() + el->superCluster()->seed()->eta() : std::numeric_limits<float>::max() );
            //el_dEtaIn ->push_back( el->deltaEtaSuperClusterTrackAtVtx());

            el_dPhiIn ->push_back( el->deltaPhiSuperClusterTrackAtVtx());

            float ooEmooP = -999;
            if( !(el->ecalEnergy() == 0 || !std::isfinite(el->ecalEnergy())) ){
              ooEmooP = fabs(1.0/el->ecalEnergy() - el->eSuperClusterOverP()/el->ecalEnergy() );
            }

            el_ooEmooP -> push_back( ooEmooP );

            // the isolation might need to be updated. Need to be careful if use this variable
            // https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Recipe80X
            // https://github.com/ikrav/cmssw/blob/egm_id_80X_v1/RecoEgamma/ElectronIdentification/plugins/cuts/GsfEleEffAreaPFIsoCut.cc#L83-L94
            // checked in MC chIso is not always the same as chadiso. Not sure which one is more appropriate
            float chIso = el->chargedHadronIso();
            float nhIso = el->neutralHadronIso();
            float phIso= el->photonIso();
            el_chIso->push_back(chIso);
            el_neuIso->push_back(nhIso);
            el_phoIso->push_back(phIso);
            double rhoPrime = std::max(0., *rho_h);
            //float aeff = ElectronEffectiveArea::GetElectronEffectiveArea(ElectronEffectiveArea::kEleGammaAndNeutralHadronIso03, el->superCluster()->eta(), ElectronEffectiveArea::kEleEAData2012);
            //el_aeff->push_back(aeff);
            //el_pfIsoRho->push_back(( chIso + std::max(0.0, nhIso + phIso - rhoPrime*(aeff)) )/ el->pt());

            // from CMSSW code
            // https://github.com/ikrav/cmssw/blob/egm_id_80X_v1/RecoEgamma/ElectronIdentification/plugins/cuts/GsfEleEffAreaPFIsoCut.cc#L83-L94
            const float chadiso = el->pfIsolationVariables().sumChargedHadronPt;
            const float nhadiso = el->pfIsolationVariables().sumNeutralHadronEt;
            const float phoiso  = el->pfIsolationVariables().sumPhotonEt;
            float eA = _effectiveAreas.getEffectiveArea( fabs(el->superCluster()->eta()) );

            el_aeff->push_back(eA);
            el_pfIsoRho->push_back(( chadiso + std::max(0.0, nhadiso + phoiso - rhoPrime*(eA)) )/ el->pt());

            // vertex displacement
            float d0 = -999;
            float dz = -999;
            if(vertices_h->size() > 0){
              d0 = (-1) * el->gsfTrack()->dxy((*vertices_h)[0].position() );
              dz = el->gsfTrack()->dz( (*vertices_h)[0].position() );
            }

            el_d0->push_back( d0 );
            el_dz->push_back( dz );

            // Conversion veto
            bool passConversionVeto = false;
            if( beamSpot_h.isValid() && conversions_h.isValid()) {
              passConversionVeto = !ConversionTools::hasMatchedConversion(*el,conversions_h,
                		        beamSpot_h->position());
            }

            el_passConvVeto -> push_back( passConversionVeto );

            // seems from 90X the numberofHits has been changed to numberofAllHits()
            // http://cmslxr.fnal.gov/dxr/CMSSW/source/DataFormats/TrackReco/interface/HitPattern.h?from=hitpattern#146
            // http://cmslxr.fnal.gov/source/DataFormats/TrackReco/interface/HitPattern.h?v=CMSSW_8_0_24
            el_expectedMissingInnerHits ->push_back( el->gsfTrack()->hitPattern().numberOfAllHits(reco::HitPattern::MISSING_INNER_HITS));

            el_charge -> push_back(el->charge());
            el_sc_eta->push_back(el->superCluster()->eta());
            el_sc_e->push_back(el->superCluster()->energy());

            if( _detail > 1 ) {

                el_dEtaClusterTrack -> push_back( el->deltaEtaSuperClusterTrackAtVtx());
                el_dPhiClusterTrack -> push_back( el->deltaPhiSuperClusterTrackAtVtx());
                

                el_sc_rawE->push_back(el->superCluster()->rawEnergy());
                el_ecalIso->push_back(el->ecalIso());
                el_ecalPfIso->push_back(el->ecalPFClusterIso());

                float puChIso = el->puChargedHadronIso();
                el_puChIso->push_back(puChIso);
                el_pfIsoRaw->push_back(( chIso + nhIso + phIso ) / el->pt());
                el_pfIsoDbeta->push_back(( chIso + std::max(0.0, nhIso + phIso - 0.5*puChIso) )/ el->pt());


                el_trkSumPt->push_back(el->dr03TkSumPt());
                el_ecalRecHitSumEt->push_back(el->dr03EcalRecHitSumEt());
                el_hcalTowerSumEt->push_back(el->dr03HcalTowerSumEt());
            }
        }
    }
}



