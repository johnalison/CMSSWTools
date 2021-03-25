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
    globalTag = "94X_mcRun2_asymptotic_v3"
else:
    globalTag = "80X_dataRun2_2016LegacyRepro_v4"

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
    from CMSSWTools.TrigTools.ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8_RunIISummer16MiniAODv3_MINIAODSIM import ZH_HToBB_ZToBB_source
    process.source = ZH_HToBB_ZToBB_source
else:
    process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring("/store/data/Run2016G/JetHT/MINIAOD/07Aug17-v1/110000/D2542926-547E-E711-876A-484D7E8DF0D3.root")
                                #fileNames = cms.untracked.vstring("/store/data/Run2016G/JetHT/MINIAOD/07Aug17-v1/110000/041CA316-887D-E711-8C62-008CFA197D10.root")
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
from CMSSWTools.TrigTools.TurnOns_4j_3b_2016 import triggerConfig_4j_3b, triggerConfigL1Unprescaled_4j_3b, triggerStudyBase_4j_3b
triggerStudyBase_4j_3b.isMC = cms.bool(options.isMC)
triggerStudyBase_4j_3b.isBBMC = cms.bool(options.isMC)

#
#  TurnOns for 2b
#
from CMSSWTools.TrigTools.TurnOns_2b100_2016 import triggerConfig_2b100, triggerConfigL1Unprescaled_2b100, triggerStudyBase_2b100
triggerStudyBase_2b100.isMC = cms.bool(options.isMC)
triggerStudyBase_2b100.isBBMC = cms.bool(options.isMC)


#
#  TurnOns for 2b
#
from CMSSWTools.TrigTools.TurnOns_2j_2j_3b_2016 import triggerConfig_2j_2j_3b, triggerConfigL1Unprescaled_2j_2j_3b, triggerStudyBase_2j_2j_3b
triggerStudyBase_2j_2j_3b.isMC = cms.bool(options.isMC)
triggerStudyBase_2j_2j_3b.isBBMC = cms.bool(options.isMC)



hltSeeds = [("",     cms.vstring()), 
            ("HT125",cms.vstring("HLT_PFHT125_v")),
            ("HT200",cms.vstring("HLT_PFHT200_v")),
            ]

L1Seeds_4j = [("HLTOnly",       triggerConfig_4j_3b),
              ("L1Unprescaled", triggerConfigL1Unprescaled_4j_3b),
          ]

L1Seeds_2j100 = [("HLTOnly",       triggerConfig_2b100),
                 ("L1Unprescaled", triggerConfigL1Unprescaled_2b100),
                 ]

L1Seeds_2j_2j_3b = [("HLTOnly",       triggerConfig_2j_2j_3b),
                    ("L1Unprescaled", triggerConfigL1Unprescaled_2j_2j_3b),
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
        #   4j_3b
        #
        for l in L1Seeds_4j:
         
            l1Name = l[0]


            hltPreSelection = h[1]
            filtersToPass = l[1]

            triggerStudyConfigured = triggerStudyBase_4j_3b.clone()
            triggerStudyConfigured.filtersToPass = filtersToPass
            triggerStudyConfigured.offlinePreSelection = offPreSelection
            triggerStudyConfigured.hltPreSelection = hltPreSelection

            fullName = "triggerStudy_4j_3b_"+hltName+l1Name+offName

            if not options.isMC:
                triggerStudyConfigured.trigObjs = cms.InputTag("selectedPatTrigger")

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
            if not options.isMC:
                triggerStudyConfigured.trigObjs = cms.InputTag("selectedPatTrigger")

            fullName = "triggerStudy_2b100_"+hltName+l1Name+offName

            setattr(process,fullName,triggerStudyConfigured)
            process.p *= getattr(process,fullName)


        #
        #   2j_2j_3b
        #
        for l in L1Seeds_2j_2j_3b:
         
            l1Name = l[0]

            hltPreSelection = h[1]
            filtersToPass = l[1]

            triggerStudyConfigured = triggerStudyBase_2j_2j_3b.clone()
            triggerStudyConfigured.filtersToPass = filtersToPass
            triggerStudyConfigured.offlinePreSelection = offPreSelection
            triggerStudyConfigured.hltPreSelection = hltPreSelection
            if not options.isMC:
                triggerStudyConfigured.trigObjs = cms.InputTag("selectedPatTrigger")

            fullName = "triggerStudy_2j_2j_3b_"+hltName+l1Name+offName

            setattr(process,fullName,triggerStudyConfigured)
            process.p *= getattr(process,fullName)






#
#  Trigger Emulation
#
from CMSSWTools.TrigTools.TriggerEmulation2016 import triggerEmulation

triggerEmulation.isMC = cms.bool(options.isMC)
triggerEmulation.isBBMC = cms.bool(options.isMC)


for o in offlinePreSelection:

    offName = o[0]
    offPreSelection = o[1]


    triggerEmulationConfigured = triggerEmulation.clone()
    triggerEmulationConfigured.offlinePreSelection = offPreSelection
    if not options.isMC:
        triggerEmulationConfigured.trigObjs = cms.InputTag("selectedPatTrigger")

    fullName = "triggerEmulation"+offName

    setattr(process,fullName,triggerEmulationConfigured)
    process.p *= getattr(process,fullName)


#
#  Trigger Study
#
from CMSSWTools.TrigTools.TriggerCombStudy2016 import triggerCombStudy

triggerCombStudy.isMC = cms.bool(options.isMC)
triggerCombStudy.isBBMC = cms.bool(options.isMC)

for o in offlinePreSelection:

    offName = o[0]
    offPreSelection = o[1]

    triggerCombStudyConfigured = triggerCombStudy.clone()
    triggerCombStudyConfigured.offlinePreSelection = offPreSelection
    if not options.isMC:
        triggerCombStudyConfigured.trigObjs = cms.InputTag("selectedPatTrigger")

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
