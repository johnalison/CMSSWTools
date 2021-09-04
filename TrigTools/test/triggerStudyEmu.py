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
    #globalTag = "102X_upgrade2018_realistic_v15"
    globalTag = "106X_upgrade2018_realistic_v16_L1v1"
else:
    #globalTag = "102X_upgrade2018_realistic_v21"
    #globalTag = "102X_dataRun2_v14"
    globalTag = "106X_dataRun2_v35"
    #106X_dataRun2_v33
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
process.GlobalTag.globaltag = globalTag


if options.isMC:
    process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring("/store/mc/RunIISummer20UL18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/10000/DEB42E22-D25F-4B45-BB61-2E76E94A678E.root")
    )
else:
    process.source = cms.Source("PoolSource",
                                #fileNames = cms.untracked.vstring("/store/data/Run2018D/MuonEG/MINIAOD/12Nov2019_UL2018_rsb-v1/20000/003E1A62-7AB4-7741-98E8-CE6A66AD68DA.root")
                                #fileNames = cms.untracked.vstring("/store/data/Run2018B/MuonEG/MINIAOD/UL2018_MiniAODv2-v1/30000/2FEA8B87-4A57-1948-B119-8FF1B6682F1A.root")
                                fileNames = cms.untracked.vstring("/store/data/Run2018A/MuonEG/MINIAOD/UL2018_MiniAODv2-v1/30000/904042EA-9CDB-474A-9899-AA750746EAB4.root")
                                

    )


process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))



# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)


process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")


## PFchs selection
process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))


postfix = "PFlow"

#jetSource = 'ak4Jets'
pfCandidates = 'packedPFCandidates'
pvSource = 'offlineSlimmedPrimaryVertices'
svSource = 'slimmedSecondaryVertices'
muSource = 'slimmedMuons'
elSource = 'slimmedElectrons'
jetSource = 'slimmedJets'
patJetSource = 'selectedUpdatedPatJets'+postfix

jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
if not options.isMC:
    jetCorrectionsAK4[1].append('L2L3Residual')


bTagInfos = [
    'pfImpactParameterTagInfos'
   ,'pfSecondaryVertexTagInfos'
   ,'pfInclusiveSecondaryVertexFinderTagInfos'
   ,'pfSecondaryVertexNegativeTagInfos'
   ,'pfInclusiveSecondaryVertexFinderNegativeTagInfos'
   ,'softPFMuonsTagInfos'
   ,'softPFElectronsTagInfos'
#   ,'pfInclusiveSecondaryVertexFinderCvsLTagInfos'
#   ,'pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos'
   ,'pfDeepFlavourTagInfos'
]


bTagDiscriminators = set([
#    'pfJetBProbabilityBJetTags'
#   ,'pfJetProbabilityBJetTags'
#   ,'pfPositiveOnlyJetBProbabilityBJetTags'
#   ,'pfPositiveOnlyJetProbabilityBJetTags'
    #,'pfNegativeOnlyJetBProbabilityBJetTags'
   #,'pfNegativeOnlyJetProbabilityBJetTags'
#   ,'pfTrackCountingHighPurBJetTags'
#   ,'pfTrackCountingHighEffBJetTags'
    #,'pfNegativeTrackCountingHighPurBJetTags'
    #,'pfNegativeTrackCountingHighEffBJetTags'
#   ,'pfSimpleSecondaryVertexHighEffBJetTags'
#   ,'pfSimpleSecondaryVertexHighPurBJetTags'
    #,'pfNegativeSimpleSecondaryVertexHighEffBJetTags'
    #,'pfNegativeSimpleSecondaryVertexHighPurBJetTags'
    'pfCombinedSecondaryVertexV2BJetTags'
#   ,'pfPositiveCombinedSecondaryVertexV2BJetTags'
    #,'pfNegativeCombinedSecondaryVertexV2BJetTags'
   ,'pfCombinedInclusiveSecondaryVertexV2BJetTags'
#   ,'pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags'
    #,'pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'softPFMuonBJetTags'
#   ,'positiveSoftPFMuonBJetTags'
    #,'negativeSoftPFMuonBJetTags'
   ,'softPFElectronBJetTags'
#   ,'positiveSoftPFElectronBJetTags'
    #,'negativeSoftPFElectronBJetTags'
   ,'pfCombinedMVAV2BJetTags'
    #,'pfNegativeCombinedMVAV2BJetTags'
#   ,'pfPositiveCombinedMVAV2BJetTags'
#   ,'pfCombinedCvsBJetTags'
    #,'pfNegativeCombinedCvsBJetTags'
#   ,'pfPositiveCombinedCvsBJetTags'
#   ,'pfCombinedCvsLJetTags'
    #,'pfNegativeCombinedCvsLJetTags'
#   ,'pfPositiveCombinedCvsLJetTags'
    # DeepCSV
  , 'pfDeepCSVJetTags:probudsg'
  , 'pfDeepCSVJetTags:probb'
  , 'pfDeepCSVJetTags:probc'
  , 'pfDeepCSVJetTags:probbb'
#  , 'pfNegativeDeepCSVJetTags:probudsg'
#  , 'pfNegativeDeepCSVJetTags:probb'
#  , 'pfNegativeDeepCSVJetTags:probc'
#  , 'pfNegativeDeepCSVJetTags:probbb'
#  , 'pfPositiveDeepCSVJetTags:probudsg'
#  , 'pfPositiveDeepCSVJetTags:probb'
#  , 'pfPositiveDeepCSVJetTags:probc'
#  , 'pfPositiveDeepCSVJetTags:probbb'
    # DeepFlavour
  , 'pfDeepFlavourJetTags:probb'
  , 'pfDeepFlavourJetTags:probbb'
  , 'pfDeepFlavourJetTags:problepb'
  , 'pfDeepFlavourJetTags:probc'
  , 'pfDeepFlavourJetTags:probuds'
  , 'pfDeepFlavourJetTags:probg'
#  , 'pfNegativeDeepFlavourJetTags:probb'
#  , 'pfNegativeDeepFlavourJetTags:probbb'
#  , 'pfNegativeDeepFlavourJetTags:problepb'
#  , 'pfNegativeDeepFlavourJetTags:probc'
#  , 'pfNegativeDeepFlavourJetTags:probuds'
#  , 'pfNegativeDeepFlavourJetTags:probg'
    # DeepFlavour with pruned input
#   , 'pfDeepFlavourPrunedJetTags:probb'
#   , 'pfDeepFlavourPrunedJetTags:probbb'
#   , 'pfDeepFlavourPrunedJetTags:problepb'
#   , 'pfDeepFlavourPrunedJetTags:probc'
#   , 'pfDeepFlavourPrunedJetTags:probuds'
#   , 'pfDeepFlavourPrunedJetTags:probg'
#   , 'pfNegativeDeepFlavourPrunedJetTags:probb'
#   , 'pfNegativeDeepFlavourPrunedJetTags:probbb'
#   , 'pfNegativeDeepFlavourPrunedJetTags:problepb'
#   , 'pfNegativeDeepFlavourPrunedJetTags:probc'
#   , 'pfNegativeDeepFlavourPrunedJetTags:probuds'
#   , 'pfNegativeDeepFlavourPrunedJetTags:probg'
])


