import FWCore.ParameterSet.Config as cms

def addTurnOn(pt, matchBtag=False, isCalo=False):
    turnOn = cms.PSet()
    
    histName = "PF"+str(pt)
    if isCalo: histName = "Calo"+str(pt)
    histName += "inMJ"

    if matchBtag:
        histName += "MatchBtag"
    histName += "TandP"

    jetFilter = "hltQuadPFCentralJetLooseID30"
    if isCalo: jetFilter = "hltQuadCentralJet30"

    turnOn.histName = cms.string(histName)
    turnOn.numPtCut = cms.double(float(pt))
    turnOn.numPtName = cms.string(jetFilter)
    turnOn.tagCut = cms.string("Btag")
    turnOn.tagFilterMatch = cms.string(jetFilter)
    turnOn.tagFilterMin = cms.uint32(1)
    
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")

    return turnOn


def addTurnOnFilterMatch(name, numFilter, denFilter, tagFilter, matchBtag=False):
    turnOn = cms.PSet()
    
    histName = name
    histName += "filter"

    if matchBtag:
        histName += "MatchBtag"

    histName += "TandP"
    
    turnOn.histName = cms.string(histName)
    turnOn.numFilterMatch = cms.string(numFilter)
    turnOn.denEventFilter = cms.string(denFilter)

    turnOn.tagCut = cms.string("Btag")
    turnOn.tagFilterMatch = cms.string(tagFilter)
    turnOn.tagFilterMin = cms.uint32(1)
    
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")

    return turnOn



def addBTagTurnOn(matchBtag=False, isTrueB=False, is2b100=False):
    turnOn = cms.PSet()
    
    histName = "CaloCSV"
    histName += "inMJ"

    if is2b100: histName += "2b100"

    if matchBtag:
        histName += "MatchBtag"

    if isTrueB:
        histName += "TrueB"

    histName += "TandP"

    if is2b100:
        numFilter = "hltBTagCaloCSVp014DoubleWithMatching"
        denJetMatch = "hltDoubleJetsC100"
        denEventFilter = "hltDoubleJetsC100"
    else:
        numFilter = "hltBTagCaloCSVp087Triple"
        denJetMatch = "hltQuadCentralJet45"
        denEventFilter = "hltQuadCentralJet45"

    turnOn.histName = cms.string(histName)
    turnOn.numFilterMatch = cms.string(numFilter)
    turnOn.denJetMatch    = cms.string(denJetMatch)
    turnOn.denEventFilter    = cms.string(denEventFilter)
    turnOn.tagCut = cms.string("Btag")
    
        
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")
        if isTrueB: turnOn.probeCut = cms.string("trueBBtag")
    elif isTrueB:
        turnOn.probeCut = cms.string("trueB")

    return turnOn



def add2b100L1TurnOn(matchBtag=False):
    turnOn = cms.PSet()
    
    histName = "L12b100"
    histName += "inMJ"

    if matchBtag:
        histName += "MatchBtag"
    histName += "TandP"

    jetFilter = "hltL1sDoubleJetC100IorDoubleJetC112IorDoubleJetC120IorSingleJet200"

    turnOn.histName = cms.string(histName)
    turnOn.numFilterMatch = cms.string(jetFilter)

    turnOn.tagCut = cms.string("Btag")
    turnOn.tagFilterMatch = cms.string(jetFilter)
    turnOn.tagFilterMin = cms.uint32(1)
    
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")

    return turnOn






#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet()

#
#  PF 
#
for pfPt in [30,45,90,100]:
    jetTurnOnConfig.append(addTurnOn(pfPt))
    jetTurnOnConfig.append(addTurnOn(pfPt, matchBtag=True))



