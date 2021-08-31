// -*- C++ -*-
#if !defined(TriggerStudy_H)
#define TriggerStudy_H

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"

namespace CMSSWTools {

  bool passJetID(const pat::Jet* pfjet);

  class TriggerStudy : public edm::EDAnalyzer {
  private:

    //
    // Config
    //
    edm::InputTag trigObjsTag_;
    edm::InputTag trigResultsTag_;
    vector<edm::ParameterSet> filtersToPass_;
    vector<string> pathsToPass_;
    vector<string> hltPreSelection_;
    string year_;
    edm::ParameterSet offlinePreSelection_;
    unsigned int minNSelJet_ = 0;
    unsigned int minNSelMuon_ = 0;
    unsigned int minNSelElec_ = 0;
    unsigned int minNTagJet_ = 0;
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

    edm::EDGetTokenT<reco::VertexCollection> vtxToken_;
    edm::EDGetTokenT<reco::BeamSpot> bsToken_;
    edm::EDGetTokenT<edm::View<pat::Electron> > electronToken_;
    edm::EDGetTokenT<reco::ConversionCollection> conversionsToken_;
    edm::EDGetTokenT<edm::ValueMap<bool> > electronIdMapToken_;
    edm::EDGetTokenT<pat::MuonCollection> muonToken_;
    edm::EDGetTokenT<pat::METCollection> metToken_;

    // Event Data
    struct eventData { 

      vector<float> jet_pts;
      vector<float> tagJet_pts;
  
      vector<const pat::Jet*> selJets;
      vector<const pat::Jet*> tagJets;

      vector<const pat::Muon*> selMuons;
      vector<const pat::Muon*> allMuons;

      vector<const pat::Electron*> selElecs;
      vector<const pat::Electron*> allElecs;

      float hT = 0;
      float hT_noLep = 0;
      float hT_jetID = 0;
      float hT_jetID_noLep = 0;

      float hT30 = 0;
      float hT30_jetID = 0;

      float mBB  = -1;
      float pTBB = -1;
      vector<const reco::GenParticle*> bQuarks;
      vector<const reco::GenParticle*> bosons;
      const reco::Vertex* pVtx  = nullptr;; 
      const reco::BeamSpot* beamspot  = nullptr;;
      const pat::MET* met = nullptr;

      void resetEvent(){
	
	pVtx = nullptr;
	beamspot = nullptr;
	met = nullptr;

	jet_pts .clear();
	tagJet_pts.clear();
  
	selJets.clear();
	tagJets.clear();

	selMuons.clear();
	allMuons.clear();

	selElecs.clear();
	allElecs.clear();
  
	hT = 0;
	hT_noLep = 0;
	hT_jetID = 0;
	hT_jetID_noLep = 0;

	hT30 = 0;
	hT30_jetID = 0;


	mBB  = -1;
	pTBB = -1;
	bQuarks.clear();
	bosons .clear();

      }

      
    };

    eventData thisEvent;

    void getSelectedJets(edm::Handle<edm::View<pat::Jet> > jetsHandle);
    void getSelectedMuons(edm::Handle<pat::MuonCollection> muonsHandle, const reco::Vertex &pVtx);
    void getSelectedElectrons(edm::Handle<edm::View<pat::Electron> > elecsHandle, edm::Handle<reco::ConversionCollection> convHandle, edm::Handle<edm::ValueMap<bool> > eIDHandle);

    // Trigger Decisiosn
    void setEventLevelHLTFilterDecisions(const std::vector<bool>& L1word, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked, vector<string>& filterNames, vector<bool>& filterPassed);
    


    // counters
    unsigned int NEvents_all = 0;
    unsigned int NEvents_passLeptonPreSelection = 0;
    unsigned int NEvents_passHLTPreSelection = 0;
    unsigned int NEvents_passOfflinePreSelection = 0;

    struct jetHists {

      TH1F* h_pt;
      TH1F* h_pt_s;
      TH1F* h_phi;
      TH1F* h_eta;
      TH1F* h_deepFlavour;
      TH1F* h_deepCSV;
      TH1F* h_neutralHadronFrac;
      TH1F* h_neutralEMFrac;
      TH1F* h_chargedHadronEnergyFraction ;
      TH1F* h_muonEnergyFraction          ;
      TH1F* h_chargedEmEnergyFraction     ;
      TH1F* h_Constituents       ;
      TH1F* h_neutralMultiplicity;
      TH1F* h_chargedMultiplicity;
      TH1F* h_passJetID;
      TH1F* h_puID;

