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


#include <vector>
#include <string>
#include <iostream>
#include <math.h>



using std::cout; using std::endl;
using std::string; using std::vector;


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


  void printFilters(const float eta,const float phi,const vector<pat::TriggerObjectStandAlone>& trigObjs,const float maxDeltaR=0.1)
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



  bool foundFilter(const string& filter, const vector<pat::TriggerObjectStandAlone>& trigObjs){
    for(auto& trigObj : trigObjs){
      if(trigObj.hasFilterLabel(filter))
	return true;
    }

    return false;
  }


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
  bool isMC_;
  vector<edm::ParameterSet> jetTurnOns_;

  //trigger results stores whether a given path passed or failed
  //a path is series of filters
  edm::EDGetTokenT<edm::TriggerResults> trigResultsToken_;
  //triggers are the objects the trigger is run on, with a list of filters they pass
  //match to these to see if a given electron/photon/whatever passed a given filter
  edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > trigObjsToken_;

  edm::EDGetTokenT<edm::View<pat::Jet> > jetsToken_;
  edm::EDGetTokenT<edm::View<reco::GenJet> > truthJetsToken_;
  edm::EDGetTokenT<edm::View<reco::GenParticle> > truthPartsToken_;
  edm::Service<TFileService> fs;

  struct eventHists {

    TH1F* h_mBB;
    TH1F* h_pTBB;
    TH1F* h_nSelJets;
    TH1F* h_hT;    
    TH1F* h_hT30;    
    TH1F* h_hT_s;    
    TH1F* h_hT30_s;    

    eventHists(edm::Service<TFileService>& fs, string cutName ){
      h_mBB      = fs->make<TH1F>( ("mBB_"+cutName).c_str()  , "m_{BB}", 100,  0., 1000. );
      h_pTBB     = fs->make<TH1F>( ("pTBB_"+cutName).c_str()  , "pT_{BB}", 100,  0., 1000. );
      h_nSelJets = fs->make<TH1F>( ("nSelJet_"+cutName).c_str()  , "Selected Jet Multiplicity",  16,  -0.5, 15.5 );
      h_hT       = fs->make<TH1F>( ("hT_"+cutName).c_str()  , "hT",  200,  0, 1000 );
      h_hT30     = fs->make<TH1F>( ("hT30_"+cutName).c_str()  , "hT (jets pt > 30 GeV)",  200,  0, 1000 );
    }

    void Fill(double mBB, double pTBB, unsigned int nSelJets, double hT, double hT30 ){
      h_mBB      ->Fill(mBB);
      h_pTBB     ->Fill(pTBB);
      h_nSelJets ->Fill(nSelJets);
      h_hT       ->Fill(hT);
      h_hT30     ->Fill(hT30);
    }

  };


  struct jetHists {

    TH1F* h_pt;
    TH1F* h_pt_s;
    TH1F* h_phi;
    TH1F* h_eta;
    TH1F* h_deepFlavour;


    jetHists(TFileDirectory& jetDir, string cutName ){
      h_pt          = jetDir.make<TH1F>( ("pt_"+cutName).c_str()  , "p_{T}", 250,  0., 500. );
      h_pt_s        = jetDir.make<TH1F>( ("pt_s_"+cutName).c_str()  , "p_{T}",200,  0., 100. );
      h_phi         = jetDir.make<TH1F>( ("phi_"+cutName).c_str()  , "phi",  100,  -3.2, 3.2 );
      h_eta         = jetDir.make<TH1F>( ("eta_"+cutName).c_str()  , "eta",  100,  -4, 4 );
      h_deepFlavour = jetDir.make<TH1F>( ("deepFlavour_"+cutName).c_str()  , "deepFlavour",  100,  -0.1, 1.1 );
    }

    void Fill(double pt, double eta, double phi, double deepFlavour ){
      h_pt          ->Fill(pt);
      h_pt_s        ->Fill(pt);
      h_phi         ->Fill(phi);
      h_eta         ->Fill(eta);
      h_deepFlavour ->Fill(deepFlavour);
    }

  };

  //
  //  Event Hists
  //
  vector<eventHists> hAll;
  vector<eventHists> hPassNJet;
  vector<eventHists> hPassPreSelMed;
  vector<eventHists> hPassPreSel;

  //
  //  Jet Hists
  //
  vector<jetHists> hJets_num; 
  vector<jetHists> hJets_den; 
  

