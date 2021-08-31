import FWCore.ParameterSet.Config as cms

         #hltL1DoubleJet100er2p3dEtaMax1p6Ior112er2p3dEtaMax1p6
L1NameMC = "hltL1DoubleJet100er2p3dEtaMax1p6Ior112er2p3dEtaMax1p6" # MC 
L1Name   = "hltL1DoubleJet100er2p3dEtaMax1p6" # DAta

#
#  Jet trigger turn ons
#
def make_jetTurnOnConfig(isMC=False):

    thisL1 = L1NameMC if isMC else L1Name

    return cms.VPSet(
        cms.PSet(numFilterMatch = cms.string(thisL1),
             histName = cms.string("L1100"),
         ),

    cms.PSet(numFilterMatch = cms.string(thisL1),
             histName = cms.string("L1100DenMatch"),
             denEventFilter = cms.string("hltDoubleCaloBJets100eta2p3"), 
         ),

    cms.PSet(numFilterMatch = cms.string(thisL1),
             histName = cms.string("L1100TandP"),
             denEventFilter = cms.string(thisL1),
             tagFilterMatch = cms.string(thisL1),
             tagFilterMin = cms.uint32(2)
         ),

    cms.PSet(numFilterMatch = cms.string("hltL1sSingleJet60"),
             histName = cms.string("L1100PtReq"),
             numPtName = cms.string("hltL1sSingleJet60"),
             numPtCut = cms.double(100),
             #denEventFilter = cms.string("hltL1sSingleJet60"),
             denJetMatch = cms.string("hltL1sSingleJet60"),
         ),
    

    cms.PSet(numFilterMatch = cms.string(thisL1),
             histName = cms.string("L1100TandPDenMatch"),
             denEventFilter = cms.string(thisL1),
             denJetMatch = cms.string("hltL1sSingleJet60"),
             tagFilterMatch = cms.string(thisL1),
             tagFilterMin = cms.uint32(2)
         ),


    #
    #  Calo 100
    #
    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100"),
             denEventFilter = cms.string(thisL1),
         ),

    cms.PSet(numFilterMatch = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("Calo100DenMatch"),
             denEventFilter = cms.string(thisL1),
             denJetMatch = cms.string(thisL1),
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
def make_triggerConfig_2b100(isMC=False):

    thisL1 = L1NameMC if isMC else L1Name

    return cms.VPSet(
        cms.PSet(filterName = cms.string(thisL1),
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

def make_triggerConfigL1Unprescaled_2b100(isMC=False):
    triggerConfigL1Unprescaled_2b100 = triggerConfigL1Unprescaled_L1_2b100.copy()
    triggerConfigL1Unprescaled_2b100.extend(make_triggerConfig_2b100(isMC))
    return triggerConfigL1Unprescaled_2b100



#
#  Base config with the nominal options (customized below)
#
def make_triggerStudyBase_2b100(isMC=False):
    triggerStudyBase_2b100 = cms.EDAnalyzer("TriggerStudy",           
                                            isMC = cms.bool(False),
                                            isBBMC = cms.bool(False),
                                            testL1 = cms.bool(False),
                                            doEmulation = cms.bool(False),
                                            trigObjs = cms.InputTag("slimmedPatTrigger"),
                                            trigResults = cms.InputTag("TriggerResults","","HLT"),
                                            filtersToPass = cms.VPSet(),
                                            triggersToPlot = cms.VPSet(),
                                            jetTurnOns = make_jetTurnOnConfig(isMC),
                                            hltPreSelection = cms.vstring(),
                                            offlinePreSelection = cms.PSet(),
                                            pathsToPass = cms.vstring(),
                                            jets = cms.InputTag("slimmedJets"),
                                            L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                            truthJets = cms.InputTag("slimmedGenJets"),
                                            truthParts = cms.InputTag("prunedGenParticles"),
                                            AlgInputTag = cms.InputTag("gtStage2Digis"),
    )
