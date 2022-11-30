import re

def sbl_normalization(text):

  normalized = ""

  pattern = r"([\s\u05BE\u05C0\u05C3\u05D0-\u05EA])([\u0591-\u05BD\u05BF\u05C1\u05C2\u05C4\u05C5\u05C7]*)"

  norm_classes = {
    "\u0307": 230, 
    "\u0591": 220, 
    "\u0592": 230, 
    "\u0593": 230, 
    "\u0594": 230, 
    "\u0595": 230, 
    "\u0596": 220, 
    "\u0597": 230, 
    "\u0598": 230, 
    "\u0599": 232, 
    "\u059A": 222, 
    "\u059B": 220, 
    "\u059C": 230, 
    "\u059D": 230, 
    "\u059E": 230, 
    "\u059F": 230, 
    "\u05A0": 230, 
    "\u05A1": 230, 
    "\u05A2": 220, 
    "\u05A3": 220, 
    "\u05A4": 220, 
    "\u05A5": 220, 
    "\u05A6": 220, 
    "\u05A7": 220, 
    "\u05A8": 230, 
    "\u05A9": 232, 
    "\u05AA": 220, 
    "\u05AB": 230, 
    "\u05AC": 230, 
    "\u05AD": 222, 
    "\u05AE": 232, 
    "\u05AF": 230,
    "\u05B0": 220, 
    "\u05B1": 220, 
    "\u05B2": 220, 
    "\u05B3": 220, 
    "\u05B4": 220, 
    "\u05B5": 220, 
    "\u05B6": 220, 
    "\u05B7": 220, 
    "\u05B8": 220, 
    "\u05B9": 27, 
    "\u05BA": 27, 
    "\u05BB": 220, 
    "\u05BC": 21, 
    "\u05BD": 220, 
    "\u05BF": 23, 
    "\u05C1": 10, 
    "\u05C2": 11, 
    "\u05C4": 230, 
    "\u05C5": 220, 
    "\u05C7": 220
 }

  for match in re.findall(pattern, text):

    normalized += match[0]

    if len(match[1]) < 2:
      normalized += match[1]

    else:
      normalized += "".join(sorted(match[1], key=lambda x : norm_classes[x]))

  return normalized

def is_sbl_normalized(text):

  return sbl_normalization(text) == text
