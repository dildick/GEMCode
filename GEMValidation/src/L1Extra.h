#ifndef GEMValidation_L1Extra_h
#define GEMValidation_L1Extra_h

class L1Extra : GMTCand
{
 public:
  L1Extra();
  ~L1Extra();

  /*  
  init(const L1MuRegionalCand *t, CSCTFPtLUT* ptLUT, 
       edm::ESHandle< L1MuTriggerScales > &muScales, 
       edm::ESHandle< L1MuTriggerPtScale > &muPtScale);
  */
  //  const L1MuionalCand * l1cand;
  GMTCand* gmtCand();
  
 private:
  double pt_;
  double eta_;
  double phi_;
  double dr_;
};

#endif
