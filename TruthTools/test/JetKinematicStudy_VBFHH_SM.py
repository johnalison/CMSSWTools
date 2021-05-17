from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')

options.parseArguments()

from CMSSWTools.TruthTools.JetKinematicStudyBase import process, cms

nTruthBosons = 2


members = [attr for attr in dir(process) if not callable(getattr(process, attr)) and not attr.startswith("__")]

for m in members:
    if hasattr(getattr(process,m),"nTruthBosons" ):
        setattr(getattr(process,m),"nTruthBosons",cms.uint32(nTruthBosons))


process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))



# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)



process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/20BB8453-87B9-704B-833F-94790C015EA3.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/0617FE59-7FF7-B64B-9CF2-E837C98154FB.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1738379B-DEEE-F44B-A906-199435CD6C8C.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/CE1254A1-67BE-024C-9C28-3D1419C7968F.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1CE97BFD-C3C8-6049-B76B-BDA877CCC66B.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1768956B-C7C8-9F44-852F-71FE416C92E8.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/50E0E4EE-308C-F449-96B3-C9944E00F27C.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/4D442350-B37B-2041-BA43-3696DA5BB58F.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/62A356D2-7B0C-2246-89FA-DF9F08E9988B.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/AAA6CA3F-DE1A-764C-A7FD-43BC85A47A3E.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/85EBB140-28A0-194A-B3DF-51715E147AC5.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/F93F7C48-5731-6B4A-B976-31ECB8B5E494.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/FE3800E6-745B-B14E-A8B9-DC4C0898AB10.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/48271980-A0F0-404F-B282-BCD46589E24A.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/17FDC4F3-FF23-3048-8D41-A43760749B49.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/73ADA5A3-ADD6-AB4B-8211-C208D1820861.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/4FAD55A5-FCFB-FE4D-B8DA-030F2A153E7B.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/DEF71437-EE21-B942-9B22-A35DAAEB8E17.root',
        '/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/BBD59F80-E4A5-3D49-B402-543F097FE5BF.root',

    )
)

