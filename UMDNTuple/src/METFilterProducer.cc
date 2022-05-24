#include <bitset>
#include <sstream>
#include <iostream>
#include "UMDNTuple/UMDNTuple/interface/METFilterProducer.h"
#include "FWCore/Framework/interface/Event.h"

METFilterProducer::METFilterProducer(  ) :
    _passing_filters(0)
{

}

void METFilterProducer::initialize( const std::string &prefix,
            const edm::EDGetTokenT<edm::TriggerResults>& trigTok,
            const std::vector<std::string> &filtMap,
            TTree *tree, TTree *infotree) {

    _prefix = prefix;
    _filterToken = trigTok;
    _infoTree = infotree;

    tree->Branch("passedFilters", &_passing_filters );

    _filter_idx_map.clear();
    _filter_map.clear();

    for( std::vector<std::string>::const_iterator itr = filtMap.begin();
            itr != filtMap.end(); ++itr ) {

        int filt_idx;

        std::string::size_type sep_pos = itr->find(":");
        std::string idx_str = itr->substr(0, sep_pos );
        std::string filt_name = itr->substr(sep_pos+1, itr->size() );

        std::stringstream idx_ss(idx_str);

        idx_ss >> filt_idx;

        _filter_map[filt_name] = filt_idx;

    }

}

void METFilterProducer::addecalBadCalibReducedMINIAODFilterToken( const edm::EDGetTokenT<bool> & tok)  { 
    _ecalBadCalibReducedMINIAODFilterToken = tok;
}

void METFilterProducer::produce(const edm::Event &iEvent ) {

    edm::Handle<edm::TriggerResults> filters;
    iEvent.getByToken(_filterToken,filters);

    if( !filters.isValid() || filters.failedToGet() ) {
        std::cout << "could not get filter results.  Will not set filters!" << std::endl;
        return;
    }

    _passing_filters->clear();

    const edm::TriggerNames filtNames( iEvent.triggerNames( *filters ) );

    if( _filter_idx_map.size() == 0 ) {

        for (unsigned i = 0; i < filtNames.size(); i++) {

            std::string filtname = filtNames.triggerName(i);

            std::map<std::string, int>::const_iterator mitr = _filter_map.find(filtname);

            if( mitr != _filter_map.end() ) {
                _filter_idx_map.push_back( std::make_pair(i, mitr->second) );
            }
        }
    }

    for( std::vector<std::pair<int,int> >::const_iterator mitr = _filter_idx_map.begin();
            mitr != _filter_idx_map.end(); ++mitr ) {
        if( filters->accept( mitr->first ) ) {
            _passing_filters->push_back( mitr->second );
        }
    }

    // now handle the manually added filters
    // check that they were requested in the list and get the ID
    for( std::map<std::string,int>::const_iterator mitr = _filter_map.begin();
            mitr != _filter_map.end(); ++mitr ) {
        if( mitr->first == "Flag_ecalBadCalibReducedMINIAODFilter" ) {
            edm::Handle<bool> ifilterecalBadCalib;
            iEvent.getByToken(_ecalBadCalibReducedMINIAODFilterToken, ifilterecalBadCalib);
            if( *ifilterecalBadCalib ) _passing_filters->push_back( mitr->second );
        }
    }

}

void METFilterProducer::endRun() {

    int filter_ids = 0;
    std::vector<char*> descriptions;
    descriptions.push_back(new char[1024]);

    _infoTree->Branch( "filter_ids", &filter_ids, "filter_ids/I" );
    _infoTree->Branch( "filter_names", descriptions.back(), "filter_names/C");

    for( std::map<std::string, int>::const_iterator itr = _filter_map.begin();
            itr != _filter_map.end(); ++itr ) {

        filter_ids = itr->second;
        strcpy( descriptions.back(), itr->first.c_str() );

        _infoTree->Fill();
    }

}
