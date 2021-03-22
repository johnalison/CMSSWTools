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



HLT_Ht300_4j_3b = cms.PSet(hltPath= cms.string("HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v"),
                           L1Paths = cms.vstring("L1_QuadJet60er3p0", "L1_HTT380er", "L1_HTT280er_QuadJet_70_55_40_35_er2p5"),
                           )


HLT_2j100_dEta1p6_2b = cms.PSet(hltPath=cms.string("HLT_DoublePFJets100MaxDeta1p6_DoubleCaloBTagCSV_p33_v"),
                                L1Paths = cms.vstring("L1_DoubleJet100er2p3_dEta_Max1p6"),
                                )


triggersToStudy = cms.VPSet(
    
    cms.PSet(name=cms.string("Ht300_4j_3b"),
             requireOR=cms.VPSet(HLT_Ht300_4j_3b),
         ),

    cms.PSet(name=cms.string("2j110_dEta1p6_2b"),
             requireOR=cms.VPSet(HLT_2j100_dEta1p6_2b),
             vetoOR=cms.VPSet(HLT_Ht300_4j_3b),
         ),

    cms.PSet(name=cms.string("Ht300_4j_3b_OR_2j100_2b"),
             requireOR=cms.VPSet(HLT_Ht300_4j_3b, HLT_2j100_dEta1p6_2b)
         ),                            
    
)

triggerCombStudy.triggersToPlot = triggersToStudy