for turnOnPair in [
        # 4j_3b
        ("Calo45",   "hltQuadCentralJet45",                 "hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF", "hltQuadCentralJet45"),
        ("PF45",     "hltPFCentralJetLooseIDQuad30",        "hltBTagCaloCSVp087Triple"                               , "hltQuadCentralJet45"),

        # 2b100
        ("Calo100",  "hltDoubleJetsC100",              "hltL1sDoubleJetC100IorDoubleJetC112IorDoubleJetC120IorSingleJet200"   , "hltDoubleJetsC100"),
        ("PF100",    "hltDoublePFJetsC100",            "hltBTagCaloCSVp014DoubleWithMatching", "hltDoubleJetsC100"),
        ("PF100Dr",  "hltDoublePFJetsC100MaxDeta1p6",  "hltDoublePFJetsC100"           ,  "hltDoubleJetsC100"),   
        
        # 2j_2j_3b
        ("Calo30",   "hltQuadCentralJet30",                 "hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet", "hltQuadCentralJet30"),
        ("Calo90",   "hltDoubleCentralJet90",               "hltQuadCentralJet30",                               "hltQuadCentralJet30"),
        ("PF30",     "hltQuadPFCentralJetLooseID30",        "hltBTagCaloCSVp087Triple"                         , "hltQuadCentralJet30"),
        ("PF90",     "hltDoublePFCentralJetLooseID90",      "hltQuadPFCentralJetLooseID30"                     , "hltQuadCentralJet30"),

]:


    jetTurnOnConfig.append(addTurnOnFilterMatch(turnOnPair[0], turnOnPair[1], turnOnPair[2], turnOnPair[3] ))
    jetTurnOnConfig.append(addTurnOnFilterMatch(turnOnPair[0], turnOnPair[1], turnOnPair[2], turnOnPair[3],  matchBtag=True))



#
#  Calo 
#
for caloPt in [30,45,90,100]:
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True))
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True, matchBtag=True))


jetTurnOnConfig.append(add2b100L1TurnOn())
jetTurnOnConfig.append(add2b100L1TurnOn(matchBtag=True))


#
# Calo BTags
#
jetTurnOnConfig.append(addBTagTurnOn())
jetTurnOnConfig.append(addBTagTurnOn(matchBtag=True))

jetTurnOnConfig.append(addBTagTurnOn(is2b100=True, ))
jetTurnOnConfig.append(addBTagTurnOn(is2b100=True, matchBtag=True))


#
#  MC True
#
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True))
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True, matchBtag=True))
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True))
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True, matchBtag=True))


#print "jetTurnOnConfig is" 
#print jetTurnOnConfig.dumpPython()

#L1Name = "hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF"

#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfig_EMuPFBtagDeepCSV = cms.VPSet(

#    cms.PSet(filterName = cms.string("hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23"),
#             histName = cms.string("L1ORAll"),
#             mult = cms.uint32(1),
#             pt = cms.double(-1.0)),
#
#    cms.PSet(filterName = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
#             histName = cms.string("EMu"),
#             mult = cms.uint32(1),
#             pt = cms.double(-1.0)),
#



    cms.PSet(filterName = cms.string("hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltL1sDoubleJetC100IorDoubleJetC112IorDoubleJetC120IorSingleJet200"),
             histName = cms.string("L1ORAll_2b"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),



    cms.PSet(filterName = cms.string("hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet"),
             histName = cms.string("L1ORAll_2j_2j_3b"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("3CaloBtags"),
             mult = cms.uint32(3),
             pt = cms.double(-1)),


    cms.PSet(filterName = cms.string("hltQuadCentralJet45"),
             histName = cms.string("4Calo45"),
             mult = cms.uint32(4),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltDoubleJetsC100"),
             histName = cms.string("2Calo100"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),


    cms.PSet(filterName = cms.string("hltBTagCaloCSVp014DoubleWithMatching"),
             histName = cms.string("2CaloBTags"),
             mult = cms.uint32(2),
             pt = cms.double(-1)),

    cms.PSet(filterName = cms.string("hltDoublePFJetsC100"),
             histName = cms.string("2PF100"),
             mult = cms.uint32(2),
             pt = cms.double(100)),


    cms.PSet(filterName = cms.string("hltQuadCentralJet30"),
             histName = cms.string("4Calo30"),
             mult = cms.uint32(4),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltDoubleCentralJet90"),
             histName = cms.string("2Calo90"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),
    
    cms.PSet(filterName = cms.string("hltBTagCaloCSVp087Triple"),
             histName = cms.string("3CaloBtags"),
             mult = cms.uint32(3),
             pt = cms.double(-1)),
    
    cms.PSet(filterName = cms.string("hltQuadPFCentralJetLooseID30"),
             histName = cms.string("4PF30"),
             mult = cms.uint32(4),
             pt = cms.double(30)),


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
                                                   #jets = cms.InputTag("slimmedJets"),
                                                   L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                                   truthJets = cms.InputTag("slimmedGenJets"),
                                                   truthParts = cms.InputTag("prunedGenParticles"),
                                                   AlgInputTag = cms.InputTag("gtStage2Digis"),
)
