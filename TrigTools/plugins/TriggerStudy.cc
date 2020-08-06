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

  struct hists {

    TH1F* h_mBB;
    TH1F* h_pTBB;
    TH1F* h_nSelJets;

    hists(edm::Service<TFileService>& fs, string cutName ){
      h_mBB      = fs->make<TH1F>( ("mBB_"+cutName).c_str()  , "m_{BB}", 100,  0., 1000. );
      h_pTBB     = fs->make<TH1F>( ("pTBB_"+cutName).c_str()  , "pT_{BB}", 100,  0., 1000. );
      h_nSelJets = fs->make<TH1F>( ("nSelJet_"+cutName).c_str()  , "Selected Jet Multiplicity",  16,  -0.5, 15.5 );
    }

    void Fill(double mBB, double pTBB, unsigned int nSelJets){
      h_mBB      ->Fill(mBB);
      h_pTBB     ->Fill(pTBB);
      h_nSelJets ->Fill(nSelJets);
    }


  };

  vector<hists> hAll;
  vector<hists> hPassNJet;
  vector<hists> hPassPreSel;
 
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
  trigResultsToken_(consumes<edm::TriggerResults>(trigResultsTag_)),
  trigObjsToken_(consumes<vector<pat::TriggerObjectStandAlone> >(trigObjsTag_)),
  jetsToken_(consumes<edm::View<pat::Jet> >(iPara.getParameter<edm::InputTag>("jets"))),
  truthJetsToken_(consumes<edm::View<reco::GenJet> >(iPara.getParameter<edm::InputTag>("truthJets"))),
  truthPartsToken_(consumes<edm::View<reco::GenParticle> >(iPara.getParameter<edm::InputTag>("truthParts")))
{
  
}

void TriggerStudy::beginJob()
{
  //TFileDirectory subDir = fs->mkdir( "TriggerStudy" );

  hAll        .push_back(hists(fs,"all"));
  hPassNJet   .push_back(hists(fs,"passNJet_all"));
  hPassPreSel .push_back(hists(fs,"passPreSel_all"));

  for(edm::ParameterSet filterInfo : filtersToPass_){
    string name = filterInfo.getParameter<string>("histName");
    hAll           .push_back(hists(fs,name));
    hPassNJet  .push_back(hists(fs,"passNJet_"+name));
    hPassPreSel.push_back(hists(fs,"passPreSel_"+name));
    //h_mBB.push_back(fs->make<TH1F>( ("mBB_"+name).c_str()  , "m_{BB}", 100,  0., 1000. ));
    //h_mBB_passNJet.push_back(fs->make<TH1F>( ("mBB_passNJet_"+name).c_str()  , "m_{BB}", 100,  0., 1000. ));
    //h_mBB_passPreSel.push_back(fs->make<TH1F>( ("mBB_passPreSel_"+name).c_str()  , "m_{BB}", 100,  0., 1000. ));
  }

}



