import FWCore.ParameterSet.Config as cms

process = cms.Process("GEMDIGIANA")

## Standard sequence
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

## TrackingComponentsRecord required for matchers
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')

## global tag for 2019 upgrade studies
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

# the analyzer configuration
process.load('GEMCode.GEMValidation.GEMDigiAnalyzer_cfi')
process.GEMDigiAnalyzer.simTrackMatching.cscComparatorDigi.input = ""
process.GEMDigiAnalyzer.simTrackMatching.cscWireDigi.input = ""
process.GEMDigiAnalyzer.simTrackMatching.cscCLCT.input = ""
process.GEMDigiAnalyzer.simTrackMatching.cscALCT.input = ""
process.GEMDigiAnalyzer.simTrackMatching.cscLCT.input = ""
process.GEMDigiAnalyzer.simTrackMatching.cscMPLCT.input = ""
process.GEMDigiAnalyzer.simTrackMatching.tfTrack.input = ""
process.GEMDigiAnalyzer.simTrackMatching.tfCand.input = ""
process.GEMDigiAnalyzer.simTrackMatching.gmtCand.input = ""
process.GEMDigiAnalyzer.simTrackMatching.l1Extra.input = ""
process.GEMDigiAnalyzer.simTrackMatching.gemRecHit.input = ""

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring("file:out_digi.root")
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("gem_digi_ana.root")
)

process.p = cms.Path(process.GEMDigiAnalyzer)

