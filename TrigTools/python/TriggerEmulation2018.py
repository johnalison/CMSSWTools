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
    
    # HT330_4j_3b
    cms.PSet(histName = cms.string("L1ORAll")),
    ##cms.PSet(histName = cms.string("4Calo30")),  ## Fully efficieny
    cms.PSet(histName = cms.string("CaloHt320")),
    #cms.PSet(histName = cms.string("2CaloBTags")), ## Fully efficieny for 4b presection
    cms.PSet(histName = cms.string("4PF30")), ## Fully efficieny for 4b presection
    cms.PSet(histName = cms.string("1PF75")),
    cms.PSet(histName = cms.string("2PF60")),
    cms.PSet(histName = cms.string("3PF45")),
    cms.PSet(histName = cms.string("4PF40")),
    cms.PSet(histName = cms.string("PFHt330")),
    #cms.PSet(histName = cms.string("3PFBtags")),
    cms.PSet(histName = cms.string("HT330_4j_3b")),

    cms.PSet(histName = cms.string("2b116_L1ORAll")),
    cms.PSet(histName = cms.string("2b116_2Calo100")),
    cms.PSet(histName = cms.string("2b116_2CaloBTags")),
    cms.PSet(histName = cms.string("2b116_2PF116")),
    cms.PSet(histName = cms.string("2b116")),

    cms.PSet(histName = cms.string("HLT_OR")),



)




triggerEmulation.filtersToPass = triggerConfigEMU