void TriggerStudy::analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)
{ 

  auto trigResultsHandle = getHandle(iEvent,trigResultsToken_) ;
  auto trigObjsHandle = getHandle(iEvent,trigObjsToken_); 
  edm::Handle<edm::View<pat::Jet> > jetsHandle = getHandle(iEvent,jetsToken_);
  edm::Handle<edm::View<reco::GenJet> > truthJetsHandle = getHandle(iEvent,truthJetsToken_);
  edm::Handle<edm::View<reco::GenParticle> > truthPartsHandle = getHandle(iEvent,truthPartsToken_);
  

  //
  //  Get Truth
  //
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
  float mBB  = pBB.M();
  float pTBB = pBB.Pt();

  //cout << " mBB " << mBB  <<endl;


  //if(bosons.size() != 2 || bQuarks.size() != 4){
  //  cout << " nBosons " << bosons.size() << " nBQuarks " << bQuarks.size() << endl;
  //
  //  for(const reco::GenParticle& tPart : *truthPartsHandle){
  //    int pdgId = tPart.pdgId();
  //  
  //    bool isBoson = (pdgId == 25 || pdgId == 23);
  //    bool isBQuark = abs(pdgId) == 5;
  //
  //    if(!isBoson and !isBQuark) continue;
  //
  //    if(!tPart.isLastCopy()) continue;
  //
  //    cout << "Truth Part " << tPart.pt() << " " << tPart.eta()   << " " << tPart.phi()  << "  pdgID " << tPart.pdgId() << " nDaughters " << tPart.numberOfDaughters() 
  //	   << " nMothers " << tPart.numberOfMothers()
  //	   << " mother was " << tPart.mother()->pdgId()
  //	   << " status " << tPart.status()
  //	   << " isLastCopy " << tPart.isLastCopy()
  //	   << endl;
  //  }
  //
  //}

  //
  //  Get reco
  //  
  edm::LogInfo ("TrigerStudy") << "Printing jets " << endl;

  unsigned int nSelectedJets = 0;
  unsigned int nTaggedJets = 0;
  for(auto& jet : *jetsHandle){
    double eta = jet.eta();
    double pt = jet.pt();    
    double deepFlavour = (jet.bDiscriminator("pfDeepFlavourJetTags:probb") + jet.bDiscriminator("pfDeepFlavourJetTags:probbb") + jet.bDiscriminator("pfDeepFlavourJetTags:problepb"));


    //cout << "Reco Jet  " << pt << " " << eta << " " << jet.phi() << " " << deepFlavour << endl;
    if(fabs(eta) > 2.5) continue;


    if(pt < 40) continue;
    ++nSelectedJets;


    if(deepFlavour < 0.6) continue;
    //if(deepFlavour < 0.2770) continue;
    ++nTaggedJets;


  }

  bool pass_nJets = nSelectedJets > 3;
  bool pass_nBJets = nTaggedJets > 3;
  bool pass_preSelection = pass_nJets and pass_nBJets;
  //cout << " nSelectedJets / nTaggedJets " << nSelectedJets << " / " << nTaggedJets << endl;

  hAll.at(0).Fill(mBB, pTBB, nSelectedJets);
  if(pass_nJets)        hPassNJet  .at(0).Fill(mBB, pTBB, nSelectedJets);
  if(pass_preSelection) hPassPreSel.at(0).Fill(mBB, pTBB, nSelectedJets);
    

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

    hAll.at(filterNum).Fill(mBB, pTBB, nSelectedJets);
    if(pass_nJets)        hPassNJet  .at(filterNum).Fill(mBB, pTBB, nSelectedJets);
    if(pass_preSelection) hPassPreSel.at(filterNum).Fill(mBB, pTBB, nSelectedJets);
 
    ++filterNum;
  }
    
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResultsHandle);
  for(auto& pathName : pathsToPass_){
    size_t pathIndex = getPathIndex(pathName,trigNames);
    if(pathIndex>=trigNames.size()) cout <<" path "<<pathName<<" not found in menu"<<endl;
    else{
      //cout <<" path index "<<pathIndex << " "<<trigNames.triggerName(pathIndex)<<  " was run " << trigResultsHandle->wasrun(pathIndex) << endl;
      //const edm::HLTPathStatus& pathStatus  = trigResultsHandle->at(pathIndex);
      //cout << "\t path status state: " << pathStatus.state() << " index " << pathStatus.index() << endl;
      if(printFilters)cout << " .... " << trigResultsHandle->accept(pathIndex) << endl;
    }
  }

  