      jetHists(TFileDirectory& jetDir, string cutName ){
	h_pt          = jetDir.make<TH1F>( ("pt"+cutName).c_str()  , "p_{T}", 250,  0., 500. );
	h_pt_s        = jetDir.make<TH1F>( ("pt_s"+cutName).c_str()  , "p_{T}",200,  0., 100. );
	h_phi         = jetDir.make<TH1F>( ("phi"+cutName).c_str()  , "phi",  100,  -3.2, 3.2 );
	h_eta         = jetDir.make<TH1F>( ("eta"+cutName).c_str()  , "eta",  100,  -4, 4 );
	h_deepFlavour = jetDir.make<TH1F>( ("deepFlavour"+cutName).c_str()  , "deepFlavour",  100,  -0.1, 1.1 );
	h_deepCSV     = jetDir.make<TH1F>( ("deepCSV"+cutName).c_str()  , "deepCSV",  100,  -0.1, 1.1 );
	h_neutralHadronFrac = jetDir.make<TH1F>( ("neutralHadronFrac"+cutName).c_str()  , "neutralHadronFrac",  100,  -0.1, 1.1 );
	h_neutralEMFrac     = jetDir.make<TH1F>( ("neutralEMFrac"+cutName).c_str()  , "neutralEMFrac",  100,  -0.1, 1.1 );
	h_chargedHadronEnergyFraction  = jetDir.make<TH1F>( ("chargedHadronEnergyFraction"+cutName).c_str()  , "chargedHadronEnergyFraction",  100,  -0.1, 1.1 );
	h_muonEnergyFraction           = jetDir.make<TH1F>( ("muonEnergyFraction"+cutName).c_str()  , "muonEnergyFraction",  100,  -0.1, 1.1 );
	h_chargedEmEnergyFraction      = jetDir.make<TH1F>( ("chargedEmEnergyFraction"+cutName).c_str()  , "chargedEmEnergyFraction",  100,  -0.1, 1.1 );
	h_Constituents      = jetDir.make<TH1F>( ("Constituents"+cutName).c_str()  , "Constituents",  50,  -0.5, 49.5 );
	h_neutralMultiplicity  = jetDir.make<TH1F>( ("neutralMultiplicity"+cutName).c_str()  , "Constituents",  50,  -0.5, 49.5 );
	h_chargedMultiplicity  = jetDir.make<TH1F>( ("chargedMultiplicity"+cutName).c_str()  , "Constituents",  50,  -0.5, 49.5 );
	h_passJetID  = jetDir.make<TH1F>( ("passJetID"+cutName).c_str()  , "passJetID",  2,  -0.5, 1.5 );
	h_puID      = jetDir.make<TH1F>( ("puID"+cutName).c_str()  , "puID",  100,  -1.1, 1.1 );

      }



      void Fill(const pat::Jet* jet, float weight = 1.0 ){

	h_pt          ->Fill(jet->pt(), weight);
	h_pt_s        ->Fill(jet->pt(), weight);
	h_phi         ->Fill(jet->phi(), weight);
	h_eta         ->Fill(jet->eta(), weight);

	double deepFlavour = (jet->bDiscriminator("pfDeepFlavourJetTags:probb") + jet->bDiscriminator("pfDeepFlavourJetTags:probbb") + jet->bDiscriminator("pfDeepFlavourJetTags:problepb"));
	if(deepFlavour < 0) deepFlavour = -0.5;
	h_deepFlavour ->Fill(deepFlavour, weight);

	double deepCSV = (jet->bDiscriminator("pfDeepCSVJetTags:probb") + jet->bDiscriminator("pfDeepCSVJetTags:probbb")); 
	if(deepCSV < 0) deepCSV = -0.5;
	h_deepCSV      -> Fill(deepCSV, weight);

	h_neutralHadronFrac           -> Fill(jet->neutralHadronEnergyFraction(), weight);
	h_neutralEMFrac               -> Fill(jet->neutralEmEnergyFraction(), weight);
	h_chargedHadronEnergyFraction -> Fill(jet->chargedHadronEnergyFraction(), weight);
	h_muonEnergyFraction          -> Fill(jet->muonEnergyFraction() , weight);
	h_chargedEmEnergyFraction     -> Fill(jet->chargedEmEnergyFraction(), weight);
      
	h_Constituents         ->Fill(jet->chargedMultiplicity()+jet->neutralMultiplicity(), weight);
	h_neutralMultiplicity  ->Fill(jet->neutralMultiplicity(), weight);
	h_chargedMultiplicity  ->Fill(jet->chargedMultiplicity(), weight); 

	h_passJetID         ->Fill(CMSSWTools::passJetID(jet), weight);
	h_puID         ->Fill(jet->userFloat("pileupJetId:fullDiscriminant")  , weight);

	//      cout << " " << jet.pt()  << " " << jet.pt()*jet.jecFactor("Uncorrected") <<  " " << jet.userFloat("caloJetMap:pt") << " " << jet.userFloat("pileupJetId:fullDiscriminant")   << " " << jet.userFloat("pileupJetId:fullId") << endl;;

      }

    

    };