from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import _patJets as patJetsDefault
storedDiscriminators = set([x.value() for x in patJetsDefault.discriminatorSources])
print "INFO: Removing b-tag discriminators already stored in MiniAOD (with the exception of JP taggers)"
jptaggers = {i for i in bTagDiscriminators if 'ProbabilityBJetTags' in i or i.startswith('pfDeepCSV')}
bTagDiscriminators = (bTagDiscriminators - storedDiscriminators) | jptaggers
print "bTagDiscriminators are"
print bTagDiscriminators

## Reco jets
from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
process.ak4Jets = ak4PFJets.clone(src = cms.InputTag('pfCHS'), doAreaFastjet = True, srcPVs = cms.InputTag(pvSource))

## Load standard PAT objects (here we only need PAT muons but the framework will figure out what it needs to run using the unscheduled mode)
process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

from PhysicsTools.PatAlgos.tools.jetTools import *

updateJetCollection(
        process,
        jetSource = cms.InputTag(jetSource),
        jetCorrections = jetCorrectionsAK4,
        pfCandidates = cms.InputTag(pfCandidates),
        pvSource = cms.InputTag(pvSource),
        svSource = cms.InputTag(svSource),
        muSource = cms.InputTag(muSource),
        elSource = cms.InputTag(elSource),
        btagInfos = bTagInfos,
        btagDiscriminators = list(bTagDiscriminators),
        explicitJTA = False,
        postfix = postfix
    )


# Need ?
process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')



#-------------------------------------
## Add TagInfos to PAT jets
for i in ['patJets',  
          'updatedPatJetsTransientCorrected']:
    m = i + postfix
    if hasattr(process,m) and getattr( getattr(process,m), 'addBTagInfo' ):
        print "Switching 'addTagInfos' for " + m + " to 'True'"
        setattr( getattr(process,m), 'addTagInfos', cms.bool(True) )






#electron id
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)


# Set up electron ID (VID framework)
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
switchOnVIDElectronIdProducer(process, dataFormat=DataFormat.MiniAOD)
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff']
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)


#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v
#HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v


#process.hltL1sMu5EG23IorMu5IsoEG20IorMu7EG23IorMu7IsoEG20IorMuIso7EG23  # L1
#hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter   # EMU DZ

#from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL17
#process.pileupJetIdUpdated = process.pileupJetId.clone( 
#        jets=cms.InputTag(patJetSource),
#        inputIsCorrected=True,
#        applyJec=False,
#        vertexes=cms.InputTag("offlineSlimmedPrimaryVertices"),
#        algos = cms.VPSet(_chsalgos_106X_UL17),
#    )


