import re

# simple keyword rules
KEYWORD_MAP = {
    'harappan': 'Harappan Civilization',
    'city planning': 'Urban Planning',
    'ashoka': 'Ashokan Edicts',
    'edicts': 'Ashokan Edicts',
    'burzahom': 'Rock‑cut Shrines',
    'chandraketugarh': 'Terracotta Art',
    'ganeshwar': 'Copper Artefacts',
    'revenue': 'Revenue/Land System',
    'brahmin': 'Brahmadeya',
    'tank': 'Village Tank Revenue',
    'scientific': 'History of Indian Science',
    'instrument': 'Ancient Indian Surgery',
    'sine': 'Trigonometry in Ancient India'
}


def rule_based(text):
    found = set()
    t = text.lower()
    for kw, concept in KEYWORD_MAP.items():
        if re.search(r'\b' + re.escape(kw) + r'\b', t):
            found.add(concept)
    return list(found)
