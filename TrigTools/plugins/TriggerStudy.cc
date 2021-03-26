#ifndef CMSSWTools_TRIGTOOLS_TRIGGERSTUDY
#define CMSSWTools_TRIGTOOLS_TRIGGERSTUDY

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/HLTPathStatus.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/L1Trigger/interface/Jet.h"

#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"

#include "CondFormats/L1TObjects/interface/L1TUtmTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1TUtmTriggerMenuRcd.h"
#include "TriggerEmulator/nTupleAnalysis/interface/TrigEmulatorTool.h"


#include <vector>
#include <string>
#include <iostream>
#include <math.h>
#include <array>



using std::cout; using std::endl;
using std::string; using std::vector;
typedef std::array<float, 4> JetInfo;


//little helper function to get handles easier
//note the use of annoymous namespace to avoid linking conflicts
namespace{
  template<typename T>
    edm::Handle<T> getHandle(const edm::Event& iEvent,const edm::EDGetTokenT<T>& token)
  {
    edm::Handle<T> handle;
    iEvent.getByToken(token,handle);
    return handle;
  }
}

namespace{

  void addJetInfo(std::vector<JetInfo>& jetInfo, float pt, float eta, float phi, float deepFlavour ){
    jetInfo.push_back(JetInfo{ {pt, eta, phi, deepFlavour} });
  }
}



//the functions which actually match the trigger objects and see if it passes
namespace{
  vector<const pat::TriggerObjectStandAlone*> getMatchedObjs(const float eta,const float phi,const vector<pat::TriggerObjectStandAlone>& trigObjs,const float maxDeltaR=0.1, string filterLabel = "")
  {
    vector<const pat::TriggerObjectStandAlone*> matchedObjs;
    const float maxDR2 = maxDeltaR*maxDeltaR;
    for(auto& trigObj : trigObjs){
      if(filterLabel != "" && !trigObj.hasFilterLabel(filterLabel)) continue;
      const float dR2 = reco::deltaR2(eta,phi,trigObj.eta(),trigObj.phi());
      if(dR2<maxDR2) matchedObjs.push_back(&trigObj);
    }
    return matchedObjs;
  }

  void printAllFilters(const float eta,const float phi,const vector<pat::TriggerObjectStandAlone>& trigObjs,const float maxDeltaR=0.1)
  {
    const auto matchedObjs = getMatchedObjs(eta,phi,trigObjs,maxDeltaR);
    for(const auto trigObj : matchedObjs){

      //normally would auto this but to make it clearer for the example
      const vector<string>& objFilters = trigObj->filterLabels();
	
      for(const string& s : objFilters){
	cout << " \t\t matched Filter is " << s << endl;
      }
    }
    return;
  }


  /*
  bool checkFilters(const float eta,const float phi,const vector<pat::TriggerObjectStandAlone>& trigObjs,const vector<string>& filterNames,const float maxDeltaR=0.1)
  {
    bool passAnyFilter=false;
    const auto matchedObjs = getMatchedObjs(eta,phi,trigObjs,maxDeltaR);
    for(auto& filterName : filterNames){
      for(const auto trigObj : matchedObjs){
	//normally would auto this but to make it clearer for the example
	const vector<string>& objFilters = trigObj->filterLabels();
	
	for(const string& s : objFilters){
	  cout << " s is " << s << endl;
	}

	//I dont think filterLabels are sorted so use std::find to see if filterName is in 
	//the list of passed filters for this object
	if(std::find(objFilters.begin(),objFilters.end(),filterName)!=objFilters.end()){
	  cout <<" object "<<trigObj->pt() <<" "<< trigObj->eta() << " " << trigObj->phi() << " passes "<<filterName<< endl;
	  cout << " \t hasPAthLastFilterACcepted: " << trigObj->hasPathLastFilterAccepted() << " L3 " << trigObj->hasPathL3FilterAccepted() << endl;
	  if(!trigObj->hasFilterLabel(filterName))	    cout << " ERROR " << endl;

	  passAnyFilter=true;
	}
      }//end loop over matched trigger objects
    }//end loop over filter lables
    return passAnyFilter;
  }
  */

  bool checkFilter(const float eta,const float phi,const vector<pat::TriggerObjectStandAlone>& trigObjs,const string& filterName,const float maxDeltaR=0.1)
  {
    const auto matchedObjs = getMatchedObjs(eta,phi,trigObjs,maxDeltaR);
    for(const auto trigObj : matchedObjs){
      //normally would auto this but to make it clearer for the example
      //const vector<string>& objFilters = trigObj->filterLabels();
	
      if(trigObj->hasFilterLabel(filterName)) return true;

    }//end loop over matched trigger objects

    return false;
  }


  //this function determines the index of the path in trigger results, if not
  //found it returns an index equal to the size of triggerNames
  //note it matches on whether the name in triggernames starts with the pathName
  //this is because HLT paths are of form HLT_TriggerName_vX where X is the version number
  //X changes frequiently so often you want to match all versions which can be
  //achieved by passing in HLT_TriggerName_v to this function 
  size_t getPathIndex(const string& pathName,const edm::TriggerNames& trigNames){
    for(size_t index = 0;index<trigNames.size(); index++){
      if(trigNames.triggerName(index).find(pathName)==0){
	return index;
      }
    }
    return trigNames.size();
  }


  /*
  bool foundFilter(const string& filter, const vector<pat::TriggerObjectStandAlone>& trigObjs){
    for(auto& trigObj : trigObjs){
      if(trigObj.hasFilterLabel(filter))
	return true;
    }

    return false;
  }
  */

  /*
  vector<const pat::TriggerObjectStandAlone*> getAllMatchedJets(edm::Handle<edm::View<pat::Jet> > jetsHandle, const vector<pat::TriggerObjectStandAlone>& trigObjs,string filterLabel = "", const float maxDeltaR=0.1, bool debug=false)
  {
    vector<const pat::TriggerObjectStandAlone*> allMatchedObjs;

    for(auto& jet : *jetsHandle){
      double eta = jet.eta();
      double phi = jet.phi();
      const vector<const pat::TriggerObjectStandAlone*> matchedJets = getMatchedObjs(eta,phi,trigObjs,0.1,filterLabel);

      // There are sometimes duplicate PF jets,  take only one
      if(matchedJets.size() > 0) allMatchedObjs.push_back(matchedJets.at(0));

      if(debug){
	if(matchedJets.size() > 1){
	  cout << jet.pt() << " " << jet.eta() << " " << jet.phi();
	  cout << " nMatchedJets " << filterLabel << " " << matchedJets.size() << endl;
    
	  for(auto& trigObjMatch : matchedJets){
	    const float dR2 = reco::deltaR2(eta,phi,trigObjMatch->eta(),trigObjMatch->phi());
	    cout << " \t dR " << sqrt(dR2) << " pt "  << trigObjMatch->pt() << endl;
	  }
	}
      }//debug
    }// jetHandle


    return allMatchedObjs;
  }
  */


