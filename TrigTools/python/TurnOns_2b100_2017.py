import FWCore.ParameterSet.Config as cms

         #hltL1DoubleJet100er2p3dEtaMax1p6Ior112er2p3dEtaMax1p6
L1NameMC = "hltL1DoubleJet100er2p3dEtaMax1p6Ior112er2p3dEtaMax1p6" # MC 
L1Name   = "hltL1DoubleJet100er2p3dEtaMax1p6*" # DAta

#
#  Jet trigger turn ons
#
jetTurnOnConfig =  cms.VPSet(
        cms.PSet(numFilterMatch = cms.string(L1Name),
             histName = cms.string("L1100"),
         ),

    cms.PSet(numFilterMatch = cms.string(L1Name),
             histName = cms.string("L1100DenMatch"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"), 
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
             numPtCut = cms.double(100),
             #denEventFilter = cms.string("hltL1sSingleJet60"),
             denJetMatch = cms.string("hltL1sSingleJet60"),
         ),
    

    cms.PSet(numFilterMatch = cms.string(L1Name),
             histName = cms.string("L1100TandPDenMatch"),
             denEventFilter = cms.string(L1Name),
             denJetMatch = cms.string("hltL1sSingleJet60"),
             tagFilterMatch = cms.string(L1Name),
             tagFilterMin = cms.uint32(2)
         ),


    #
    #  Calo 100
    #
    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100"),
             denEventFilter = cms.string(L1Name),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100DenMatch"),
             denEventFilter = cms.string(L1Name),
             denJetMatch = cms.string(L1Name),
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
    cms.PSet(numFilterMatch = cms.string("hltBTagCalo80x6CSVp0p92DoubleWithMatching"),
             histName = cms.string("CaloDeepCSV0p7MatchTrueB"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCalo80x6CSVp0p92DoubleWithMatching"), 
             histName = cms.string("CaloDeepCSV0p7MatchTrueBtag"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("trueBtag"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCalo80x6CSVp0p92DoubleWithMatching"), 
             histName = cms.string("CaloDeepCSV0p7MatchBtag"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCalo80x6CSVp0p92DoubleWithMatching"), 
             histName = cms.string("CaloDeepCSV0p7MatchBtagDenMatch"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"),
             denJetMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             probeCut = cms.string("Btag"),
         ),

    #
    #  PFJet 100
    #

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets100Eta2p3"), 
             histName = cms.string("PFJets100"),
             denEventFilter = cms.string("hltBTagCalo80x6CSVp0p92DoubleWithMatching"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets100Eta2p3"), 
             histName = cms.string("PFJets100DenMatch"),
             denEventFilter = cms.string("hltBTagCalo80x6CSVp0p92DoubleWithMatching"),
             denJetMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
         ),

    #
    #  DR
    #
    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets100Eta2p3MaxDeta1p6"), 
             histName = cms.string("PFJets100Dr"),
             denEventFilter = cms.string("hltDoublePFJets100Eta2p3"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoublePFJets100Eta2p3MaxDeta1p6"), 
             histName = cms.string("PFJets100DrDenMatch"),
             denEventFilter = cms.string("hltDoublePFJets100Eta2p3"),
             denJetMatch = cms.string("hltDoublePFJets100Eta2p3"),
         ),



)



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_2b100 =  cms.VPSet(
    cms.PSet(filterNamesOR = cms.vstring(L1Name,L1NameMC),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),
    
        cms.PSet(filterName = cms.string("hltDoubleCaloBJets100eta2p3"),
                 histName = cms.string("2Calo100"),
                 mult = cms.uint32(2),
                 pt = cms.double(-1.0)),
    
        cms.PSet(filterName = cms.string("hltBTagCalo80x6CSVp0p92DoubleWithMatching"),
                 histName = cms.string("2CaloBTags"),
                 mult = cms.uint32(2),
                 pt = cms.double(-1)),
    
        cms.PSet(filterName = cms.string("hltDoublePFJets100Eta2p3"),
                 histName = cms.string("2PF100"),
                 mult = cms.uint32(2),
                 pt = cms.double(100)),
    
        cms.PSet(filterName = cms.string("hltDoublePFJets100Eta2p3MaxDeta1p6"),
                 histName = cms.string("2PF100dR"),
                 mult = cms.uint32(1),
                 pt = cms.double(100)),
    
)



#
#  L1 Requirements
#
triggerConfigL1Unprescaled_L1_2b100 = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_DoubleJet100er2p3_dEta_Max1p6"),
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
