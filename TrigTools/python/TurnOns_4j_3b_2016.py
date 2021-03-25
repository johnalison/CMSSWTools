import FWCore.ParameterSet.Config as cms

L1Name = "hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF"

#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(
    cms.PSet(numFilterMatch = cms.string("hltQuadCentralJet45"),
             histName = cms.string("Calo45"),
             denEventFilter = cms.string(L1Name),
         ),


    #
    #  CaloCSV
    #
    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSV"),
             denEventFilter = cms.string("hltQuadCentralJet45"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchBtag"),
             denEventFilter = cms.string("hltQuadCentralJet45"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchBtagDenMatch"),
             denEventFilter = cms.string("hltQuadCentralJet45"),
             denJetMatch = cms.string("hltQuadCentralJet45"),
             probeCut = cms.string("Btag"),
         ),



    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchTrueB"),
             denEventFilter = cms.string("hltQuadCentralJet45"),
             denJetMatch = cms.string("hltQuadCentralJet45"),
             probeCut = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("CaloCSVMatchTrueBtag"),
             denEventFilter = cms.string("hltQuadCentralJet45"),
             denJetMatch = cms.string("hltQuadCentralJet45"),
             probeCut = cms.string("trueBtag"),
         ),



    #
    #  PF45
    #
    cms.PSet(numFilterMatch = cms.string("hltQuadPFCentralJetLooseID45"),
             histName = cms.string("PF45"),
             denEventFilter = cms.string("hltBTagCaloCSVp087Triple"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltQuadPFCentralJetLooseID45"),
             histName = cms.string("PF45DenMatch"),
             denEventFilter = cms.string("hltBTagCaloCSVp087Triple"),
             denJetMatch = cms.string("hltQuadCentralJet45"),
         ),

    


)



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_4j_3b = cms.VPSet(

    cms.PSet(filterName = cms.string(L1Name),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltQuadCentralJet45"),
             histName = cms.string("4Calo45"),
             mult = cms.uint32(4),
             pt = cms.double(-1.0)),

    
    cms.PSet(filterName = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("3CaloBtags"),
             mult = cms.uint32(3),
             pt = cms.double(-1)),
    
    cms.PSet(filterName = cms.string("hltQuadPFCentralJetLooseID45"),
             histName = cms.string("4PF45"),
             mult = cms.uint32(4),
             pt = cms.double(45)),
    
)


#
#  L1 Requirements
#
triggerConfigL1Unprescaled_L1_4j_3b = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_QuadJetC50", "L1_HTT280"),
                                                               histName = cms.string("passL1"),
                                                               mult = cms.uint32(1),
                                                               pt = cms.double(-1.0))
                                   )
triggerConfigL1Unprescaled_4j_3b = triggerConfigL1Unprescaled_L1_4j_3b.copy()
triggerConfigL1Unprescaled_4j_3b.extend(triggerConfig_4j_3b)





#
#  Base config with the nominal options (customized below)
#
triggerStudyBase_4j_3b = cms.EDAnalyzer("TriggerStudy",           
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
