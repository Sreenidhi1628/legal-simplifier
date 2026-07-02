RISK_KEYWORDS = [
    "penalty", "termination", "liable", "forfeit",
    "eviction", "breach", "indemnify", "arbitration",
    "jurisdiction", "non-refundable", "waive", "lawsuit",
    "legal action", "default", "seizure", "blacklist",
    "fine", "sue", "court", "damages"
]

def detect_risks(text):
    risks = []
    sentences = text.split(".")
    for sentence in sentences:
        for keyword in RISK_KEYWORDS:
            if keyword.lower() in sentence.lower():
                risks.append({
                    "clause": sentence.strip(),
                    "risk_word": keyword
                })
                break
    return risks
