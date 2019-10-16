#include "UMDNTuple/UMDNTuple/interface/PhotonProducer.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/Event.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"

PhotonProducer::PhotonProducer(  ) : 
    ph_n(0),
    ph_pt(0),
    ph_eta(0),
    ph_phi(0),
    ph_e(0),
    ph_ptOrig(0),
    ph_etaOrig(0),
    ph_phiOrig(0),
    ph_eOrig(0),
    ph_passVIDLoose(0),
    ph_passVIDMedium(0),
    ph_passVIDTight(0),
    ph_chIso(0),
    ph_neuIso(0),
    ph_phoIso(0),
    ph_chIsoCorr(0),
    ph_neuIsoCorr(0),
    ph_phoIsoCorr(0),
    ph_aeffch(0),
    ph_aeffnh(0),
    ph_aeffph(0),
    ph_sc_eta(0),
    ph_sc_phi(0),
    ph_hOverE(0),
    ph_hOverE_hdronic(0),
    ph_sigmaIEIE(0),
    ph_sigmaIEIEFull5x5(0),
    ph_r9(0),
    ph_r9Full5x5(0),
    ph_etaWidth(0),
    ph_phiWidth(0),
    ph_passEleVeto(0),
    ph_hasPixSeed(0),
    ph_sc_rawE(0),
    ph_ecalIso(0),
    ph_hcalIso(0),
    ph_trkIso(0),
    ph_pfIsoPUChHad(0),
    ph_pfIsoEcal(0),
    ph_pfIsoHcal(0),
    ph_E3x3(0),
    ph_E1x5(0),
    ph_E2x5(0),
    ph_E5x5(0),
    //ph_sigmaIetaIphi(0),
    //ph_sigmaIphiIphi(0),
    ph_E1x5Full5x5(0),
    ph_E2x5Full5x5(0),
    ph_E3x3Full5x5(0),
    ph_E5x5Full5x5(0),
    _effectiveAreasCH("src/UMDNTuple/UMDNTuple/data/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt"),
    _effectiveAreasNH("src/UMDNTuple/UMDNTuple/data/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt"),
    _effectiveAreasPH("src/UMDNTuple/UMDNTuple/data/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt"),
    _detail(0),
    _tree(0)
{

}

