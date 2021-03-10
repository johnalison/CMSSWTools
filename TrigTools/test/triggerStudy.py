# Import configurations
import FWCore.ParameterSet.Config as cms



from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')

options.register ('isMC',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "is this MC")

options.register ('globalTag',
                  None,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.string,
                  "Global Tag")


options.parseArguments()


# set up process
process = cms.Process("TriggerStudy")

if not options.globalTag:
    print "ERROR : specify globalTag"
    print "\t eg: for MC we have used 'globalTag=102X_upgrade2018_realistic_v20' in the past. "
    print "\t eg: for Data we have used 'globalTag=102X_upgrade2018_realistic_v21' in the past. "
    print "\t get this from the dataset name"
    print "\t exiting..."
    import sys
    sys.exit(-1)
    

#
# Setup L1
#
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
print "globalTag is ",options.globalTag
process.GlobalTag = GlobalTag(process.GlobalTag, str(options.globalTag), '')
    

# MC  dasgoclient -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8D07021F-FD00-D442-B0E6-9077266B320B.root")
                            #)

from CMSSWTools.TrigTools.ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8_RunIIAutumn18MiniAOD_MINIAODSIM import ZH_HToBB_ZToBB_source
process.source = ZH_HToBB_ZToBB_source

#from CMSSWTools.TrigTools.ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_ext2_v1 import ZZTo4b_source
#process.source = ZZTo4b_source

#process.source = cms.Source("PoolSource",
#                              fileNames = cms.untracked.vstring("/store/data/Run2018D/JetHT/MINIAOD/PromptReco-v2/000/320/500/00000/048048EB-EA95-E811-9A1D-FA163ECE26BB.root")
#)
process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))


# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)


#
#  Jet trigger turn ons
#
jetTurnOnConfig = cms.VPSet(
    cms.PSet(numFilterMatch = cms.string("hltQuadCentralJet30"),
             histName = cms.string("Calo30"),
             denFilter = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSV"),
             denFilter = cms.string("hltCaloQuadJet30HT320"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSVMatchBtag"),
             denFilter = cms.string("hltCaloQuadJet30HT320"),
             tagFilterMatch = cms.string("Btag"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSVMatchTrueB"),
             denFilter = cms.string("hltCaloQuadJet30HT320"),
             tagFilterMatch = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltPFCentralJetLooseIDQuad30"),
             histName = cms.string("PF30"),
             denFilter = cms.string("hltBTagCaloDeepCSVp17Double"), 
         ),
    
    cms.PSet(numFilterMatch = cms.string("hlt1PFCentralJetLooseID75"),
             histName = cms.string("PF75"),
             denFilter = cms.string("hltPFCentralJetLooseIDQuad30"), 
         ),
    
    cms.PSet(numFilterMatch = cms.string("hlt2PFCentralJetLooseID60"),
             histName = cms.string("PF60"),
             denFilter = cms.string("hlt1PFCentralJetLooseID75"), 
         ),
    
    cms.PSet(numFilterMatch = cms.string("hlt3PFCentralJetLooseID45"),
             histName = cms.string("PF45"),
             denFilter = cms.string("hlt2PFCentralJetLooseID60"),
         ),
    
    cms.PSet(numFilterMatch = cms.string("hlt4PFCentralJetLooseID40"),
             histName = cms.string("PF40"),
             denFilter = cms.string("hlt3PFCentralJetLooseID45"),
         ),
    
    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSV"),
             denFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSVMatchBtag"),
             denFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             tagFilterMatch = cms.string("Btag"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSVMatchTrueB"),
             denFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             tagFilterMatch = cms.string("trueB"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("PFDeepCSVMatchTrueBtag"),
             denFilter = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
             tagFilterMatch = cms.string("trueBtag"),
         ),


    )
    


#
#   The HLT part of the trigger path (the L1 is added below)
#
triggerConfigHLT = cms.VPSet(
    cms.PSet(filterName = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
             histName = cms.string("L1ORAll"),
             mult = cms.uint32(1),
             pt = cms.double(-1.0)),

    cms.PSet(filterName = cms.string("hltQuadCentralJet30"),
             histName = cms.string("4Calo30"),
             mult = cms.uint32(4),
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
    
    cms.PSet(filterName = cms.string("hltBTagPFDeepCSV4p5Triple"),
             histName = cms.string("3PFBtags"),
             mult = cms.uint32(3),
             pt = cms.double(-1)),
)

#
#  Building the differnet trigger paths (with differnet L1 seeds)
#
triggerConfigL1HTQuadJet = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT320er_QuadJet_70_55_40_40_er2p4"),
                                                histName = cms.string("passL1"),
                                                mult = cms.uint32(1),
                                                pt = cms.double(-1.0))
                                   )
triggerConfigL1HTQuadJetHLT = triggerConfigL1HTQuadJet.copy()
triggerConfigL1HTQuadJetHLT.extend(triggerConfigHLT)

triggerConfigL1HT = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT360er"),
                                       histName = cms.string("passL1"),
                                       mult = cms.uint32(1),
                                       pt = cms.double(-1.0)),
                                     )
triggerConfigL1HTHLT = triggerConfigL1HT.copy()
triggerConfigL1HTHLT.extend(triggerConfigHLT)


triggerConfigL1HTQuadJetOrHT = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT320er_QuadJet_70_55_40_40_er2p4","L1_HTT360er"),
                                                  histName = cms.string("passL1"),
                                                  mult = cms.uint32(1),
                                                  pt = cms.double(-1.0)),
                                     )
triggerConfigL1HTQuadJetOrHTHLT = triggerConfigL1HTQuadJetOrHT.copy()
triggerConfigL1HTQuadJetOrHTHLT.extend(triggerConfigHLT)


