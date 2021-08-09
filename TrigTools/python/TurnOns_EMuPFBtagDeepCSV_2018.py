import FWCore.ParameterSet.Config as cms

#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(
    #cms.PSet(numFilterMatch = cms.string("hltQuadCentralJet30"),
    #         histName = cms.string("Calo30"),
    #         denEventFilter = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
    #     ),

    cms.PSet(numFilterMatch = cms.string("hltPFJetFilterTwoC30"),
             histName = cms.string("PF30"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
         ),

    cms.PSet(histName = cms.string("PF30Test"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(30.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
         ),


    cms.PSet(histName = cms.string("PF30TandP"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(30.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
             tagCut = cms.string("Btag"),
         ),



    cms.PSet(histName = cms.string("PF40"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(40.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
         ),

    cms.PSet(histName = cms.string("PF40TandP"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(40.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
             tagCut = cms.string("Btag"),
         ),




    cms.PSet(histName = cms.string("PF45"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(45.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
         ),

    cms.PSet(histName = cms.string("PF45TandP"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(45.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
             tagCut = cms.string("Btag"),
         ),



    cms.PSet(histName = cms.string("PF60"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(60.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
         ),

    cms.PSet(histName = cms.string("PF60TandP"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(60.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
             tagCut = cms.string("Btag"),
         ),

    
    cms.PSet(histName = cms.string("PF75"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(75.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
         ),

    cms.PSet(histName = cms.string("PF75TandP"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(75.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
             tagCut = cms.string("Btag"),
         ),




    cms.PSet(histName = cms.string("PF116"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(116.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
         ),

    cms.PSet(histName = cms.string("PF116TandP"),
             denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             numPtCut = cms.double(116.),
             numPtName = cms.string("hltPFJetFilterTwoC30"),
             tagCut = cms.string("Btag"),
         ),




    #
    #  The BTags
    #
    cms.PSet(histName = cms.string("PFDeepCSV"),
             numFilterMatch = cms.string("hltBTagPFDeepCSV1p5Single"),
             denEventFilter = cms.string("hltPFJetFilterTwoC30"),
             denJetMatch    = cms.string("hltPFJetFilterTwoC30"),
         ),


    cms.PSet(histName = cms.string("PFDeepCSVTandP"),
             numFilterMatch = cms.string("hltBTagPFDeepCSV1p5Single"),
             denEventFilter = cms.string("hltPFJetFilterTwoC30"),
             denJetMatch    = cms.string("hltPFJetFilterTwoC30"),
             tagCut = cms.string("Btag"),
         ),


    cms.PSet(histName = cms.string("PFDeepCSVMatchBtag"),
             numFilterMatch = cms.string("hltBTagPFDeepCSV1p5Single"),
             denEventFilter = cms.string("hltPFJetFilterTwoC30"),
             denJetMatch    = cms.string("hltPFJetFilterTwoC30"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(histName = cms.string("PFDeepCSVMatchBtagTandP"),
             numFilterMatch = cms.string("hltBTagPFDeepCSV1p5Single"),
             denEventFilter = cms.string("hltPFJetFilterTwoC30"),
             denJetMatch    = cms.string("hltPFJetFilterTwoC30"),
             probeCut = cms.string("Btag"),
             tagCut = cms.string("Btag"),
         ),


    cms.PSet(histName = cms.string("PFDeepCSVMatchBtagDenMatch"),
             numFilterMatch = cms.string("hltBTagPFDeepCSV1p5Single"),
             denEventFilter = cms.string("hltPFJetFilterTwoC30"),
             denJetMatch    = cms.string("hltPFJetFilterTwoC30"),
             probeCut = cms.string("Btag"),
         ),

    cms.PSet(histName = cms.string("PFDeepCSVMatchTrueB"),
             numFilterMatch = cms.string("hltBTagPFDeepCSV1p5Single"),
             denEventFilter = cms.string("hltPFJetFilterTwoC30"),
             denJetMatch    = cms.string("hltPFJetFilterTwoC30"),
             probeCut = cms.string("trueB"),
         ),


    cms.PSet(histName = cms.string("PFDeepCSVMatchTrueBtag"),
             numFilterMatch = cms.string("hltBTagPFDeepCSV1p5Single"),
             denEventFilter = cms.string("hltPFJetFilterTwoC30"),
             denJetMatch    = cms.string("hltPFJetFilterTwoC30"),
             probeCut = cms.string("trueBtag"),
         ),





    )



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_EMuPFBtagDeepCSV = cms.VPSet(

    cms.PSet(filterName = cms.string("hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             histName = cms.string("EMu"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),
    

    cms.PSet(filterName = cms.string("hltPFJetFilterTwoC30"),
             histName = cms.string("2PF30"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltBTagPFDeepCSV1p5Single"),
             histName = cms.string("2PFBTag"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),


)





#
#  Base config with the nominal options (customized below)
#
triggerStudyBase_EMuPFBtagDeepCSV = cms.EDAnalyzer("TriggerStudy",           
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
