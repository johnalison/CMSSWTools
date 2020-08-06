# Import configurations
import FWCore.ParameterSet.Config as cms

# set up process
process = cms.Process("TrigExample")

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

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8D07021F-FD00-D442-B0E6-9077266B320B.root")
)

# set the number of events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)


process.trigExample = cms.EDAnalyzer("MiniAODTriggerExample",           
                                     trigObjs = cms.InputTag("slimmedPatTrigger"),
                                     trigResults = cms.InputTag("TriggerResults","","HLT"),
                                     filtersToPass = cms.vstring("hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet",
                                                                 "hltQuadCentralJet30",  # 4 Calo jets pt > 30
                                                                 "hltCaloQuadJet30HT320", # Calo Ht > 320
                                                                 "hltBTagCaloDeepCSVp17Double", # Two calo jets 0.17
                                                                 "hltPFCentralJetLooseIDQuad30", # 4 PF jets pt > 30
                                                                 "hlt1PFCentralJetLooseID75",
                                                                 "hlt2PFCentralJetLooseID60",
                                                                 "hlt3PFCentralJetLooseID45",
                                                                 "hlt4PFCentralJetLooseID40",
                                                                 "hltPFCentralJetsLooseIDQuad30HT330",  # PF Ht > 330
                                                                 "hltBTagPFDeepCSV4p5Triple" # 3 PF Jet 0.24
                                                             ),
                                     pathsToPass = cms.vstring("HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v",),
                                     eles = cms.InputTag("slimmedElectrons"),
                                     jets = cms.InputTag("slimmedJets")
                                  )


process.p = cms.Path(process.trigExample)
