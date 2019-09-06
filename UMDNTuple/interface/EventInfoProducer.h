#ifndef EVENTINFOPRODUCER_H
#define EVENTINFOPRODUCER_H
#include <vector>
#include <string>
#include "TTree.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"


class EventInfoProducer {

    public :
        EventInfoProducer();

        void initialize( 
                        const edm::EDGetTokenT<std::vector<reco::Vertex> > & , 
                        const edm::EDGetTokenT<std::vector<PileupSummaryInfo> > & ,
                        const edm::EDGetTokenT<GenEventInfoProduct> & ,
                        const edm::EDGetTokenT<LHEEventProduct> & , 
                        const edm::EDGetTokenT<LHERunInfoProduct> & , 
                        const edm::EDGetTokenT<double> & ,
                        const edm::EDGetTokenT<double> & ,
                        const edm::EDGetTokenT<double> & ,
                        const edm::EDGetTokenT<double> & ,
			 TTree *, TTree *, bool);

        void disableEventWeights() {_disableEventWeights=true;}
        void produce(const edm::Event &iEvent );

        void endRun( const edm::Run & );


    private :

        Bool_t isData;
        unsigned eventNumber;
        unsigned lumiSection;
        unsigned runNumber;
        unsigned bxNumber;
        int vtx_n;
        int pu_n;
        int truepu_n;
        std::vector<double> *EventWeights;
        float rho;
        float prefweight;
        float  prefweightup;
        float  prefweightdown;


        float pdf_id1;
        float pdf_id2;
        float pdf_x1;
        float pdf_x2;
        float pdf_scale;

        edm::EDGetTokenT<std::vector<PileupSummaryInfo> > _puToken;
        edm::EDGetTokenT<std::vector<reco::Vertex> > _vertexToken;
        edm::EDGetTokenT<GenEventInfoProduct> _generatorToken;
        edm::EDGetTokenT<LHEEventProduct> _lheEventToken;
        edm::EDGetTokenT<LHERunInfoProduct> _lheRunToken;
        edm::EDGetTokenT<double> _rhoToken;
        edm::EDGetTokenT< double > _prefweight_token;
        edm::EDGetTokenT< double > _prefweightup_token;
        edm::EDGetTokenT< double > _prefweightdown_token;

        TTree * _infoTree;
        bool _isMC;
        bool _disableEventWeights;
};
#endif
