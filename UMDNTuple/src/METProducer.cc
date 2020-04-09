#include "UMDNTuple/UMDNTuple/interface/METProducer.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/Event.h"

METProducer::METProducer(  ) : 
    met_pt(0),
    met_phi(0),
    allmet_pt(0),
    allmet_phi(0),
    met_JetResUp_pt(0),
    met_JetResUp_phi(0),
    met_JetResDown_pt(0),
    met_JetResDown_phi(0),
    met_JetEnUp_pt(0),
    met_JetEnUp_phi(0),
    met_JetEnDown_pt(0),
    met_JetEnDown_phi(0),
    met_MuonEnUp_pt(0),
    met_MuonEnUp_phi(0),
    met_MuonEnDown_pt(0),
    met_MuonEnDown_phi(0),
    met_ElectronEnUp_pt(0),
    met_ElectronEnUp_phi(0),
    met_ElectronEnDown_pt(0),
    met_ElectronEnDown_phi(0),
    met_PhotonEnUp_pt(0),
    met_PhotonEnUp_phi(0),
    met_PhotonEnDown_pt(0),
    met_PhotonEnDown_phi(0),
    met_UnclusteredEnUp_pt(0),
    met_UnclusteredEnUp_phi(0),
    met_UnclusteredEnDown_pt(0),
    met_UnclusteredEnDown_phi(0),
    met_Type1XY_pt(0)       ,
    met_Type1XY_phi(0)      ,
    met_Type1Smear_pt(0)    ,
    met_Type1Smear_phi(0)   ,
    met_Type1SmearXY_pt(0)  ,
    met_Type1SmearXY_phi(0) ,
    _detail(1)
{

}

void METProducer::initialize( const std::string &prefix, 
                              const edm::EDGetTokenT<edm::View<pat::MET> >&metTok,
                              TTree *tree, int detail) {

    _prefix = prefix;
    _metToken = metTok;
    _detail = detail;

    tree->Branch( (prefix + "_pt" ).c_str(), &met_pt );
    tree->Branch( (prefix + "_phi").c_str(), &met_phi );
    if( _detail > 0 ) {
        tree->Branch( (prefix + "_all_pt" ).c_str(), &allmet_pt );
        tree->Branch( (prefix + "_all_phi").c_str(), &allmet_phi );

        tree->Branch( (prefix + "_JetResUp_pt").c_str()           , &met_JetResUp_pt );
        tree->Branch( (prefix + "_JetResUp_phi").c_str()          , &met_JetResUp_phi );
        tree->Branch( (prefix + "_JetResDown_pt").c_str()         , &met_JetResDown_pt );
        tree->Branch( (prefix + "_JetResDown_phi").c_str()        , &met_JetResDown_phi );
        tree->Branch( (prefix + "_JetEnUp_pt").c_str()            , &met_JetEnUp_pt );
        tree->Branch( (prefix + "_JetEnUp_phi").c_str()           , &met_JetEnUp_phi );
        tree->Branch( (prefix + "_JetEnDown_pt").c_str()          , &met_JetEnDown_pt );
        tree->Branch( (prefix + "_JetEnDown_phi").c_str()         , &met_JetEnDown_phi );
        tree->Branch( (prefix + "_MuonEnUp_pt").c_str()           , &met_MuonEnUp_pt );
        tree->Branch( (prefix + "_MuonEnUp_phi").c_str()          , &met_MuonEnUp_phi );
        tree->Branch( (prefix + "_MuonEnDown_pt").c_str()         , &met_MuonEnDown_pt );
        tree->Branch( (prefix + "_MuonEnDown_phi").c_str()        , &met_MuonEnDown_phi );
        tree->Branch( (prefix + "_ElectronEnUp_pt").c_str()       , &met_ElectronEnUp_pt );
        tree->Branch( (prefix + "_ElectronEnUp_phi").c_str()      , &met_ElectronEnUp_phi );
        tree->Branch( (prefix + "_ElectronEnDown_pt").c_str()     , &met_ElectronEnDown_pt );
        tree->Branch( (prefix + "_ElectronEnDown_phi").c_str()    , &met_ElectronEnDown_phi );
        tree->Branch( (prefix + "_PhotonEnUp_pt").c_str()         , &met_PhotonEnUp_pt );
        tree->Branch( (prefix + "_PhotonEnUp_phi").c_str()        , &met_PhotonEnUp_phi );
        tree->Branch( (prefix + "_PhotonEnDown_pt").c_str()       , &met_PhotonEnDown_pt );
        tree->Branch( (prefix + "_PhotonEnDown_phi").c_str()      , &met_PhotonEnDown_phi );
        tree->Branch( (prefix + "_UnclusteredEnUp_pt").c_str()    , &met_UnclusteredEnUp_pt );
        tree->Branch( (prefix + "_UnclusteredEnUp_phi").c_str()   , &met_UnclusteredEnUp_phi );
        tree->Branch( (prefix + "_UnclusteredEnDown_pt").c_str()  , &met_UnclusteredEnDown_pt );
        tree->Branch( (prefix + "_UnclusteredEnDown_phi").c_str() , &met_UnclusteredEnDown_phi );
        tree->Branch( (prefix + "_Type1XY_pt").c_str() , &met_Type1XY_pt );
        tree->Branch( (prefix + "_Type1XY_phi").c_str() , &met_Type1XY_phi );
        tree->Branch( (prefix + "_Type1Smear_pt").c_str() , &met_Type1Smear_pt );
        tree->Branch( (prefix + "_Type1Smear_phi").c_str() , &met_Type1Smear_phi );
        tree->Branch( (prefix + "_Type1SmearXY_pt").c_str() , &met_Type1SmearXY_pt );
        tree->Branch( (prefix + "_Type1SmearXY_phi").c_str() , &met_Type1SmearXY_phi );

    }


}


