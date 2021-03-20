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


# MC  dasgoclient -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8D07021F-FD00-D442-B0E6-9077266B320B.root")
                            #)

#from CMSSWTools.TrigTools.ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8_RunIIAutumn18MiniAOD_MINIAODSIM import ZH_HToBB_ZToBB_source
#process.source = ZH_HToBB_ZToBB_source

#from CMSSWTools.TrigTools.ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_ext2_v1 import ZZTo4b_source
#process.source = ZZTo4b_source

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/69F49A13-5100-DB4B-B809-4016B4C2A3CB.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/87D6FC74-37A0-C146-98D7-8E23CB2463F4.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/C8EAC210-E31B-9F42-9EBF-F375332BFF54.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/F44FB500-F597-1846-A69F-A4310D8D19A5.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/05A59850-A677-7745-A857-923FAA4BE576.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/0AD42490-4CFB-CD47-A118-32A0D3CBF1D1.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/1956C4D0-2BA5-B944-83EA-9A4FC65ED28F.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/2C1CFF50-20D4-AC4E-B5E1-30B054C0EEBB.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/2EBBF75F-C820-F748-9724-E5D59D297A8A.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/51E46B16-1244-CD4B-9578-DD2F7EE1A692.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/588D08C9-01F5-B242-94C1-22CC22653CF3.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/6549C57A-9BB3-BC48-8934-91341B645B14.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/73F78F97-2F64-9E4C-92D9-632A66115DE9.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/8133FADB-3C25-9F4A-90B5-451EFF03E0F7.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/8CB939AC-D800-0A40-BA71-A5A1B2B3D8CB.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/C2B5D5A3-934B-6349-850B-5B0476828189.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/E63B4433-2800-5541-B059-A442F07C9E6C.root",
                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/EB958EC5-03E8-7F4F-9F4D-9A926C4B3EE4.root",
                            )
                        )
process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))


# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)



#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v


#process.hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23  # L1
#hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter   # EMU DZ

process.triggerStudy = cms.EDAnalyzer("TriggerStudy",           
                                      hltPreSelection = cms.vstring("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v"),
                                      offlinePreSelection = cms.PSet(),
                                      isBBMC = cms.bool(False),
                                      isMC = cms.bool(options.isMC),
                                      testL1 = cms.bool(False),
                                      trigObjs = cms.InputTag("slimmedPatTrigger"),
                                      trigResults = cms.InputTag("TriggerResults","","HLT"),
                                      filtersToPass = cms.VPSet(  # Not really Needed bc we have the input trigger

                                          cms.PSet(filterName = cms.string("hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23"),
                                                   histName = cms.string("L1"),
                                                   mult = cms.uint32(1),
                                                   pt = cms.double(-1.0)),

                                          cms.PSet(filterName = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
                                                   histName = cms.string("L1"),
                                                   mult = cms.uint32(1),
                                                   pt = cms.double(-1.0)),

                                          cms.PSet(filterName = cms.string("hltPFJetFilterTwoC30"),
                                                   histName = cms.string("2PF30"),
                                                   mult = cms.uint32(2),
                                                   pt = cms.double(30)),

                                      ), 

                                      jetTurnOns = cms.VPSet(
                                          cms.PSet(numFilterMatch = cms.string("hltCaloJetFilterTwoC30"),
                                                   histName = cms.string("Calo30"),
                                               ),

                                          cms.PSet(histName = cms.string("Calo30Test"),
                                                   numPtCut = cms.double(30.),
                                                   numPtName = cms.string("hltCaloJetFilterTwoC30"),
                                               ),

                                          cms.PSet(histName = cms.string("Calo30Test2"),
                                                   numPtCut = cms.double(30.),
                                                   numPtName = cms.string("hltCaloJetFilterTwoC30"),
                                                   tagFilterMatch = cms.string("hltCaloJetFilterTwoC30"),
                                               ),

                                          
                                          cms.PSet(histName = cms.string("PF30"),
                                                   numPtCut = cms.double(30.),
                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
                                               ),

                                          cms.PSet(histName = cms.string("PF75"),
                                                   numPtCut = cms.double(75.),
                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
                                               ),

                                          cms.PSet(histName = cms.string("PF60"),
                                                   numPtCut = cms.double(60.),
                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
                                               ),

                                          cms.PSet(histName = cms.string("PF45"),
                                                   numPtCut = cms.double(45.),
                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
                                               ),

                                          cms.PSet(histName = cms.string("PF40"),
                                                   numPtCut = cms.double(40.),
                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
                                               ),
                                      ),
                                      pathsToPass = cms.vstring(),
                                      jets = cms.InputTag("slimmedJets"),
                                      L1Jets = cms.InputTag("caloStage2Digis","Jet"),
                                      truthJets = cms.InputTag("slimmedGenJets"),
                                      truthParts = cms.InputTag("prunedGenParticles"),
                                      AlgInputTag = cms.InputTag("gtStage2Digis"),
                                      ExtInputTag = cms.InputTag("gtStage2Digis"),
                                  )


process.triggerStudyPassNJet = process.triggerStudy.clone()
process.triggerStudyPassNJet.offlinePreSelection = cms.PSet(minNSelJet = cms.uint32(2))


process.triggerStudyPassPreSelMed = process.triggerStudy.clone()
process.triggerStudyPassPreSelMed.offlinePreSelection = cms.PSet(minNSelJet = cms.uint32(2),
                                                                 minNTagMedJet = cms.uint32(2))


process.p = cms.Path(process.triggerStudy + process.triggerStudyPassNJet + process.triggerStudyPassPreSelMed)


# initialize MessageLogger and output report
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
