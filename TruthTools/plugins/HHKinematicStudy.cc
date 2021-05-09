#ifndef CMSSWTools_TRUTHTOOLS_HHKINEMATICSTUDY
#define CMSSWTools_TRUTHTOOLS_HHKINEMATICSTUDY

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/HLTPathStatus.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"



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



class HHKinematicStudy : public edm::EDAnalyzer {
private:

  edm::ParameterSet offlinePreSelection_;
  unsigned int minNSelJet_ = 0;
  unsigned int minNTagMedJet_ = 0;
  unsigned int minNTagTightJet_ = 0;


  bool isBBMC_;

  edm::EDGetTokenT<edm::View<pat::Jet> > jetsToken_;
  edm::EDGetTokenT<edm::View<reco::GenJet> > truthJetsToken_;
  edm::EDGetTokenT<edm::View<reco::GenParticle> > truthPartsToken_;
  edm::Service<TFileService> fs;

  unsigned int nTruthBosons_ = 0;

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

  struct bosonHists {

    TH1F* h_m      = nullptr;
    TH1F* h_pT     = nullptr;
    TH1F* h_eta    = nullptr;
    TH1F* h_phi    = nullptr;

    bosonHists(edm::Service<TFileService>& fs, string name ){
      h_m      = fs->make<TH1F>( ("m_" +name).c_str()    , "m_{B};m_{B};Entries",  100,  0., 1000. );
      h_pT     = fs->make<TH1F>( ("pT_"+name).c_str()    , "pT_{B};pT_{B};Entries", 100,  0., 1000. );
      h_eta     = fs->make<TH1F>( ("eta_"+name).c_str()  , "eta_{B};#eta_{B};Entries", 100,  -4., 4. );
      h_phi     = fs->make<TH1F>( ("phi_"+name).c_str()  , "phi_{B};#phi_{B};Entries", 100,  -3.2, 3.2 );
    }

    void Fill(const reco::GenParticle* boson, float weight = 1.0 ){
      reco::ParticleState::LorentzVector p4 = boson->p4();
      
      h_m       -> Fill(p4.M()   ,weight);
      h_pT      -> Fill(p4.Pt()  ,weight);
      h_eta     -> Fill(p4.Eta() ,weight);
      h_phi     -> Fill(p4.Phi() ,weight);
    }

  };


  struct eventHists {

    TH1F* h_mBB      = nullptr;
    TH1F* h_mBB_l    = nullptr;
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
	h_mBB      = fs->make<TH1F>( ("mBB_"+cutName).c_str()  ,   "m_{BB};m_{BB};Entries", 100,  0., 1000. );
	h_mBB_l      = fs->make<TH1F>( ("mBB_l_"+cutName).c_str(), "m_{BB};m_{BB};Entries", 100,  0., 2000. );
	h_pTBB     = fs->make<TH1F>( ("pTBB_"+cutName).c_str()  ,  "pT_{BB}", 100,  0., 1000. );
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
      if(h_mBB_l)  h_mBB_l      ->Fill(mBB, weight);
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
  map<string, eventHists*> hAll;
  bosonHists* hHiggsBosons;
  bosonHists* hVBosons;


public:
  explicit HHKinematicStudy(const edm::ParameterSet& iPara);
  ~HHKinematicStudy(){ }
  void beginJob() override;
  void beginRun(edm::Run const&, edm::EventSetup const&) override;
  void endJob() override;
  void analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)override;

};

HHKinematicStudy::HHKinematicStudy(const edm::ParameterSet& iPara):
  offlinePreSelection_(iPara.getParameter<edm::ParameterSet>("offlinePreSelection")),
  isBBMC_(iPara.getParameter<bool>("isBBMC")),

  jetsToken_(consumes<edm::View<pat::Jet> >(iPara.getParameter<edm::InputTag>("jets"))),
  truthJetsToken_(consumes<edm::View<reco::GenJet> >(iPara.getParameter<edm::InputTag>("truthJets"))),
  truthPartsToken_(consumes<edm::View<reco::GenParticle> >(iPara.getParameter<edm::InputTag>("truthParts"))),
  nTruthBosons_ (iPara.getParameter<unsigned int>("nTruthBosons"))
			       //algInputTag_(iPara.getParameter<edm::InputTag>("AlgInputTag")),
			       //extInputTag_(iPara.getParameter<edm::InputTag>("ExtInputTag"))
{
  if(offlinePreSelection_.exists("minNSelJet"))
     minNSelJet_      = offlinePreSelection_.getParameter<unsigned int>("minNSelJet");

  if(offlinePreSelection_.exists("minNTagMedJet"))
    minNTagMedJet_   = offlinePreSelection_.getParameter<unsigned int>("minNTagMedJet");

  if(offlinePreSelection_.exists("minNTagTightJet"))
    minNTagTightJet_ = offlinePreSelection_.getParameter<unsigned int>("minNTagTightJet");
  
  edm::LogInfo("HHKinematicStudy") << " Offline Selection: minNSelJet: " << minNSelJet_ << "  minNTagMedJet: " << minNTagMedJet_ << " minNTagTightJet: " << minNTagTightJet_;

}