  vector<const pat::TriggerObjectStandAlone*> getAllTrigObjs(const vector<pat::TriggerObjectStandAlone>& trigObjs,string filterLabel = "", bool debug=false)
  {
    vector<const pat::TriggerObjectStandAlone*> allTrigObjs;

    for(auto& trigObj : trigObjs){
      if(!trigObj.hasFilterLabel(filterLabel)) continue;

      if(debug){
	cout << "Test jet " << filterLabel << " with pt " << trigObj.pt()  << " eta " << trigObj.eta() << " phi " << trigObj.phi() << endl;
      }


      //
      // Overlap removal
      //
      bool passOverlap = true;
      //for(auto& otherTrigObj : allTrigObjs){
      //	const float dR2 = reco::deltaR2(otherTrigObj->eta(),otherTrigObj->phi(),trigObj.eta(),trigObj.phi());
      //	if(dR2 < 0.1*0.1) {
      //	  
      //	  if(debug){
      //	    cout << "Killing jet " << filterLabel << " with pt " << trigObj.pt()  << " eta " << trigObj.eta() << " phi " << trigObj.phi() << " ... Overlap of " << sqrt(dR2) << endl;
      //	  }
      //
      //	  passOverlap = false;
      //	}
      //}// overlap loop
      
      if(passOverlap){
	if(debug){
	  cout << " Added " << endl;
	}
	allTrigObjs.push_back(&trigObj);
      }
      
    }


    return allTrigObjs;
  }


  



}//namespace


class TriggerStudy : public edm::EDAnalyzer {
private:

  edm::InputTag trigObjsTag_;
  edm::InputTag trigResultsTag_;
  vector<edm::ParameterSet> filtersToPass_;
  vector<string> pathsToPass_;
  vector<string> hltPreSelection_;
  string year_;
  edm::ParameterSet offlinePreSelection_;
  unsigned int minNSelJet_ = 0;
  unsigned int minNTagMedJet_ = 0;
  unsigned int minNTagTightJet_ = 0;

  bool isMC_;
  bool isBBMC_;
  bool testL1_;
  bool doEmulation_ = false;
  vector<edm::ParameterSet> jetTurnOns_;
  vector<edm::ParameterSet> triggersToPlot_;

  //trigger results stores whether a given path passed or failed
  //a path is series of filters
  edm::EDGetTokenT<edm::TriggerResults> trigResultsToken_;
  //triggers are the objects the trigger is run on, with a list of filters they pass
  //match to these to see if a given electron/photon/whatever passed a given filter
  edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > trigObjsToken_;

  edm::EDGetTokenT<edm::View<pat::Jet> > jetsToken_;
  edm::EDGetTokenT<BXVector<l1t::Jet> > L1JetsToken_;
  edm::EDGetTokenT<BXVector<GlobalAlgBlk> > GlobalAlgToken_;
  edm::EDGetTokenT<edm::View<reco::GenJet> > truthJetsToken_;
  edm::EDGetTokenT<edm::View<reco::GenParticle> > truthPartsToken_;
  edm::Service<TFileService> fs;


  // counters
  unsigned int NEvents_all = 0;
  unsigned int NEvents_passHLTPreSelection = 0;
  unsigned int NEvents_passOfflinePreSelection = 0;
  

  struct jetHists {

    TH1F* h_pt;
    TH1F* h_pt_s;
    TH1F* h_phi;
    TH1F* h_eta;
    TH1F* h_deepFlavour;


    jetHists(TFileDirectory& jetDir, string cutName ){
      h_pt          = jetDir.make<TH1F>( ("pt"+cutName).c_str()  , "p_{T}", 250,  0., 500. );
      h_pt_s        = jetDir.make<TH1F>( ("pt_s"+cutName).c_str()  , "p_{T}",200,  0., 100. );
      h_phi         = jetDir.make<TH1F>( ("phi"+cutName).c_str()  , "phi",  100,  -3.2, 3.2 );
      h_eta         = jetDir.make<TH1F>( ("eta"+cutName).c_str()  , "eta",  100,  -4, 4 );
      h_deepFlavour = jetDir.make<TH1F>( ("deepFlavour"+cutName).c_str()  , "deepFlavour",  100,  -0.1, 1.1 );
    }



    void Fill(double pt, double eta, double phi, double deepFlavour, float weight = 1.0 ){
      h_pt          ->Fill(pt, weight);
      h_pt_s        ->Fill(pt, weight);
      h_phi         ->Fill(phi, weight);
      h_eta         ->Fill(eta, weight);
      h_deepFlavour ->Fill(deepFlavour, weight);
    }

    void Fill(JetInfo jInfo, float weight = 1.0 ){
      Fill(jInfo.at(0), jInfo.at(1), jInfo.at(2), jInfo.at(3), weight);
    }


  };


  struct eventHists {

    TH1F* h_mBB      = nullptr;
    TH1F* h_pTBB     = nullptr;
    TH1F* h_nSelJets = nullptr;
    TH1F* h_hT       = nullptr;    
    TH1F* h_hT30     = nullptr;    
    TH1F* h_hT_s     = nullptr;    
    TH1F* h_hT30_s   = nullptr;    
    TH1F* h_hT30_l   = nullptr;    

    jetHists* h_selJets = nullptr;
    jetHists* h_tagJets = nullptr;
    jetHists* h_leadJet = nullptr;
    jetHists* h_sublJet = nullptr;
    jetHists* h_leadTag = nullptr;
    jetHists* h_sublTag = nullptr;


    eventHists(edm::Service<TFileService>& fs, string cutName, bool isBBMC ){
      if(isBBMC){
	h_mBB      = fs->make<TH1F>( ("mBB_"+cutName).c_str()  , "m_{BB}", 100,  0., 1000. );
	h_pTBB     = fs->make<TH1F>( ("pTBB_"+cutName).c_str()  , "pT_{BB}", 100,  0., 1000. );
      }
      h_nSelJets = fs->make<TH1F>( ("nSelJet_"+cutName).c_str()  , "Selected Jet Multiplicity",  16,  -0.5, 15.5 );
      h_hT       = fs->make<TH1F>( ("hT_"+cutName).c_str()  , "hT",  200,  0, 1000 );
      h_hT30     = fs->make<TH1F>( ("hT30_"+cutName).c_str()  , "hT (jets pt > 30 GeV)",  200,  0, 1000 );
      h_hT30_l   = fs->make<TH1F>( ("hT30_l_"+cutName).c_str()  , "hT (jets pt > 30 GeV)",  200,  0, 2000 );
      

      TFileDirectory selJetsDir = fs->mkdir( "selJets" );
      TFileDirectory tagJetsDir = fs->mkdir( "tagJets" );
      TFileDirectory leadJetDir = fs->mkdir( "leadJet" );
      TFileDirectory sublJetDir = fs->mkdir( "sublJet" );
      TFileDirectory leadTagDir = fs->mkdir( "leadTag" );
      TFileDirectory sublTagDir = fs->mkdir( "sublTag" );


      h_selJets = new jetHists(selJetsDir, "_"+cutName);
      h_tagJets = new jetHists(tagJetsDir, "_"+cutName);
      h_leadJet = new jetHists(leadJetDir, "_"+cutName);
      h_sublJet = new jetHists(sublJetDir, "_"+cutName);
      h_leadTag = new jetHists(leadTagDir, "_"+cutName);
      h_sublTag = new jetHists(sublTagDir, "_"+cutName);

    }

