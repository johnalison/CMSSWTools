import FWCore.ParameterSet.Config as cms
#
#  Base config with the nominal options (customized below)
#
triggerEmulation = cms.EDAnalyzer("TriggerStudy",           
                                  isMC = cms.bool(False),
                                  isBBMC = cms.bool(False),
                                  testL1 = cms.bool(False),
                                  doEmulation = cms.bool(True),
                                  trigObjs = cms.InputTag("slimmedPatTrigger"),
                                  trigResults = cms.InputTag("TriggerResults","","HLT"),
                                  filtersToPass = cms.VPSet(),
                                  triggersToPlot = cms.VPSet(),
                                  jetTurnOns = cms.VPSet(),
                                  hltPreSelection = cms.vstring(),
                                  offlinePreSelection = cms.PSet(),
                                  pathsToPass = cms.vstring(""),
                                  year = cms.string("2016"),
                                  jets = cms.InputTag("slimmedJets"),
                                  L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                  truthJets = cms.InputTag("slimmedGenJets"),
                                  truthParts = cms.InputTag("prunedGenParticles"),
                                  AlgInputTag = cms.InputTag("gtStage2Digis"),
)



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfigEMU = cms.VPSet(
    
    # HT300_4j_3b
    cms.PSet(histName = cms.string("L1ORAll")),
    cms.PSet(histName = cms.string("4Calo45")), 
    cms.PSet(histName = cms.string("3CaloBtags")),
    cms.PSet(histName = cms.string("4j_3b")),

    cms.PSet(histName = cms.string("2b100_L1ORAll")),
    cms.PSet(histName = cms.string("2b100_2Calo100")),
    cms.PSet(histName = cms.string("2b100_2CaloBTags")),
    cms.PSet(histName = cms.string("2b100_2PF100")),
    cms.PSet(histName = cms.string("2b100")),

    cms.PSet(histName = cms.string("2j_2j_3b_L1ORAll")),
    cms.PSet(histName = cms.string("2j_2j_3b_4Calo30")),
    cms.PSet(histName = cms.string("2j_2j_3b_2Calo90")),
    cms.PSet(histName = cms.string("2j_2j_3b_3CaloBTags")),
    cms.PSet(histName = cms.string("2j_2j_3b_4PF30")),
    cms.PSet(histName = cms.string("2j_2j_3b")),

    cms.PSet(histName = cms.string("HLT_OR")),



)




triggerEmulation.filtersToPass = triggerConfigEMU
