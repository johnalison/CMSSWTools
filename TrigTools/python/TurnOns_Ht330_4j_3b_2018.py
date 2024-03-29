import FWCore.ParameterSet.Config as cms

#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(
    cms.PSet(numFilterMatch = cms.string("hltQuadCentralJet30"),
             histName = cms.string("Calo30"),
             denEventFilter = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSV"),
             denEventFilter = cms.string("hltCaloQuadJet30HT320"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSVDenMatch"),
             denEventFilter = cms.string("hltCaloQuadJet30HT320"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSVMatchBtag"),
             denEventFilter = cms.string("hltCaloQuadJet30HT320"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSVMatchBtagDenMatch"),
             denEventFilter = cms.string("hltCaloQuadJet30HT320"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSVMatchTrueB"),
             denEventFilter = cms.string("hltCaloQuadJet30HT320"),
             probeCut = cms.string("trueB"),
         ),

    #
    # PF30
    #
    cms.PSet(numFilterMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
             histName = cms.string("PF30"),
             denEventFilter = cms.string("hltBTagCaloDeepCSVp17Double"), 
         ),

    cms.PSet(numFilterMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
             histName = cms.string("PF30DenMatch"),
             denEventFilter = cms.string("hltBTagCaloDeepCSVp17Double"), 
             denJetMatch = cms.string("hltQuadCentralJet30"),
         ),

    
    #
    #  PF75
    #
    cms.PSet(numFilterMatch = cms.string("hlt1PFCentralJetLooseID75"),
             histName = cms.string("PF75"),
             denEventFilter = cms.string("hltPFCentralJetLooseIDQuad30"), 
         ),

    cms.PSet(numFilterMatch = cms.string("hlt1PFCentralJetLooseID75"),
             histName = cms.string("PF75DenMatch"),
             denEventFilter = cms.string("hltPFCentralJetLooseIDQuad30"), 
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),

    
    #
    #  PF60
    #
    cms.PSet(numFilterMatch = cms.string("hlt2PFCentralJetLooseID60"),
             histName = cms.string("PF60"),
             denEventFilter = cms.string("hlt1PFCentralJetLooseID75"), 
         ),

    cms.PSet(numFilterMatch = cms.string("hlt2PFCentralJetLooseID60"),
             histName = cms.string("PF60DenMatch"),
             denEventFilter = cms.string("hlt1PFCentralJetLooseID75"), 
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),
    

    #
    #  PF45
    #
    cms.PSet(numFilterMatch = cms.string("hlt3PFCentralJetLooseID45"),
             histName = cms.string("PF45"),
             denEventFilter = cms.string("hlt2PFCentralJetLooseID60"),
         ),

    cms.PSet(numFilterMatch = cms.string("hlt3PFCentralJetLooseID45"),
             histName = cms.string("PF45DenMatch"),
             denEventFilter = cms.string("hlt2PFCentralJetLooseID60"),
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),

    
    #
    #  PF40
    #
    cms.PSet(numFilterMatch = cms.string("hlt4PFCentralJetLooseID40"),
             histName = cms.string("PF40"),
             denEventFilter = cms.string("hlt3PFCentralJetLooseID45"),
         ),

    cms.PSet(numFilterMatch = cms.string("hlt4PFCentralJetLooseID40"),
             histName = cms.string("PF40DenMatch"),
             denEventFilter = cms.string("hlt3PFCentralJetLooseID45"),
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),

    #
    #  PFDeepCSV
    #
    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSV"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSVMatchBtag"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSVMatchBtagDenMatch"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             denJetMatch = cms.string("hlt4PFCentralJetLooseID40"),
             probeCut = cms.string("Btag"),
         ),



    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSVMatchTrueB"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             denJetMatch = cms.string("hlt4PFCentralJetLooseID40"),
             probeCut = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSVMatchTrueBtag"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             denJetMatch = cms.string("hlt4PFCentralJetLooseID40"),
             probeCut = cms.string("trueBtag"),
         ),


    )



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_Ht330_4j_3b = cms.VPSet(
    cms.PSet(filterName = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltQuadCentralJet30"),
             histName = cms.string("4Calo30"),
             mult = cms.uint32(4),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltCaloQuadJet30HT320"), # Calo Ht > 320"),
             histName = cms.string("CaloHt320"),
             mult = cms.uint32(1),
             pt = cms.double(320)),

    cms.PSet(filterName = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("2CaloBTags"),
             mult = cms.uint32(2),
             pt = cms.double(-1)),

    cms.PSet(filterName = cms.string("hltPFCentralJetLooseIDQuad30"),
             histName = cms.string("4PF30"),
             mult = cms.uint32(4),
             pt = cms.double(30)),
    
    cms.PSet(filterName = cms.string("hlt1PFCentralJetLooseID75"),
             histName = cms.string("1PF75"),
             mult = cms.uint32(1),
             pt = cms.double(75)),
    
    cms.PSet(filterName = cms.string("hlt2PFCentralJetLooseID60"),
             histName = cms.string("2PF60"),
             mult = cms.uint32(2),
             pt = cms.double(60)),
    
    cms.PSet(filterName = cms.string("hlt3PFCentralJetLooseID45"),
             histName = cms.string("3PF45"),
             mult = cms.uint32(3),
             pt = cms.double(45)),
    
    cms.PSet(filterName = cms.string("hlt4PFCentralJetLooseID40"),
             histName = cms.string("4PF40"),
             mult = cms.uint32(4),
             pt = cms.double(40)),
    
    cms.PSet(filterName = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             histName = cms.string("PFHt330"),
             mult = cms.uint32(1),
             pt = cms.double(330)),
    
    cms.PSet(filterName = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("3PFBtags"),
             mult = cms.uint32(3),
             pt = cms.double(-1)),
)