    void Fill(double mBB, double pTBB, unsigned int nSelJets, double hT, double hT30, vector<JetInfo> selJets, vector<JetInfo> tagJets, float weight = 1.0 ){
      if(h_mBB)  h_mBB      ->Fill(mBB, weight);
      if(h_pTBB) h_pTBB     ->Fill(pTBB, weight);
      h_nSelJets ->Fill(nSelJets, weight);
      h_hT       ->Fill(hT, weight);
      h_hT30     ->Fill(hT30, weight);
      h_hT30_l     ->Fill(hT30, weight);

      for(const JetInfo& jInfo: selJets){
      	h_selJets->Fill(jInfo, weight);
      }

      for(const JetInfo& jInfo: tagJets){
      	h_tagJets->Fill(jInfo, weight);
      }

      if(selJets.size() > 0) h_leadJet->Fill(selJets.at(0), weight);
      if(selJets.size() > 1) h_sublJet->Fill(selJets.at(1), weight);

      if(tagJets.size() > 0) h_leadTag->Fill(tagJets.at(0), weight);
      if(tagJets.size() > 1) h_sublTag->Fill(tagJets.at(1), weight);

    }

  };


  //
  //  Event Hists
  //
  vector<eventHists> hAll;
  vector<eventHists> hTrigStudy;

  //
  //  Jet Hists
  //
  vector<jetHists> hJets_num; 
  vector<jetHists> hJets_den; 

  vector<string> L1Names_;
  vector<unsigned int> L1Indices_;  
  map<std::string, unsigned int> L1_NamesToPos;


  //
  //  Trigger Emulation
  //
  TriggerEmulator::TrigEmulatorTool* trigEmulatorDetails = nullptr;
  TriggerEmulator::TrigEmulatorTool* trigEmulator = nullptr;

public:
  explicit TriggerStudy(const edm::ParameterSet& iPara);
  ~TriggerStudy(){ }
  void beginJob() override;
  void beginRun(edm::Run const&, edm::EventSetup const&) override;
  void endJob() override;
  void analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)override;

};

