# Import configurations
import FWCore.ParameterSet.Config as cms


# set up process
process = cms.Process("JetKinematicStudy")


#
# Input data
#
# MC  dasgoclient -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8D07021F-FD00-D442-B0E6-9077266B320B.root")
                            #)
#from CMSSWTools.TrigTools.GluGluToHHTo4B_node_SM_13TeV_madgraph_RunIIFall17MiniAODv2_PU2017_MINIAODSIM import HH_HToBB_source
#process.source = HH_HToBB_source

#from CMSSWTools.TrigTools.ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8_RunIIAutumn18MiniAOD_MINIAODSIM import ZH_HToBB_ZToBB_source
#process.source = ZH_HToBB_ZToBB_source
nTruthBosons = 2

#
#  Base config with the nominal options (customized below)
#
plotsBase = cms.EDAnalyzer("HHKinematicStudy",           
                           isBBMC = cms.bool(True),
                           offlinePreSelection = cms.PSet(),
                           jets = cms.InputTag("slimmedJets"),
                           truthJets = cms.InputTag("slimmedGenJets"),
                           truthParts = cms.InputTag("prunedGenParticles"),
                           nTruthBosons = cms.uint32(2),
                       )




offlinePreSelection = [("",             cms.PSet()),
                       ("PassNJet",     cms.PSet(minNSelJet = cms.uint32(4))),
                       ("PassPreSel",   cms.PSet(minNSelJet = cms.uint32(4),
                                                 minNTagTightJet = cms.uint32(4))), 
]



process.p = cms.Path()

    
for o in offlinePreSelection:
        
    offName = o[0]
    offPreSelection = o[1]

    plotsConfiged = plotsBase.clone()
    plotsConfiged.offlinePreSelection = offPreSelection

    fullName = "HHStudy_"+offName

    setattr(process,fullName,plotsConfiged)
    process.p *= getattr(process,fullName)




#print process.p.dumpPython()



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
