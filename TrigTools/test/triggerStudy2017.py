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
    globalTag = "94X_mc2017_realistic_v14"
else:
    globalTag = "94X_dataRun2_ReReco_EOY17_v2"

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
    

#
# Input data
#
# MC  dasgoclient -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring("/store/mc/RunIIAutumn18MiniAOD/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8D07021F-FD00-D442-B0E6-9077266B320B.root")
                            #)
if options.isMC:
    from CMSSWTools.TrigTools.ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8_RunIIFall17MiniAODv2_MINIAODSIM import ZH_HToBB_ZToBB_source
    process.source = ZH_HToBB_ZToBB_source
else:
    process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring("/store/data/Run2017C/JetHT/MINIAOD/17Nov2017-v1/30000/1EAC0263-39D5-E711-8937-4C79BA180A7B.root"),
    )

process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))


# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)

#
#  TurnOns for HT330 + 4j + 3b
#
from CMSSWTools.TrigTools.TurnOns_Ht300_4j_3b_2017 import triggerConfig_Ht300_4j_3b, triggerConfigL1Unprescaled_Ht300_4j_3b, triggerStudyBase_Ht300_4j_3b
triggerStudyBase_Ht300_4j_3b.isMC = cms.bool(options.isMC)
triggerStudyBase_Ht300_4j_3b.isBBMC = cms.bool(options.isMC)

#
#  TurnOns for 2b
#
from CMSSWTools.TrigTools.TurnOns_2b100_2017 import triggerConfig_2b100, triggerConfigL1Unprescaled_2b100, triggerStudyBase_2b100
triggerStudyBase_2b100.isMC = cms.bool(options.isMC)
triggerStudyBase_2b100.isBBMC = cms.bool(options.isMC)



hltSeeds = [("",     cms.vstring()), 
            ("HT180",cms.vstring("HLT_PFHT180_v")),
            ("HT250",cms.vstring("HLT_PFHT250_v")),
            ]

L1Seeds_ht_4j = [("HLTOnly",       triggerConfig_Ht300_4j_3b),
                 ("L1Unprescaled", triggerConfigL1Unprescaled_Ht300_4j_3b),
             ]

L1Seeds_2j100 = [("HLTOnly",       triggerConfig_2b100),
                 ("L1Unprescaled", triggerConfigL1Unprescaled_2b100),
                 ]

offlinePreSelection = [("",             cms.PSet()),
                       ("PassNJet",     cms.PSet(minNSelJet = cms.uint32(4))),
                       ("PassPreSel",   cms.PSet(minNSelJet = cms.uint32(4),
                                                 minNTagTightJet = cms.uint32(4))), 
                       #("PassPreSelMed",cms.PSet(minNSelJet = cms.uint32(4),
                       #                          minNTagMedJet = cms.uint32(4))), 
                   ]


process.p = cms.Path()



for h in hltSeeds: 
    
    hltName = h[0]
    
    for o in offlinePreSelection:
        
        offName = o[0]
        offPreSelection = o[1]

        #
        #   HT300_4j_3b
        #
        for l in L1Seeds_ht_4j:
         
            l1Name = l[0]


            hltPreSelection = h[1]
            filtersToPass = l[1]

            triggerStudyConfigured = triggerStudyBase_Ht300_4j_3b.clone()
            triggerStudyConfigured.filtersToPass = filtersToPass
            triggerStudyConfigured.offlinePreSelection = offPreSelection
            triggerStudyConfigured.hltPreSelection = hltPreSelection

            fullName = "triggerStudy_Ht300_4j_3b_"+hltName+l1Name+offName

            setattr(process,fullName,triggerStudyConfigured)
            process.p *= getattr(process,fullName)


        #
        #   2b100
        #
        for l in L1Seeds_2j100:
         
            l1Name = l[0]

            hltPreSelection = h[1]
            filtersToPass = l[1]

            triggerStudyConfigured = triggerStudyBase_2b100.clone()
            triggerStudyConfigured.filtersToPass = filtersToPass
            triggerStudyConfigured.offlinePreSelection = offPreSelection
            triggerStudyConfigured.hltPreSelection = hltPreSelection

            fullName = "triggerStudy_2b100_"+hltName+l1Name+offName

            setattr(process,fullName,triggerStudyConfigured)
            process.p *= getattr(process,fullName)






#
#  Trigger Emulation
#
from CMSSWTools.TrigTools.TriggerEmulation2017 import triggerEmulation

triggerEmulation.isMC = cms.bool(options.isMC)
triggerEmulation.isBBMC = cms.bool(options.isMC)


for o in offlinePreSelection:

    offName = o[0]
    offPreSelection = o[1]

    triggerEmulationConfigured = triggerEmulation.clone()
    triggerEmulationConfigured.offlinePreSelection = offPreSelection

    fullName = "triggerEmulation"+offName

    setattr(process,fullName,triggerEmulationConfigured)
    process.p *= getattr(process,fullName)


#
#  Trigger Study
#
from CMSSWTools.TrigTools.TriggerCombStudy2017 import triggerCombStudy

triggerCombStudy.isMC = cms.bool(options.isMC)
triggerCombStudy.isBBMC = cms.bool(options.isMC)

for o in offlinePreSelection:

    offName = o[0]
    offPreSelection = o[1]

    triggerCombStudyConfigured = triggerCombStudy.clone()
    triggerCombStudyConfigured.offlinePreSelection = offPreSelection

    fullName = "triggerCombStudy"+offName

    setattr(process,fullName,triggerCombStudyConfigured)
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