TriggerStudy::TriggerStudy(const edm::ParameterSet& iPara):
  trigObjsTag_(iPara.getParameter<edm::InputTag>("trigObjs")),
  trigResultsTag_(iPara.getParameter<edm::InputTag>("trigResults")),
  filtersToPass_(iPara.getParameter<vector<edm::ParameterSet> >("filtersToPass")), 
  pathsToPass_(iPara.getParameter<vector<string> >("pathsToPass")),
  hltPreSelection_(iPara.getParameter<vector<string> >("hltPreSelection")),
  offlinePreSelection_(iPara.getParameter<edm::ParameterSet>("offlinePreSelection")),
  isMC_(iPara.getParameter<bool>("isMC")),
  isBBMC_(iPara.getParameter<bool>("isBBMC")),
  testL1_(iPara.getParameter<bool>("testL1")),
  doEmulation_(iPara.getParameter<bool>("doEmulation")),
  jetTurnOns_(iPara.getParameter<vector<edm::ParameterSet> >("jetTurnOns")), 
  triggersToPlot_(iPara.getParameter<vector<edm::ParameterSet> >("triggersToPlot")), 
  trigResultsToken_(consumes<edm::TriggerResults>(trigResultsTag_)),
  trigObjsToken_(consumes<vector<pat::TriggerObjectStandAlone> >(trigObjsTag_)),
  jetsToken_(consumes<edm::View<pat::Jet> >(iPara.getParameter<edm::InputTag>("jets"))),
  L1JetsToken_(consumes<BXVector<l1t::Jet> >(iPara.getParameter<edm::InputTag>("L1Jets"))),
  GlobalAlgToken_(consumes<BXVector<GlobalAlgBlk> >(iPara.getParameter<edm::InputTag>("AlgInputTag"))),
  truthJetsToken_(consumes<edm::View<reco::GenJet> >(iPara.getParameter<edm::InputTag>("truthJets"))),
  truthPartsToken_(consumes<edm::View<reco::GenParticle> >(iPara.getParameter<edm::InputTag>("truthParts")))
			       //algInputTag_(iPara.getParameter<edm::InputTag>("AlgInputTag")),
			       //extInputTag_(iPara.getParameter<edm::InputTag>("ExtInputTag"))
{
  if(offlinePreSelection_.exists("minNSelJet"))
     minNSelJet_      = offlinePreSelection_.getParameter<unsigned int>("minNSelJet");

  if(offlinePreSelection_.exists("minNTagMedJet"))
    minNTagMedJet_   = offlinePreSelection_.getParameter<unsigned int>("minNTagMedJet");

  if(offlinePreSelection_.exists("minNTagTightJet"))
    minNTagTightJet_ = offlinePreSelection_.getParameter<unsigned int>("minNTagTightJet");
  
  edm::LogInfo("TriggerStudy") << " Offline Selection: minNSelJet: " << minNSelJet_ << "  minNTagMedJet: " << minNTagMedJet_ << " minNTagTightJet: " << minNTagTightJet_;



  if(doEmulation_){

    year_ = iPara.getParameter<string>("year");
    cout << "Making Emulator for year" << year_ << endl;

    if(year_ == "2018"){
      trigEmulatorDetails = new TriggerEmulator::TrigEmulatorTool("trigEmulatorDetails", 1, 100, year_);

      trigEmulatorDetails->AddTrig("EMU_L1ORAll",    {"L1ORAll_Ht330_4j_3b"});
      trigEmulatorDetails->AddTrig("EMU_CaloHt320",  {"L1ORAll_Ht330_4j_3b","CaloHt320"});

      trigEmulatorDetails->AddTrig("EMU_4PF30",      {"L1ORAll_Ht330_4j_3b","CaloHt320"}, {"PF30DenMatch"},{4});
      trigEmulatorDetails->AddTrig("EMU_1PF75",      {"L1ORAll_Ht330_4j_3b","CaloHt320"}, {"PF30DenMatch","PF75DenMatch"},{4,1});
      trigEmulatorDetails->AddTrig("EMU_2PF60",      {"L1ORAll_Ht330_4j_3b","CaloHt320"}, {"PF30DenMatch","PF75DenMatch","PF60DenMatch"},{4,1,2});
      trigEmulatorDetails->AddTrig("EMU_3PF45",      {"L1ORAll_Ht330_4j_3b","CaloHt320"}, {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch"},{4,1,2,3});
      trigEmulatorDetails->AddTrig("EMU_4PF40",      {"L1ORAll_Ht330_4j_3b","CaloHt320"}, {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4});
    
      trigEmulatorDetails->AddTrig("EMU_PFHt330",       {"L1ORAll_Ht330_4j_3b","CaloHt320","PFHt330"},     {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4});
      trigEmulatorDetails->AddTrig("EMU_HT330_4j_3b",   {"L1ORAll_Ht330_4j_3b","CaloHt320","PFHt330"},     {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4},{"PFDeepCSVMatchBtagDenMatch"},{3});

      //trigEmulatorDetails->AddTrig("EMU_2b116_L1ORAll",   {}, {"L1112TandPDenMatch"}, {2});
      //trigEmulatorDetails->AddTrig("EMU_2b116_2Calo100",  {}, {"L1112TandPDenMatch","Calo100DenMatch"}, {2, 2});
      //trigEmulatorDetails->AddTrig("EMU_2b116_2CaloBTags",{}, {"L1112TandPDenMatch"}, {2},                    {"CaloDeepCSV0p7MatchBtag"},{2});
      //trigEmulatorDetails->AddTrig("EMU_2b116_2PF116",    {}, {"L1112TandPDenMatch","PF116DenMatch"}, {2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});
      //trigEmulatorDetails->AddTrig("EMU_2b116",           {}, {"L1112TandPDenMatch","PF116DenMatch","PF116DrDenMatch"}, {2, 2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});

      trigEmulatorDetails->AddTrig("EMU_2b116_L1ORAll",   {"L1ORAll_2b116"}  );
      trigEmulatorDetails->AddTrig("EMU_2b116_2Calo100",  {"L1ORAll_2b116"}, {"Calo100DenMatch"}, {2});
      trigEmulatorDetails->AddTrig("EMU_2b116_2CaloBTags",{"L1ORAll_2b116"}, {}, {},                    {"CaloDeepCSV0p7MatchBtag"},{2});
      trigEmulatorDetails->AddTrig("EMU_2b116_2PF116",    {"L1ORAll_2b116"}, {"PF116DenMatch"}, {2}, {"CaloDeepCSV0p7MatchBtag"},{2});
      trigEmulatorDetails->AddTrig("EMU_2b116",           {"L1ORAll_2b116"}, {"PF116DenMatch","PF116DrDenMatch"}, {2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});



      trigEmulator = new TriggerEmulator::TrigEmulatorTool("trigEmulator", 1, 100, year_);
      trigEmulator->AddTrig("EMU_HT330_4j_3b",   {"L1ORAll_Ht330_4j_3b","CaloHt320","PFHt330"},     {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4},{"PFDeepCSVMatchBtagDenMatch"},{3});
      //trigEmulator->AddTrig("EMU_2b116",    {},  {"L1112TandPDenMatch","PF116DenMatch","PF116DrDenMatch"}, {2, 2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});
      trigEmulator->AddTrig("EMU_2b116",    {"L1ORAll_2b116"},  {"PF116DenMatch","PF116DrDenMatch"}, {2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});
    }

    if(year_ == "2017"){

      trigEmulatorDetails = new TriggerEmulator::TrigEmulatorTool("trigEmulatorDetails", 1, 100, year_);

      trigEmulatorDetails->AddTrig("EMU_L1ORAll",    {"L1ORAll_Ht300_4j_3b"});
      trigEmulatorDetails->AddTrig("EMU_CaloHt300",  {"L1ORAll_Ht300_4j_3b","CaloHt300"});

      trigEmulatorDetails->AddTrig("EMU_4PF30",      {"L1ORAll_Ht300_4j_3b","CaloHt300"}, {"PF30DenMatch"},{4});
      trigEmulatorDetails->AddTrig("EMU_1PF75",      {"L1ORAll_Ht300_4j_3b","CaloHt300"}, {"PF30DenMatch","PF75DenMatch"},{4,1});
      trigEmulatorDetails->AddTrig("EMU_2PF60",      {"L1ORAll_Ht300_4j_3b","CaloHt300"}, {"PF30DenMatch","PF75DenMatch","PF60DenMatch"},{4,1,2});
      trigEmulatorDetails->AddTrig("EMU_3PF45",      {"L1ORAll_Ht300_4j_3b","CaloHt300"}, {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch"},{4,1,2,3});
      trigEmulatorDetails->AddTrig("EMU_4PF40",      {"L1ORAll_Ht300_4j_3b","CaloHt300"}, {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4});
    
      trigEmulatorDetails->AddTrig("EMU_PFHt300",       {"L1ORAll_Ht300_4j_3b","CaloHt300","PFHt300"},     {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4});
      trigEmulatorDetails->AddTrig("EMU_HT300_4j_3b",   {"L1ORAll_Ht300_4j_3b","CaloHt300","PFHt300"},     {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4},{"PFDeepCSVMatchBtagDenMatch"},{3});
      
      //trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {}, {"L1100TandP"}, {2});
      //trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {}, {"L1100TandP","Calo100DenMatch"}, {2, 2});
      //trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{}, {"L1100TandP"}, {2},                    {"CaloDeepCSV0p7MatchBtag"},{2});
      //trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {}, {"L1100TandP","PF100DenMatch"}, {2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});
      //trigEmulatorDetails->AddTrig("EMU_2b100",           {}, {"L1100TandP","PF100DenMatch","PF100DrDenMatch"}, {2, 2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});

      trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {"L1ORAll_2b100"});
      trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {"L1ORAll_2b100"}, {"Calo100DenMatch"}, {2});
      trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{"L1ORAll_2b100"}, {}, {},                    {"CaloDeepCSV0p7MatchBtag"},{2});
      trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {"L1ORAll_2b100"}, {"PF100DenMatch"}, { 2}, {"CaloDeepCSV0p7MatchBtag"},{2});
      trigEmulatorDetails->AddTrig("EMU_2b100",           {"L1ORAll_2b100"}, {"PF100DenMatch","PF100DrDenMatch"}, {2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});



      trigEmulator = new TriggerEmulator::TrigEmulatorTool("trigEmulator", 1, 100, year_);
      trigEmulator->AddTrig("EMU_HT300_4j_3b",   {"L1ORAll_Ht300_4j_3b","CaloHt300","PFHt300"},     {"PF30DenMatch","PF75DenMatch","PF60DenMatch","PF45DenMatch","PF40DenMatch"},{4,1,2,3,4},{"PFDeepCSVMatchBtagDenMatch"},{3});
      //trigEmulator->AddTrig("EMU_2b100",    {},  {"L1100TandP","PF100DenMatch","PF100DrDenMatch"}, {2, 2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});
      trigEmulator->AddTrig("EMU_2b100",    {"L1ORAll_2b100"},  {"PF100DenMatch","PF100DrDenMatch"}, {2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});


    }


    if(year_ == "2016"){

      trigEmulatorDetails = new TriggerEmulator::TrigEmulatorTool("trigEmulatorDetails", 1, 100, year_);

      trigEmulatorDetails->AddTrig("EMU_L1ORAll",    {"L1ORAll_4j_3b"});
      trigEmulatorDetails->AddTrig("EMU_4Calo45",    {"L1ORAll_4j_3b"}, {"Calo45"},{4});
      trigEmulatorDetails->AddTrig("EMU_3CaloBtags", {"L1ORAll_4j_3b"}, {"Calo45"},{4},{"CaloCSVMatchBtagDenMatch"},{3});
      trigEmulatorDetails->AddTrig("EMU_4j_3b",      {"L1ORAll_4j_3b"}, {"Calo45","PF45DenMatch"},{4,4},{"CaloCSVMatchBtagDenMatch"},{3});
    
      //trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {}, {"L1100TandPDenMatch"}, {2});
      //trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {}, {"L1100TandPDenMatch","Calo100DenMatch"}, {2, 2});
      //trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{}, {"L1100TandPDenMatch"}, {2},                    {"CaloCSV0p84MatchBtag"},{2});
      //trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {}, {"L1100TandPDenMatch","PF100DenMatch"}, {2, 2}, {"CaloCSV0p84MatchBtag"},{2});
      //trigEmulatorDetails->AddTrig("EMU_2b100",           {}, {"L1100TandPDenMatch","PF100DenMatch","PF100DrDenMatch"}, {2, 2, 2}, {"CaloCSV0p84MatchBtag"},{2});

      trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {"L1ORAll_2b100"} );
      trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {"L1ORAll_2b100"}, {"Calo100DenMatch"}, {2});
      trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{"L1ORAll_2b100"}, {}, {},                    {"CaloCSV0p84MatchBtag"},{2});
      trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {"L1ORAll_2b100"}, {"PF100DenMatch"}, {2},    {"CaloCSV0p84MatchBtag"},{2});
      trigEmulatorDetails->AddTrig("EMU_2b100",           {"L1ORAll_2b100"}, {"PF100DenMatch","PF100DrDenMatch"}, {2, 2}, {"CaloCSV0p84MatchBtag"},{2});


      trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_L1ORAll",       {"L1ORAll_2j_2j_3b"});
      trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_4Calo30",       {"L1ORAll_2j_2j_3b"}, {"Calo30"},{4});
      trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_2Calo90",       {"L1ORAll_2j_2j_3b"}, {"Calo30","Calo90DenMatch"},{4,2});
      trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_3CaloBTags",    {"L1ORAll_2j_2j_3b"}, {"Calo30","Calo90DenMatch"},{4,2},{"CaloCSVMatchBtagDenMatch"},{3});
      trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_4PF30",         {"L1ORAll_2j_2j_3b"}, {"Calo30","Calo90DenMatch","PF30DenMatch"},{4,2,4},{"CaloCSVMatchBtagDenMatch"},{3});
      trigEmulatorDetails->AddTrig("EMU_2j_2j_3b",               {"L1ORAll_2j_2j_3b"}, {"Calo30","Calo90DenMatch","PF30DenMatch","PF90DenMatch"},{4,2,4,2},{"CaloCSVMatchBtagDenMatch"},{3});


      trigEmulator = new TriggerEmulator::TrigEmulatorTool("trigEmulator", 1, 100, year_);
      trigEmulator->AddTrig("EMU_4j_3b",      {"L1ORAll_4j_3b"}, {"Calo45","PF45DenMatch"},{4,4},{"CaloCSVMatchBtagDenMatch"},{3});
      //trigEmulator->AddTrig("EMU_2b100",    {},  {"L1100TandPDenMatch","PF100DenMatch","PF100DrDenMatch"}, {2, 2, 2}, {"CaloCSV0p84MatchBtag"},{2});
      trigEmulator->AddTrig("EMU_2b100",    {"L1ORAll_2b100"},  {"PF100DenMatch","PF100DrDenMatch"}, {2, 2}, {"CaloCSV0p84MatchBtag"},{2});
      trigEmulator->AddTrig("EMU_2j_2j_3b", {"L1ORAll_2j_2j_3b"}, {"Calo30","Calo90DenMatch","PF30DenMatch","PF90DenMatch"},{4,2,4,2},{"CaloCSVMatchBtagDenMatch"},{3});

    }


  }


}