    struct muonHists {

      TH1F* h_pt;
      TH1F* h_pt_s;
      TH1F* h_phi;
      TH1F* h_eta;
      TH1F* h_passID;
      TH1F* h_relIso;

      muonHists(TFileDirectory& jetDir, string cutName ){
	h_pt          = jetDir.make<TH1F>( ("pt"+cutName).c_str()  , "p_{T}", 250,  0., 500. );
	h_pt_s        = jetDir.make<TH1F>( ("pt_s"+cutName).c_str()  , "p_{T}",200,  0., 100. );
	h_phi         = jetDir.make<TH1F>( ("phi"+cutName).c_str()  , "phi",  100,  -3.2, 3.2 );
	h_eta         = jetDir.make<TH1F>( ("eta"+cutName).c_str()  , "eta",  100,  -4, 4 );
	h_passID      = jetDir.make<TH1F>( ("passID"+cutName).c_str()  , "passID",  2,  -0.5, 1.5 );
	h_relIso      = jetDir.make<TH1F>( ("relIso"+cutName).c_str()  , "relIso",  100,  -0.1, 1.1 );
      }

      void Fill(const pat::Muon* muon, const reco::Vertex* pVtx, float weight = 1.0 ){
	h_pt          ->Fill(muon->pt(), weight);
	h_pt_s        ->Fill(muon->pt(), weight);
	h_phi         ->Fill(muon->phi(), weight);
	h_eta         ->Fill(muon->eta(), weight);

	//cf. https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2
	//bool isMedium(muon::isMediumMuon(mu));
	bool isTight(muon::isTightMuon(*muon,*pVtx));
	bool passID(isTight);
	h_passID   ->Fill(passID, weight);

	double nhIso   = muon->neutralHadronIso();
	double puchIso = muon->puChargedHadronIso();
	double chIso   = muon->chargedHadronIso() ;
	double gIso    = muon->photonIso() ;
	double relIso  = (TMath::Max(Float_t(nhIso+gIso-0.5*puchIso),Float_t(0.))+chIso)/muon->pt();
	h_relIso   ->Fill(relIso, weight);

      }

    

    };


    struct elecHists {

      TH1F* h_pt;
      TH1F* h_pt_s;
      TH1F* h_phi;
      TH1F* h_eta;
      TH1F* h_passID;
      TH1F* h_passConvID;
      TH1F* h_passPID;

      elecHists(TFileDirectory& jetDir, string cutName ){
	h_pt          = jetDir.make<TH1F>( ("pt"+cutName).c_str()  , "p_{T}", 250,  0., 500. );
	h_pt_s        = jetDir.make<TH1F>( ("pt_s"+cutName).c_str()  , "p_{T}",200,  0., 100. );
	h_phi         = jetDir.make<TH1F>( ("phi"+cutName).c_str()  , "phi",  100,  -3.2, 3.2 );
	h_eta         = jetDir.make<TH1F>( ("eta"+cutName).c_str()  , "eta",  100,  -4, 4 );
	h_passID      = jetDir.make<TH1F>( ("passID"+cutName).c_str()  , "passID",  2,  -0.5, 1.5 );
	h_passConvID      = jetDir.make<TH1F>( ("passConvID"+cutName).c_str()  , "passConvID",  2,  -0.5, 1.5 );
	h_passPID      = jetDir.make<TH1F>( ("passPID"+cutName).c_str()  , "passPID",  2,  -0.5, 1.5 );

      }

