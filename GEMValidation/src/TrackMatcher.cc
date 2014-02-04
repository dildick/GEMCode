#include "GEMCode/GEMValidation/src/TrackMatcher.h"

TrackMatcher::TrackMatcher() 
{
}

TrackMatcher::TrackMatcher(const TrackMatcher& rhs) 
{
}

TrackMatcher::~TrackMatcher() 
{
}


//_____________________________________________________________________________
/*
 * Return the best TrackFinder track from a collection of TFTracks
 * Option to sort the TFTracks according to pt
 */
TFTrack* 
TrackMatcher::bestTFTrack(bool sortPtFirst)
{
  return 0;
  /*
  if (tfTracks_.size()==0) return NULL;
  
  // determine max # of matched stubs in the TFTrack collection
  int maxNMatchedMPC = 0;
  for (unsigned i=0; i<tfTracks_.size(); i++) {
    int nst=0;
    for (size_t s=0; s<tfTracks_.at(i).ids.size(); s++) 
      if (tfTracks_.at(i).mplcts[s]->deltaOk) nst++;
    if (nst>maxNMatchedMPC) maxNMatchedMPC = nst;
  }
  // collect tracks with max # of matched stubs
  std::vector<unsigned> bestMatchedTracks;
  for (unsigned i=0; i<tfTracks_.size(); i++) {
    int nst=0;
    for (size_t s=0; s<tfTracks_.at(i).ids.size(); s++) 
      if (tfTracks_.at(i).mplcts[s]->deltaOk) nst++;
    if (nst==maxNMatchedMPC) bestMatchedTracks.push_back(i);
  }
  
  // already found the best TFTrack
  if (bestMatchedTracks.size()==1) return &(tfTracks_[bestMatchedTracks[0]]);
  
  // case when you have more than 1 best TFTrack
  // first sort by quality
  double qBase  = 1000000.;
  // then sort by Pt inside the cone (if sortPtFirst), then sort by DR
  double ptBase = 0.;
  if (sortPtFirst) ptBase = 1000.;
  unsigned maxI = 99;
  double maxRank = -999999.;
  for (unsigned i=0; i<tfTracks_.size(); i++) {
    if (bestMatchedTracks.size()) {
      bool gotit=0;
      for (unsigned m=0;m<bestMatchedTracks.size();m++) if (bestMatchedTracks[m]==i) gotit=1;
      if (!gotit) continue;
    }
    double rr = qBase*tfTracks_.at(i).q_packed + ptBase*tfTracks_.at(i).pt_packed + 1./(0.01 + tfTracks_.at(i).dr);
    if (rr > maxRank) { maxRank = rr; maxI = i;}
  }
  if (maxI==99) return NULL;
  return &(tfTracks_.at(maxI));
  */
}