#
#  TurnOns for HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v
#
from CMSSWTools.TrigTools.TurnOns_EMuPFBtagDeepCSV_2018 import triggerConfig_EMuPFBtagDeepCSV, triggerStudyBase_EMuPFBtagDeepCSV
triggerStudyBase_EMuPFBtagDeepCSV.isMC = cms.bool(options.isMC)
triggerStudyBase_EMuPFBtagDeepCSV.jets = cms.InputTag(patJetSource)
triggerStudyBase_EMuPFBtagDeepCSV.vtxColl = cms.InputTag("offlineSlimmedPrimaryVertices")
#triggerStudyBase_EMuPFBtagDeepCSV.offlineBeamSpot = cms.InputTag("")
triggerStudyBase_EMuPFBtagDeepCSV.electronColl = cms.InputTag("slimmedElectrons")
triggerStudyBase_EMuPFBtagDeepCSV.conversions = cms.InputTag("reducedEgamma:reducedConversions")
#        cutBasedElectronID-Fall17-94X-V2-medium
triggerStudyBase_EMuPFBtagDeepCSV.electronIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-medium")
triggerStudyBase_EMuPFBtagDeepCSV.muonColl = cms.InputTag("slimmedMuons")
triggerStudyBase_EMuPFBtagDeepCSV.metColl = cms.InputTag("slimmedMETs")


from CMSSWTools.TrigTools.TurnOns_Ht330_4j_3b_2018 import triggerConfigL1Unprescaled_Ht330_4j_3b, triggerConfig_Ht330_4j_3b, triggerConfigL1HTQuadJet_Ht330_4j_3b, triggerConfigL1HT_Ht330_4j_3b
from CMSSWTools.TrigTools.TurnOns_2b116_2018       import triggerConfigL1Unprescaled_2b116


hltSeeds = [("",     cms.vstring()), 
            ("PreSelEMu_",cms.vstring("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v")),
            #("PreSelEMu2j30_",cms.vstring("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v")),
            #("HT250",cms.vstring("HLT_PFHT250_v")),
            ]

# HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v"),
# HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v


L1Seeds_EMuPFBtagDeepCSV = [("HLT_EMu",                    triggerConfig_EMuPFBtagDeepCSV, True),
                            ("HLT_Ht330_4j_3b",            triggerConfigL1Unprescaled_Ht330_4j_3b, False),
                            ("HLT_Ht330_4j_3b_L1OR",       triggerConfig_Ht330_4j_3b, False),
                            ("HLT_Ht330_4j_3b_L1HT",       triggerConfigL1HT_Ht330_4j_3b, False),
                            ("HLT_Ht330_4j_3b_L1HTQuadJet",triggerConfigL1HTQuadJet_Ht330_4j_3b, False),
                            ("HLT_2b116",                  triggerConfigL1Unprescaled_2b116, False),
                        ]

offlinePreSelection = [("",             cms.PSet(minNSelMuon = cms.uint32(0)), False),

                       ("_offEMu",      cms.PSet(minNSelMuon = cms.uint32(1), minNSelElec = cms.uint32(1)), True),

                       ("_offEmu2Jet",     cms.PSet(minNSelMuon = cms.uint32(1), minNSelElec = cms.uint32(1),
                                                 minNSelJet = cms.uint32(2)), True),

                       ("_offEmu2Tag",     cms.PSet(minNSelMuon = cms.uint32(1), minNSelElec = cms.uint32(1),
                                                 minNSelJet = cms.uint32(2),
                                                 minNTagJet = cms.uint32(2)),True), 
                   ]

process.analyzerSeq = cms.Sequence( )
#process.p = cms.Path()

#process.analyzerSeq *= process.pileupJetIdUpdated

for h in hltSeeds: 
    
    hltName = h[0]


    for o in offlinePreSelection:
        
        offName = o[0]
        offPreSelection = o[1]
        doJetTurnOns = o[2]

        #
        #   EMU
        #
        for l in L1Seeds_EMuPFBtagDeepCSV:
         
            l1Name = l[0]

            hltPreSelection = h[1]
            filtersToPass = l[1]
            doJetTurnOnsL1 = l[2]

            triggerStudyConfigured = triggerStudyBase_EMuPFBtagDeepCSV.clone()
            triggerStudyConfigured.filtersToPass = filtersToPass
            triggerStudyConfigured.offlinePreSelection = offPreSelection
            triggerStudyConfigured.hltPreSelection = hltPreSelection
            fullName = "triggerStudy_EMuPFBtagDeepCSV_"+hltName+l1Name+offName

            if not doJetTurnOns or not doJetTurnOnsL1:
                print "Turning off jet turn ons for selection ",fullName
                triggerStudyConfigured.jetTurnOns = cms.VPSet()



            setattr(process,fullName,triggerStudyConfigured)
            process.analyzerSeq *= getattr(process,fullName)










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

#print process.dumpPython()



#Trick to make it work in 9_1_X
process.tsk = cms.Task()
for mod in process.producers_().itervalues():
    process.tsk.add(mod)
for mod in process.filters_().itervalues():
    process.tsk.add(mod)


from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()



process.p = cms.Path(
    process.allEvents
    #* process.filtSeq
    #* process.selectedEvents
    * process.analyzerSeq,
    process.tsk
)


open('pydump.py','w').write(process.dumpPython())


