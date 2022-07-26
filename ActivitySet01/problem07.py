# Strings
def str():
  #
    text = "X-DSPAM-Confidence:    0.8475"
    string=text.find("0.8475")
    answer=text[string::1]
    finalanswer=float(answer)
    print(finalanswer)

str()