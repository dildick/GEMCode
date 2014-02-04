#ifndef GEMValidation_TrackMatcher_h
#define GEMValidation_TrackMatcher_h

/**\class TrackMatcher

 Description: Matching of tracks to SimTrack

 Original Author:  "Sven Dildick"
*/

#include "GEMCode/GEMValidation/src/CSCDigiMatcher.h"
#include "GEMCode/GEMValidation/src/TFTrack.h" 
#include "GEMCode/GEMValidation/src/TFCand.h" 
#include "GEMCode/GEMValidation/src/GMTRegCand.h" 
#include "GEMCode/GEMValidation/src/GMTCand.h" 
#include "GEMCode/GEMValidation/src/L1Extra.h" 

class TrackMatcher// : public CSCStubMatcher
{
 public:
  /// constructor
  TrackMatcher();
  /// copy constructor
  TrackMatcher(const TrackMatcher&);
  /// destructor
  ~TrackMatcher();

  const std::vector<TFTrack*>& tfTracks() const {return tfTracks_;}
  TFTrack* bestTFTrack(bool sortPtFirst=1);
  const std::vector<TFCand*>& tfCands() const {return tfCands_;}
  TFCand* bestTFCand(bool sortPtFirst=1);
  const std::vector<GMTRegCand*>& gmtRegCands() const {return gmtRegCands_;}
  GMTRegCand* bestGmtRegcand(bool sortPtFirst=1);
  const std::vector<GMTCand*>& gmtCands() const {return gmtCands_;}
  GMTCand* bestGmtcand(bool sortPtFirst=1);
  const std::vector<L1Extra*>& l1Extras() const {return l1Extras_;}
  L1Extra* bestL1Extra(bool sortPtFirst=1);
  
 private:
  std::vector<TFTrack*> tfTracks_;
  std::vector<TFCand*> tfCands_;
  std::vector<GMTRegCand*> gmtRegCands_;
  std::vector<GMTCand*> gmtCands_;
  std::vector<L1Extra*> l1Extras_;
};

#endif
