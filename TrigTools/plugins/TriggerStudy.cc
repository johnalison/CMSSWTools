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
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include <math.h>

#include "CMSSWTools/TrigTools/interface/TriggerStudy.h"


using std::cout; using std::endl;
using std::string; using std::vector;

using TriggerEmulator::hTTurnOn;   using TriggerEmulator::jetTurnOn; using TriggerEmulator::bTagTurnOn;

using namespace CMSSWTools;

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

  //void printAllFilters(const float eta,const float phi,const vector<pat::TriggerObjectStandAlone>& trigObjs,const float maxDeltaR=0.1)
  //{
  //  const auto matchedObjs = getMatchedObjs(eta,phi,trigObjs,maxDeltaR);
  //  for(const auto trigObj : matchedObjs){
  //
  //    //normally would auto this but to make it clearer for the example
  //    const vector<string>& objFilters = trigObj->filterLabels();
  //	
  //    for(const string& s : objFilters){
  //	cout << " \t\t matched Filter is " << s << endl;
  //    }
  //  }
  //  return;
  //}


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
  truthPartsToken_(consumes<edm::View<reco::GenParticle> >(iPara.getParameter<edm::InputTag>("truthParts"))),
  vtxToken_(consumes<reco::VertexCollection>(iPara.getParameter<edm::InputTag>("vtxColl"))),
  bsToken_(consumes<reco::BeamSpot>(edm::InputTag("offlineBeamSpot",""))),
  electronToken_(consumes<edm::View<pat::Electron> >(iPara.getParameter<edm::InputTag>("electronColl"))),
  conversionsToken_(mayConsume< reco::ConversionCollection >(iPara.getParameter<edm::InputTag>("conversions"))),
  electronIdMapToken_(consumes<edm::ValueMap<bool> >(iPara.getParameter<edm::InputTag>("electronIdMap"))),
  muonToken_(consumes<pat::MuonCollection>(iPara.getParameter<edm::InputTag>("muonColl"))),
  metToken_(consumes<pat::METCollection>(iPara.getParameter<edm::InputTag>("metColl")))
  

			       //algInputTag_(iPara.getParameter<edm::InputTag>("AlgInputTag")),
			       //extInputTag_(iPara.getParameter<edm::InputTag>("ExtInputTag"))
{

  //
  // Load the Event Selection
  //
  if(offlinePreSelection_.exists("minNSelMuon"))
     minNSelMuon_      = offlinePreSelection_.getParameter<unsigned int>("minNSelMuon");

  if(offlinePreSelection_.exists("minNSelElec"))
     minNSelElec_      = offlinePreSelection_.getParameter<unsigned int>("minNSelElec");


  if(offlinePreSelection_.exists("minNSelJet"))
     minNSelJet_      = offlinePreSelection_.getParameter<unsigned int>("minNSelJet");

  if(offlinePreSelection_.exists("minNTagJet"))
    minNTagJet_ = offlinePreSelection_.getParameter<unsigned int>("minNTagJet");
  
  edm::LogInfo("TriggerStudy") << " Offline Selection: minNSelJet: " << minNSelJet_ << "  minNTagJet: " << minNTagJet_ 
			       << " minNSelMuon: " << minNSelMuon_ 
			       << " minNSelElec: " << minNSelElec_;

  if(doEmulation_){
    year_ = iPara.getParameter<string>("year");
    setupTrigEmulator(year_);
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

    hJets_num_pt100.push_back(jetHists(jetDir,"_"+name+"_pt100"));
    hJets_den_pt100.push_back(jetHists(jetDir,"_"+name+"_pt100_den"));

    hJets_num_jetID.push_back(jetHists(jetDir,"_"+name+"_jetID"));
    hJets_den_jetID.push_back(jetHists(jetDir,"_"+name+"_jetID_den"));

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
  edm::LogInfo("TriggerStudy") << "Total Events " << NEvents_all << " pass HLT Preselection " << NEvents_passHLTPreSelection 
			       << " pass Lepton Preselection " << NEvents_passLeptonPreSelection
			       << " pass Offline Preselection " << NEvents_passOfflinePreSelection;
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
  //cout << "  Run/Event/Lumi: " << iEvent.id().run() << " / " << iEvent.id().event() << " / " << iEvent.id().luminosityBlock() << endl;

  auto trigResultsHandle = getHandle(iEvent,trigResultsToken_) ;
  auto trigObjsHandle = getHandle(iEvent,trigObjsToken_); 


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

  //
  // Clear Event Data
  //
  thisEvent.resetEvent();
  

  //
  //  Get Truth
  //
  if(isMC_){
    fillTruthInfo(iEvent);

    if(isBBMC_){
      if(thisEvent.bosons.size() != 2){
	cout << "ERROR not 2 bosons ..." << thisEvent.bosons.size() << " ... skipping " << endl;
	return;
      }
    
      if(thisEvent.bQuarks.size() < 4){
	cout << "ERROR too few b-quarks ..." << thisEvent.bQuarks.size() << " ... skipping " << endl;
	return;
      }

      //const LorentzVector&
      reco::ParticleState::LorentzVector pB1 = thisEvent.bosons.at(0)->p4();
      reco::ParticleState::LorentzVector pB2 = thisEvent.bosons.at(1)->p4();
      reco::ParticleState::LorentzVector pBB = pB1 + pB2;
      thisEvent.mBB  = pBB.M();
      thisEvent.pTBB = pBB.Pt();
    }
    
  }


  //
  //  Get offline info
  //  
  LogDebug ("TrigerStudy") << "Printing jets " << endl;
  
  //
  //  Get the PV
  //
  edm::Handle<reco::VertexCollection> primaryVertices = getHandle(iEvent, vtxToken_);
  //iEvent.getByToken(vtxToken_, primaryVertices);
  const reco::Vertex &pVtx = *(primaryVertices->begin());
  thisEvent.pVtx = &pVtx;

   //
   //  Get beam spot
   //
  edm::Handle<reco::BeamSpot> bsHandle = getHandle(iEvent, bsToken_);
  const reco::BeamSpot &beamspot = *bsHandle.product();
  thisEvent.beamspot = &beamspot;


  // 
  //  Get Selected Muons
  // 
  edm::Handle<pat::MuonCollection> muonsHandle = getHandle(iEvent, muonToken_);
  getSelectedMuons(muonsHandle, pVtx);
  //cout << " NSel Muons " << thisEvent.selMuons.size()<< endl;

  if(thisEvent.selMuons.size() < minNSelMuon_) {
    LogDebug ("TrigerStudy") << "Failed minNSelMuon " << endl;
    return;
  }


  //
  //  Get Selected Electrons
  //
  edm::Handle<edm::View<pat::Electron> > elecsHandle = getHandle(iEvent, electronToken_);  
  edm::Handle<reco::ConversionCollection> convHandle = getHandle(iEvent, conversionsToken_);
  edm::Handle<edm::ValueMap<bool> > eIDHandle = getHandle(iEvent, electronIdMapToken_);
  getSelectedElectrons(elecsHandle, convHandle, eIDHandle);
  //cout << " NSel Eelcs " << thisEvent.selElecs.size()<< endl;

  if(thisEvent.selElecs.size() < minNSelElec_) {
    LogDebug ("TrigerStudy") << "Failed minNSelElec " << endl;
    return;
  }
  ++NEvents_passLeptonPreSelection;

  //
  //  Get Met
  //
  edm::Handle<pat::METCollection> metHandle = getHandle(iEvent, metToken_);
  const pat::MET &met = metHandle->front();
  thisEvent.met = &met;
  //cout << " Met is " << met.pt() << endl;



  // 
  //  Get Selected Jets
  // 
  edm::Handle<edm::View<pat::Jet> > jetsHandle = getHandle(iEvent,jetsToken_);
  getSelectedJets(jetsHandle);


  //
  //  Offline Cuts
  //
  if(thisEvent.selJets.size() < minNSelJet_) {
    LogDebug ("TrigerStudy") << "Failed minNSelJet " << endl;
    return;
  }

  if(thisEvent.tagJets.size() < minNTagJet_) {
    LogDebug ("TrigerStudy") << "Failed minNTagJet " << endl;
    return;
  }
  ++NEvents_passOfflinePreSelection;


  // Fill all events
  hAll.at(0).Fill(thisEvent);
    

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
    doTrigEmulation();
    
  } else{
    
    
    //
    //  Checking the filters
    //
    vector<string> filterNames;
    vector<bool>   filterPassed;
    setEventLevelHLTFilterDecisions(L1word, trigObjsUnpacked, filterNames, filterPassed);

    
    //
    //  Print Filters fill hists
    //
    bool printFilters = false;
    if(printFilters) cout << " filters Passed: ";

    //
    //  Event Level Plots for all filters
    //
    unsigned int filterNum = 1; // 0 is All
    for(bool thisFilter : filterPassed){
      if(printFilters) cout << thisFilter << " ";
      if(!thisFilter) break;
    
      hAll.at(filterNum).Fill(thisEvent);
      ++filterNum;
    }


    //
    // Now jet turn ons
    //
    fillJetTurnOnPlots(jetsHandle, trigObjsUnpacked, filterNames, filterPassed);


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
      hTrigStudy.at(iTrig).Fill(thisEvent);
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

  
  
}//analyze


void TriggerStudy::setupTrigEmulator(std::string year){
  cout << "Making Emulator for year" << year << endl;
    
  if(year == "2018"){
    trigEmulatorDetails = new TriggerEmulator::TrigEmulatorTool("trigEmulatorDetails", 1, 100, year);

    trigEmulatorDetails->AddTrig("EMU_L1ORAll",    {hTTurnOn::L1ORAll_Ht330_4j_3b});
    trigEmulatorDetails->AddTrig("EMU_CaloHt320",  {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320});

    trigEmulatorDetails->AddTrig("EMU_4PF30",      {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320}, {jetTurnOn::PF30DenMatch},{4});
    trigEmulatorDetails->AddTrig("EMU_1PF75",      {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch},{4,1});
    trigEmulatorDetails->AddTrig("EMU_2PF60",      {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch},{4,1,2});
    trigEmulatorDetails->AddTrig("EMU_3PF45",      {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch},{4,1,2,3});
    trigEmulatorDetails->AddTrig("EMU_4PF40",      {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4});
    
    trigEmulatorDetails->AddTrig("EMU_PFHt330",       {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320,hTTurnOn::PFHt330},     {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4});
    trigEmulatorDetails->AddTrig("EMU_HT330_4j_3b",   {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320,hTTurnOn::PFHt330},     {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4},{bTagTurnOn::PFDeepCSVMatchBtagDenMatch},{3});

    //trigEmulatorDetails->AddTrig("EMU_2b116_L1ORAll",   {}, {"L1112TandPDenMatch"}, {2});
    //trigEmulatorDetails->AddTrig("EMU_2b116_2Calo100",  {}, {"L1112TandPDenMatch","Calo100DenMatch"}, {2, 2});
    //trigEmulatorDetails->AddTrig("EMU_2b116_2CaloBTags",{}, {"L1112TandPDenMatch"}, {2},                    {"CaloDeepCSV0p7MatchBtag"},{2});
    //trigEmulatorDetails->AddTrig("EMU_2b116_2PF116",    {}, {"L1112TandPDenMatch","PF116DenMatch"}, {2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});
    //trigEmulatorDetails->AddTrig("EMU_2b116",           {}, {"L1112TandPDenMatch","PF116DenMatch","PF116DrDenMatch"}, {2, 2, 2}, {"CaloDeepCSV0p7MatchBtag"},{2});

    trigEmulatorDetails->AddTrig("EMU_2b116_L1ORAll",   {hTTurnOn::L1ORAll_2b116}  );
    trigEmulatorDetails->AddTrig("EMU_2b116_2Calo100",  {hTTurnOn::L1ORAll_2b116}, {jetTurnOn::Calo100DenMatch}, {2});
    trigEmulatorDetails->AddTrig("EMU_2b116_2CaloBTags",{hTTurnOn::L1ORAll_2b116}, {}, {},                    {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    trigEmulatorDetails->AddTrig("EMU_2b116_2PF116",    {hTTurnOn::L1ORAll_2b116}, {jetTurnOn::PF116DenMatch}, {2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    trigEmulatorDetails->AddTrig("EMU_2b116",           {hTTurnOn::L1ORAll_2b116}, {jetTurnOn::PF116DenMatch,jetTurnOn::PF116DrDenMatch}, {2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});



    trigEmulator = new TriggerEmulator::TrigEmulatorTool("trigEmulator", 1, 100, year);
    trigEmulator->AddTrig("EMU_HT330_4j_3b",   {hTTurnOn::L1ORAll_Ht330_4j_3b,hTTurnOn::CaloHt320,hTTurnOn::PFHt330},     {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4},{bTagTurnOn::PFDeepCSVMatchBtagDenMatch},{3});
    //trigEmulator->AddTrig("EMU_2b116",    {},  {"L1112TandPDenMatch",jetTurnOn::PF116DenMatch,jetTurnOn::PF116DrDenMatch}, {2, 2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    trigEmulator->AddTrig("EMU_2b116",    {hTTurnOn::L1ORAll_2b116},  {jetTurnOn::PF116DenMatch,jetTurnOn::PF116DrDenMatch}, {2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
  }

  if(year == "2017"){

    trigEmulatorDetails = new TriggerEmulator::TrigEmulatorTool("trigEmulatorDetails", 1, 100, year);

    trigEmulatorDetails->AddTrig("EMU_L1ORAll",    {hTTurnOn::L1ORAll_Ht300_4j_3b});
    trigEmulatorDetails->AddTrig("EMU_CaloHt300",  {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300});

    trigEmulatorDetails->AddTrig("EMU_4PF30",      {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300}, {jetTurnOn::PF30DenMatch},{4});
    trigEmulatorDetails->AddTrig("EMU_1PF75",      {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch},{4,1});
    trigEmulatorDetails->AddTrig("EMU_2PF60",      {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch},{4,1,2});
    trigEmulatorDetails->AddTrig("EMU_3PF45",      {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch},{4,1,2,3});
    trigEmulatorDetails->AddTrig("EMU_4PF40",      {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300}, {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4});
    
    trigEmulatorDetails->AddTrig("EMU_PFHt300",       {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300,hTTurnOn::PFHt300},     {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4});
    trigEmulatorDetails->AddTrig("EMU_HT300_4j_3b",   {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300,hTTurnOn::PFHt300},     {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4},{bTagTurnOn::PFDeepCSVMatchBtagDenMatch},{3});
      
    //trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {}, {"L1100TandP"}, {2});
    //trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {}, {"L1100TandP",jetTurnOn::Calo100DenMatch}, {2, 2});
    //trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{}, {"L1100TandP"}, {2},                    {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    //trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {}, {"L1100TandP","PF100DenMatch"}, {2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    //trigEmulatorDetails->AddTrig("EMU_2b100",           {}, {"L1100TandP","PF100DenMatch","PF100DrDenMatch"}, {2, 2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});

    trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {hTTurnOn::L1ORAll_2b100});
    trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {hTTurnOn::L1ORAll_2b100}, {jetTurnOn::Calo100DenMatch}, {2});
    trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{hTTurnOn::L1ORAll_2b100}, {}, {},                    {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {hTTurnOn::L1ORAll_2b100}, {jetTurnOn::PF100DenMatch}, { 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    trigEmulatorDetails->AddTrig("EMU_2b100",           {hTTurnOn::L1ORAll_2b100}, {jetTurnOn::PF100DenMatch,jetTurnOn::PF100DrDenMatch}, {2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});



    trigEmulator = new TriggerEmulator::TrigEmulatorTool("trigEmulator", 1, 100, year);
    trigEmulator->AddTrig("EMU_HT300_4j_3b",   {hTTurnOn::L1ORAll_Ht300_4j_3b,hTTurnOn::CaloHt300,hTTurnOn::PFHt300},     {jetTurnOn::PF30DenMatch,jetTurnOn::PF75DenMatch,jetTurnOn::PF60DenMatch,jetTurnOn::PF45DenMatch,jetTurnOn::PF40DenMatch},{4,1,2,3,4},{bTagTurnOn::PFDeepCSVMatchBtagDenMatch},{3});
    //trigEmulator->AddTrig("EMU_2b100",    {},  {"L1100TandP",jetTurnOn::PF100DenMatch,jetTurnOn::PF100DrDenMatch}, {2, 2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});
    trigEmulator->AddTrig("EMU_2b100",    {hTTurnOn::L1ORAll_2b100},  {jetTurnOn::PF100DenMatch,jetTurnOn::PF100DrDenMatch}, {2, 2}, {bTagTurnOn::CaloDeepCSV0p7MatchBtag},{2});


  }


  if(year == "2016"){

    trigEmulatorDetails = new TriggerEmulator::TrigEmulatorTool("trigEmulatorDetails", 1, 100, year);

    trigEmulatorDetails->AddTrig("EMU_L1ORAll",    {hTTurnOn::L1ORAll_4j_3b});
    trigEmulatorDetails->AddTrig("EMU_4Calo45",    {hTTurnOn::L1ORAll_4j_3b}, {jetTurnOn::Calo45},{4});
    trigEmulatorDetails->AddTrig("EMU_3CaloBtags", {hTTurnOn::L1ORAll_4j_3b}, {jetTurnOn::Calo45},{4},{bTagTurnOn::CaloCSVMatchBtagDenMatch},{3});
    trigEmulatorDetails->AddTrig("EMU_4j_3b",      {hTTurnOn::L1ORAll_4j_3b}, {jetTurnOn::Calo45,jetTurnOn::PF45DenMatch},{4,4},{bTagTurnOn::CaloCSVMatchBtagDenMatch},{3});
    
    //trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {}, {"L1100TandPDenMatch"}, {2});
    //trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {}, {"L1100TandPDenMatch",jetTurnOn::Calo100DenMatch}, {2, 2});
    //trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{}, {"L1100TandPDenMatch"}, {2},                    {"CaloCSV0p84MatchBtag"},{2});
    //trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {}, {"L1100TandPDenMatch",jetTurnOn::PF100DenMatch}, {2, 2}, {"CaloCSV0p84MatchBtag"},{2});
    //trigEmulatorDetails->AddTrig("EMU_2b100",           {}, {"L1100TandPDenMatch",jetTurnOn::PF100DenMatch,jetTurnOn::PF100DrDenMatch}, {2, 2, 2}, {"CaloCSV0p84MatchBtag"},{2});

    trigEmulatorDetails->AddTrig("EMU_2b100_L1ORAll",   {hTTurnOn::L1ORAll_2b100} );
    trigEmulatorDetails->AddTrig("EMU_2b100_2Calo100",  {hTTurnOn::L1ORAll_2b100}, {jetTurnOn::Calo100DenMatch}, {2});
    trigEmulatorDetails->AddTrig("EMU_2b100_2CaloBTags",{hTTurnOn::L1ORAll_2b100}, {}, {},                    {bTagTurnOn::CaloCSV0p84MatchBtag},{2});
    trigEmulatorDetails->AddTrig("EMU_2b100_2PF100",    {hTTurnOn::L1ORAll_2b100}, {jetTurnOn::PF100DenMatch}, {2},    {bTagTurnOn::CaloCSV0p84MatchBtag},{2});
    trigEmulatorDetails->AddTrig("EMU_2b100",           {hTTurnOn::L1ORAll_2b100}, {jetTurnOn::PF100DenMatch,jetTurnOn::PF100DrDenMatch}, {2, 2}, {bTagTurnOn::CaloCSV0p84MatchBtag},{2});


    trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_L1ORAll",       {hTTurnOn::L1ORAll_2j_2j_3b});
    trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_4Calo30",       {hTTurnOn::L1ORAll_2j_2j_3b}, {jetTurnOn::Calo30},{4});
    trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_2Calo90",       {hTTurnOn::L1ORAll_2j_2j_3b}, {jetTurnOn::Calo30,jetTurnOn::Calo90DenMatch},{4,2});
    trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_3CaloBTags",    {hTTurnOn::L1ORAll_2j_2j_3b}, {jetTurnOn::Calo30,jetTurnOn::Calo90DenMatch},{4,2},{bTagTurnOn::CaloCSVMatchBtagDenMatch},{3});
    trigEmulatorDetails->AddTrig("EMU_2j_2j_3b_4PF30",         {hTTurnOn::L1ORAll_2j_2j_3b}, {jetTurnOn::Calo30,jetTurnOn::Calo90DenMatch,jetTurnOn::PF30DenMatch},{4,2,4},{bTagTurnOn::CaloCSVMatchBtagDenMatch},{3});
    trigEmulatorDetails->AddTrig("EMU_2j_2j_3b",               {hTTurnOn::L1ORAll_2j_2j_3b}, {jetTurnOn::Calo30,jetTurnOn::Calo90DenMatch,jetTurnOn::PF30DenMatch,jetTurnOn::PF90DenMatch},{4,2,4,2},{bTagTurnOn::CaloCSVMatchBtagDenMatch},{3});


    trigEmulator = new TriggerEmulator::TrigEmulatorTool("trigEmulator", 1, 100, year);
    trigEmulator->AddTrig("EMU_4j_3b",      {hTTurnOn::L1ORAll_4j_3b}, {jetTurnOn::Calo45,jetTurnOn::PF45DenMatch},{4,4},{bTagTurnOn::CaloCSVMatchBtagDenMatch},{3});
    //trigEmulator->AddTrig("EMU_2b100",    {},  {"L1100TandPDenMatch",jetTurnOn::PF100DenMatch,jetTurnOn::PF100DrDenMatch}, {2, 2, 2}, {bTagTurnOn::CaloCSV0p84MatchBtag},{2});
    trigEmulator->AddTrig("EMU_2b100",    {hTTurnOn::L1ORAll_2b100},  {jetTurnOn::PF100DenMatch,jetTurnOn::PF100DrDenMatch}, {2, 2}, {bTagTurnOn::CaloCSV0p84MatchBtag},{2});
    trigEmulator->AddTrig("EMU_2j_2j_3b", {hTTurnOn::L1ORAll_2j_2j_3b}, {jetTurnOn::Calo30,jetTurnOn::Calo90DenMatch,jetTurnOn::PF30DenMatch,jetTurnOn::PF90DenMatch},{4,2,4,2},{bTagTurnOn::CaloCSVMatchBtagDenMatch},{3});

  }

}//setupTrigEmulator

void TriggerStudy::fillTruthInfo(const edm::Event& iEvent){

  edm::Handle<edm::View<reco::GenJet> >      truthJetsHandle  = getHandle(iEvent,truthJetsToken_);
  edm::Handle<edm::View<reco::GenParticle> > truthPartsHandle = getHandle(iEvent,truthPartsToken_);

  for(const reco::GenParticle& tPart : *truthPartsHandle){
    int pdgId = tPart.pdgId();

    bool isBoson = (pdgId == 25 || pdgId == 23);
    bool isBQuark = abs(pdgId) == 5;

    if(!isBoson and !isBQuark) continue;

    if(!tPart.isLastCopy()) continue;

    if(isBoson)  thisEvent.bosons.push_back(&tPart);
    if(isBQuark) thisEvent.bQuarks.push_back(&tPart);

    //    cout << "Truth Part " << tPart.pt() << " " << tPart.eta()   << " " << tPart.phi()  << "  pdgID " << tPart.pdgId() << " nDaughters " << tPart.numberOfDaughters() 
    //	 << " nMothers " << tPart.numberOfMothers()
    //	 << " status " << tPart.status()
    //	 << " isLastCopy " << tPart.isLastCopy()
    //	 << endl;
  }


}//fillTruthInfo

void TriggerStudy::doTrigEmulation(){

  trigEmulatorDetails->SetWeights  (thisEvent.jet_pts, thisEvent.tagJet_pts, thisEvent.hT30);


  unsigned int filterNum = 1; // 0 is All
  for(edm::ParameterSet filterInfo : filtersToPass_){
    string name = filterInfo.getParameter<string>("histName");

    if(name == "HLT_OR"){
      float triggerWeight = trigEmulator->GetWeightOR(thisEvent.jet_pts, thisEvent.tagJet_pts, thisEvent.hT30);
      hAll.at(filterNum).Fill(thisEvent, triggerWeight);	
    }else{
      float triggerWeight = trigEmulatorDetails->GetWeight("EMU_"+name);      
      hAll.at(filterNum).Fill(thisEvent, triggerWeight);
    }

    ++filterNum;
  }

}//doTrigEmulation




void TriggerStudy::setEventLevelHLTFilterDecisions(const std::vector<bool>& L1word, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked, 
						   vector<string>& filterNames, vector<bool>& filterPassed){
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
}//setEventLevelHLTFilterDecisions




void TriggerStudy::fillJetTurnOnPlots(edm::Handle<edm::View<pat::Jet> > jetsHandle, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked,
				      const vector<string>& filterNames, const vector<bool>& filterPassed)
{
  //
  //  Loop on Jets
  //
  for(const pat::Jet& jet : *jetsHandle){
      
    double eta = jet.eta();
    double phi = jet.phi();    

    //printAllFilters(eta, phi, trigObjsUnpacked, 0.1);

    if(fabs(eta) > 2.4) continue;

    // 
    // Loop on HLT filters 
    //
    unsigned int turnOnNum = -1; 
    for(edm::ParameterSet jetTurnOnInfo : jetTurnOns_){
      ++turnOnNum;

      bool passDenominator = true;

      //
      //  Require event filter passed (if requested)
      //
      if(jetTurnOnInfo.exists("denEventFilter")){
	passDenominator = checkDenEventFilter(jetTurnOnInfo, filterNames, filterPassed);
      }//denFilter


      // 
      //  Required the den object to be matched to a filter (if requested)
      //
      if(jetTurnOnInfo.exists("denJetMatch") ){
	vector<const pat::TriggerObjectStandAlone*> onlineMatch = getMatchedObjs(eta, phi, trigObjsUnpacked, 0.1, jetTurnOnInfo.getParameter<string>("denJetMatch"));
	if(!onlineMatch.size()) passDenominator = false;
      }
      
      //
      //  Require tag to match a HLT filter (Matches on the "away side" dR > 0.4)
      // 
      if(jetTurnOnInfo.exists("tagFilterMatch")){
	passDenominator = tagJetFilterMatch(jetTurnOnInfo, jetsHandle, trigObjsUnpacked, eta, phi);
      }// tagFilterMatch


      //
      //  Require tag to pass cuts (Matches on the "near side" dR < 0.4)
      // 
      if(jetTurnOnInfo.exists("tagCut")){
	passDenominator = tagJetCut(jetTurnOnInfo, jetsHandle, eta, phi);
      }// tagCut


      //
      //  Require tag (Matches on the "near side" dR < 0.4)
      // 
      if(jetTurnOnInfo.exists("probeCut")){
	passDenominator = probeJetCut(jetTurnOnInfo, jetsHandle, jet);
      }// probeCut

      //
      //  Only fill histograms if demonator is passed
      //
      if(!passDenominator){
	continue;
      }

      // 
      // Fill the denominator
      // 
      hJets_den.at(turnOnNum).Fill(&jet);
      if(jet.pt() > 100) hJets_den_pt100.at(turnOnNum).Fill(&jet);
      if(passJetID(&jet)) hJets_den_jetID.at(turnOnNum).Fill(&jet);
	  

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
	
      //
      // Require a pt cut on the Numerator
      //
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


      //
      //  Fill Numerator hists
      //
      if(passNumerator){
	hJets_num.at(turnOnNum).Fill(&jet);
	if(jet.pt() > 100) hJets_num_pt100.at(turnOnNum).Fill(&jet);
	if(passJetID(&jet)) hJets_num_jetID.at(turnOnNum).Fill(&jet);

      }

    }// Turn Ons

  }// jets
}//fillJetTurnOnPlots


bool TriggerStudy::checkDenEventFilter(const edm::ParameterSet& jetTurnOnInfo, const vector<string>& filterNames, const vector<bool>& filterPassed){

  string denName  = jetTurnOnInfo.getParameter<string>("denEventFilter");

  vector<string>::const_iterator itr = std::find(filterNames.begin(), filterNames.end(), denName);
  if(itr == filterNames.end()){
    cout << "ERROR denEventFilter " << denName << " not found in filterNames  " << endl;
    return false;
  }

  unsigned int denIndex = std::distance(filterNames.begin(), itr);
  for(unsigned int iFilt = 0; iFilt < (denIndex+1); ++iFilt){
    if(!filterPassed.at(iFilt)){
      return false;
    }
  }

  
  return true;
}//checkDenEventFilter



bool TriggerStudy::tagJetFilterMatch(const edm::ParameterSet& jetTurnOnInfo, edm::Handle<edm::View<pat::Jet> > jetsHandle, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked, float probeEta, float probePhi ){

  string tagName  = jetTurnOnInfo.getParameter<string>("tagFilterMatch");	
  unsigned int    tagMin   = jetTurnOnInfo.getParameter<unsigned int>("tagFilterMin");	

  // Loop on jets{
  unsigned int nTags = 0;
	  
  for(auto& jetTag : *jetsHandle){
    double etaTag = jetTag.eta();
    double phiTag = jetTag.phi();    

    //cout << " \t probe cand is pt / eta / phi " << jetProbe.pt() << " / " << etaProbe << " / " << phiProbe << endl;
	  	  
    const float dR2 = reco::deltaR2(probeEta,probePhi,etaTag,phiTag);
    static const float dR2min = 0.4*0.4;

    if(dR2 < dR2min) 
      continue;

    if(checkFilter(etaTag,phiTag,trigObjsUnpacked,tagName))
      nTags++;

  }
	
  if(nTags < tagMin){
    //cout << "Fail probe"<< endl;
    return false;
  }

  return true;
}//tagJetFilterMatch



bool TriggerStudy::tagJetCut(const edm::ParameterSet& jetTurnOnInfo, edm::Handle<edm::View<pat::Jet> > jetsHandle,
			     float probeEta, float probePhi){

  bool passTagCut = false;

  // Only support away side btagging
  string tagName  = jetTurnOnInfo.getParameter<string>("tagCut");	
	  
  bool reqBTag  = (tagName == "Btag");
	  
  bool passBTag  = !reqBTag;

  if(reqBTag){

    // Loop on jets{
    for(auto& jetTag : *jetsHandle){
    
      double ptTag  = jetTag.pt();    
      if(ptTag < 30) continue;

      double etaTag = jetTag.eta();
      double phiTag = jetTag.phi();    
    
      //cout << " \t tag cand is pt / eta / phi " << jetTag.pt() << " / " << etaTag << " / " << phiTag << " / " << (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb")) << endl;
    	  	  
      const float dR2 = reco::deltaR2(probeEta,probePhi,etaTag,phiTag);
      static const float dR2min = 0.4*0.4;
    
      if(dR2 < dR2min) 
	continue;
    
      //cout << " \t pass Tag " << endl;
      double tagDeepFlavour = (jetTag.bDiscriminator("pfDeepFlavourJetTags:probb") + jetTag.bDiscriminator("pfDeepFlavourJetTags:probbb") + jetTag.bDiscriminator("pfDeepFlavourJetTags:problepb"));
      if(tagDeepFlavour < 0.6) continue;
    
      passBTag = true;
      break;
    }
  }
	  
  passTagCut = (passBTag);

  if(!passTagCut){
    return false;
    //cout << "Fail tag"<< endl;
  }

  return true;
}//tagJetCut


bool TriggerStudy::probeJetCut(const edm::ParameterSet& jetTurnOnInfo, edm::Handle<edm::View<pat::Jet> > jetsHandle, const pat::Jet& jet){
			       
  bool passProbeCut = false;

  // Only support near side btagging and truth bcuts 
  string probeName  = jetTurnOnInfo.getParameter<string>("probeCut");	
	  
  bool reqBTag  = (probeName == "Btag"  || probeName == "trueBtag");
  bool reqTrueB = (probeName == "trueB" || probeName == "trueBtag");
	  
  bool passBTag  = !reqBTag;
  bool passTrueB = !reqTrueB;

  if(reqBTag){
    
    double tagDeepFlavour = (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb"));
    if(tagDeepFlavour > 0.6){
      passBTag = true;
    }
    
  }

  if(reqTrueB){
    //cout << "Matching to trueB. " << endl;
    //cout << " nBQs " << bQuarks.size() << endl;
    for(const reco::GenParticle* bQ :  thisEvent.bQuarks){
      double etaTrueB = bQ->p4().eta();
      double phiTrueB = bQ->p4().phi();    
	      
      const float dR2 = reco::deltaR2(jet.eta(),jet.phi(),etaTrueB,phiTrueB);
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
    return false;
  }
  
  return true;
}//probeJetCut


void TriggerStudy::getSelectedJets(edm::Handle<edm::View<pat::Jet> > jetsHandle){

  for(const pat::Jet& jet : *jetsHandle){

    double pt = jet.pt();    
    double eta = jet.eta();
    if(fabs(eta) > 2.4) continue;
    
    if(pt<30) continue;
    thisEvent.hT30+=pt;
    
    if(pt < 40) continue;
    thisEvent.hT+=pt;

    
    // Add overlapp removal
    bool passOverlap = true;
    double phi = jet.phi();
    for(const pat::Electron* elec : thisEvent.selElecs){
      const float dR2 = reco::deltaR2(eta,phi,elec->eta(),elec->phi());
      if(dR2 < 0.4*0.4){
	passOverlap = false;
	//cout << "failed electron overlap  " << sqrt(dR2) << endl;
      }
    }


    for(const pat::Muon* muon : thisEvent.selMuons){
      const float dR2 = reco::deltaR2(eta,phi,muon->eta(),muon->phi());
      if(dR2 < 0.4*0.4){
	passOverlap = false;
	//cout << "failed muon overlap  " << sqrt(dR2) << endl;
      }
    }

    if(!passOverlap) continue;

    thisEvent.jet_pts.push_back(pt);
    thisEvent.selJets.push_back(&jet);

    double deepFlavour = (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb"));
    //cout << " " << jet.pt()  << " " << jet.eta() << " " << jet.phi() << " " << deepFlavour << " " << jet.pt()*jet.jecFactor("Uncorrected") <<  " " << jet.userFloat("caloJetMap:pt") << " " << jet.userFloat("pileupJetId:fullDiscriminant") 
    //  //<< " " << jet.userFloat("pileupJetIdUpdated:fullDiscriminant") << " " << jet.userFloat("pileupJetIdUpdated:fullId")  
    //	 << endl;;


    if(deepFlavour < 0.6) continue;

    thisEvent.tagJet_pts.push_back(pt);
    thisEvent.tagJets.push_back(&jet);
  }
}

void TriggerStudy::getSelectedMuons(edm::Handle<pat::MuonCollection> muonsHandle, const reco::Vertex &pVtx){

  float muon_cut_pt_ = 25;
  float muon_cut_eta_ = 2.4;
  float muon_cut_iso_ = 0.12;
  //iEvent.getByToken(muonToken_, muHa);

  for (const pat::Muon &mu : *muonsHandle) { 
    bool passKinPreSel( mu.pt() > 8  && fabs(mu.eta()) < muon_cut_eta_ );
    if(!passKinPreSel) continue;
    thisEvent.allMuons.push_back(&mu);
    
    bool passKin( mu.pt() > muon_cut_pt_  && fabs(mu.eta()) < muon_cut_eta_ );
    if(!passKin) continue;

    //cf. https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2
    //bool isMedium(muon::isMediumMuon(mu));
    bool isTight(muon::isTightMuon(mu,pVtx));
    bool passID(isTight);
    if(!passID) continue;

    double nhIso   = mu.neutralHadronIso();
    double puchIso = mu.puChargedHadronIso();
    double chIso   = mu.chargedHadronIso() ;
    double gIso    = mu.photonIso() ;
    double relIso  = (TMath::Max(Float_t(nhIso+gIso-0.5*puchIso),Float_t(0.))+chIso)/mu.pt();
    bool passIso( relIso < muon_cut_iso_ );
    if(!passIso)  continue;
    thisEvent.selMuons.push_back(&mu);
  }
}


void TriggerStudy::getSelectedElectrons(edm::Handle<edm::View<pat::Electron> > elecsHandle, edm::Handle<reco::ConversionCollection> convHandle, edm::Handle<edm::ValueMap<bool> > eIDHandle){
  float electron_cut_pt_ = 25;
  float electron_cut_eta_ = 2.4;
  //float electron_cut_iso_ = 0.11;
  

  for (size_t i = 0; i < elecsHandle->size(); ++i)
    {
      const auto el = elecsHandle->ptrAt(i);
      const pat::Electron & elec = *el;
  
      bool passKin(elec.pt() > electron_cut_pt_ && 
		   fabs(elec.superCluster()->eta()) < electron_cut_eta_ && 
		   (elec.isEB() || elec.isEE()));
      if(!passKin) continue;

      thisEvent.allElecs.push_back(&elec);

      // Conversion rejection
      bool passConvVeto = !ConversionTools::hasMatchedConversion(elec,*convHandle,thisEvent.beamspot->position());

      //cut-based electron id+iso
      //cf. https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
      bool passElectronID = (*eIDHandle)[el];
      bool passID( passConvVeto && passElectronID);
      if(!passID) continue;

      thisEvent.selElecs.push_back(&elec);
    }
}


//
//
// 
bool CMSSWTools::passJetID(const pat::Jet* pfjet){
    
  double NHF  = pfjet->neutralHadronEnergyFraction();
  double NEMF = pfjet->neutralEmEnergyFraction();
  double CHF  = pfjet->chargedHadronEnergyFraction();
  double MUF  = pfjet->muonEnergyFraction();
  double CEMF = pfjet->chargedEmEnergyFraction();
  int    NumConst = pfjet->chargedMultiplicity()+pfjet->neutralMultiplicity();
  //int    NumNeutralParticles =pfjet->neutralMultiplicity();
  int    CHM      = pfjet->chargedMultiplicity(); 
  return (abs(pfjet->eta())<=2.6 && CEMF<0.8 && CHM>0 && CHF>0 && NumConst>1 && NEMF<0.9 && MUF <0.8 && NHF < 0.9 );

}






DEFINE_FWK_MODULE(TriggerStudy);
#endif
