text = 'X-DSPAM-Confidence:    0.8475'
stext = text[text.find(':')+1:]
n = float(stext.strip())
print(n)
