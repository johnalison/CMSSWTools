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
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/2548BA6C-B720-0D41-BCE6-4F9DDF35E635.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/CDDFB44F-4196-DB4F-A007-DC92451270B8.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/27CA998E-2DA3-D24F-902A-B40CB73CC68E.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/874B2D41-95E5-494F-814A-0D74E17624F3.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/4A41995E-E372-4E45-8FEB-C99CA23026A1.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/00BCD371-163E-0F4E-BB83-4DE14BA23B41.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/24A9A14B-AF8D-0C4A-BAF2-D68BA14872BF.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/579D331D-2D73-6A45-95C6-622DA42AC501.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/B852EDC3-389E-AF4A-9A74-5A370EC21A73.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/015DC66C-43E1-2F48-B96A-D5BB942C0D24.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/FCCF25AE-C5B2-AE46-B670-1C531AA7162F.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C5175468-32BA-D842-8B13-AE27FCA138A4.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/7422CB44-3A4A-5E44-BD21-8E2BFBA97589.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/DE26947B-18F1-A04F-BC55-8A99673C9919.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/3ADE8FA7-C346-CD4D-BC3A-3B8736A6C4A5.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/30358BC7-AA15-6C42-8E14-000F0EA8C0FB.root",
        "/store/mc/RunIIAutumn18MiniAOD/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/93240100-1DF8-6145-9896-49BB669B9906.root",
    )
)

