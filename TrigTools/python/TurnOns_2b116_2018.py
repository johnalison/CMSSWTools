import FWCore.ParameterSet.Config as cms

#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(
    cms.PSet(numFilterMatch = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             histName = cms.string("L1112"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             histName = cms.string("L1112DenMatch"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"), 
         ),

    cms.PSet(numFilterMatch = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             histName = cms.string("L1112TandP"),
             denEventFilter = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             tagFilterMatch = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             tagFilterMin = cms.uint32(2)
         ),

    cms.PSet(numFilterMatch = cms.string("hltL1sSingleJet60"),
             histName = cms.string("L1112PtReq"),
             numPtName = cms.string("hltL1sSingleJet60"),
             numPtCut = cms.double(112),
             #denEventFilter = cms.string("hltL1sSingleJet60"),
             denJetMatch = cms.string("hltL1sSingleJet60"),
         ),
    

    cms.PSet(numFilterMatch = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             histName = cms.string("L1112TandPDenMatch"),
             denEventFilter = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             denJetMatch = cms.string("hltL1sSingleJet60"),
             tagFilterMatch = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             tagFilterMin = cms.uint32(2)
         ),


    #
    #  Calo 100
    #
    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100"),
             denEventFilter = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100DenMatch"),
             denEventFilter = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             denJetMatch = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
         ),



    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100TandP"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             tagFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             tagFilterMin = cms.uint32(2)
         ),



    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100TandPDenMatch"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             denJetMatch = cms.string("hltL1sSingleJet60"),
             tagFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             tagFilterMin = cms.uint32(2)
         ),


    #
    #  Calo BTag
    #
    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"), 
             histName = cms.string("CaloDeepCSV0p7MatchTrueB"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"), 
             histName = cms.string("CaloDeepCSV0p7MatchTrueBtag"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("trueBtag"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"), 
             histName = cms.string("CaloDeepCSV0p7MatchBtag"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"), 
             histName = cms.string("CaloDeepCSV0p7MatchBtagDenMatch"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             denJetMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("Btag"),
         ),

    #
    #  PFJet 116
    #

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets116Eta2p3"), 
             histName = cms.string("PFJets116"),
             denEventFilter = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets116Eta2p3"), 
             histName = cms.string("PFJets116DenMatch"),
             denEventFilter = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"),
             denJetMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
         ),

    #
    #  DR
    #
    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets116Eta2p3MaxDeta1p6"), 
             histName = cms.string("PFJets116Dr"),
             denEventFilter = cms.string("hltDoublePFJets116Eta2p3"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets116Eta2p3MaxDeta1p6"), 
             histName = cms.string("PFJets116DrDenMatch"),
             denEventFilter = cms.string("hltDoublePFJets116Eta2p3"),
             denJetMatch = cms.string("hltDoublePFJets116Eta2p3"),
         ),



    )



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_2b116 = cms.VPSet(
    cms.PSet(filterName = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("2Calo100"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"), 
             histName = cms.string("2CaloBTags"),
             mult = cms.uint32(2),
             pt = cms.double(-1)),

    cms.PSet(filterName = cms.string("hltDoublePFJets116Eta2p3"),
             histName = cms.string("2PF116"),
             mult = cms.uint32(2),
             pt = cms.double(116)),

    cms.PSet(filterName = cms.string("hltDoublePFJets116Eta2p3MaxDeta1p6"),
             histName = cms.string("2PF116dR"),
             mult = cms.uint32(1),
             pt = cms.double(116)),

)


#
#  L1 Requirements
#


triggerConfigL1Unprescaled_L1_2b116 = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_DoubleJet112er2p3_dEta_Max1p6", "L1_DoubleJet150er2p5"),
                                                         histName = cms.string("passL1"),
                                                         mult = cms.uint32(1),
                                                         pt = cms.double(-1.0))
)
triggerConfigL1Unprescaled_2b116 = triggerConfigL1Unprescaled_L1_2b116.copy()
triggerConfigL1Unprescaled_2b116.extend(triggerConfig_2b116)



#
#  Base config with the nominal options (customized below)
#
triggerStudyBase_2b116 = cms.EDAnalyzer("TriggerStudy",           
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