triggerConfigL1Unprescaled = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_ETT2000","L1_HTT360er","L1_HTT320er_QuadJet_70_55_40_40_er2p4"),
                                                histName = cms.string("passL1"),
                                                mult = cms.uint32(1),
                                                pt = cms.double(-1.0))
                                   )
triggerConfigL1UnprescaledHLT = triggerConfigL1Unprescaled.copy()
triggerConfigL1UnprescaledHLT.extend(triggerConfigHLT)


triggerConfigL1HTT120 = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT120er"),
                                             histName = cms.string("passL1"),
                                             mult = cms.uint32(1),
                                             pt = cms.double(-1.0))
                                )
triggerConfigL1HTT120HLT = triggerConfigL1HTT120.copy()
triggerConfigL1HTT120HLT.extend(triggerConfigHLT)


triggerConfigL1HTT160 = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_HTT160er"),
                                             histName = cms.string("passL1"),
                                             mult = cms.uint32(1),
                                             pt = cms.double(-1.0))
                                )
triggerConfigL1HTT160HLT = triggerConfigL1HTT160.copy()
triggerConfigL1HTT160HLT.extend(triggerConfigHLT)




#
#  Base config with the nominal options (customized below)
#
triggerStudyBase = cms.EDAnalyzer("TriggerStudy",           
                                  isMC = cms.bool(options.isMC),
                                  isBBMC = cms.bool(options.isMC),
                                  testL1 = cms.bool(False),
                                  doEmulation = cms.bool(False),
                                  trigObjs = cms.InputTag("slimmedPatTrigger"),
                                  trigResults = cms.InputTag("TriggerResults","","HLT"),
                                  filtersToPass = cms.VPSet(),
                                  jetTurnOns = jetTurnOnConfig,
                                  hltPreSelection = cms.vstring(),
                                  offlinePreSelection = cms.PSet(),
                                  pathsToPass = cms.vstring("HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v",),
                                  jets = cms.InputTag("slimmedJets"),
                                  L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                  truthJets = cms.InputTag("slimmedGenJets"),
                                  truthParts = cms.InputTag("prunedGenParticles"),
                                  AlgInputTag = cms.InputTag("gtStage2Digis"),
                              )



hltSeeds = [("",     cms.vstring()), 
            ("HT180",cms.vstring("HLT_PFHT180_v")),
            ("HT250",cms.vstring("HLT_PFHT250_v")),
            ]

L1Seeds = [("HLTOnly",       triggerConfigHLT),
           ("L1HTQuad",      triggerConfigL1HTQuadJetHLT),
           ("L1HT",          triggerConfigL1HTHLT),
           ("L1HTQuadOrHT",  triggerConfigL1HTQuadJetOrHTHLT),
           ("L1Unprescaled", triggerConfigL1UnprescaledHLT),
           ("L1HT120",       triggerConfigL1HTT120HLT),
           ("L1HT160",       triggerConfigL1HTT160HLT),
           ]

offlinePreSelection = [("",             cms.PSet()),
                       ("PassNJet",     cms.PSet(minNSelJet = cms.uint32(4))),
                       ("PassPreSel",   cms.PSet(minNSelJet = cms.uint32(4),
                                                 minNTagTightJet = cms.uint32(4))), 
                       ("PassPreSelMed",cms.PSet(minNSelJet = cms.uint32(4),
                                                 minNTagMedJet = cms.uint32(4))), 
                   ]
process.p = cms.Path()

for h in hltSeeds: 
    
    hltName = h[0]
    
    for l in L1Seeds:
         
        l1Name = l[0]

        for o in offlinePreSelection:

            offName = o[0]

            hltPreSelection = h[1]
            filtersToPass = l[1]
            offPreSelection = o[1]


            triggerStudyConfigured = triggerStudyBase.clone()
            triggerStudyConfigured.filtersToPass = filtersToPass
            triggerStudyConfigured.offlinePreSelection = offPreSelection
            triggerStudyConfigured.hltPreSelection = hltPreSelection

            fullName = "triggerStudy"+hltName+l1Name+offName

            setattr(process,fullName,triggerStudyConfigured)
            process.p *= getattr(process,fullName)



#print process.p.dumpPython()


#
#  Trigger Emulation
#


#
#  Base config with the nominal options (customized below)
#
triggerEmulation = cms.EDAnalyzer("TriggerStudy",           
                                  isMC = cms.bool(options.isMC),
                                  isBBMC = cms.bool(options.isMC),
                                  testL1 = cms.bool(False),
                                  doEmulation = cms.bool(True),
                                  trigObjs = cms.InputTag("slimmedPatTrigger"),
                                  trigResults = cms.InputTag("TriggerResults","","HLT"),
                                  filtersToPass = cms.VPSet(),
                                  jetTurnOns = cms.VPSet(),
                                  hltPreSelection = cms.vstring(),
                                  offlinePreSelection = cms.PSet(),
                                  pathsToPass = cms.vstring("HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v",),
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
)




triggerEmulation.filtersToPass = triggerConfigEMU

for o in offlinePreSelection:

    offName = o[0]
    offPreSelection = o[1]


    triggerEmulationConfigured = triggerEmulation.clone()
    triggerEmulationConfigured.offlinePreSelection = offPreSelection

    fullName = "triggerEmulation"+offName

    setattr(process,fullName,triggerEmulationConfigured)
    process.p *= getattr(process,fullName)




## initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('TriggerStudy')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
    limit = cms.untracked.int32(0)
)
process.MessageLogger.cerr.FwkSummary = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(10000),
    limit = cms.untracked.int32(100000)
)
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(10000),
    limit = cms.untracked.int32(10000)
)


process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

#print process.dumpPython()
