#ifndef METFILTERPRODUCER_H
#define METFILTERPRODUCER_H
#include <vector>
#include <string>
#include "TTree.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"


class METFilterProducer {

    public :
        METFilterProducer();

        //void initialize( const TTree *tree );
        void initialize( const std::string &prefix, 
                         const edm::EDGetTokenT<edm::TriggerResults >&, 
                         const std::vector<std::string> &,
                         TTree *, TTree* );

        void produce(const edm::Event &iEvent );
        void addecalBadCalibReducedMINIAODFilterToken( const edm::EDGetTokenT<bool> &);
        void endRun( );


    private :

        std::string _prefix;

        edm::EDGetTokenT<edm::TriggerResults> _filterToken;
        edm::EDGetTokenT<bool> _ecalBadCalibReducedMINIAODFilterToken;

        std::map<std::string, int> _filter_map;
        std::vector<std::pair<int, int> > _filter_idx_map;

        std::vector<int> *_passing_filters;

        TTree *_infoTree;

};
#endif
