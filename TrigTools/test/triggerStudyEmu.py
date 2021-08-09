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




#
#  Get the global Tag
#
if options.isMC:
    globalTag = "102X_upgrade2018_realistic_v15"
else:
    #globalTag = "102X_upgrade2018_realistic_v21"
    globalTag = "102X_dataRun2_v14"
    #globalTag = "102X_dataRun2_Prompt_v6"
if not options.globalTag is None:
    print "Overidding global tag with",options.globalTag
    globalTag = options.globalTag



#
# Setup L1
#
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
print "globalTag is ",globalTag
process.GlobalTag = GlobalTag(process.GlobalTag, str(globalTag), '')


#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring(
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/69F49A13-5100-DB4B-B809-4016B4C2A3CB.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/87D6FC74-37A0-C146-98D7-8E23CB2463F4.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/C8EAC210-E31B-9F42-9EBF-F375332BFF54.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/F44FB500-F597-1846-A69F-A4310D8D19A5.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/05A59850-A677-7745-A857-923FAA4BE576.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/0AD42490-4CFB-CD47-A118-32A0D3CBF1D1.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/1956C4D0-2BA5-B944-83EA-9A4FC65ED28F.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/2C1CFF50-20D4-AC4E-B5E1-30B054C0EEBB.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/2EBBF75F-C820-F748-9724-E5D59D297A8A.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/51E46B16-1244-CD4B-9578-DD2F7EE1A692.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/588D08C9-01F5-B242-94C1-22CC22653CF3.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/6549C57A-9BB3-BC48-8934-91341B645B14.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/73F78F97-2F64-9E4C-92D9-632A66115DE9.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/8133FADB-3C25-9F4A-90B5-451EFF03E0F7.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/8CB939AC-D800-0A40-BA71-A5A1B2B3D8CB.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/C2B5D5A3-934B-6349-850B-5B0476828189.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/E63B4433-2800-5541-B059-A442F07C9E6C.root",
#                                "/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/EB958EC5-03E8-7F4F-9F4D-9A926C4B3EE4.root",
#                            )
#                        )
#process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))

if options.isMC:
    process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring("/store/mc/RunIISummer20UL18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/10000/DEB42E22-D25F-4B45-BB61-2E76E94A678E.root")
    )
else:
    process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring("/store/data/Run2018D/MuonEG/MINIAOD/12Nov2019_UL2018_rsb-v1/20000/003E1A62-7AB4-7741-98E8-CE6A66AD68DA.root")
    )


process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))



# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)



from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL17
process.pileupJetIdUpdated = process.pileupJetId.clone( 
        jets=cms.InputTag("slimmedJets"),
        inputIsCorrected=True,
        applyJec=False,
        vertexes=cms.InputTag("offlineSlimmedPrimaryVertices"),
        algos = cms.VPSet(_chsalgos_106X_UL17),
    )


#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v


#process.hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23  # L1
#hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter   # EMU DZ


#
#  TurnOns for HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v
#
from CMSSWTools.TrigTools.TurnOns_EMuPFBtagDeepCSV_2018 import triggerConfig_EMuPFBtagDeepCSV, triggerStudyBase_EMuPFBtagDeepCSV
triggerStudyBase_EMuPFBtagDeepCSV.isMC = cms.bool(options.isMC)

hltSeeds = [("",     cms.vstring()), 
            ("EMu",cms.vstring("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v")),
            ("EMuDiJet30",cms.vstring("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v")),
            #("HT250",cms.vstring("HLT_PFHT250_v")),
            ]

# HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v"),
# HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v


L1Seeds_EMuPFBtagDeepCSV = [("HLTOnly",       triggerConfig_EMuPFBtagDeepCSV),
]

offlinePreSelection = [("",             cms.PSet()),
                       ("Pass2Jet",     cms.PSet(minNSelJet = cms.uint32(2))),
                       ("Pass2Tag",     cms.PSet(minNSelJet = cms.uint32(2),
                                                 minNTagTightJet = cms.uint32(2))), 
                   ]

process.p = cms.Path()