void TriggerStudy::beginJob()
{

  hAll           .push_back(eventHists(fs,"all", isBBMC_));

  for(edm::ParameterSet filterInfo : filtersToPass_){
    string name = filterInfo.getParameter<string>("histName");
    hAll          .push_back(eventHists(fs,name,isBBMC_));
  }

  TFileDirectory jetDir = fs->mkdir( "jetHists" );

  for(edm::ParameterSet jetTurnOnInfo : jetTurnOns_){
    string name = jetTurnOnInfo.getParameter<string>("histName");
    hJets_num.push_back(jetHists(jetDir,"_"+name));
    hJets_den.push_back(jetHists(jetDir,"_"+name+"_den"));
  }


  for(edm::ParameterSet triggerPath : triggersToPlot_){
    string name = triggerPath.getParameter<string>("name");
    hTrigStudy.push_back(eventHists(fs,"passHLT_"+name,isBBMC_));
  }


}


void TriggerStudy::beginRun(edm::Run const&, edm::EventSetup const& evSetup){
  
  L1Names_.clear();
  L1Indices_.clear();

  edm::ESHandle<L1TUtmTriggerMenu> menu;
  evSetup.get<L1TUtmTriggerMenuRcd>().get(menu);
  auto const& mapping = menu->getAlgorithmMap();
  unsigned int L1NamePos = 0;
  for (auto const& keyval : mapping) {
    std::string name = keyval.first;
    unsigned int index = keyval.second.getIndex();
    L1Names_.push_back(name);
    L1Indices_.push_back(index);
    L1_NamesToPos.insert(std::pair<std::string, unsigned int>(name, L1NamePos));
    //cout << "name " << keyval.first << " index " << keyval.second.getIndex() << endl;
    ++L1NamePos;
  }

}

void TriggerStudy::endJob()
{
  edm::LogInfo("TriggerStudy") << "Total Events " << NEvents_all << " pass HLT Preselection " << NEvents_passHLTPreSelection << " pass Offline Preselection " << NEvents_passOfflinePreSelection;
}

