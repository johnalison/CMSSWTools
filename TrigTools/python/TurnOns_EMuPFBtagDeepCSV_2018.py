import FWCore.ParameterSet.Config as cms

def addTurnOn(pt, matchBtag=False, isCalo=False):
    turnOn = cms.PSet()
    
    histName = "PF"+str(pt)
    if isCalo: histName = "Calo"+str(pt)

    if matchBtag:
        histName += "MatchBtag"
    histName += "TandP"

    jetFilter = "hltPFJetFilterTwoC30"
    if isCalo: jetFilter = "hltCaloJetFilterTwoC30"

    turnOn.histName = cms.string(histName)
    turnOn.denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter")
    turnOn.numPtCut = cms.double(float(pt))
    turnOn.numPtName = cms.string(jetFilter)
    turnOn.tagCut = cms.string("Btag")
    turnOn.tagFilterMatch = cms.string(jetFilter)
    turnOn.tagFilterMin = cms.uint32(1)
    
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")

    return turnOn


def addBTagTurnOn(matchBtag=False, isCalo=False, isTrueB=False):
    turnOn = cms.PSet()
    
    histName = "PFDeepCSV"
    if isCalo: histName = "CaloDeepCSV"

    if matchBtag:
        histName += "MatchBtag"

    if isTrueB:
        histName += "TrueB"

    histName += "TandP"


    numFilter       = "hltBTagPFDeepCSV1p5Single"
    denJetMatch    = "hltPFJetFilterTwoC30"
    if isCalo: 
        numFilter = "hltBTagCaloDeepCSV1p5Single"
        denJetMatch = "hltCaloJetFilterTwoC30"


    turnOn.histName = cms.string(histName)
    turnOn.numFilterMatch = cms.string(numFilter)
    turnOn.denJetMatch    = cms.string(denJetMatch)
    turnOn.tagCut = cms.string("Btag")
    
    
    
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")
        if isTrueB: turnOn.probeCut = cms.string("trueBBtag")
    elif isTrueB:
        turnOn.probeCut = cms.string("trueB")

    return turnOn






#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet()

#
#  PF 30
#
for pfPt in [30,40,45,60,75,116]:
    jetTurnOnConfig.append(addTurnOn(pfPt))
    jetTurnOnConfig.append(addTurnOn(pfPt, matchBtag=True))


#
#  Calo 30
#
for caloPt in [30,100]:
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True))
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True, matchBtag=True))



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

    cms.PSet(filterName = cms.string("hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
             histName = cms.string("EMu"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),
    
#
#    cms.PSet(filterName = cms.string("hltPFJetFilterTwoC30"),
#             histName = cms.string("2PF30"),
#             mult = cms.uint32(2),
#             pt = cms.double(-1.0)),
#
#
#
#    cms.PSet(filterName = cms.string("hltCaloJetFilterTwoC30"),
#             histName = cms.string("2Calo30"),
#             mult = cms.uint32(2),
#             pt = cms.double(-1.0)),
#
#
#    cms.PSet(filterName = cms.string("hltBTagPFDeepCSV1p5Single"),
#             histName = cms.string("2PFBTag"),
#             mult = cms.uint32(2),
#             pt = cms.double(-1.0)),
#

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