      void Fill(const pat::Electron* elec, const reco::BeamSpot* beamspot, float weight = 1.0 ){
	h_pt          ->Fill(elec->pt(), weight);
	h_pt_s        ->Fill(elec->pt(), weight);
	h_phi         ->Fill(elec->phi(), weight);
	h_eta         ->Fill(elec->eta(), weight);

	//cf. https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2
	//bool isMedium(muon::isMediumMuon(mu));
	//bool isTight(muon::isTightMuon(*muon,*pVtx));
	//bool passID(isTight);
	//h_passID   ->Fill(passID, weight);

	//// Conversion rejection
	//bool passConvVeto = !ConversionTools::hasMatchedConversion(elec,*convHandle,thisEvent.beamspot->position());
	//
	////cut-based electron id+iso
	////cf. https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
	//cout << "Getting electron ID " << endl;
	//bool passElectronID = (*eIDHandle)[el];
	//cout << "passElectronID: " << passElectronID << endl;
	//bool passID( passConvVeto && passElectronID);


      }

    

    };




    struct eventHists {

      TH1F* h_mBB      = nullptr;
      TH1F* h_pTBB     = nullptr;
      TH1F* h_nSelJets = nullptr;
      TH1F* h_nTagJets = nullptr;

      TH1F* h_nSelMuons = nullptr;
      TH1F* h_nAllMuons = nullptr;

      TH1F* h_nSelElecs = nullptr;
      TH1F* h_nAllElecs = nullptr;

      //TH1F* h_hT_s     = nullptr;    
      TH1F* h_hT       = nullptr;    
      TH1F* h_hT_l     = nullptr;    

      //TH1F* h_hT_noLep_s     = nullptr;    
      TH1F* h_hT_noLep       = nullptr;    
      TH1F* h_hT_noLep_l     = nullptr;    

      //TH1F* h_hT_jetID_s     = nullptr;    
      TH1F* h_hT_jetID       = nullptr;    
      TH1F* h_hT_jetID_l     = nullptr;    

      //TH1F* h_hT_jetID_noLep_s     = nullptr;    
      TH1F* h_hT_jetID_noLep       = nullptr;    
      TH1F* h_hT_jetID_noLep_l     = nullptr;    

      //TH1F* h_hT30_s   = nullptr;    
      TH1F* h_hT30     = nullptr;    
      TH1F* h_hT30_l   = nullptr;    

      //TH1F* h_hT30_jetID_s   = nullptr;    
      TH1F* h_hT30_jetID     = nullptr;    
      TH1F* h_hT30_jetID_l   = nullptr;    

      TH1F* h_met       = nullptr;    

      jetHists* h_selJets = nullptr;
      jetHists* h_tagJets = nullptr;
      jetHists* h_leadJet = nullptr;
      jetHists* h_sublJet = nullptr;
      jetHists* h_leadTag = nullptr;
      //jetHists* h_sublTag = nullptr;

      muonHists* h_allMuons = nullptr;
      muonHists* h_selMuons = nullptr;

      elecHists* h_allElecs = nullptr;
      elecHists* h_selElecs = nullptr;


