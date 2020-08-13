# Import configurations
import FWCore.ParameterSet.Config as cms



from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')

options.register ('isMC',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "is this MC")

options.parseArguments()


# set up process
process = cms.Process("TriggerStudy")

#
# Setup L1
#
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v20', '')
    

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

# L1
#process.hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet = cms.EDFilter( "HLTL1TSeed",
#    L1SeedsLogicalExpression = cms.string( "L1_QuadJet60er2p5 OR L1_HTT280er OR L1_HTT320er OR L1_HTT360er OR L1_ETT2000 OR L1_HTT400er OR L1_HTT450er OR L1_HTT280er_QuadJet_70_55_40_35_er2p4 OR L1_HTT320er_QuadJet_70_55_40_40_er2p4 OR L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3 OR L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3" ),


##L1_QuadJet60er2p5 - Prescaled
#L1_ETT2000 - GOOD
##L1_HTT280er - Prescaled
##L1_HTT320er - Prescaled
#L1_HTT360er - GOOD
#L1_HTT400er - GOOD
#L1_HTT450er - GOOD
##L1_HTT280er_QuadJet_70_55_40_35_er2p4  - PRescaled
#L1_HTT320er_QuadJet_70_55_40_40_er2p4  - GOOD
#L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3 - GOOD
#L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3 - GOOD
##

jetTurnOnConfig = cms.VPSet(
    cms.PSet(numFilterMatch = cms.string("hltQuadCentralJet30"),
             histName = cms.string("Calo30"),
             denFilter = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
         ),

    cms.PSet(numFilterMatch = cms.string("hltBTagCaloDeepCSVp17Double"), 
             histName = cms.string("CaloDeepCSV"),
             denFilter = cms.string("hltCaloQuadJet30HT320"),
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
    )
    



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


triggerConfigL1Unprescaled = cms.VPSet(cms.PSet(L1Names = cms.vstring("L1_ETT2000","L1_HTT360er","L1_HTT320er_QuadJet_70_55_40_40_er2p4"),
                                                histName = cms.string("L1Unprescaled"),
                                                mult = cms.uint32(1),
                                                pt = cms.double(-1.0))
                                   )




#
#  HLT Only 
#
process.triggerStudyHLT = cms.EDAnalyzer("TriggerStudy",           
                                         isMC = cms.bool(options.isMC),
                                         isBBMC = cms.bool(options.isMC),
                                         testL1 = cms.bool(False),
                                         trigObjs = cms.InputTag("slimmedPatTrigger"),
                                         trigResults = cms.InputTag("TriggerResults","","HLT"),
                                         filtersToPass = triggerConfigHLT,
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
#
#  L1 and HLT 
#
triggerConfigL1andHLT = triggerConfigL1Unprescaled.copy()
triggerConfigL1andHLT.extend(triggerConfigHLT)

#print triggerConfigL1andHLT.dumpPython()

process.triggerStudyL1andHLT = process.triggerStudyHLT.clone()
process.triggerStudyL1andHLT.filtersToPass = triggerConfigL1andHLT

process.triggerStudyPassNJet = process.triggerStudyL1andHLT.clone()
process.triggerStudyPassNJet.offlinePreSelection = cms.PSet(minNSelJet = cms.uint32(4))

process.triggerStudyPassPreSel = process.triggerStudyL1andHLT.clone()
process.triggerStudyPassPreSel.offlinePreSelection = cms.PSet(minNSelJet = cms.uint32(4),
                                                              minNTagTightJet = cms.uint32(4))


process.triggerStudyPassPreSelMed = process.triggerStudyL1andHLT.clone()
process.triggerStudyPassPreSelMed.offlinePreSelection = cms.PSet(minNSelJet = cms.uint32(4),
                                                                 minNTagMedJet = cms.uint32(4))

process.p = cms.Path(process.triggerStudyHLT + process.triggerStudyL1andHLT + process.triggerStudyPassNJet + process.triggerStudyPassPreSel + process.triggerStudyPassPreSelMed )


hltPreSelection = [("HT180","HLT_PFHT180_v"),
                   ("HT250","HLT_PFHT250_v")]


for hltCut in hltPreSelection:

    #
    #  All
    #
    setattr(process,"triggerStudy"+hltCut[0],process.triggerStudyL1andHLT.clone())
    getattr(process,"triggerStudy"+hltCut[0]).hltPreSelection = cms.vstring(hltCut[1])
    process.p *= getattr(process,"triggerStudy"+hltCut[0])

    #
    #  Pass NJet
    #
    setattr(process,"triggerStudyPassNJet"+hltCut[0],process.triggerStudyPassNJet.clone())
    getattr(process,"triggerStudyPassNJet"+hltCut[0]).hltPreSelection = cms.vstring(hltCut[1])
    process.p *= getattr(process,"triggerStudyPassNJet"+hltCut[0])

    #
    #  Pass PreSel
    #
    setattr(process,"triggerStudyPassPreSel"+hltCut[0],process.triggerStudyPassPreSel.clone())
    getattr(process,"triggerStudyPassPreSel"+hltCut[0]).hltPreSelection = cms.vstring(hltCut[1])
    process.p *= getattr(process,"triggerStudyPassPreSel"+hltCut[0])

    #
    #  Pass PreSelMed
    #
    setattr(process,"triggerStudyPassPreSelMed"+hltCut[0],process.triggerStudyPassPreSelMed.clone())
    getattr(process,"triggerStudyPassPreSelMed"+hltCut[0]).hltPreSelection = cms.vstring(hltCut[1])
    process.p *= getattr(process,"triggerStudyPassPreSelMed"+hltCut[0])



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