#
#  L1 Requirements
#
triggerConfigL1HTQuadJet_L1_Ht330_4j_3b = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT320er_QuadJet_70_55_40_40_er2p4"),
                                                histName = cms.string("passL1"),
                                                mult = cms.uint32(1),
                                                pt = cms.double(-1.0))
                                   )
triggerConfigL1HTQuadJet_Ht330_4j_3b = triggerConfigL1HTQuadJet_L1_Ht330_4j_3b.copy()
triggerConfigL1HTQuadJet_Ht330_4j_3b.extend(triggerConfig_Ht330_4j_3b)

triggerConfigL1HT_L1_Ht330_4j_3b = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT360er"),
                                                      histName = cms.string("passL1"),
                                                      mult = cms.uint32(1),
                                                      pt = cms.double(-1.0)),
)
triggerConfigL1HT_Ht330_4j_3b = triggerConfigL1HT_L1_Ht330_4j_3b.copy()
triggerConfigL1HT_Ht330_4j_3b.extend(triggerConfig_Ht330_4j_3b)


#triggerConfigL1HTQuadJetOrHT = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT320er_QuadJet_70_55_40_40_er2p4","L1_HTT360er"),
#                                                  histName = cms.string("passL1"),
#                                                  mult = cms.uint32(1),
#                                                  pt = cms.double(-1.0)),
#                                     )
#triggerConfigL1HTQuadJetOrHTHLT = triggerConfigL1HTQuadJetOrHT.copy()
#triggerConfigL1HTQuadJetOrHTHLT.extend(triggerConfigHLT)


triggerConfigL1Unprescaled_L1_Ht330_4j_3b = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_ETT2000","L1_HTT360er","L1_HTT320er_QuadJet_70_55_40_40_er2p4"),
                                                histName = cms.string("passL1"),
                                                mult = cms.uint32(1),
                                                pt = cms.double(-1.0))
                                   )
triggerConfigL1Unprescaled_Ht330_4j_3b = triggerConfigL1Unprescaled_L1_Ht330_4j_3b.copy()
triggerConfigL1Unprescaled_Ht330_4j_3b.extend(triggerConfig_Ht330_4j_3b)





#
#  Base config with the nominal options (customized below)
#
triggerStudyBase_Ht330_4j_3b = cms.EDAnalyzer("TriggerStudy",           
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