      eventHists(edm::Service<TFileService>& fs, string cutName, bool isBBMC ){
	if(isBBMC){
	  h_mBB      = fs->make<TH1F>( ("mBB_"+cutName).c_str()  , "m_{BB}", 100,  0., 1000. );
	  h_pTBB     = fs->make<TH1F>( ("pTBB_"+cutName).c_str()  , "pT_{BB}", 100,  0., 1000. );
	}
	h_nSelJets = fs->make<TH1F>( ("nSelJet_"+cutName).c_str()  , "Selected Jet Multiplicity",  16,  -0.5, 15.5 );
	h_nSelMuons = fs->make<TH1F>( ("nSelMuons_"+cutName).c_str()  , "Selected Muon Multiplicity",  5,  -0.5, 4.5 );
	h_nAllMuons = fs->make<TH1F>( ("nAllMuons_"+cutName).c_str()  , "PreSelected Muon Multiplicity",  5,  -0.5, 4.5 );

	h_nSelElecs = fs->make<TH1F>( ("nSelElecs_"+cutName).c_str()  , "Selected Elec Multiplicity",  10,  -0.5, 9.5 );
	h_nAllElecs = fs->make<TH1F>( ("nAllElecs_"+cutName).c_str()  , "PreSelected Elec Multiplicity",  10,  -0.5, 9.5 );

	h_nTagJets = fs->make<TH1F>( ("nTagJet_"+cutName).c_str()  , "Tag Jet Multiplicity",  16,  -0.5, 15.5 );

	h_hT       = fs->make<TH1F>( ("hT_"+cutName).c_str()  , "hT",  200,  0, 1000 );
	h_hT_l     = fs->make<TH1F>( ("hT_l_"+cutName).c_str()  , "hT",  200,  0, 1000 );

	h_hT_noLep       = fs->make<TH1F>( ("hT_noLep_"+cutName).c_str()  , "hT",  200,  0, 1000 );
	h_hT_noLep_l     = fs->make<TH1F>( ("hT_noLep_l_"+cutName).c_str()  , "hT",  200,  0, 1000 );

	h_hT_jetID       = fs->make<TH1F>( ("hT_jetID_"+cutName).c_str()  , "hT",  200,  0, 1000 );
	h_hT_jetID_l     = fs->make<TH1F>( ("hT_jetID_l_"+cutName).c_str()  , "hT",  200,  0, 1000 );

	h_hT_jetID_noLep       = fs->make<TH1F>( ("hT_jetID_noLep_"+cutName).c_str()  , "hT",  200,  0, 1000 );
	h_hT_jetID_noLep_l     = fs->make<TH1F>( ("hT_jetID_noLep_l_"+cutName).c_str()  , "hT",  200,  0, 1000 );

	h_hT30     = fs->make<TH1F>( ("hT30_"+cutName).c_str()  , "hT (jets pt > 30 GeV)",  200,  0, 1000 );
	h_hT30_l   = fs->make<TH1F>( ("hT30_l_"+cutName).c_str()  , "hT (jets pt > 30 GeV)",  200,  0, 2000 );

	h_hT30_jetID     = fs->make<TH1F>( ("hT30_jetID_"+cutName).c_str()  , "hT (jets pt > 30 GeV)",  200,  0, 1000 );
	h_hT30_jetID_l   = fs->make<TH1F>( ("hT30_jetID_l_"+cutName).c_str()  , "hT (jets pt > 30 GeV)",  200,  0, 2000 );


	h_met       = fs->make<TH1F>( ("MeT_"+cutName).c_str()  , "MeT",  200,  0, 1000 );      

	TFileDirectory selJetsDir = fs->mkdir( "selJets" );
	TFileDirectory tagJetsDir = fs->mkdir( "tagJets" );
	TFileDirectory leadJetDir = fs->mkdir( "leadJet" );
	TFileDirectory sublJetDir = fs->mkdir( "sublJet" );
	TFileDirectory leadTagDir = fs->mkdir( "leadTag" );
	//TFileDirectory sublTagDir = fs->mkdir( "sublTag" );

	TFileDirectory allMuonDir = fs->mkdir( "allMuons" );
	TFileDirectory selMuonDir = fs->mkdir( "selMuons" );

	TFileDirectory allElecDir = fs->mkdir( "allElecs" );
	TFileDirectory selElecDir = fs->mkdir( "selElecs" );


	h_selJets = new jetHists(selJetsDir, "_"+cutName);
	h_tagJets = new jetHists(tagJetsDir, "_"+cutName);
	h_leadJet = new jetHists(leadJetDir, "_"+cutName);
	h_sublJet = new jetHists(sublJetDir, "_"+cutName);
	h_leadTag = new jetHists(leadTagDir, "_"+cutName);
	//h_sublTag = new jetHists(sublTagDir, "_"+cutName);

	h_allMuons = new muonHists(allMuonDir, "_"+cutName);
	h_selMuons = new muonHists(selMuonDir, "_"+cutName);

	h_allElecs = new elecHists(allElecDir, "_"+cutName);
	h_selElecs = new elecHists(selElecDir, "_"+cutName);

      }