public:
  explicit TriggerStudy(const edm::ParameterSet& iPara);
  ~TriggerStudy(){}
  void beginJob() override;
  void analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)override;

};

TriggerStudy::TriggerStudy(const edm::ParameterSet& iPara):
  trigObjsTag_(iPara.getParameter<edm::InputTag>("trigObjs")),
  trigResultsTag_(iPara.getParameter<edm::InputTag>("trigResults")),
  filtersToPass_(iPara.getParameter<vector<edm::ParameterSet> >("filtersToPass")), 
  pathsToPass_(iPara.getParameter<vector<string> >("pathsToPass")),
  hltPreSelection_(iPara.getParameter<vector<string> >("hltPreSelection")),
  isMC_(iPara.getParameter<bool>("isMC")),
  jetTurnOns_(iPara.getParameter<vector<edm::ParameterSet> >("jetTurnOns")), 
  trigResultsToken_(consumes<edm::TriggerResults>(trigResultsTag_)),
  trigObjsToken_(consumes<vector<pat::TriggerObjectStandAlone> >(trigObjsTag_)),
  jetsToken_(consumes<edm::View<pat::Jet> >(iPara.getParameter<edm::InputTag>("jets"))),
  truthJetsToken_(consumes<edm::View<reco::GenJet> >(iPara.getParameter<edm::InputTag>("truthJets"))),
  truthPartsToken_(consumes<edm::View<reco::GenParticle> >(iPara.getParameter<edm::InputTag>("truthParts")))
{
  
}

void TriggerStudy::beginJob()
{

  hAll           .push_back(eventHists(fs,"all"));
  hPassNJet      .push_back(eventHists(fs,"passNJet_all"));
  hPassPreSelMed .push_back(eventHists(fs,"passPreSelMed_all"));
  hPassPreSel    .push_back(eventHists(fs,"passPreSel_all"));


  for(edm::ParameterSet filterInfo : filtersToPass_){
    string name = filterInfo.getParameter<string>("histName");
    hAll          .push_back(eventHists(fs,name));
    hPassNJet     .push_back(eventHists(fs,"passNJet_"+name));
    hPassPreSelMed.push_back(eventHists(fs,"passPreSelMed_"+name));
    hPassPreSel   .push_back(eventHists(fs,"passPreSel_"+name));
  }

  TFileDirectory jetDir = fs->mkdir( "jetHists" );

  for(edm::ParameterSet jetTurnOnInfo : jetTurnOns_){
    string name = jetTurnOnInfo.getParameter<string>("histName");
    hJets_num.push_back(jetHists(jetDir,name));
    hJets_den.push_back(jetHists(jetDir,name+"_den"));
  }

}