void PhotonProducer::initialize( const std::string &prefix,
                                 const edm::EDGetTokenT<edm::View<pat::Photon> >&photTok,
                                 TTree *tree, float minPt, int detail) {

    _prefix = prefix;
    _photToken = photTok;
    _detail = detail;
    _tree = tree;
    _minPt = minPt;

    tree->Branch( (prefix + "_n" ).c_str(), &ph_n,(prefix + "_n/I" ).c_str()  );

    tree->Branch( (prefix + "_pt" ).c_str(), &ph_pt );
    tree->Branch( (prefix + "_eta").c_str(), &ph_eta );
    tree->Branch( (prefix + "_phi").c_str(), &ph_phi );
    tree->Branch( (prefix + "_e"  ).c_str(), &ph_e );
    tree->Branch( (prefix + "_ptOrig" ).c_str(), &ph_ptOrig );
    tree->Branch( (prefix + "_etaOrig").c_str(), &ph_etaOrig );
    tree->Branch( (prefix + "_phiOrig").c_str(), &ph_phiOrig );
    tree->Branch( (prefix + "_eOrig"  ).c_str(), &ph_eOrig );

    if( detail > 0 ) {

        tree->Branch( (prefix + "_passVIDLoose").c_str(), &ph_passVIDLoose );
        tree->Branch( (prefix + "_passVIDMedium").c_str(), &ph_passVIDMedium );
        tree->Branch( (prefix + "_passVIDTight").c_str(), &ph_passVIDTight );

        tree->Branch( (prefix + "_chIso").c_str(), &ph_chIso );
        tree->Branch( (prefix + "_neuIso").c_str(), &ph_neuIso );
        tree->Branch( (prefix + "_phoIso").c_str(), &ph_phoIso );

        tree->Branch( (prefix + "_chIsoCorr").c_str(), &ph_chIsoCorr );
        tree->Branch( (prefix + "_neuIsoCorr").c_str(), &ph_neuIsoCorr );
        tree->Branch( (prefix + "_phoIsoCorr").c_str(), &ph_phoIsoCorr );

        tree->Branch( (prefix + "_aeffch").c_str(), &ph_aeffch );
        tree->Branch( (prefix + "_aeffnh").c_str(), &ph_aeffnh );
        tree->Branch( (prefix + "_aeffph").c_str(), &ph_aeffph );

        tree->Branch( (prefix + "_sc_eta").c_str(), &ph_sc_eta );
        tree->Branch( (prefix + "_sc_phi").c_str(), &ph_sc_phi );

        tree->Branch( (prefix + "_hOverE").c_str(), &ph_hOverE );
        tree->Branch( (prefix + "_hOverE_hadronic").c_str(), &ph_hOverE_hdronic);
        tree->Branch( (prefix + "_sigmaIEIE").c_str(), &ph_sigmaIEIE );
        tree->Branch( (prefix + "_sigmaIEIEFull5x5").c_str(), &ph_sigmaIEIEFull5x5 );
        tree->Branch( (prefix + "_r9").c_str(), &ph_r9 );
        tree->Branch( (prefix + "_r9Full5x5").c_str(), &ph_r9Full5x5 );
        tree->Branch( (prefix + "_etaWidth").c_str(), &ph_etaWidth );
        tree->Branch( (prefix + "_phiWidth").c_str(), &ph_phiWidth );

        tree->Branch( (prefix + "_passEleVeto").c_str(), &ph_passEleVeto  );
        tree->Branch( (prefix + "_hasPixSeed").c_str(), &ph_hasPixSeed  );

        if( detail > 1 ) {

            tree->Branch( (prefix + "_sc_rawE").c_str(), &ph_sc_rawE );

            tree->Branch( (prefix + "_ecalIso").c_str(), &ph_ecalIso );
            tree->Branch( (prefix + "_hcalIso").c_str(), &ph_hcalIso );
            tree->Branch( (prefix + "_trkIso").c_str(), &ph_trkIso );
            tree->Branch( (prefix + "_pfIsoPUChHad").c_str(), &ph_pfIsoPUChHad );
            tree->Branch( (prefix + "_pfIsoEcal").c_str(), &ph_pfIsoEcal );
            tree->Branch( (prefix + "_pfIsoHcal").c_str(), &ph_pfIsoHcal );
            tree->Branch( (prefix + "_E3x3").c_str(), &ph_E3x3 );
            tree->Branch( (prefix + "_E1x5").c_str(), &ph_E1x5 );
            tree->Branch( (prefix + "_E2x5").c_str(), &ph_E2x5 );
            tree->Branch( (prefix + "_E5x5").c_str(), &ph_E5x5 );
            //tree->Branch( (prefix + "_sigmaIetaIphi").c_str(), &ph_sigmaIetaIphi );
            //tree->Branch( (prefix + "_sigmaIphiIphi").c_str(), &ph_sigmaIphiIphi );

            tree->Branch( (prefix + "_E1x5Full5x5").c_str(), &ph_E1x5Full5x5 );
            tree->Branch( (prefix + "_E2x5Full5x5").c_str(), &ph_E2x5Full5x5 );
            tree->Branch( (prefix + "_E3x3Full5x5").c_str(), &ph_E3x3Full5x5 );
            tree->Branch( (prefix + "_E5x5Full5x5").c_str(), &ph_E5x5Full5x5 );
        }
    }

}

void PhotonProducer::addUserString( PhotonUserVar type, const std::string userString) {

    // isolation
    if( type == PhotonChIso) {
        _ChIso = userString;
    }
    if( type == PhotonNeuIso ) {
        _NeuIso = userString;
    }
    if( type == PhotonPhoIso) {
        _PhoIso = userString;
    }
    // id
    if( type == PhotonVIDLoose ){
        _VIDLoose = userString;
    }
    if( type == PhotonVIDMedium ){
        _VIDMedium = userString;
    }
    if( type == PhotonVIDTight ){
        _VIDTight = userString;
    }

}
        
void PhotonProducer::addConversionsToken( const edm::EDGetTokenT<reco::ConversionCollection> & tok) {
    _ConversionsToken = tok;
}
void PhotonProducer::addBeamSpotToken( const edm::EDGetTokenT<reco::BeamSpot> & tok) {
    _beamSpotToken= tok;
}
void PhotonProducer::addRhoToken( const edm::EDGetTokenT<double> & tok) {
    _rhoToken = tok;
}
//void PhotonProducer::addElectronsToken( const edm::EDGetTokenT<edm::View<pat::Electron> > & tok) {
//    _ElectronsToken = tok;
//}
void PhotonProducer::addEnergyCalib( const std::string eneCalib) {
   // photon energy scale and smearing corrections
      _eneCalib = eneCalib;
}

