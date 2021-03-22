import FWCore.ParameterSet.Config as cms

L1Name = "hltL1sDoubleJetC100IorDoubleJetC112IorDoubleJetC120IorSingleJet200"

#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(
    cms.PSet(numFilterMatch = cms.string(L1Name),
             histName = cms.string("L1100"),
         ),

    cms.PSet(numFilterMatch = cms.string(L1Name),
             histName = cms.string("L1100DenMatch"),
             denEventFilter = cms.string("hltDoubleJetsC100"),
         ),

    cms.PSet(numFilterMatch = cms.string(L1Name),
             histName = cms.string("L1100TandP"),
             denEventFilter = cms.string(L1Name),
             tagFilterMatch = cms.string(L1Name),
             tagFilterMin = cms.uint32(2)
         ),

    cms.PSet(numFilterMatch = cms.string("hltL1sSingleJet60"),
             histName = cms.string("L1100PtReq"),
             numPtName = cms.string("hltL1sSingleJet60"),
             numPtCut = cms.double(110),
             #denEventFilter = cms.string("hltL1sSingleJet60"),
             denJetMatch = cms.string("hltL1sSingleJet60"),
         ),
    

    cms.PSet(numFilterMatch = cms.string(L1Name),
             histName = cms.string("L1112TandPDenMatch"),
             denEventFilter = cms.string(L1Name),
             denJetMatch = cms.string("hltL1sSingleJet60"),
             tagFilterMatch = cms.string(L1Name),
             tagFilterMin = cms.uint32(2)
         ),


    #
    #  Calo 100
    #
    cms.PSet(numFilterMatch = cms.string("hltDoubleJetsC100"),
             histName = cms.string("Calo100"),
             denEventFilter = cms.string(L1Name),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoubleJetsC100"),
             histName = cms.string("Calo100DenMatch"),
             denEventFilter = cms.string(L1Name),
             denJetMatch = cms.string(L1Name),
         ),



    cms.PSet(numFilterMatch = cms.string("hltDoubleJetsC100"),
             histName = cms.string("Calo100TandP"),
             denEventFilter = cms.string("hltDoubleJetsC100"),
             tagFilterMatch = cms.string("hltDoubleJetsC100"),
             tagFilterMin = cms.uint32(2)
         ),



    cms.PSet(numFilterMatch = cms.string("hltDoubleJetsC100"),
             histName = cms.string("Calo100TandPDenMatch"),
             denEventFilter = cms.string("hltDoubleJetsC100"),
             denJetMatch = cms.string("hltL1sSingleJet60"),
             tagFilterMatch = cms.string("hltDoubleJetsC100"),
             tagFilterMin = cms.uint32(2)
         ),


    #
    #  Calo BTag
    #
    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp014DoubleWithMatching"),
             histName = cms.string("CaloDeepCSV0p84MatchTrueB"),
             denEventFilter = cms.string("hltDoubleJetsC100"),
             probeCut = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp014DoubleWithMatching"), 
             histName = cms.string("CaloDeepCSV0p84MatchTrueBtag"),
             denEventFilter = cms.string("hltDoubleJetsC100"),
             probeCut = cms.string("trueBtag"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp014DoubleWithMatching"), 
             histName = cms.string("CaloDeepCSV0p84MatchBtag"),
             denEventFilter = cms.string("hltDoubleJetsC100"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp014DoubleWithMatching"), 
             histName = cms.string("CaloDeepCSV0p84MatchBtagDenMatch"),
             denEventFilter = cms.string("hltDoubleJetsC100"),
             denJetMatch = cms.string("hltDoubleJetsC100"),
             probeCut = cms.string("Btag"),
         ),

    #
    #  PFJet 100
    #

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJetsC100"), 
             histName = cms.string("PFJets100"),
             denEventFilter = cms.string("hltBTagCaloCSVp014DoubleWithMatching"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJetsC100"), 
             histName = cms.string("PFJets100DenMatch"),
             denEventFilter = cms.string("hltBTagCaloCSVp014DoubleWithMatching"),
             denJetMatch = cms.string("hltDoubleJetsC100"),
         ),

    #
    #  DR
    #
    cms.PSet(numFilterMatch = cms.string("hltDoublePFJetsC100MaxDeta1p6"), 
             histName = cms.string("PFJets100Dr"),
             denEventFilter = cms.string("hltDoublePFJetsC100"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJetsC100MaxDeta1p6"), 
             histName = cms.string("PFJets100DrDenMatch"),
             denEventFilter = cms.string("hltDoublePFJetsC100"),
             denJetMatch = cms.string("hltDoublePFJetsC100"),
         ),



    )



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_2b100 = cms.VPSet(
    cms.PSet(filterName = cms.string(L1Name),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),


    cms.PSet(filterName = cms.string("hltDoubleJetsC100"),
             histName = cms.string("2Calo100"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltBTagCaloCSVp014DoubleWithMatching"),
             histName = cms.string("2CaloBTags"),
             mult = cms.uint32(2),
             pt = cms.double(-1)),

    cms.PSet(filterName = cms.string("hltDoublePFJetsC100"),
             histName = cms.string("2PF100"),
             mult = cms.uint32(2),
             pt = cms.double(100)),

    cms.PSet(filterName = cms.string("hltDoublePFJetsC100MaxDeta1p6"),
             histName = cms.string("2PF100dR"),
             mult = cms.uint32(1),
             pt = cms.double(100)),

)


#
#  L1 Requirements
#

triggerConfigL1Unprescaled_L1_2b100 = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_DoubleJetC100","L1_SingleJet200"),
                                                         histName = cms.string("passL1"),
                                                         mult = cms.uint32(1),
                                                         pt = cms.double(-1.0))
)
triggerConfigL1Unprescaled_2b100 = triggerConfigL1Unprescaled_L1_2b100.copy()
triggerConfigL1Unprescaled_2b100.extend(triggerConfig_2b100)



#
#  Base config with the nominal options (customized below)
#
triggerStudyBase_2b100 = cms.EDAnalyzer("TriggerStudy",           
                                  isMC = cms.bool(False),
                                  isBBMC = cms.bool(False),
                                  testL1 = cms.bool(False),
                                  doEmulation = cms.bool(False),
                                  trigObjs = cms.InputTag("slimmedPatTrigger"),
                                  trigResults = cms.InputTag("TriggerResults","","HLT"),
                                  filtersToPass = cms.VPSet(),
                                  triggersToPlot = cms.VPSet(),
                                  jetTurnOns = jetTurnOnConfig,
                                  hltPreSelection = cms.vstring(),
                                  offlinePreSelection = cms.PSet(),
                                  pathsToPass = cms.vstring(),
                                  jets = cms.InputTag("slimmedJets"),
                                  L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                  truthJets = cms.InputTag("slimmedGenJets"),
                                  truthParts = cms.InputTag("prunedGenParticles"),
                                  AlgInputTag = cms.InputTag("gtStage2Digis"),
                              )