for h in hltSeeds: 
    
    hltName = h[0]


    for o in offlinePreSelection:
        
        offName = o[0]
        offPreSelection = o[1]

        #
        #   EMU
        #
        for l in L1Seeds_EMuPFBtagDeepCSV:
         
            l1Name = l[0]

            hltPreSelection = h[1]
            filtersToPass = l[1]

            triggerStudyConfigured = triggerStudyBase_EMuPFBtagDeepCSV.clone()
            triggerStudyConfigured.filtersToPass = filtersToPass
            triggerStudyConfigured.offlinePreSelection = offPreSelection
            triggerStudyConfigured.hltPreSelection = hltPreSelection

            fullName = "triggerStudy_EMuPFBtagDeepCSV_"+hltName+l1Name+offName

            setattr(process,fullName,triggerStudyConfigured)
            process.p *= getattr(process,fullName)





#
#process.triggerStudy = cms.EDAnalyzer("TriggerStudy",           
#                                      hltPreSelection = cms.vstring("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v"),
#                                      offlinePreSelection = cms.PSet(),
#                                      isBBMC = cms.bool(False),
#                                      isMC = cms.bool(options.isMC),
#                                      testL1 = cms.bool(False),
#                                      trigObjs = cms.InputTag("slimmedPatTrigger"),
#                                      trigResults = cms.InputTag("TriggerResults","","HLT"),
#                                      filtersToPass = cms.VPSet(  # Not really Needed bc we have the input trigger
#
#                                          cms.PSet(filterName = cms.string("hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23"),
#                                                   histName = cms.string("L1"),
#                                                   mult = cms.uint32(1),
#                                                   pt = cms.double(-1.0)),
#
#                                          cms.PSet(filterName = cms.string("hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter"),
#                                                   histName = cms.string("L1"),
#                                                   mult = cms.uint32(1),
#                                                   pt = cms.double(-1.0)),
#
#                                          cms.PSet(filterName = cms.string("hltPFJetFilterTwoC30"),
#                                                   histName = cms.string("2PF30"),
#                                                   mult = cms.uint32(2),
#                                                   pt = cms.double(30)),
#
#                                      ), 
#
#                                      jetTurnOns = cms.VPSet(
#                                          cms.PSet(numFilterMatch = cms.string("hltCaloJetFilterTwoC30"),
#                                                   histName = cms.string("Calo30"),
#                                               ),
#
#                                          cms.PSet(histName = cms.string("Calo30Test"),
#                                                   numPtCut = cms.double(30.),
#                                                   numPtName = cms.string("hltCaloJetFilterTwoC30"),
#                                               ),
#
#                                          cms.PSet(histName = cms.string("Calo30Test2"),
#                                                   numPtCut = cms.double(30.),
#                                                   numPtName = cms.string("hltCaloJetFilterTwoC30"),
#                                                   tagFilterMatch = cms.string("hltCaloJetFilterTwoC30"),
#                                               ),
#
#                                          
#                                          cms.PSet(histName = cms.string("PF30"),
#                                                   numPtCut = cms.double(30.),
#                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
#                                               ),
#
#                                          cms.PSet(histName = cms.string("PF75"),
#                                                   numPtCut = cms.double(75.),
#                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
#                                               ),
#
#                                          cms.PSet(histName = cms.string("PF60"),
#                                                   numPtCut = cms.double(60.),
#                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
#                                               ),
#
#                                          cms.PSet(histName = cms.string("PF45"),
#                                                   numPtCut = cms.double(45.),
#                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
#                                               ),
#
#                                          cms.PSet(histName = cms.string("PF40"),
#                                                   numPtCut = cms.double(40.),
#                                                   numPtName = cms.string("hltPFJetFilterTwoC30"),
#                                               ),
#                                      ),
#                                      pathsToPass = cms.vstring(),
#                                      jets = cms.InputTag("slimmedJets"),
#                                      L1Jets = cms.InputTag("caloStage2Digis","Jet"),
#                                      truthJets = cms.InputTag("slimmedGenJets"),
#                                      truthParts = cms.InputTag("prunedGenParticles"),
#                                      AlgInputTag = cms.InputTag("gtStage2Digis"),
#                                      ExtInputTag = cms.InputTag("gtStage2Digis"),
#                                  )
#
#
#process.triggerStudyPassNJet = process.triggerStudy.clone()
#process.triggerStudyPassNJet.offlinePreSelection = cms.PSet(minNSelJet = cms.uint32(2))
#
#
#process.triggerStudyPassPreSelMed = process.triggerStudy.clone()
#process.triggerStudyPassPreSelMed.offlinePreSelection = cms.PSet(minNSelJet = cms.uint32(2),
#                                                                 minNTagMedJet = cms.uint32(2))
#
#
#process.p = cms.Path(process.triggerStudy + process.triggerStudyPassNJet + process.triggerStudyPassPreSelMed)


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
