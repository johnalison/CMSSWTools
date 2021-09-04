import FWCore.ParameterSet.Config as cms

def addTurnOn(pt, matchBtag=False, isCalo=False):
    turnOn = cms.PSet()
    
    histName = "PF"+str(pt)
    if isCalo: histName = "Calo"+str(pt)
    histName += "inMJ"

    if matchBtag:
        histName += "MatchBtag"
    histName += "TandP"

    jetFilter = "hltPFCentralJetLooseIDQuad30"
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


def addBTagTurnOn(matchBtag=False, isCalo=False, isTrueB=False, is2b100=False):
    turnOn = cms.PSet()
    
    histName = "PFCSV"
    if isCalo: histName = "CaloCSV"
    histName += "inMJ"

    if is2b100: histName += "2b100"

    if matchBtag:
        histName += "MatchBtag"

    if isTrueB:
        histName += "TrueB"

    histName += "TandP"

    numFilter       = "hltBTagPFCSVp070Triple"
    denJetMatch    = "hlt4PFCentralJetLooseID40"
    denEventFilter = "hltPFCentralJetsLooseIDQuad30HT300"
    if isCalo: 
        if is2b100:
            numFilter = "hltBTagCalo80x6CSVp0p92DoubleWithMatching"
            denJetMatch = "hltDoubleCaloBJets100eta2p3"
            denEventFilter = "hltDoubleCaloBJets100eta2p3"
        else:
            numFilter = "hltBTagCaloCSVp05Double"
            denJetMatch = "hltQuadCentralJet30"
            denEventFilter = "hltCaloQuadJet30HT300"

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


def add2b100L1TurnOn(matchBtag=False, doMaxDEta=False):
    turnOn = cms.PSet()
    
    histName = "L12b100"
    histName += "inMJ"
    if doMaxDEta: histName += "maxDEta"

    if matchBtag:
        histName += "MatchBtag"
    histName += "TandP"

    jetFilter = "hltL1DoubleJet100er2p3dEtaMax1p6*"

    turnOn.histName = cms.string(histName)
    turnOn.numFilterMatch = cms.string(jetFilter)

    turnOn.tagCut = cms.string("Btag")
    turnOn.tagFilterMatch = cms.string(jetFilter)
    turnOn.tagFilterMin = cms.uint32(1)

    if doMaxDEta: turnOn.tagFilterMaxDEta = cms.double(1.6)
            
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")

    return turnOn






#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet()

#
#  PF 30
#
for pfPt in [30,40,45,60,75,100]:
    jetTurnOnConfig.append(addTurnOn(pfPt))
    jetTurnOnConfig.append(addTurnOn(pfPt, matchBtag=True))


#
#  Calo 30
#
for caloPt in [30,100]:
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True))
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True, matchBtag=True))


jetTurnOnConfig.append(add2b100L1TurnOn())
jetTurnOnConfig.append(add2b100L1TurnOn(matchBtag=True))

jetTurnOnConfig.append(add2b100L1TurnOn(doMaxDEta = True ))
jetTurnOnConfig.append(add2b100L1TurnOn(doMaxDEta = True, matchBtag=True))



#
#  PF BTags
#
jetTurnOnConfig.append(addBTagTurnOn())
jetTurnOnConfig.append(addBTagTurnOn(matchBtag=True))


#
# Calo BTags
#
jetTurnOnConfig.append(addBTagTurnOn(isCalo=True))
jetTurnOnConfig.append(addBTagTurnOn(isCalo=True, matchBtag=True))

jetTurnOnConfig.append(addBTagTurnOn(is2b100=True, isCalo=True))
jetTurnOnConfig.append(addBTagTurnOn(is2b100=True, isCalo=True, matchBtag=True))


#
#  MC True
#
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True))
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True, matchBtag=True))
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True, isCalo=True))
jetTurnOnConfig.append(addBTagTurnOn(isTrueB=True, isCalo=True, matchBtag=True))


#print "jetTurnOnConfig is" 
#print jetTurnOnConfig.dumpPython()



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

    cms.PSet(filterName = cms.string("hltCaloQuadJet30HT300"), # Calo Ht > 320"),
             histName = cms.string("CaloHt300"),
             mult = cms.uint32(1),
             pt = cms.double(300)),

    
    cms.PSet(filterName = cms.string("hltPFCentralJetsLooseIDQuad30HT300"),
             histName = cms.string("PFHt300"),
             mult = cms.uint32(1),
             pt = cms.double(300)),

    cms.PSet(filterName = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("2Calo100"),
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
                                                   #jets = cms.InputTag("slimmedJets"),
                                                   L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                                   truthJets = cms.InputTag("slimmedGenJets"),
                                                   truthParts = cms.InputTag("prunedGenParticles"),
                                                   AlgInputTag = cms.InputTag("gtStage2Digis"),
)