void TriggerStudy::analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)
{ 

  auto trigResultsHandle = getHandle(iEvent,trigResultsToken_) ;
  auto trigObjsHandle = getHandle(iEvent,trigObjsToken_); 
  edm::Handle<edm::View<pat::Jet> > jetsHandle = getHandle(iEvent,jetsToken_);

  //
  //  HLT Preselection
  //
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResultsHandle);
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

  

  float mBB = -1;
  float pTBB = -1;

  //
  //  Get Truth
  //
  if(isMC_){
    edm::Handle<edm::View<reco::GenJet> > truthJetsHandle = getHandle(iEvent,truthJetsToken_);
    edm::Handle<edm::View<reco::GenParticle> > truthPartsHandle = getHandle(iEvent,truthPartsToken_);

    vector<const reco::GenParticle*> bosons;
    vector<const reco::GenParticle*> bQuarks;
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
  //  Get reco
  //  
  edm::LogInfo ("TrigerStudy") << "Printing jets " << endl;

  unsigned int nSelectedJets = 0;
  unsigned int nTaggedJetsMed = 0;
  unsigned int nTaggedJets = 0;
  
  float hT = 0;
  float hT30 = 0;
  for(auto& jet : *jetsHandle){
    double eta = jet.eta();
    double pt = jet.pt();    
    double deepFlavour = (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb"));


    //cout << "Reco Jet  " << pt << " " << eta << " " << jet.phi() << " " << deepFlavour << endl;
    if(fabs(eta) > 2.5) continue;
    
    if(pt<30) continue;
    hT30+=pt;

    if(pt < 40) continue;
    ++nSelectedJets;
    hT+=pt;

    if(deepFlavour < 0.2770) continue;
    ++nTaggedJetsMed;

    if(deepFlavour < 0.6) continue;
    ++nTaggedJets;
  }

  bool pass_nJets = nSelectedJets > 3;
  bool pass_nBJetsMed = nTaggedJetsMed > 3;
  bool pass_nBJets = nTaggedJets > 3;
  bool pass_preSelectionMed = pass_nJets and pass_nBJetsMed;
  bool pass_preSelection = pass_nJets and pass_nBJets;
  //cout << " nSelectedJets / nTaggedJets " << nSelectedJets << " / " << nTaggedJets << endl;

  hAll.at(0).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
  if(pass_nJets)           hPassNJet     .at(0).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
  if(pass_preSelectionMed) hPassPreSelMed.at(0).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
  if(pass_preSelection)    hPassPreSel   .at(0).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
    

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



  //
  //  Checking the filters
  //
  vector<string> filterNames;
  vector<bool> filterPassed;
  for(edm::ParameterSet filterInfo : filtersToPass_){
    string name = filterInfo.getParameter<string>("filterName");

    unsigned int mult = filterInfo.getParameter<unsigned int>("mult");
    double pt = filterInfo.getParameter<double>("pt");
    vector<const pat::TriggerObjectStandAlone*> releventTrigObs = getAllTrigObjs(trigObjsUnpacked, name);
    bool passFilter = true;

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
    
    //filtersPassed.push_back(foundFilter(filter,trigObjsUnpacked));
    filterNames .push_back(name);
    filterPassed.push_back(passFilter);
  }

  //
  //  Print Filters fill hists
  //
  bool printFilters = false;
  if(printFilters){
    cout << " preselection Passed: ";
    cout << pass_nJets << " " << pass_nBJets << " " << pass_preSelection << " ... ";
  }

  if(printFilters) cout << " filters Passed: ";

  unsigned int filterNum = 1; // 0 is All
  for(bool thisFilter : filterPassed){
    if(printFilters) cout << thisFilter << " ";
    if(!thisFilter) break;

    hAll.at(filterNum).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
    if(pass_nJets)           hPassNJet     .at(filterNum).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
    if(pass_preSelectionMed) hPassPreSelMed.at(filterNum).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
    if(pass_preSelection)    hPassPreSel   .at(filterNum).Fill(mBB, pTBB, nSelectedJets, hT, hT30);
 
    ++filterNum;
  }

  //
  //  Print  the final decision
  //
  if(printFilters){
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

    if(fabs(eta) > 2.5) continue;


    // 
    // Loop on filter reqs
    //
    unsigned int turnOnNum = 0; // 0 is All
    for(edm::ParameterSet jetTurnOnInfo : jetTurnOns_){
      string denName  = jetTurnOnInfo.getParameter<string>("denominatorReq");

      bool passDen = true;
      if(denName != ""){

	vector<string>::iterator itr = std::find(filterNames.begin(), filterNames.end(), denName);
	if(itr == filterNames.end()){
	  cout << "ERROR " << denName << " not found " << endl;
	  continue;
	}

	unsigned int denIndex = std::distance(filterNames.begin(), itr);
	for(unsigned int iFilt = 0; iFilt < (denIndex+1); ++iFilt){
	  if(!filterPassed.at(iFilt)) passDen = false;
	}
	
      }

      if(passDen){
	hJets_den.at(turnOnNum).Fill(pt,eta, phi, deepFlavour);

	string numName  = jetTurnOnInfo.getParameter<string>("filterName");
	if(checkFilter(eta,phi,trigObjsUnpacked,numName) )
	  hJets_num.at(turnOnNum).Fill(pt,eta, phi, deepFlavour);
      }
      
      ++turnOnNum;
    }// Turn Ons

  }// jets




}



DEFINE_FWK_MODULE(TriggerStudy);
#endif
