// -*- C++ -*-
#if !defined(TriggerStudy_H)
#define TriggerStudy_H


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

    // Event Data
    void resetEvent();
    unsigned int nSelectedJets = 0;
    unsigned int nTaggedJetsMed = 0;
    unsigned int nTaggedJets = 0;


    vector<float> jet_pts;
    vector<float> tagJet_pts;
  
    vector<const pat::Jet*> selJets;
    vector<const pat::Jet*> tagJets;
  
    float hT = 0;
    float hT30 = 0;

    // Trigger Decisiosn
    void setEventLevelHLTFilterDecisions(const std::vector<bool>& L1word, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked, vector<string>& filterNames, vector<bool>& filterPassed);
    


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

      void Fill(double mBB, double pTBB, unsigned int nSelJets, double hT, double hT30, vector<const pat::Jet*> selJets, vector<const pat::Jet*> tagJets, float weight = 1.0 ){
	if(h_mBB)  h_mBB      ->Fill(mBB, weight);
	if(h_pTBB) h_pTBB     ->Fill(pTBB, weight);
	h_nSelJets ->Fill(nSelJets, weight);
	h_hT       ->Fill(hT, weight);
	h_hT30     ->Fill(hT30, weight);
	h_hT30_l     ->Fill(hT30, weight);

	for(const pat::Jet* jet: selJets){
	  h_selJets->Fill(jet, weight);
	}

	for(const pat::Jet* jet: tagJets){
	  h_tagJets->Fill(jet, weight);
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

    vector<jetHists> hJets_num_pt100; 
    vector<jetHists> hJets_den_pt100; 

    vector<jetHists> hJets_num_jetID; 
    vector<jetHists> hJets_den_jetID; 

    void fillJetTurnOnPlots(edm::Handle<edm::View<pat::Jet> > jetsHandle, const vector<pat::TriggerObjectStandAlone>& trigObjsUnpacked, const vector<string>& filterNames, const vector<bool>& filterPassed);
    bool checkDenEventFilter(const edm::ParameterSet& jetTurnOnInfo, const vector<string>& filterNames, const vector<bool>& filterPassed);
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
    float mBB  = -1;
    float pTBB = -1;
    vector<const reco::GenParticle*> bQuarks;
    vector<const reco::GenParticle*> bosons;
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