void TriggerStudy::analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)
{ 
  ++NEvents_all;
  //if(iEvent.isRealData()) isBBMC_ = false;

  //
  // Get the L1
  //
  edm::Handle<GlobalAlgBlkBxCollection> L1handleResults;
  iEvent.getByToken(GlobalAlgToken_, L1handleResults);
  const std::vector<bool>* L1wordp = &L1handleResults->at(0, 0).getAlgoDecisionFinal();

  auto const& L1word = *L1wordp;
  //unsigned L1Indices_size = L1Indices_.size();
  //for (size_t nidx = 0; nidx < L1Indices_size; nidx++) {
  //unsigned int index = L1Indices_[nidx];
    //bool result = word[index];
    //cout << L1Names_[nidx] << " is PAssed " << result << endl;
  //}

      
  LogDebug ("TrigerStudy") << "  Run/Event/Lumi: " << iEvent.id().run() << " / " << iEvent.id().event() << " / " << iEvent.id().luminosityBlock();

  auto trigResultsHandle = getHandle(iEvent,trigResultsToken_) ;
  auto trigObjsHandle = getHandle(iEvent,trigObjsToken_); 
  edm::Handle<edm::View<pat::Jet> > jetsHandle = getHandle(iEvent,jetsToken_);


  //
  //  HLT Preselection
  //
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResultsHandle);
  //for(unsigned int iTrig = 0; iTrig < trigNames.size(); ++iTrig){
  //  cout << "\t " << trigNames.triggerName(iTrig)<<endl;
  //}

  for(auto& pathName : hltPreSelection_){
    size_t pathIndex = getPathIndex(pathName,trigNames);
    if(pathIndex>=trigNames.size()) cout <<" path "<<pathName<<" not found in menu"<<endl;
    else{
      bool accept = trigResultsHandle->accept(pathIndex);
      //cout << " result for "  << pathName << " is " << accept << endl;
      if(!accept){
	//cout << " skipping... "  << endl;
	return;
      }
      
    }
  }
  ++NEvents_passHLTPreSelection;
  

  float mBB = -1;
  float pTBB = -1;
  vector<const reco::GenParticle*> bQuarks;

  //
  //  Get Truth
  //
  if(isBBMC_){
    edm::Handle<edm::View<reco::GenJet> > truthJetsHandle = getHandle(iEvent,truthJetsToken_);
    edm::Handle<edm::View<reco::GenParticle> > truthPartsHandle = getHandle(iEvent,truthPartsToken_);

    vector<const reco::GenParticle*> bosons;
    for(const reco::GenParticle& tPart : *truthPartsHandle){
      int pdgId = tPart.pdgId();
    
      bool isBoson = (pdgId == 25 || pdgId == 23);
      bool isBQuark = abs(pdgId) == 5;

      if(!isBoson and !isBQuark) continue;

      if(!tPart.isLastCopy()) continue;

      if(isBoson)  bosons.push_back(&tPart);
      if(isBQuark) bQuarks.push_back(&tPart);

      //    cout << "Truth Part " << tPart.pt() << " " << tPart.eta()   << " " << tPart.phi()  << "  pdgID " << tPart.pdgId() << " nDaughters " << tPart.numberOfDaughters() 
      //	 << " nMothers " << tPart.numberOfMothers()
      //	 << " status " << tPart.status()
      //	 << " isLastCopy " << tPart.isLastCopy()
      //	 << endl;
    }

    if(bosons.size() != 2){
      cout << "ERROR not 2 bosons ..." << bosons.size() << " ... skipping " << endl;
      return;
    }

    if(bQuarks.size() < 4){
      cout << "ERROR too few b-quarks ..." << bQuarks.size() << " ... skipping " << endl;
      return;
    }

    //const LorentzVector&
    reco::ParticleState::LorentzVector pB1 = bosons.at(0)->p4();
    reco::ParticleState::LorentzVector pB2 = bosons.at(1)->p4();
    reco::ParticleState::LorentzVector pBB = pB1 + pB2;
    mBB  = pBB.M();
    pTBB = pBB.Pt();
  }
  //cout << " mBB " << mBB  <<endl;


  //
  //  Get offline info
  //  
  LogDebug ("TrigerStudy") << "Printing jets " << endl;

  unsigned int nSelectedJets = 0;
  unsigned int nTaggedJetsMed = 0;
  unsigned int nTaggedJets = 0;

  vector<float> jet_pts;
  vector<float> tagJet_pts;
  
  vector<JetInfo> sel_JetInfo;
  vector<JetInfo> tag_JetInfo;

  
  float hT = 0;
  float hT30 = 0;
  for(const pat::Jet& jet : *jetsHandle){
    double eta = jet.eta();
    double pt = jet.pt();    
    double phi = jet.phi();    
    double deepFlavour = (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb"));
    //cout << jet.neutralHadronEnergyFraction() << endl;
    //cout << jet.userFloat("pileupJetId:fullDiscriminant")<< endl;;
    //cout << "Reco Jet  " << pt << " " << eta << " " << jet.phi() << " " << deepFlavour << endl;
    if(fabs(eta) > 2.5) continue;
    
    if(pt<30) continue;
    hT30+=pt;
    jet_pts.push_back(pt);
    addJetInfo(sel_JetInfo, pt, eta, phi, deepFlavour);

    if(deepFlavour >= 0.6) {
      tagJet_pts.push_back(pt);
      addJetInfo(tag_JetInfo, pt, eta, phi, deepFlavour);
    }
    
    if(pt < 40) continue;
    ++nSelectedJets;
    hT+=pt;

    if(deepFlavour < 0.2770) continue;
    ++nTaggedJetsMed;

    if(deepFlavour < 0.6) continue;
    ++nTaggedJets;
  }

  //
  //  Offline Cuts
  //
  if(nSelectedJets < minNSelJet_) {
    LogDebug ("TrigerStudy") << "Failed minNSelJet " << endl;
    return;
  }

  if(nTaggedJetsMed < minNTagMedJet_) {
    LogDebug ("TrigerStudy") << "Failed minNTagMedJet " << endl;
    return;
  }

  if(nTaggedJets < minNTagTightJet_) {
    LogDebug ("TrigerStudy") << "Failed minNTagTightJet " << endl;
    return;
  }
  ++NEvents_passOfflinePreSelection;


  hAll.at(0).Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);
    

  //now we will look at the filters passed
  //before we do this we need to make a new collection of trig objects
  //with their filters unpacked
  //we have to make a new copy as the unpacking modifies them and CMSSW
  //forbids (for very good reasons) modification of products in the event
  vector<pat::TriggerObjectStandAlone> trigObjsUnpacked;
  for(auto& trigObj : *trigObjsHandle){
    trigObjsUnpacked.push_back(trigObj);
    trigObjsUnpacked.back().unpackFilterLabels(iEvent,*trigResultsHandle);
  }


  if(doEmulation_){

    //
    //  Trigger Emulation
    //

    trigEmulatorDetails->SetWeights  (jet_pts, tagJet_pts, hT30);


    unsigned int filterNum = 1; // 0 is All
    for(edm::ParameterSet filterInfo : filtersToPass_){
      string name = filterInfo.getParameter<string>("histName");

      if(name == "HLT_OR"){
	float triggerWeight = trigEmulator->GetWeightOR(jet_pts, tagJet_pts, hT30);
	hAll.at(filterNum).Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo, triggerWeight);	
      }else{
	float triggerWeight = trigEmulatorDetails->GetWeight("EMU_"+name);      
	hAll.at(filterNum).Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo, triggerWeight);
      }

      ++filterNum;
    }


    //hAll.at(0).Fill(mBB, pTBB, nSelectedJets, hT, hT30, 1);

    //cout << trigEmulatorDetails->GetWeight("EMU_4PF30") << endl;


  } else{
    
    
    //
    //  Checking the filters
    //
    vector<string> filterNames;
    vector<bool> filterPassed;
    for(edm::ParameterSet filterInfo : filtersToPass_){

      bool passFilter = true;
      string name;
    
      //
      //  L1 Selection
      //
      if(filterInfo.exists("L1Names")){
	//cout << "-----" << endl;
	bool passL1OR = false;
	vector<string> L1Names = filterInfo.getParameter<vector<string> >("L1Names");      
	name = filterInfo.getParameter<string>("histName");
	for(const string& L1N : L1Names){
    
	  unsigned int L1Index = L1Indices_.at(L1_NamesToPos[L1N]);
	  //cout << "Checking name " << L1N << " at position " << L1_NamesToPos[L1N] << " at index  " << L1Index << " passed ... " << bool(L1word[L1Index]) << endl;
	  if(L1word[L1Index]){
	    passL1OR = true;
	  }
	}
          
	if(!passL1OR) passFilter = false;
      }
    
        
      //
      //  HLT Selection
      //
      if(filterInfo.exists("filterName")){
	name = filterInfo.getParameter<string>("filterName");
    
	unsigned int mult = filterInfo.getParameter<unsigned int>("mult");
	double pt = filterInfo.getParameter<double>("pt");
	vector<const pat::TriggerObjectStandAlone*> releventTrigObs = getAllTrigObjs(trigObjsUnpacked, name);
    
    
	if(mult > 0 && releventTrigObs.size() < mult){
	  //if(releventTrigObs.size() > 0) cout << name << " Fails with size " << releventTrigObs.size() << endl;
	  passFilter = false;
	}
    
	if(pt   > 0){
	  bool passPt = false;
	  for(auto& trigObj : releventTrigObs){
	    if(trigObj->pt() > pt) passPt = true;
	  }
          
	  if(!passPt) passFilter = false;
	}
      } // HLT Selection
    
    
    
        //filtersPassed.push_back(foundFilter(filter,trigObjsUnpacked));
      filterNames .push_back(name);
      filterPassed.push_back(passFilter);
    }
    
    //
    //  Print Filters fill hists
    //
    bool printFilters = false;
    
    if(printFilters) cout << " filters Passed: ";
    
    unsigned int filterNum = 1; // 0 is All
    for(bool thisFilter : filterPassed){
      if(printFilters) cout << thisFilter << " ";
      if(!thisFilter) break;
    
      hAll.at(filterNum).Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);
      ++filterNum;
    }


    //
    // Now jet turn ons
    //


    //
    //  Loop on Jets
    //
    for(auto& jet : *jetsHandle){
      double eta = jet.eta();
      double pt  = jet.pt();    
      double phi = jet.phi();    
      double deepFlavour = (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb"));

      //printAllFilters(eta, phi, trigObjsUnpacked, 0.1);

      if(fabs(eta) > 2.5) continue;

      // 
      // Loop on filter reqs
      //
      unsigned int turnOnNum = -1; 
      for(edm::ParameterSet jetTurnOnInfo : jetTurnOns_){
	++turnOnNum;

	//bool printOut = (jetTurnOnInfo.getParameter<string>("numFilterMatch") == "hltL1DoubleJet112er2p3dEtaMax1p6");
	//printOut = printOut && (jetTurnOnInfo.getParameter<string>("histName") == "L1112TandP");

	//if(printOut){
	//  
	//
	//  vector<string>::iterator itr = std::find(filterNames.begin(), filterNames.end(), "hltL1DoubleJet112er2p3dEtaMax1p6");
	//  if(itr == filterNames.end()){
	//    cout << "ERROR not found " << endl;
	//    continue;
	//  }
	//
	//  unsigned int denIndex = std::distance(filterNames.begin(), itr);
	//  for(unsigned int iFilt = 0; iFilt < (denIndex+1); ++iFilt){
	//    if(filterPassed.at(iFilt)){
	//      cout << "Passed Event" << endl;
	//    }else{
	//      printOut = false;
	//    }
	//  }
	//
	//  vector<const pat::TriggerObjectStandAlone*> onlineMatch = getMatchedObjs(eta, phi, trigObjsUnpacked, 0.1, "hltL1DoubleJet112er2p3dEtaMax1p6");
	//  for(auto& trigObj : onlineMatch){
	//    cout << "\t " << trigObj->pt()  << endl;
	//    printAllFilters(eta, phi, trigObjsUnpacked, 0.1);
	//  }
	//}


	//
	//  Require event filter passed (if requested)
	//
	bool passDenominator = true;
	if(jetTurnOnInfo.exists("denEventFilter")){
	  string denName  = jetTurnOnInfo.getParameter<string>("denEventFilter");

	  vector<string>::iterator itr = std::find(filterNames.begin(), filterNames.end(), denName);
	  if(itr == filterNames.end()){
	    cout << "ERROR denEventFilter " << denName << " not found in filterNames  " << endl;
	    continue;
	  }

	  unsigned int denIndex = std::distance(filterNames.begin(), itr);
	  for(unsigned int iFilt = 0; iFilt < (denIndex+1); ++iFilt){
	    if(!filterPassed.at(iFilt)){
	      passDenominator = false;
	    }
	  }

	  if(passDenominator && jetTurnOnInfo.exists("denJetMatch") ){
	    vector<const pat::TriggerObjectStandAlone*> onlineMatch = getMatchedObjs(eta, phi, trigObjsUnpacked, 0.1, jetTurnOnInfo.getParameter<string>("denJetMatch"));
	    if(!onlineMatch.size()) passDenominator = false;
	  }
		
	}//denFilter
      
	//
	//  Require tag (Matches on the "away side" dR > 0.4)
	// 
	if(jetTurnOnInfo.exists("tagFilterMatch")){
	  string tagName  = jetTurnOnInfo.getParameter<string>("tagFilterMatch");	
	  unsigned int    tagMin   = jetTurnOnInfo.getParameter<unsigned int>("tagFilterMin");	

	  // Loop on jets{
	  unsigned int nTags = 0;
	  
	  for(auto& jetTag : *jetsHandle){
	    double etaTag = jetTag.eta();
	    double phiTag = jetTag.phi();    

	    //cout << " \t probe cand is pt / eta / phi " << jetProbe.pt() << " / " << etaProbe << " / " << phiProbe << endl;
	  	  
	    const float dR2 = reco::deltaR2(eta,phi,etaTag,phiTag);
	    static const float dR2min = 0.4*0.4;

	    if(dR2 < dR2min) 
	      continue;

	    if(checkFilter(etaTag,phiTag,trigObjsUnpacked,tagName))
	      nTags++;

	  }
	
	  if(nTags < tagMin){
	    //cout << "Fail probe"<< endl;
	    passDenominator = false;
	  }else{
	    //cout << "Pass tag " << nTags << endl;
	  }


	}// tagFilterMatch


	//
	//  Require tag (Matches on the "near side" dR < 0.4)
	// 
	if(jetTurnOnInfo.exists("probeCut")){

	  bool passProbeCut = false;

	  // Only support near side btagging and truth bcuts 
	  string probeName  = jetTurnOnInfo.getParameter<string>("probeCut");	
	  
	  bool reqBTag  = (probeName == "Btag"  || probeName == "trueBtag");
	  bool reqTrueB = (probeName == "trueB" || probeName == "trueBtag");
	  
	  bool passBTag  = !reqBTag;
	  bool passTrueB = !reqTrueB;

	  if(reqBTag){

	    //cout << " this jet is pt / eta / phi " << pt << " / " << eta << " / " << phi << endl;
    
	    // Loop on jets{
	    for(auto& jetTag : *jetsHandle){
    
	      double etaTag = jetTag.eta();
	      double phiTag = jetTag.phi();    
    
	      //cout << " \t tag cand is pt / eta / phi " << jetTag.pt() << " / " << etaTag << " / " << phiTag << endl;
    	  	  
	      const float dR2 = reco::deltaR2(eta,phi,etaTag,phiTag);
	      static const float dR2min = 0.4*0.4;
    
	      if(dR2 > dR2min) 
		continue;
    
	      //cout << " \t pass Tag " << endl;
	      double tagDeepFlavour = (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb"));
	      if(tagDeepFlavour < 0.6) continue;
    
	      passBTag = true;
	      break;
	    }
	  }

	  if(reqTrueB){
	    //cout << "Matching to trueB. " << endl;
	    //cout << " nBQs " << bQ->size() << endl;
	    for(const reco::GenParticle* bQ :  bQuarks){
	      double etaTrueB = bQ->p4().eta();
	      double phiTrueB = bQ->p4().phi();    
	      
	      const float dR2 = reco::deltaR2(eta,phi,etaTrueB,phiTrueB);
	      static const float dR2min = 0.4*0.4;
	      
	      if(dR2 > dR2min) 
		continue;

	      passTrueB = true;
	      break;
	    }

	  }
	  
	  passProbeCut = (passBTag & passTrueB);

	  if(!passProbeCut){
	    //cout << "Fail tag"<< endl;
	    passDenominator = false;
	  }


	}// probeCut


	if(!passDenominator){
	  continue;
	}

	// 
	// Fill the denominator
	// 
	hJets_den.at(turnOnNum).Fill(pt,eta, phi, deepFlavour);

	// 
	// Now the numerator cuts
	// 
	bool passNumerator = false;
	if(jetTurnOnInfo.exists("numFilterMatch")){
	  string numName  = jetTurnOnInfo.getParameter<string>("numFilterMatch");

	  if(checkFilter(eta,phi,trigObjsUnpacked,numName)){
	    passNumerator = true;
	  } 
	}

	//if(printOut && !passNumerator && pt > 300){
	//
	//  
	//  cout << "Failed Numerator pt: " << pt << " " << eta << " " << phi << endl;
	//  vector<string>::iterator itr = std::find(filterNames.begin(), filterNames.end(), "hltL1DoubleJet112er2p3dEtaMax1p6");
	//  if(itr == filterNames.end()){
	//    cout << "ERROR not found " << endl;
	//    continue;
	//  }
	//
	//  unsigned int denIndex = std::distance(filterNames.begin(), itr);
	//  for(unsigned int iFilt = 0; iFilt < (denIndex+1); ++iFilt){
	//    if(filterPassed.at(iFilt)){
	//      cout << "Passed Event" << endl;
	//    }
	//  }
	//
	//  printAllFilters(eta, phi, trigObjsUnpacked, 0.1);
	//  //vector<const pat::TriggerObjectStandAlone*> onlineMatch = getMatchedObjs(eta, phi, trigObjsUnpacked, 0.1, "hltL1DoubleJet112er2p3dEtaMax1p6");
	//  //for(auto& trigObj : onlineMatch){
	//  //  cout << "\t " << trigObj->pt()  << endl;
	//  //  printAllFilters(eta, phi, trigObjsUnpacked, 0.1);
	//  //}
	//  
	//}
	

	if(jetTurnOnInfo.exists("numPtCut")){	
	  string filterMatch  = jetTurnOnInfo.getParameter<string>("numPtName");
	  double filterPt     = jetTurnOnInfo.getParameter<double>("numPtCut");
	  vector<const pat::TriggerObjectStandAlone*> onlineMatch = getMatchedObjs(eta, phi, trigObjsUnpacked, 0.1, filterMatch);

	  //if(onlineMatch.size() > 1)
	  // cout << " size of filterMatches " << onlineMatch.size() << endl;

	  for(auto& trigObj : onlineMatch){
	    if(trigObj->pt() >= filterPt) passNumerator = true;
	  }

	}

	if(passNumerator){
	  hJets_num.at(turnOnNum).Fill(pt,eta, phi, deepFlavour);
	}

      }// Turn Ons

    }// jets


    //
    // Testing L1
    //
    if(testL1_){
      edm::Handle<BXVector<l1t::Jet> > L1JetsHandle = getHandle(iEvent,L1JetsToken_);
      //BXVector<l1t::Jet>
      cout << " ====== " << endl;
      cout << " PassL1 " << filterNames.at(0) << " " << filterPassed.at(0) << endl;
  
      for (int ibx = L1JetsHandle->getFirstBX(); ibx <= L1JetsHandle->getLastBX(); ++ibx) {
	for (auto itr = L1JetsHandle->begin(ibx); itr != L1JetsHandle->end(ibx); ++itr) {
  
	  cout << "Jet : "
	       << " BX=" << ibx << " ipt=" << itr->hwPt() << " ieta=" << itr->hwEta() << " iphi=" << itr->hwPhi() 
	       << " rawEt " << itr->rawEt() << " seedEt " << itr->seedEt() << " pt " << itr->pt() 
	       << std::endl;
	}
      }
    }


  }// not doing emulation


  //
  //  the Trigger study
  //
  unsigned int iTrig = 0;
  for(edm::ParameterSet triggerPath : triggersToPlot_){


    string name = triggerPath.getParameter<string>("name");

    //
    // Require
    //
    vector<edm::ParameterSet> requiredTriggers = triggerPath.getParameter<vector<edm::ParameterSet> >("requireOR");

    bool passRequired = false;
    for(edm::ParameterSet filterInfo : requiredTriggers){

      //
      // L1
      //
      vector<string> L1Paths = filterInfo.getParameter<vector<string> >("L1Paths");      
      bool passL1 = false;
      for(const string& L1N : L1Paths){
    
	unsigned int L1Index = L1Indices_.at(L1_NamesToPos[L1N]);
	//cout << "Checking name " << L1N << " at position " << L1_NamesToPos[L1N] << " at index  " << L1Index << " passed ... " << bool(L1word[L1Index]) << endl;
	if(L1word[L1Index]){
	  passL1 = true;
	}
      }
      if(!passL1) continue;

      //
      //  HLT
      //
      bool passHLT = false;
      string HLTPath = filterInfo.getParameter<string >("hltPath");      
      
      size_t pathIndex = getPathIndex(HLTPath,trigNames);
      if(pathIndex>=trigNames.size()) cout <<" path "<<HLTPath<<" not found in menu"<<endl;
      else{
	bool accept = trigResultsHandle->accept(pathIndex);
	if(accept) passHLT = true;
      }

      if(!passHLT) continue;      

      passRequired = true;
    }

    //
    // Veto
    //
    bool passVeto = true;
    if(triggerPath.exists("vetoOR")){	    

      bool passAnyVetoTrigger = false;
      vector<edm::ParameterSet> vetoedTriggers = triggerPath.getParameter<vector<edm::ParameterSet> >("vetoOR");
    
      for(edm::ParameterSet filterInfo : vetoedTriggers){
    
	//
	// L1
	//
	vector<string> L1Paths = filterInfo.getParameter<vector<string> >("L1Paths");      
	bool passL1 = false;
	for(const string& L1N : L1Paths){
        
	  unsigned int L1Index = L1Indices_.at(L1_NamesToPos[L1N]);
	  //cout << "Checking name " << L1N << " at position " << L1_NamesToPos[L1N] << " at index  " << L1Index << " passed ... " << bool(L1word[L1Index]) << endl;
	  if(L1word[L1Index]){
	    passL1 = true;
	  }
	}

	if(!passL1) continue;    
    
	//
	//  HLT
	//
	bool passHLT = false;
	string HLTPath = filterInfo.getParameter<string >("hltPath");      
          
	size_t pathIndex = getPathIndex(HLTPath,trigNames);
	if(pathIndex>=trigNames.size()) cout <<" path "<<HLTPath<<" not found in menu"<<endl;
	else{
	  bool accept = trigResultsHandle->accept(pathIndex);
	  if(accept) passHLT = true;
	}

	if(!passHLT) continue;    
    
	passAnyVetoTrigger = true;
      }

      if(passAnyVetoTrigger) passVeto = false;

    }// Veto

    
    //
    //  If fail requirementss
    // 
    if(passRequired && passVeto){
      hTrigStudy.at(iTrig).Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);
    }
    
    ++iTrig;
  }




  //
  //  Print  the final decision
  //
  if(false){
    for(auto& pathName : pathsToPass_){
      size_t pathIndex = getPathIndex(pathName,trigNames);
      if(pathIndex>=trigNames.size()) cout <<" path "<<pathName<<" not found in menu"<<endl;
      else{
	//cout <<" path index "<<pathIndex << " "<<trigNames.triggerName(pathIndex)<<  " was run " << trigResultsHandle->wasrun(pathIndex) << endl;
	//const edm::HLTPathStatus& pathStatus  = trigResultsHandle->at(pathIndex);
	//cout << "\t path status state: " << pathStatus.state() << " index " << pathStatus.index() << endl;
	cout << " .... " << trigResultsHandle->accept(pathIndex) << endl;
      }
    }
  }

  
  
}



DEFINE_FWK_MODULE(TriggerStudy);
#endif