void METProducer::produce(const edm::Event &iEvent ) {

    iEvent.getByToken(_metToken,mets);

    met_pt = mets->ptrAt(0)->pt();
    met_phi = mets->ptrAt(0)->phi();
    if( _detail > 0 ) {  
        allmet_pt->clear();
        allmet_phi->clear();
   
        //std::cout<<pat::MET::Raw<<" "<<pat::MET::METCorrectionLevelSize<<std::endl;
        //for  (int i =pat::MET::Raw ; i!=pat::MET::METCorrectionLevelSize-1;i++){
        for  (int i =0; i<10;i++){ // difference between 80X and 94X... extra corrections added
	    pat::MET::METCorrectionLevel ii = static_cast<pat::MET::METCorrectionLevel> (i);
	    //std::cout<<i<< " "<<mets->ptrAt(0)->corPt (ii)<< " "
	    //       	 	  <<mets->ptrAt(0)->corPhi(ii)<<std::endl;
        	allmet_pt->push_back(	       mets->ptrAt(0)->corPt (ii));
        	allmet_phi->push_back(	       mets->ptrAt(0)->corPhi (ii));
        }

        met_Type1XY_pt            = mets->ptrAt(0)->corPt (pat::MET::Type1XY           );
        met_Type1XY_phi           = mets->ptrAt(0)->corPhi(pat::MET::Type1XY           );
        met_Type1Smear_pt         = mets->ptrAt(0)->corPt (pat::MET::Type1Smear           );
        met_Type1Smear_phi        = mets->ptrAt(0)->corPhi(pat::MET::Type1Smear           );
        met_Type1SmearXY_pt       = mets->ptrAt(0)->corPt (pat::MET::Type1SmearXY           );
        met_Type1SmearXY_phi      = mets->ptrAt(0)->corPhi(pat::MET::Type1SmearXY           );



        met_JetResUp_pt           = mets->ptrAt(0)->shiftedPt(pat::MET::JetResUp           );
        met_JetResUp_phi          = mets->ptrAt(0)->shiftedPhi(pat::MET::JetResUp          );
        met_JetResDown_pt         = mets->ptrAt(0)->shiftedPt(pat::MET::JetResDown         );
        met_JetResDown_phi        = mets->ptrAt(0)->shiftedPhi(pat::MET::JetResDown        );
        met_JetEnUp_pt            = mets->ptrAt(0)->shiftedPt(pat::MET::JetEnUp            );
        met_JetEnUp_phi           = mets->ptrAt(0)->shiftedPhi(pat::MET::JetEnUp           );
        met_JetEnDown_pt          = mets->ptrAt(0)->shiftedPt(pat::MET::JetEnDown          );
        met_JetEnDown_phi         = mets->ptrAt(0)->shiftedPhi(pat::MET::JetEnDown         );
        met_MuonEnUp_pt           = mets->ptrAt(0)->shiftedPt(pat::MET::MuonEnUp           );
        met_MuonEnUp_phi          = mets->ptrAt(0)->shiftedPhi(pat::MET::MuonEnUp          );
        met_MuonEnDown_pt         = mets->ptrAt(0)->shiftedPt(pat::MET::MuonEnDown         );
        met_MuonEnDown_phi        = mets->ptrAt(0)->shiftedPhi(pat::MET::MuonEnDown        );
        met_ElectronEnUp_pt       = mets->ptrAt(0)->shiftedPt(pat::MET::ElectronEnUp       );
        met_ElectronEnUp_phi      = mets->ptrAt(0)->shiftedPhi(pat::MET::ElectronEnUp      );
        met_ElectronEnDown_pt     = mets->ptrAt(0)->shiftedPt(pat::MET::ElectronEnDown     );
        met_ElectronEnDown_phi    = mets->ptrAt(0)->shiftedPhi(pat::MET::ElectronEnDown    );
        met_PhotonEnUp_pt         = mets->ptrAt(0)->shiftedPt(pat::MET::PhotonEnUp         );
        met_PhotonEnUp_phi        = mets->ptrAt(0)->shiftedPhi(pat::MET::PhotonEnUp        );
        met_PhotonEnDown_pt       = mets->ptrAt(0)->shiftedPt(pat::MET::PhotonEnDown       );
        met_PhotonEnDown_phi      = mets->ptrAt(0)->shiftedPhi(pat::MET::PhotonEnDown      );
        met_UnclusteredEnUp_pt    = mets->ptrAt(0)->shiftedPt(pat::MET::UnclusteredEnUp    );
        met_UnclusteredEnUp_phi   = mets->ptrAt(0)->shiftedPhi(pat::MET::UnclusteredEnUp   );
        met_UnclusteredEnDown_pt  = mets->ptrAt(0)->shiftedPt(pat::MET::UnclusteredEnDown  );
        met_UnclusteredEnDown_phi = mets->ptrAt(0)->shiftedPhi(pat::MET::UnclusteredEnDown );
    }

}