      void Fill(const eventData& thisEvent, float weight = 1.0 ){
	if(h_mBB)  h_mBB      ->Fill(thisEvent.mBB,   weight);
	if(h_pTBB) h_pTBB     ->Fill(thisEvent.pTBB,  weight);
	h_nSelJets  ->Fill(thisEvent.selJets.size(),  weight);
	h_nTagJets  ->Fill(thisEvent.tagJets.size(),  weight);
	h_nSelMuons ->Fill(thisEvent.selMuons.size(), weight);
	h_nAllMuons ->Fill(thisEvent.allMuons.size(), weight);

	h_nSelElecs ->Fill(thisEvent.selElecs.size(), weight);
	h_nAllElecs ->Fill(thisEvent.allElecs.size(), weight);

	h_hT               ->Fill(thisEvent.hT                  , weight);
	h_hT_l     	   ->Fill(thisEvent.hT                  , weight);
	h_hT_noLep   	   ->Fill(thisEvent.hT_noLep            , weight);
	h_hT_noLep_l 	   ->Fill(thisEvent.hT_noLep            , weight);
	h_hT_jetID     	   ->Fill(thisEvent.hT_jetID            , weight);
	h_hT_jetID_l   	   ->Fill(thisEvent.hT_jetID            , weight);
	h_hT_jetID_noLep   ->Fill(thisEvent.hT_jetID_noLep      , weight);
	h_hT_jetID_noLep_l ->Fill(thisEvent.hT_jetID_noLep      , weight);

	h_hT30             ->Fill(thisEvent.hT30                 , weight);
	h_hT30_l   	   ->Fill(thisEvent.hT30                 , weight);
	h_hT30_jetID  	   ->Fill(thisEvent.hT30_jetID            , weight);
	h_hT30_jetID_l     ->Fill(thisEvent.hT30_jetID            , weight);




	h_met       ->Fill(thisEvent.met->pt(),   weight);

	for(const pat::Jet* jet: thisEvent.selJets){
	  h_selJets->Fill(jet, weight);
	}

	for(const pat::Jet* jet: thisEvent.tagJets){
	  h_tagJets->Fill(jet, weight);
	}

	for(const pat::Muon* muon: thisEvent.allMuons){
	  h_allMuons->Fill(muon, thisEvent.pVtx, weight);
	}

	for(const pat::Muon* muon: thisEvent.selMuons){
	  h_selMuons->Fill(muon, thisEvent.pVtx, weight);
	}


	for(const pat::Electron* elec: thisEvent.allElecs){
	  h_allElecs->Fill(elec, thisEvent.beamspot, weight);
	}

	for(const pat::Electron* elec: thisEvent.selElecs){
	  h_selElecs->Fill(elec, thisEvent.beamspot, weight);
	}


	if(thisEvent.selJets.size() > 0) h_leadJet->Fill(thisEvent.selJets.at(0), weight);
	if(thisEvent.selJets.size() > 1) h_sublJet->Fill(thisEvent.selJets.at(1), weight);

	if(thisEvent.tagJets.size() > 0) h_leadTag->Fill(thisEvent.tagJets.at(0), weight);
	//if(tagJets.size() > 1) h_sublTag->Fill(tagJets.at(1), weight);

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

    vector<jetHists> hJets_num_pt100; 
    vector<jetHists> hJets_den_pt100; 

    vector<jetHists> hJets_num_jetID; 
    vector<jetHists> hJets_den_jetID; 

    void fillJetTurnOnPlots(edm::Handle<edm::View<pat::Jet> > jetsHandle, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked, const vector<string>& filterNames, const vector<bool>& filterPassed);
    bool checkDenEventFilter(const edm::ParameterSet& jetTurnOnInfo, const vector<string>& filterNames, const vector<bool>& filterPassed);
    bool checkEventFilter   (const string& targetName, const vector<string>& filterNames, const vector<bool>& filterPassed);
    bool tagJetFilterMatch(const edm::ParameterSet& jetTurnOnInfo, edm::Handle<edm::View<pat::Jet> > jetsHandle, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked, float probeEta, float probePhi);
    bool tagJetCut(const edm::ParameterSet& jetTurnOnInfo, edm::Handle<edm::View<pat::Jet> > jetsHandle, float probeEta, float probePhi);
    bool probeJetCut(const edm::ParameterSet& jetTurnOnInfo, edm::Handle<edm::View<pat::Jet> > jetsHandle, const pat::Jet& jet);
		     


    vector<string> L1Names_;
    vector<unsigned int> L1Indices_;  
    map<std::string, unsigned int> L1_NamesToPos;


    //
    //  Trigger Emulation
    //
    void setupTrigEmulator(std::string year);
    TriggerEmulator::TrigEmulatorTool* trigEmulatorDetails = nullptr;
    TriggerEmulator::TrigEmulatorTool* trigEmulator = nullptr;
    void doTrigEmulation();

    //
    // Truth Info
    //
    void fillTruthInfo(const edm::Event& iEvent);

  public:
    explicit TriggerStudy(const edm::ParameterSet& iPara);
    ~TriggerStudy(){ }
    void beginJob() override;
    void beginRun(edm::Run const&, edm::EventSetup const&) override;
    void endJob() override;
    void analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)override;

  };


}


#endif // TrigEmulator_H