//
//  bool debug = false;
//  string caloJetLabel = "hltSingleCaloJet5";
//  string pfJetLabel   = "hltSinglePFJet15";
//
//  //vector<const pat::TriggerObjectStandAlone*> allCaloJets = getAllMatchedJets(jetsHandle, trigObjsUnpacked, caloJetLabel);
//  //vector<const pat::TriggerObjectStandAlone*> allPFJets   = getAllMatchedJets(jetsHandle, trigObjsUnpacked, pfJetLabel);
//  vector<const pat::TriggerObjectStandAlone*> allCaloJets = getAllTrigObjs(trigObjsUnpacked, caloJetLabel);
//  vector<const pat::TriggerObjectStandAlone*> allPFJets   = getAllTrigObjs(trigObjsUnpacked, pfJetLabel);
//
//  
//
//  if(debug) cout << " nJets " << (*jetsHandle).size() << " nCaloJets " << allCaloJets.size()  << " nPFJets " << allPFJets.size()  << endl;
//
//  //
//  //  Cuts on Calo Jets
//  // 
//  unsigned int nCaloJetCentral30 = 0;
//  double htCaloJetCentral30 = 0;
//  for(auto& caloJet : allCaloJets){
//    if(fabs(caloJet->eta()) < 2.5){
//      if(caloJet->pt() > 30){
//	++nCaloJetCentral30;
//	htCaloJetCentral30 += caloJet->pt();
//      }
//    }
//  }
//
//  bool passL1 = filterPassed.at(0);
//  if(!passL1) return;
//
//  bool passCount_hltQuadCentralJet30 = (nCaloJetCentral30 > 3);
//  bool hltQuadCentralJet30 = filterPassed.at(1);
//
//  if( (passCount_hltQuadCentralJet30 && !hltQuadCentralJet30) || (!passCount_hltQuadCentralJet30 && hltQuadCentralJet30)){
//    vector<const pat::TriggerObjectStandAlone*> allQuadCentralJet30 = getAllTrigObjs(trigObjsUnpacked, "hltQuadCentralJet30");
//
//    cout << "ERROR on hltQuadCentralJet30 count gives: " << passCount_hltQuadCentralJet30 << " ( " << nCaloJetCentral30 << " ) vs " << hltQuadCentralJet30 << endl;
//    cout << " \t n hltQuadCentralJet30 " << allQuadCentralJet30.size() << endl;
//    for(auto& caloJet : allCaloJets){
//      if(fabs(caloJet->eta()) < 2.5){
//	cout << " \t CaloJet pt " << caloJet->pt()  << endl;
//      }
//    }
//  }
//
//  if(!hltQuadCentralJet30) return;
//
//  bool passCount_hltCaloQuadJet30HT320 = (htCaloJetCentral30 >= 320.);
//  bool hltCaloQuadJet30HT320 = filterPassed.at(2);
//  
//  if( (passCount_hltCaloQuadJet30HT320 && !hltCaloQuadJet30HT320) || (!passCount_hltCaloQuadJet30HT320 && hltCaloQuadJet30HT320)){
//    cout << "ERROR hltCaloQuadJet30HT320 count gives: " << passCount_hltCaloQuadJet30HT320 << " ( " << htCaloJetCentral30 << " ) vs " << hltCaloQuadJet30HT320 << endl;
//    vector<const pat::TriggerObjectStandAlone*> allCaloQuadJet30HT320 = getAllTrigObjs(trigObjsUnpacked, "hltCaloQuadJet30HT320");
//    for(auto& htObj : allCaloQuadJet30HT320){
//      cout << " \t " << htObj->pt()<< endl;
//    }
//
//
//  }
//
//  if(!hltCaloQuadJet30HT320) return;
//
//  bool hltBTagCaloDeepCSVp17Double = filterPassed.at(3);
//  // BTaging not stored in the miniAODs !
//  if(!hltBTagCaloDeepCSVp17Double) return;  
//
//  //
//  //  Cuts on PF Jets
//  // 
//  unsigned int nPFJetCentral30 = 0;
//  //double htCaloJetCentral30 = 0;
//  for(auto& pfJet : allPFJets){
//    if(fabs(pfJet->eta()) < 2.5){
//      if(pfJet->pt() > 30){
//	++nPFJetCentral30;
//	//htCaloJetCentral30 += caloJet->pt();
//      }
//    }
//  }
//
//
//
//  bool passCount_hltPFCentralJetLooseIDQuad30 = (nPFJetCentral30 > 3);
//  bool hltPFCentralJetLooseIDQuad30 = filterPassed.at(4);
//
//
//  
//
//  
//
//
//  cout <<"checking jet "<<endl;
//  for(auto& jet : *jetsHandle){
//    cout << jet.pt() << " " << jet.eta() << " " << jet.phi() << endl;
//    checkFilters(jet.eta(),jet.phi(),trigObjsUnpacked,filtersToPass_);
//  }
//
//  cout << "Check Ht " << endl;
//  for(auto& trigObj : trigObjsUnpacked){
//    const vector<string>& objFilters = trigObj.filterLabels();
//    if(std::find(objFilters.begin(),objFilters.end(),"hltCaloQuadJet30HT320")!=objFilters.end()){
//      cout << " has filter label " << trigObj.hasFilterLabel("hltCaloQuadJet30HT320") << endl;
//      cout << " \t " << trigObj.pt() << endl; //" " << trigObj.sumEt() << endl;
//    }
//  }
//
}



DEFINE_FWK_MODULE(TriggerStudy);
#endif
