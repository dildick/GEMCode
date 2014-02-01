#ifndef GEMValidation_GMTRegCand_h
#define GEMValidation_GMTRegCand_h

class GMTRegCand : TFCand
{
 public:
  /// constructor
  GMTRegCand();
  /// copy constructor
  GMTRegCand(const GMTRegCand&);
  /// destructor
  ~GMTRegCand();

  /*  
  init(const L1MuRegionalCand *t, CSCTFPtLUT* ptLUT, 
       edm::ESHandle< L1MuTriggerScales > &muScales, 
       edm::ESHandle< L1MuTriggerPtScale > &muPtScale);
  */
  //  const L1MuRegionalCand * l1cand;
  TFCand* tfCand();
  
 private:
  double pt_;
  double eta_;
  double phi_;
  double dr_;
};

#endif
