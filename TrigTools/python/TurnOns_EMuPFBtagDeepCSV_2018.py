import FWCore.ParameterSet.Config as cms

def addTurnOn(pt, matchBtag=False, isCalo=False, useMultiJet=False):
    turnOn = cms.PSet()
    
    histName = "PF"+str(pt)
    if isCalo: histName = "Calo"+str(pt)

    if useMultiJet: histName += "inMJ"
         

    if matchBtag:
        histName += "MatchBtag"
    histName += "TandP"

    
    jetFilter = "hltPFJetFilterTwoC30" 
    if isCalo: jetFilter = "hltCaloJetFilterTwoC30"

    if useMultiJet: 
        jetFilter = "hltPFCentralJetLooseIDQuad30"
        if isCalo: jetFilter = "hltQuadCentralJet30"

    turnOn.histName = cms.string(histName)
    #turnOn.denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter") 
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
    #turnOn.denEventFilter = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter") 
    turnOn.numFilterMatch = cms.string(numFilter)
    turnOn.denEventFilter = cms.string(denFilter)

    turnOn.tagCut = cms.string("Btag")
    turnOn.tagFilterMatch = cms.string(tagFilter)
    turnOn.tagFilterMin = cms.uint32(1)
    
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")

    return turnOn



def add2b112L1TurnOn(matchBtag=False, doMaxDEta=False):
    turnOn = cms.PSet()
    
    histName = "L12b112"
    histName += "inMJ"
    if doMaxDEta: histName += "maxDEta"

    if matchBtag:
        histName += "MatchBtag"
    histName += "TandP"

    jetFilter = "hltL1DoubleJet112er2p3dEtaMax1p6"

    turnOn.histName = cms.string(histName)
    turnOn.numFilterMatch = cms.string(jetFilter)

    turnOn.tagCut = cms.string("Btag")
    turnOn.tagFilterMatch = cms.string(jetFilter)
    turnOn.tagFilterMin = cms.uint32(1)

    if doMaxDEta: turnOn.tagFilterMaxDEta = cms.double(1.6)
            
    if matchBtag:
        turnOn.probeCut = cms.string("Btag")

    return turnOn




def addBTagTurnOn(matchBtag=False, isCalo=False, isTrueB=False, useMultiJet=False, is2b116=False):
    turnOn = cms.PSet()
    
    histName = "PFDeepCSV"
    if isCalo: histName = "CaloDeepCSV"

    if useMultiJet: histName += "inMJ"

    if is2b116: histName += "2b116"

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

    if useMultiJet: 
        numFilter      = "hltBTagPFDeepCSV4p5Triple"
        denJetMatch    = "hltPFCentralJetLooseIDQuad30"
        denEventFilter = "hltPFCentralJetsLooseIDQuad30HT330"

        if isCalo: 
            if is2b116:
                numFilter = "hltBTagCaloDeepCSV0p71Double6Jets80"
                denJetMatch = "hltDoubleCaloBJets100eta2p3"
                denEventFilter = "hltDoubleCaloBJets100eta2p3"
            else:
                numFilter = "hltBTagCaloDeepCSVp17Double"
                denJetMatch = "hltQuadCentralJet30"
                denEventFilter = "hltCaloQuadJet30HT320"
        


    turnOn.histName = cms.string(histName)
    turnOn.numFilterMatch = cms.string(numFilter)
    turnOn.denJetMatch    = cms.string(denJetMatch)
    turnOn.tagCut = cms.string("Btag")

    if useMultiJet: turnOn.denEventFilter    = cms.string(denEventFilter)    
    
    
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

    jetTurnOnConfig.append(addTurnOn(pfPt, useMultiJet=True))
    jetTurnOnConfig.append(addTurnOn(pfPt, matchBtag=True, useMultiJet=True))