void PhotonProducer::produce(const edm::Event &iEvent ) {

    ph_n=0;
    ph_pt->clear();
    ph_eta->clear();
    ph_phi->clear();
    ph_e->clear();
    ph_ptOrig->clear();
    ph_etaOrig->clear();
    ph_phiOrig->clear();
    ph_eOrig->clear();

    if( _detail > 0 ) {

        ph_passVIDLoose->clear();
        ph_passVIDMedium->clear();
        ph_passVIDTight->clear();

        ph_chIso->clear();
        ph_neuIso->clear();
        ph_phoIso->clear();

        ph_chIsoCorr->clear();
        ph_neuIsoCorr->clear();
        ph_phoIsoCorr->clear();

        ph_aeffch->clear();
        ph_aeffnh->clear();
        ph_aeffph->clear();

        ph_sc_eta ->clear();
        ph_sc_phi ->clear();

        ph_hOverE->clear();
        ph_hOverE_hdronic->clear();
        ph_sigmaIEIE->clear();
        ph_sigmaIEIEFull5x5->clear();
        ph_r9->clear();
        ph_r9Full5x5->clear();
        ph_etaWidth->clear();
        ph_phiWidth->clear();

        ph_passEleVeto ->clear();
        ph_hasPixSeed ->clear();

        if( _detail > 1 ) {
            ph_sc_rawE->clear();

            ph_ecalIso->clear();
            ph_hcalIso->clear();
            ph_trkIso->clear();
            ph_pfIsoPUChHad->clear();
            ph_pfIsoEcal->clear();
            ph_pfIsoHcal->clear();
            ph_E3x3->clear();
            ph_E1x5->clear();
            ph_E2x5->clear();
            ph_E5x5->clear();
            //ph_sigmaIetaIphi->clear();
            //ph_sigmaIphiIphi->clear();

            ph_E1x5Full5x5->clear();
            ph_E2x5Full5x5->clear();
            ph_E3x3Full5x5->clear();
            ph_E5x5Full5x5->clear();
        }
    }

    edm::Handle<edm::View<pat::Photon> > photons;
    iEvent.getByToken(_photToken,photons);

    const std::string ph_VIDLoose_str  = _VIDLoose;
    const std::string ph_VIDMedium_str = _VIDMedium;
    const std::string ph_VIDTight_str  = _VIDTight;

    const std::string ph_chIso_str  = _ChIso;
    const std::string ph_neuIso_str = _NeuIso; 
    const std::string ph_phoIso_str = _PhoIso;

    const std::string phoEneCalib_str = _eneCalib;

    //edm::Handle<edm::View<pat::Electron> > electrons_h;
    //iEvent.getByToken(_ElectronsToken, electrons_h);

    edm::Handle<reco::ConversionCollection> conversions_h;
    iEvent.getByToken(_ConversionsToken, conversions_h);

    edm::Handle<reco::BeamSpot> beamSpot_h;
    iEvent.getByToken(_beamSpotToken, beamSpot_h);

    edm::Handle<double> rho_h;
    iEvent.getByToken( _rhoToken, rho_h);

    // needed for a few shower shape variables
    // do not use for now
    //EcalClusterLazyTools lazyTool(iEvent, iSetup, ecalHitEBToken_, ecalHitEEToken_, ecalHitESToken_ );

    for (unsigned int j=0; j < photons->size();++j){
        edm::Ptr<pat::Photon> ph = photons->ptrAt(j);
 
        if( ph->pt() < _minPt ) continue;

        ph_n += 1;

        ph_ptOrig  -> push_back( ph->pt() );
        ph_etaOrig -> push_back( ph->eta() );
        ph_phiOrig -> push_back( ph->phi() );
        ph_eOrig   -> push_back( ph->energy() );

        auto calibp4 = ph->p4() * ph->userFloat( phoEneCalib_str )/ph->energy() ;
        ph_pt ->push_back( calibp4.Pt() );
        ph_eta -> push_back( calibp4.Eta() );
        ph_phi -> push_back( calibp4.phi() );
        ph_e -> push_back( calibp4.E() );

        if( _detail > 0 ) {

            ph_passVIDLoose -> push_back(  ph->photonID( ph_VIDLoose_str  ) );
            ph_passVIDMedium -> push_back( ph->photonID( ph_VIDMedium_str ) );
            ph_passVIDTight -> push_back(  ph->photonID( ph_VIDTight_str  ) );

            float chIso  = ph->userFloat( ph_chIso_str  ) ;
            float neuIso = ph->userFloat( ph_neuIso_str ) ;
            float phoIso = ph->userFloat( ph_phoIso_str ) ;
            ph_chIso -> push_back(  chIso );
            ph_neuIso -> push_back( neuIso );
            ph_phoIso -> push_back( phoIso );

            // Rho corrected isolation
            // followed instructions from
            // https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedPhotonIdentificationRun2#Selection_implementation_details
            // and the implementations from ElectronProducer.cc
            double rhoPrime = std::max(0., *rho_h);
            float eACH = _effectiveAreasCH.getEffectiveArea( fabs(ph->superCluster()->eta()) );
            float eANH = _effectiveAreasNH.getEffectiveArea( fabs(ph->superCluster()->eta()) );
            float eAPH = _effectiveAreasPH.getEffectiveArea( fabs(ph->superCluster()->eta()) );
            ph_aeffch->push_back( eACH );
            ph_aeffnh->push_back( eANH );
            ph_aeffph->push_back( eAPH );
            ph_chIsoCorr ->push_back( std::max(0.0,  chIso   - rhoPrime*(eACH))  );
            ph_neuIsoCorr->push_back( std::max(0.0,  neuIso  - rhoPrime*(eANH))  );
            ph_phoIsoCorr ->push_back( std::max(0.0, phoIso  - rhoPrime*(eAPH))  );

            ph_sc_eta ->push_back(ph->superCluster()->eta());
            ph_sc_phi ->push_back(ph->superCluster()->phi());

            // update according to 
            // https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedPhotonIdentificationRun2#Selection_implementation_details
            // https://github.com/cms-sw/cmssw/blob/CMSSW_9_0_X/RecoEgamma/PhotonIdentification/plugins/cuts/PhoHadronicOverEMCut.cc#L36
            // there was a bug in the Photon ID twiki. The hoverE is supposed to be hadTowOverEm
            ph_hOverE->push_back(ph->hadTowOverEm());
            // save the wrong one just in case it is useful
            ph_hOverE_hdronic->push_back(ph->hadronicOverEm());
            ph_sigmaIEIE->push_back(ph->sigmaIetaIeta());
            ph_sigmaIEIEFull5x5->push_back(ph->full5x5_sigmaIetaIeta());
            ph_r9->push_back(ph->r9());
            ph_r9Full5x5->push_back(ph->full5x5_r9());   
            ph_etaWidth->push_back(ph->superCluster()->etaWidth());
            ph_phiWidth->push_back(ph->superCluster()->phiWidth());

            ph_passEleVeto -> push_back (ph->passElectronVeto());
            ph_hasPixSeed -> push_back( ph->hasPixelSeed());

            if( _detail > 1 ) {

                ph_sc_rawE->push_back(ph->superCluster()->rawEnergy());

                ph_ecalIso->push_back(ph->ecalIso());
                ph_hcalIso->push_back(ph->hcalIso());
                ph_trkIso->push_back(ph->trackIso());
                ph_pfIsoPUChHad->push_back(ph->puChargedHadronIso());
                ph_pfIsoEcal->push_back(ph->ecalPFClusterIso());
                ph_pfIsoHcal->push_back(ph->hcalPFClusterIso());

                // requires implementation fo lazy tools
                //const reco::CaloClusterPtr  seed_clu = photon.superCluster()->seed();
                //ph_E1x3->push_back( lazyTool.e1x3( *seed_clu ) );
                //ph_E2x2->push_back( lazyTool.e2x2( *seed_clu ) );
                //ph_S4->push_back( lazyTool.e2x2( *seed_clu ) / lazyTool.e5x5( *seed_clu ) );
                ////photon cluster shape
                ph_E3x3->push_back(ph->e3x3());
                ph_E1x5->push_back(ph->e1x5());
                ph_E2x5->push_back(ph->e2x5());
                ph_E5x5->push_back(ph->e5x5());
                //ph_sigmaIetaIphi->push_back(ph->sigmaIetaIphi());
                //ph_sigmaIphiIphi->push_back(ph->sigmaIphiIphi());

                ph_E1x5Full5x5->push_back(ph->full5x5_e1x5());    
                ph_E2x5Full5x5->push_back(ph->full5x5_e2x5());
                ph_E3x3Full5x5->push_back(ph->full5x5_e3x3());
                ph_E5x5Full5x5->push_back(ph->full5x5_e5x5());
            }
        }
    }
}
    //for( std::map< std::string, edm::EDGetTokenT<edm::ValueMap<Bool_t> > >::const_iterator itr = _tokens_bool.begin(); itr != _tokens_bool.end(); ++itr ) {

    //    ph_user_bools[itr->first]->clear();

    //    edm::Handle<edm::ValueMap<Bool_t> > bool_val;

    //    iEvent.getByToken( itr->second, bool_val );

    //    for (unsigned int j=0; j < photons->size();++j){
    //        edm::Ptr<pat::Photon> ph = photons->ptrAt(j);

    //        ph_user_bools[itr->first]->push_back( (*bool_val)[ph] );

    //    }
    //}

    //for( std::map< std::string, edm::EDGetTokenT<edm::ValueMap<float> > >::const_iterator itr = _tokens_float.begin(); itr != _tokens_float.end(); ++itr ) {

    //    edm::Handle<edm::ValueMap<Float_t> > float_val;

    //    iEvent.getByToken( itr->second, float_val );

    //    for (unsigned int j=0; j < photons->size();++j){
    //        edm::Ptr<pat::Photon> ph = photons->ptrAt(j);

    //        ph_user_floats[itr->first]->push_back( (*float_val)[ph] );

    //    }
    //}