void HHKinematicStudy::beginJob()
{

  
  hAll.insert( pair<string, eventHists*>("all", new eventHists(fs,"all", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("4j30", new eventHists(fs,"4j30", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("4j40", new eventHists(fs,"4j40", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("4j45", new eventHists(fs,"4j45", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("4j50", new eventHists(fs,"4j50", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("4j60", new eventHists(fs,"4j60", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("j75j60j45j40", new eventHists(fs,"j75j60j45j40", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("HT260_j75j60j45j40", new eventHists(fs,"HT260_j75j60j45j40", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("HT300_j75j60j45j40", new eventHists(fs,"HT300_j75j60j45j40", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("HT330_j75j60j45j40", new eventHists(fs,"HT330_j75j60j45j40", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("HT350_j75j60j45j40", new eventHists(fs,"HT350_j75j60j45j40", isBBMC_)));
  hAll.insert( pair<string, eventHists*>("HT400_j75j60j45j40", new eventHists(fs,"HT400_j75j60j45j40", isBBMC_)));

  hHiggsBosons = new bosonHists(fs,"Higgs");
  hVBosons     = new bosonHists(fs,"V");
}


void HHKinematicStudy::beginRun(edm::Run const&, edm::EventSetup const& evSetup){
  

}

void HHKinematicStudy::endJob()
{
  edm::LogInfo("HHKinematicStudy") << "Total Events " << NEvents_all << " pass HLT Preselection " << NEvents_passHLTPreSelection << " pass Offline Preselection " << NEvents_passOfflinePreSelection;
}

void HHKinematicStudy::analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)
{ 
  ++NEvents_all;
  //if(iEvent.isRealData()) isBBMC_ = false;
  

  float mBB = -1;
  float pTBB = -1;
  vector<const reco::GenParticle*> bQuarks;
  vector<const reco::GenParticle*> bosons;
  vector<const reco::GenParticle*> HiggsBosons;
  vector<const reco::GenParticle*> VBosons;


  //
  //  Get Truth
  //
  if(isBBMC_){
    edm::Handle<edm::View<reco::GenJet> > truthJetsHandle = getHandle(iEvent,truthJetsToken_);
    edm::Handle<edm::View<reco::GenParticle> > truthPartsHandle = getHandle(iEvent,truthPartsToken_);

    for(const reco::GenParticle& tPart : *truthPartsHandle){
      int pdgId = tPart.pdgId();
    
      bool isBoson      = (pdgId == 25 || pdgId == 23 || abs(pdgId) == 24) && tPart.status() == 62;
      bool isHiggsBoson = (pdgId == 25) && tPart.status() == 62;
      bool isVBoson     = (pdgId == 23 || abs(pdgId) == 24) && tPart.status() == 62;
      //bool isBQuark = abs(pdgId) == 5;

      //if(!isBoson and !isBQuark) continue;
      if(!isBoson) continue;

      //cout << "Truth Part " << tPart.pt() << " " << tPart.eta()   << " " << tPart.phi()  << "  pdgID " << tPart.pdgId() << " nDaughters " << tPart.numberOfDaughters() 
      //	 << " nMothers " << tPart.numberOfMothers()
      //	 << " status " << tPart.status()
      //	 << " isLastCopy " << tPart.isLastCopy()
      //	 << endl;

      if(!tPart.isLastCopy()) continue;

      if(isBoson)       bosons.push_back(&tPart);
      if(isHiggsBoson)  HiggsBosons.push_back(&tPart);
      if(isVBoson)      VBosons.push_back(&tPart);

      //if(isBQuark) bQuarks.push_back(&tPart);

      //cout << "Truth Part " << tPart.pt() << " " << tPart.eta()   << " " << tPart.phi()  << "  pdgID " << tPart.pdgId() << " nDaughters " << tPart.numberOfDaughters() 
      //	 << " nMothers " << tPart.numberOfMothers()
      //	 << " status " << tPart.status()
      //	 << " isLastCopy " << tPart.isLastCopy()
      //	 << endl;
    }

    if(bosons.size() != nTruthBosons_){
      cout << "ERROR not "<< nTruthBosons_ << " bosons ..." << bosons.size() << " ... skipping " << endl;
      return;
    }

    //if(bQuarks.size() < 4){
    //  cout << "ERROR too few b-quarks ..." << bQuarks.size() << " ... skipping " << endl;
    //  return;
    //}

    reco::ParticleState::LorentzVector pB1;
    reco::ParticleState::LorentzVector pB2;
    reco::ParticleState::LorentzVector pBB;


    //const LorentzVector&
    if(HiggsBosons.size() > 1){
      pB1 = HiggsBosons.at(0)->p4();
      pB2 = HiggsBosons.at(1)->p4();
      pBB = pB1 + pB2;
    }else{
      pB1 = bosons.at(0)->p4();
      pB2 = bosons.at(1)->p4();
      pBB = pB1 + pB2;
    }

    mBB  = pBB.M();
    pTBB = pBB.Pt();


  }
  //cout << " mBB " << mBB  <<endl;


  //
  //  Get offline info
  //  
  LogDebug ("TrigerStudy") << "Printing jets " << endl;
  edm::Handle<edm::View<pat::Jet> > jetsHandle = getHandle(iEvent,jetsToken_);

  unsigned int nSelectedJets = 0;
  unsigned int nTaggedJets = 0;

  unsigned int nTagJets30 = 0; 
  unsigned int nTagJets40 = 0; 
  unsigned int nTagJets45 = 0; 
  unsigned int nTagJets50 = 0; 
  unsigned int nTagJets60 = 0; 
  unsigned int nTagJets75 = 0; 


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
    ++nSelectedJets;
    hT30+=pt;
    jet_pts.push_back(pt);

    addJetInfo(sel_JetInfo, pt, eta, phi, deepFlavour);

    if(deepFlavour >= 0.2770) {
      ++nTaggedJets;
      tagJet_pts.push_back(pt);
      addJetInfo(tag_JetInfo, pt, eta, phi, deepFlavour);
    }
    

    hT+=pt;

    if(deepFlavour < 0.2770) continue;
    if(pt > 30) ++nTagJets30;
    if(pt > 40) ++nTagJets40;
    if(pt > 45) ++nTagJets45;
    if(pt > 50) ++nTagJets50;
    if(pt > 60) ++nTagJets60;
    if(pt > 75) ++nTagJets75;

  }

  //
  //  Offline Cuts
  //
  if(nSelectedJets < minNSelJet_) {
    LogDebug ("TrigerStudy") << "Failed minNSelJet " << endl;
    return;
  }

  if(nTaggedJets < minNTagTightJet_) {
    LogDebug ("TrigerStudy") << "Failed minNTagTightJet " << endl;
    return;
  }

  ++NEvents_passOfflinePreSelection;

  hAll["all"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

  for(const reco::GenParticle* higgs: HiggsBosons){
    hHiggsBosons->Fill(higgs);
  }

  for(const reco::GenParticle* v: VBosons){
    hVBosons->Fill(v);
  }

  if(nTagJets30 > 3)
    hAll["4j30"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

  if(nTagJets40 > 3)
    hAll["4j40"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

  if(nTagJets45 > 3)
    hAll["4j45"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

  if(nTagJets50 > 3)
    hAll["4j50"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

  if(nTagJets60 > 3)
    hAll["4j60"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

  if( (nTagJets40 > 3) && (nTagJets45 > 2) && (nTagJets60 > 1) && (nTagJets75 > 0)){
    hAll["j75j60j45j40"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);
    
    if(hT30> 260)
      hAll["HT260_j75j60j45j40"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

    if(hT30> 300)
      hAll["HT300_j75j60j45j40"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

    if(hT30> 330)
      hAll["HT330_j75j60j45j40"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

    if(hT30 > 350)
      hAll["HT350_j75j60j45j40"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);

    if(hT30> 400)
      hAll["HT400_j75j60j45j40"]->Fill(mBB, pTBB, nSelectedJets, hT, hT30, sel_JetInfo, tag_JetInfo);
    
  }


  
}//analyze



DEFINE_FWK_MODULE(HHKinematicStudy);
#endif
