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


HLT_Ht330_4j_3b = cms.PSet(hltPath= cms.string("HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v"),
                           L1Paths = cms.vstring("L1_ETT2000","L1_HTT360er","L1_HTT320er_QuadJet_70_55_40_40_er2p4"),
                           )


HLT_2j116_dEta1p6_2b = cms.PSet(hltPath=cms.string("HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71"),
                                L1Paths = cms.vstring("L1_DoubleJet112er2p3_dEta_Max1p6", "L1_DoubleJet150er2p5"),
                                )

HLT_J330_m30_2b = cms.PSet(hltPath=cms.string("HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02"),
                           L1Paths = cms.vstring("L1_SingleJet180"),
                           )

HLT_4j_103_88_75_15_2b_VBF1 = cms.PSet(hltPath=cms.string("HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1"),
                                       L1Paths = cms.vstring("L1_SingleJet180", "L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5"),
                                       )

HLT_2j300 = cms.PSet(hltPath=cms.string("HLT_DiPFJetAve300_HFJEC_v"),
                     L1Paths = cms.vstring("L1_SingleJet160er2p5", "L1_SingleJet180"),
                     )

HLT_j500 = cms.PSet(hltPath=cms.string("HLT_PFJet500_v"),  
                    L1Paths = cms.vstring("L1_SingleJet160er2p5", "L1_SingleJet180"),
                    )

HLT_ht1050 = cms.PSet(hltPath=cms.string("HLT_PFHT1050_v"),  
                      L1Paths = cms.vstring("L1_HTT360er","L1_HTT320er_QuadJet_70_55_40_40_er2p4"),
                      )


triggersToStudy = cms.VPSet(
    
    cms.PSet(name=cms.string("Ht330_4j_3b"),
             requireOR=cms.VPSet(HLT_Ht330_4j_3b)
         ),

    cms.PSet(name=cms.string("2b100_all"),
             requireOR=cms.VPSet(HLT_2j116_dEta1p6_2b)
         ),


    cms.PSet(name=cms.string("2j116_dEta1p6_2b"),
             requireOR=cms.VPSet(HLT_2j116_dEta1p6_2b),
             vetoOR=cms.VPSet(HLT_Ht330_4j_3b),
         ),

    cms.PSet(name=cms.string("Ht330_4j_3b_OR_2j116_2b"),
             requireOR=cms.VPSet(HLT_Ht330_4j_3b, HLT_2j116_dEta1p6_2b)
         ),                            
    
    cms.PSet(name=cms.string("2j300"),
             requireOR=cms.VPSet(HLT_2j300),
             vetoOR=cms.VPSet(HLT_Ht330_4j_3b, HLT_2j116_dEta1p6_2b),
         ),

    cms.PSet(name=cms.string("J330_m30_2b"),
             requireOR=cms.VPSet(HLT_J330_m30_2b),
             vetoOR=cms.VPSet(HLT_Ht330_4j_3b, HLT_2j116_dEta1p6_2b),
         ),
    
    cms.PSet(name=cms.string("4j_103_88_75_15_2b_VBF1"),
             requireOR=cms.VPSet(HLT_4j_103_88_75_15_2b_VBF1),
             vetoOR=cms.VPSet(HLT_Ht330_4j_3b, HLT_2j116_dEta1p6_2b),
         ),
    
    cms.PSet(name=cms.string("j500"),
             requireOR=cms.VPSet(HLT_j500),
             vetoOR=cms.VPSet(HLT_Ht330_4j_3b, HLT_2j116_dEta1p6_2b),
         ),
    
    cms.PSet(name=cms.string("ht1050"),
             requireOR=cms.VPSet(HLT_ht1050),
             vetoOR=cms.VPSet(HLT_Ht330_4j_3b, HLT_2j116_dEta1p6_2b),
         ),
    
    cms.PSet(name=cms.string("OR"),
             requireOR=cms.VPSet(HLT_Ht330_4j_3b, HLT_2j116_dEta1p6_2b, HLT_ht1050 ),
    ),                            

)

triggerCombStudy.triggersToPlot = triggersToStudy
