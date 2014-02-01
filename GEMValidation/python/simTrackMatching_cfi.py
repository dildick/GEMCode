import FWCore.ParameterSet.Config as cms

SimTrackMatching = cms.PSet(
    # common
    useCSCChamberTypes = cms.untracked.vint32(0,1,2,3,4),
    ntupleTrackChamberDelta = cms.bool(True),
    ntupleTrackEff = cms.bool(True),
    overrideminNHitsChamber = cms.bool(False),
    minNHitsChamber = cms.untracked.int32(4),
    ## per collection params
    simTrack = cms.PSet(
        input = cms.InputTag('g4SimHits'),
        minPt = cms.double(1.5),
        maxPt = cms.double(999.),
        minEta = cms.double(1.5),
        maxEta = cms.double(2.5),
        onlyMuon = cms.bool(True),
        requireVertex = cms.bool(True),
        requireGenPart = cms.bool(True),
    ),
    ## RPC
    rpcSimHit = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag('g4SimHits','MuonRPCHits'),
        simMuOnly = cms.bool(True),
        discardEleHits = cms.bool(True),
    ),
    rpcDigi = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simMuonRPCDigis"),
        minBX = cms.int32(-1),
        maxBX = cms.int32(1),
        matchDeltaStrip = cms.int32(1),
    ),
    ## ME0
    me0SimHit = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag('g4SimHits','MuonME0Hits'),
        simMuOnly = cms.bool(True),
        discardEleHits = cms.bool(True),
    ),
    ## GEM
    gemSimHit = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag('g4SimHits','MuonGEMHits'),
        simMuOnly = cms.bool(True),
        discardEleHits = cms.bool(True),
    ),
    gemDigi = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simMuonGEMDigis"),
        minBX = cms.int32(-1),
        maxBX = cms.int32(1),
        matchDeltaStrip = cms.int32(1),
    ),
    gemPad = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simMuonGEMCSCPadDigis"),
        minBX = cms.int32(-1),
        maxBX = cms.int32(1),
     ),
    gemCoPad = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simMuonGEMCSCPadDigis", "Coincidence"),
        minBX = cms.int32(-1),
        maxBX = cms.int32(1),
    ),
    gemRecHit = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("gemRecHits"),
        minBX = cms.int32(-1),
        maxBX = cms.int32(1),
        matchDeltaStrip = cms.int32(1),
    ),
    ## CSC
    cscSimHit = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag('g4SimHits','MuonCSCHits'),
        simMuOnly = cms.bool(True),
        discardEleHits = cms.bool(True),
        minNHitsChamber = cms.int32(4),
    ),
    cscStripDigi = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simMuonCSCDigis", "MuonCSCComparatorDigi"),
        minBX = cms.int32(3),
        maxBX = cms.int32(9),
        matchDeltaStrip = cms.int32(1),
        minNHitsChamber = cms.int32(4),
    ),
    cscWireDigi = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simMuonCSCDigis", "MuonCSCWireDigi"),
        minBX = cms.int32(3),
        maxBX = cms.int32(8),
        matchDeltaWG = cms.int32(1),
        minNHitsChamber = cms.int32(4),
    ),
    cscCLCT = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simCscTriggerPrimitiveDigis"),
        minBX = cms.int32(3),
        maxBX = cms.int32(9),
        minNHitsChamber = cms.int32(4),
    ),
    cscALCT = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simCscTriggerPrimitiveDigis"),
        minBX = cms.int32(3),
        maxBX = cms.int32(8),
        minNHitsChamber = cms.int32(4),
    ),
    cscLCT = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simCscTriggerPrimitiveDigis"),
        minBX = cms.int32(3),
        maxBX = cms.int32(8),
        minNHitsChamber = cms.int32(4),
        addGhosts = cms.bool(True),
    ),
    cscMPLCT = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simCscTriggerPrimitiveDigis", "MPCSORTED"),
        minBX = cms.int32(3),
        maxBX = cms.int32(8),
        minNHitsChamber = cms.int32(4),
        addGhosts = cms.bool(True),
    ),
    ## TFTrack
    tfTrack = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simCsctfTrackDigis"),
    ),
    ## CSC TFTracks
    tfCand = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simCsctfDigis", "CSC"),
   ),
    ## GMTCand
    gmtCand = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("simGmtDigis"),   
    ),
    ## L1Extra
    l1Extra = cms.PSet(
        verbose = cms.int32(0),
        input = cms.InputTag("l1extraParticles"),
    ),
)
