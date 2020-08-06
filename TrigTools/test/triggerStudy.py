# Import configurations
import FWCore.ParameterSet.Config as cms

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

from CMSSWTools.TrigTools.ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8_RunIIAutumn18MiniAOD_MINIAODSIM import ZH_HToBB_ZToBB_source
process.source = ZH_HToBB_ZToBB_source


# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(1000)
    input = cms.untracked.int32(-1)
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )



process.triggerStudy = cms.EDAnalyzer("TriggerStudy",           
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
                                      pathsToPass = cms.vstring("HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v",),
                                      jets = cms.InputTag("slimmedJets"),
                                      truthJets = cms.InputTag("slimmedGenJets"),
                                      truthParts = cms.InputTag("prunedGenParticles")
)

process.p = cms.Path(process.triggerStudy)


# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.categories.append('TriggerStudy')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
    limit = cms.untracked.int32(-1)
)
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
