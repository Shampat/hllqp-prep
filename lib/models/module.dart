class ModuleInfo {
  final String id;
  final String name;
  final String assetFile;
  final String icon;
  final String color;
  final String description;

  const ModuleInfo({
    required this.id,
    required this.name,
    required this.assetFile,
    required this.icon,
    required this.color,
    required this.description,
  });
}

const List<ModuleInfo> allModules = [
  ModuleInfo(id: 'life', name: 'Life Insurance', assetFile: 'assets/questions/life_questions.json', icon: '❤️', color: '#2196F3', description: 'Term, Whole Life, UL, Participating'),
  ModuleInfo(id: 'accident_sickness', name: 'Accident & Sickness', assetFile: 'assets/questions/accident_sickness_questions.json', icon: '🏥', color: '#4CAF50', description: 'Disability, Health, Travel'),
  ModuleInfo(id: 'disability', name: 'Disability Insurance', assetFile: 'assets/questions/disability_questions.json', icon: '🦽', color: '#FF9800', description: 'Disability benefits & riders'),
  ModuleInfo(id: 'critical_illness', name: 'Critical Illness', assetFile: 'assets/questions/critical_illness_questions.json', icon: '🫀', color: '#E91E63', description: 'CI definitions & claims'),
  ModuleInfo(id: 'segregated_funds', name: 'Segregated Funds', assetFile: 'assets/questions/seg_funds_questions.json', icon: '📊', color: '#9C27B0', description: 'Seg funds, guarantees, resets'),
  ModuleInfo(id: 'annuities', name: 'Annuities', assetFile: 'assets/questions/annuities_questions.json', icon: '💰', color: '#795548', description: 'Annuity types & taxation'),
  ModuleInfo(id: 'estate', name: 'Estate Planning', assetFile: 'assets/questions/estate_questions.json', icon: '🏠', color: '#607D8B', description: 'Estate, trusts, wills'),
  ModuleInfo(id: 'taxation', name: 'Taxation', assetFile: 'assets/questions/taxation_questions.json', icon: '🧾', color: '#009688', description: 'Tax rules for insurance'),
  ModuleInfo(id: 'ethics', name: 'Ethics & Professionalism', assetFile: 'assets/questions/ethics_questions.json', icon: '⚖️', color: '#3F51B5', description: 'Ethics, compliance, disclosure'),
];
