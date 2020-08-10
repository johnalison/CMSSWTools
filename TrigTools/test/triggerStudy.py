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

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkSummary = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(500),
    limit = cms.untracked.int32(10000000)
)
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(500),
    limit = cms.untracked.int32(10000000)
)

# MC  dasgoclient -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8D07021F-FD00-D442-B0E6-9077266B320B.root")
                            #)

#from CMSSWTools.TrigTools.ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8_RunIIAutumn18MiniAOD_MINIAODSIM import ZH_HToBB_ZToBB_source
#process.source = ZH_HToBB_ZToBB_source

#from CMSSWTools.TrigTools.ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_ext2_v1 import ZZTo4b_source
#process.source = ZZTo4b_source

Data2018D_source = cms.Source("PoolSource",
                              fileNames = cms.untracked.vstring("/store/data/Run2018D/JetHT/MINIAOD/PromptReco-v2/000/320/500/00000/048048EB-EA95-E811-9A1D-FA163ECE26BB.root")
)
process.source = Data2018D_source


process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))


# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)

# L1
#process.hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet = cms.EDFilter( "HLTL1TSeed",
#    L1SeedsLogicalExpression = cms.string( "L1_QuadJet60er2p5 OR L1_HTT280er OR L1_HTT320er OR L1_HTT360er OR L1_ETT2000 OR L1_HTT400er OR L1_HTT450er OR L1_HTT280er_QuadJet_70_55_40_35_er2p4 OR L1_HTT320er_QuadJet_70_55_40_40_er2p4 OR L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3 OR L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3" ),
#


process.triggerStudy = cms.EDAnalyzer("TriggerStudy",           
                                      isMC = cms.bool(options.isMC),
                                      trigObjs = cms.InputTag("slimmedPatTrigger"),
                                      trigResults = cms.InputTag("TriggerResults","","HLT"),
                                      filtersToPass = cms.VPSet(

                                          cms.PSet(filterName = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
                                                   histName = cms.string("L1"),
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

                                      ),

                                      jetTurnOns = cms.VPSet(
                                          cms.PSet(filterName = cms.string("hltQuadCentralJet30"),
                                                   histName = cms.string("Calo30"),
                                                   denominatorReq = cms.string("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet"),
                                               ),

                                          cms.PSet(filterName = cms.string("hltBTagCaloDeepCSVp17Double"), 
                                                   histName = cms.string("CaloDeepCSV"),
                                                   denominatorReq = cms.string("hltCaloQuadJet30HT320"),
                                               ),
                                          
                                          cms.PSet(filterName = cms.string("hltBTagCaloDeepCSVp17Double"), 
                                                   histName = cms.string("CaloDeepCSV"),
                                                   denominatorReq = cms.string("hltCaloQuadJet30HT320"),
                                               ),

                                          cms.PSet(filterName = cms.string("hltPFCentralJetLooseIDQuad30"),
                                                   histName = cms.string("PF30"),
                                                   denominatorReq = cms.string("hltBTagCaloDeepCSVp17Double"), 
                                               ),

                                          cms.PSet(filterName = cms.string("hlt1PFCentralJetLooseID75"),
                                                   histName = cms.string("PF75"),
                                                   denominatorReq = cms.string("hltPFCentralJetLooseIDQuad30"), 
                                               ),

                                          cms.PSet(filterName = cms.string("hlt2PFCentralJetLooseID60"),
                                                   histName = cms.string("PF60"),
                                                   denominatorReq = cms.string("hlt1PFCentralJetLooseID75"), 
                                               ),

                                          cms.PSet(filterName = cms.string("hlt3PFCentralJetLooseID45"),
                                                   histName = cms.string("PF45"),
                                                   denominatorReq = cms.string("hlt2PFCentralJetLooseID60"),
                                               ),

                                          cms.PSet(filterName = cms.string("hlt4PFCentralJetLooseID40"),
                                                   histName = cms.string("PF40"),
                                                   denominatorReq = cms.string("hlt3PFCentralJetLooseID45"),
                                               ),

                                          cms.PSet(filterName = cms.string("hltBTagPFDeepCSV4p5Triple"),
                                                   histName = cms.string("PFDeepCSV"),
                                                   denominatorReq = cms.string("hltPFCentralJetsLooseIDQuad30HT330"),
                                               ),

                                      ),
                                      hltPreSelection = cms.vstring(),
                                      pathsToPass = cms.vstring("HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v",),
                                      jets = cms.InputTag("slimmedJets"),
                                      truthJets = cms.InputTag("slimmedGenJets"),
                                      truthParts = cms.InputTag("prunedGenParticles")
)

process.triggerStudyHT180 = process.triggerStudy.clone()
process.triggerStudyHT180.hltPreSelection = cms.vstring("HLT_PFHT180_v")

process.triggerStudyHT250 = process.triggerStudy.clone()
process.triggerStudyHT250.hltPreSelection = cms.vstring("HLT_PFHT250_v")

#process.triggerStudyPFJet80 = process.triggerStudy.clone()
#process.triggerStudyPFJet80.hltPreSelection = cms.vstring("HLT_PFJet80_v")
#
#process.triggerStudyPFJet140 = process.triggerStudy.clone()
#process.triggerStudyPFJet140.hltPreSelection = cms.vstring("HLT_PFJet140_v")


process.p = cms.Path(process.triggerStudy + process.triggerStudyHT180 + process.triggerStudyHT250) # + process.triggerStudyPFJet80 + process.triggerStudyPFJet140)


# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.categories.append('TriggerStudy')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
    limit = cms.untracked.int32(-1)
)
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
