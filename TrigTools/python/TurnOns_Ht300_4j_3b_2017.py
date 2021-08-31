import FWCore.ParameterSet.Config as cms



#L1Name = "hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"
#L1Name = "hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet" # Data ?
L1Name  = "hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet" # MC
#L1NameMiniAOD = "hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet"
L1Name2017C = "hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet"



#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(
    cms.PSet(numFilterMatch = cms.string("hltQuadCentralJet30"),
             histName = cms.string("Calo30"),
             denEventFilter = cms.string("L1ORAll"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp05Double"), 
             histName = cms.string("CaloDeepCSV"),
             denEventFilter = cms.string("hltCaloQuadJet30HT300"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp05Double"), 
             histName = cms.string("CaloDeepCSVDenMatch"),
             denEventFilter = cms.string("hltCaloQuadJet30HT300"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp05Double"), 
             histName = cms.string("CaloDeepCSVMatchBtag"),
             denEventFilter = cms.string("hltCaloQuadJet30HT300"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp05Double"), 
             histName = cms.string("CaloDeepCSVMatchBtagDenMatch"),
             denEventFilter = cms.string("hltCaloQuadJet30HT300"),
             denJetMatch = cms.string("hltQuadCentralJet30"),
             probeCut = cms.string("Btag"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloCSVp05Double"), 
             histName = cms.string("CaloDeepCSVMatchTrueB"),
             denEventFilter = cms.string("hltCaloQuadJet30HT300"),
             probeCut = cms.string("trueB"),
         ),

    #
    # PF30
    #
    cms.PSet(numFilterMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
             histName = cms.string("PF30"),
             denEventFilter = cms.string("hltBTagCaloCSVp05Double"), 
         ),

    cms.PSet(numFilterMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
             histName = cms.string("PF30DenMatch"),
             denEventFilter = cms.string("hltBTagCaloCSVp05Double"), 
             denJetMatch = cms.string("hltQuadCentralJet30"),
         ),

    
    #
    #  PF75
    #
    cms.PSet(numFilterMatch = cms.string("hlt1PFCentralJetLooseID75"),
             histName = cms.string("PF75"),
             denEventFilter = cms.string("hltPFCentralJetLooseIDQuad30"), 
         ),

    cms.PSet(numFilterMatch = cms.string("hlt1PFCentralJetLooseID75"),
             histName = cms.string("PF75DenMatch"),
             denEventFilter = cms.string("hltPFCentralJetLooseIDQuad30"), 
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),

    
    #
    #  PF60
    #
    cms.PSet(numFilterMatch = cms.string("hlt2PFCentralJetLooseID60"),
             histName = cms.string("PF60"),
             denEventFilter = cms.string("hlt1PFCentralJetLooseID75"), 
         ),

    cms.PSet(numFilterMatch = cms.string("hlt2PFCentralJetLooseID60"),
             histName = cms.string("PF60DenMatch"),
             denEventFilter = cms.string("hlt1PFCentralJetLooseID75"), 
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),
    

    #
    #  PF45
    #
    cms.PSet(numFilterMatch = cms.string("hlt3PFCentralJetLooseID45"),
             histName = cms.string("PF45"),
             denEventFilter = cms.string("hlt2PFCentralJetLooseID60"),
         ),

    cms.PSet(numFilterMatch = cms.string("hlt3PFCentralJetLooseID45"),
             histName = cms.string("PF45DenMatch"),
             denEventFilter = cms.string("hlt2PFCentralJetLooseID60"),
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),

    
    #
    #  PF40
    #
    cms.PSet(numFilterMatch = cms.string("hlt4PFCentralJetLooseID40"),
             histName = cms.string("PF40"),
             denEventFilter = cms.string("hlt3PFCentralJetLooseID45"),
         ),

    cms.PSet(numFilterMatch = cms.string("hlt4PFCentralJetLooseID40"),
             histName = cms.string("PF40DenMatch"),
             denEventFilter = cms.string("hlt3PFCentralJetLooseID45"),
             denJetMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
         ),

    #
    #  PFDeepCSV
    #
    cms.PSet(numFilterMatch = cms.string("hltBTagPFCSVp070Triple"),
             histName = cms.string("PFDeepCSV"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT300"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagPFCSVp070Triple"),
             histName = cms.string("PFDeepCSVMatchBtag"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT300"),
             probeCut = cms.string("Btag"),
         ),


    cms.PSet(numFilterMatch = cms.string("hltBTagPFCSVp070Triple"),
             histName = cms.string("PFDeepCSVMatchBtagDenMatch"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT300"),
             denJetMatch = cms.string("hlt4PFCentralJetLooseID40"),
             probeCut = cms.string("Btag"),
         ),



    cms.PSet(numFilterMatch = cms.string("hltBTagPFCSVp070Triple"),
             histName = cms.string("PFDeepCSVMatchTrueB"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT300"),
             denJetMatch = cms.string("hlt4PFCentralJetLooseID40"),
             probeCut = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagPFCSVp070Triple"),
             histName = cms.string("PFDeepCSVMatchTrueBtag"),
             denEventFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT300"),
             denJetMatch = cms.string("hlt4PFCentralJetLooseID40"),
             probeCut = cms.string("trueBtag"),
         ),


    )



#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_Ht300_4j_3b = cms.VPSet(

    cms.PSet(filterNamesOR = cms.vstring(L1Name,L1Name2017C),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),
   
    cms.PSet(filterName = cms.string("hltQuadCentralJet30"),
             histName = cms.string("4Calo30"),
             mult = cms.uint32(4),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltCaloQuadJet30HT300"), 
             histName = cms.string("CaloHt300"),
             mult = cms.uint32(1),
             pt = cms.double(300)),

    cms.PSet(filterName = cms.string("hltBTagCaloCSVp05Double"), 
             histName = cms.string("2CaloBTags"),
             mult = cms.uint32(2),
             pt = cms.double(-1)),

    cms.PSet(filterName = cms.string("hltPFCentralJetLooseIDQuad30"),
             histName = cms.string("4PF30"),
             mult = cms.uint32(4),
             pt = cms.double(30)),
    
    cms.PSet(filterName = cms.string("hlt1PFCentralJetLooseID75"),
             histName = cms.string("1PF75"),
             mult = cms.uint32(1),
             pt = cms.double(75)),
    
    cms.PSet(filterName = cms.string("hlt2PFCentralJetLooseID60"),
             histName = cms.string("2PF60"),
             mult = cms.uint32(2),
             pt = cms.double(60)),
    
    cms.PSet(filterName = cms.string("hlt3PFCentralJetLooseID45"),
             histName = cms.string("3PF45"),
             mult = cms.uint32(3),
             pt = cms.double(45)),
    
    cms.PSet(filterName = cms.string("hlt4PFCentralJetLooseID40"),
             histName = cms.string("4PF40"),
             mult = cms.uint32(4),
             pt = cms.double(40)),
    
    cms.PSet(filterName = cms.string("hltPFCentralJetsLooseIDQuad30HT300"),
             histName = cms.string("PFHt300"),
             mult = cms.uint32(1),
             pt = cms.double(300)),
    
    cms.PSet(filterName = cms.string("hltBTagPFCSVp070Triple"),
             histName = cms.string("3PFBtags"),
             mult = cms.uint32(3),
             pt = cms.double(-1)),
)


#
#  L1 Requirements
#
def make_triggerConfigL1Unprescaled_L1_Ht300_4j_3b(isMC=False):
    if isMC:
        L1Names = cms.vstring( "L1_QuadJet60er2p7", "L1_HTT380er", "L1_HTT280er_QuadJet_70_55_40_35_er2p5")
    else:
        L1Names = cms.vstring( "L1_QuadJet60er3p0", "L1_HTT380er", "L1_HTT280er_QuadJet_70_55_40_35_er2p5")
    return cms.VPSet(cms.PSet(L1Names = L1Names,
                              histName = cms.string("passL1"),
                              mult = cms.uint32(1),
                              pt = cms.double(-1.0))
    )

def make_triggerConfigL1Unprescaled_Ht300_4j_3b(isMC=False):
    triggerConfigL1Unprescaled_L1_Ht300_4j_3b = make_triggerConfigL1Unprescaled_L1_Ht300_4j_3b(isMC)
    triggerConfigL1Unprescaled_Ht300_4j_3b = triggerConfigL1Unprescaled_L1_Ht300_4j_3b.copy()
    triggerConfigL1Unprescaled_Ht300_4j_3b.extend(triggerConfig_Ht300_4j_3b)
    return triggerConfigL1Unprescaled_Ht300_4j_3b




#
#  Base config with the nominal options (customized below)
#
triggerStudyBase_Ht300_4j_3b = cms.EDAnalyzer("TriggerStudy",           
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
