import FWCore.ParameterSet.Config as cms

#
#  Base config with the nominal options (customized below)
#
triggerCombStudy = cms.EDAnalyzer("TriggerStudy",           
                                  isMC = cms.bool(False),
                                  isBBMC = cms.bool(False),
                                  testL1 = cms.bool(False),
                                  doEmulation = cms.bool(False),
                                  trigObjs = cms.InputTag("slimmedPatTrigger"),
                                  trigResults = cms.InputTag("TriggerResults","","HLT"),
                                  filtersToPass = cms.VPSet(),
                                  triggersToPlot = cms.VPSet(),
                                  jetTurnOns = cms.VPSet(),
                                  hltPreSelection = cms.vstring(),
                                  offlinePreSelection = cms.PSet(),
                                  pathsToPass = cms.vstring(),
                                  jets = cms.InputTag("slimmedJets"),
                                  L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                  truthJets = cms.InputTag("slimmedGenJets"),
                                  truthParts = cms.InputTag("prunedGenParticles"),
                                  AlgInputTag = cms.InputTag("gtStage2Digis"),
)





#
#  OLD
#
HLT_4j_3b = cms.PSet(hltPath= cms.string("HLT_QuadJet45_TripleBTagCSV_p087_v"),
                     L1Paths = cms.vstring("L1_QuadJetC50", "L1_HTT300"),
                 )


HLT_2j_2j_3b = cms.PSet(hltPath = cms.string("HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v"),
                        L1Paths = cms.vstring("L1_HTT300","L1_SingleJet170","L1_DoubleJetC100"),
                    )


HLT_2b100 = cms.PSet(hltPath=cms.string("HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v"),
                     L1Paths = cms.vstring("L1_DoubleJetC100","L1_SingleJet200"),
)



triggersToStudy = cms.VPSet(
    
    cms.PSet(name=cms.string("4j_3b"),
             requireOR=cms.VPSet(HLT_4j_3b),
         ),

    cms.PSet(name=cms.string("2b100_all"),
             requireOR=cms.VPSet(HLT_2b100),
         ),

    cms.PSet(name=cms.string("2j_2j_3b_all"),
             requireOR=cms.VPSet(HLT_2j_2j_3b),
         ),


    #
    #  one 
    #
    cms.PSet(name=cms.string("2b100"),
             requireOR=cms.VPSet(HLT_2b100),
             vetoOR=cms.VPSet(HLT_4j_3b),
         ),

    cms.PSet(name=cms.string("2j_2j_3b"),
             requireOR=cms.VPSet(HLT_2j_2j_3b),
             vetoOR=cms.VPSet(HLT_4j_3b),
         ),

    #
    #  2 
    #
    cms.PSet(name=cms.string("2b100_vs_All"),
             requireOR=cms.VPSet(HLT_2b100),
             vetoOR=cms.VPSet(HLT_4j_3b,HLT_2j_2j_3b ),
         ),

    
    cms.PSet(name=cms.string("2j_2j_3b_vs_All"),
             requireOR=cms.VPSet(HLT_2j_2j_3b),
             vetoOR=cms.VPSet(HLT_4j_3b, HLT_2b100),
         ),

    #
    #  All 3
    #
    cms.PSet(name=cms.string("OR"),
             requireOR=cms.VPSet(HLT_4j_3b, HLT_2b100, HLT_2j_2j_3b),
         ),                            
    
)

triggerCombStudy.triggersToPlot = triggersToStudy
