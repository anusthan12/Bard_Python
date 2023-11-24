from bardapi import Bard
import os
os.environ["_BARD_API_KEY"] = "Xwis-87uHPl5Qhk8q29A5dEoJdFKyp4I1HMouwqvcdgRRwoLm4Qeig4NFBrbtcHxaUVW_g."
message = input("Enter Your Prompt: ")
print(Bard().get_answer(str(message))['content'])