for turnOnPair in [("Calo30",   "hltQuadCentralJet30",                 "hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet", "hltQuadCentralJet30"),
                   ("PF30",     "hltPFCentralJetLooseIDQuad30",        "hltBTagCaloDeepCSVp17Double"                            , "hltQuadCentralJet30"),
                   ("PF75",     "hlt1PFCentralJetLooseID75",           "hltPFCentralJetLooseIDQuad30"                           , "hltQuadCentralJet30"),
                   ("PF60",     "hlt2PFCentralJetLooseID60",           "hlt1PFCentralJetLooseID75"                              , "hltQuadCentralJet30"),
                   ("PF45",     "hlt3PFCentralJetLooseID45",           "hlt2PFCentralJetLooseID60"                              , "hltQuadCentralJet30"),
                   ("PF40",     "hlt4PFCentralJetLooseID40",           "hlt3PFCentralJetLooseID45"                              , "hltQuadCentralJet30"),

                   ("Calo100",  "hltDoubleCaloBJets100eta2p3",         "hltL1DoubleJet112er2p3dEtaMax1p6"   , "hltDoubleCaloBJets100eta2p3"),
                   ("PF116",    "hltDoublePFJets116Eta2p3",            "hltBTagCaloDeepCSV0p71Double6Jets80", "hltDoubleCaloBJets100eta2p3"),
                   ("PF116Dr",  "hltDoublePFJets116Eta2p3MaxDeta1p6",  "hltDoublePFJets116Eta2p3"           , "hltDoubleCaloBJets100eta2p3"),   ]:


    jetTurnOnConfig.append(addTurnOnFilterMatch(turnOnPair[0], turnOnPair[1], turnOnPair[2], turnOnPair[3] ))
    jetTurnOnConfig.append(addTurnOnFilterMatch(turnOnPair[0], turnOnPair[1], turnOnPair[2], turnOnPair[3],  matchBtag=True))
    


#
#  Calo 30
#
for caloPt in [30,100]:
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True))
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True, matchBtag=True))

    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True, useMultiJet=True))
    jetTurnOnConfig.append(addTurnOn(caloPt, isCalo=True, matchBtag=True, useMultiJet=True))



jetTurnOnConfig.append(add2b112L1TurnOn())
jetTurnOnConfig.append(add2b112L1TurnOn(matchBtag=True))

jetTurnOnConfig.append(add2b112L1TurnOn(doMaxDEta = True ))
jetTurnOnConfig.append(add2b112L1TurnOn(doMaxDEta = True, matchBtag=True))



#
#  PF BTags
#
jetTurnOnConfig.append(addBTagTurnOn())
jetTurnOnConfig.append(addBTagTurnOn(matchBtag=True))

jetTurnOnConfig.append(addBTagTurnOn(useMultiJet=True))
jetTurnOnConfig.append(addBTagTurnOn(useMultiJet=True, matchBtag=True))


#
# Calo BTags
#
jetTurnOnConfig.append(addBTagTurnOn(isCalo=True))
jetTurnOnConfig.append(addBTagTurnOn(isCalo=True, matchBtag=True))

jetTurnOnConfig.append(addBTagTurnOn(useMultiJet=True, isCalo=True))
jetTurnOnConfig.append(addBTagTurnOn(useMultiJet=True, isCalo=True, matchBtag=True))

jetTurnOnConfig.append(addBTagTurnOn(is2b116=True, useMultiJet=True, isCalo=True))
jetTurnOnConfig.append(addBTagTurnOn(is2b116=True, useMultiJet=True, isCalo=True, matchBtag=True))



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

    cms.PSet(filterName = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltQuadCentralJet30"),
             histName = cms.string("4Calo30"),
             mult = cms.uint32(4),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltL1DoubleJet112er2p3dEtaMax1p6"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),





    cms.PSet(filterName = cms.string("hltCaloQuadJet30HT320"), # Calo Ht > 320"),
             histName = cms.string("CaloHt320"),
             mult = cms.uint32(1),
             pt = cms.double(320)),

    cms.PSet(filterName = cms.string("hltBTagCaloDeepCSVp17Double"), 
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
    
    cms.PSet(filterName = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             histName = cms.string("PFHt330"),
             mult = cms.uint32(1),
             pt = cms.double(330)),

    cms.PSet(filterName = cms.string("hltBTagCaloDeepCSV0p71Double6Jets80"), 
             histName = cms.string("2CaloBTags"),
             mult = cms.uint32(2),
             pt = cms.double(-1)),


    cms.PSet(filterName = cms.string("hltDoubleCaloBJets100eta2p3"),
             histName = cms.string("2Calo100"),
             mult = cms.uint32(2),
             pt = cms.double(-1.0)),


    cms.PSet(filterName = cms.string("hltDoublePFJets116Eta2p3"),
             histName = cms.string("2PF116"),
             mult = cms.uint32(2),
             pt = cms.double(116)),


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
