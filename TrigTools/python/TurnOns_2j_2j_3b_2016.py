import FWCore.ParameterSet.Config as cms

L1Name = "hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet"

#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(

    #
    #  Calo 30
    #
    cms.PSet(numFilterMatch = cms.string("hltQuadCentralJet30"),
             histName = cms.string("Calo30"),
             denEventFilter = cms.string(L1Name),
         ),

    #
    # Calo 90
    #
    cms.PSet(numFilterMatch = cms.string("hltDoubleCentralJet90"),
             histName = cms.string("Calo90"),
             denEventFilter = cms.string("hltQuadCentralJet30"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoubleCentralJet90"),
             histName = cms.string("Calo90DenMatch"),
             denEventFilter = cms.string("hltQuadCentralJet30"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoubleCentralJet90"),
             histName = cms.string("Calo90TandP"),
             denEventFilter = cms.string("hltDoubleCentralJet90"),
             tagFilterMatch = cms.string("hltDoubleCentralJet90"),
             tagFilterMin = cms.uint32(2),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoubleCentralJet90"),
             histName = cms.string("Calo90TandPDenMatch"),
             denEventFilter = cms.string("hltDoubleCentralJet90"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
             tagFilterMatch = cms.string("hltDoubleCentralJet90"),
             tagFilterMin = cms.uint32(2),
         ),



    #
    #  CaloCSV
    #
    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSV"),
             denEventFilter = cms.string("hltDoubleCentralJet90"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchBtag"),
             denEventFilter = cms.string("hltDoubleCentralJet90"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchBtagDenMatch"),
             denEventFilter = cms.string("hltDoubleCentralJet90"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchTrueB"),
             denEventFilter = cms.string("hltDoubleCentralJet90"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
             probeCut = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchTrueBtag"),
             denEventFilter = cms.string("hltDoubleCentralJet90"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
             probeCut = cms.string("trueBtag"),
         ),



    #
    #  PF30
    #
    cms.PSet(numFilterMatch = cms.string("hltQuadPFCentralJetLooseID30"),
             histName = cms.string("PF30"),
             denEventFilter = cms.string("hltBTagCaloCSVp087Triple"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltQuadPFCentralJetLooseID30"),
             histName = cms.string("PF30DenMatch"),
             denEventFilter = cms.string("hltBTagCaloCSVp087Triple"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
         ),

    #
    #  PF90
    #
    cms.PSet(numFilterMatch = cms.string("hltDoublePFCentralJetLooseID90"),
             histName = cms.string("PF90"),
             denEventFilter = cms.string("hltQuadPFCentralJetLooseID30"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoublePFCentralJetLooseID90"),
             histName = cms.string("PF90DenMatch"),
             denEventFilter = cms.string("hltQuadPFCentralJetLooseID30"),
             denJetMatch = cms.string("hltQuadPFCentralJetLooseID30"),
         ),

    


)



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_2j_2j_3b = cms.VPSet(

    cms.PSet(filterName = cms.string(L1Name),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltQuadCentralJet30"),
             histName = cms.string("4Calo30"),
             mult = cms.uint32(4),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltDoubleCentralJet90"),
             histName = cms.string("2Calo90"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),
    
    cms.PSet(filterName = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("3CaloBtags"),
             mult = cms.uint32(3),
             pt = cms.double(-1)),
    
    cms.PSet(filterName = cms.string("hltQuadPFCentralJetLooseID30"),
             histName = cms.string("4PF30"),
             mult = cms.uint32(4),
             pt = cms.double(30)),

    cms.PSet(filterName = cms.string("hltDoublePFCentralJetLooseID90"),
             histName = cms.string("2PF90"),
             mult = cms.uint32(2),
             pt = cms.double(90)),

    
)


#
#  L1 Requirements
#
triggerConfigL1Unprescaled_L1_2j_2j_3b = cms.VPSet(cms.PSet(L1Name = cms.vstring("L1_HTT300","L1_SingleJet170","L1_DoubleJetC100"),
                                                         histName = cms.string("passL1"),
                                                         mult = cms.uint32(1),
                                                         pt = cms.double(-1.0))
                                   )
triggerConfigL1Unprescaled_2j_2j_3b = triggerConfigL1Unprescaled_L1_2j_2j_3b.copy()
triggerConfigL1Unprescaled_2j_2j_3b.extend(triggerConfig_2j_2j_3b)





#
#  Base config with the nominal options (customized below)
#
triggerStudyBase_2j_2j_3b = cms.EDAnalyzer("TriggerStudy",           
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
