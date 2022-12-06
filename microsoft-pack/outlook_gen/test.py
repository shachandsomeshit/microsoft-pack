# Error = 0
# solution = 0
# SoundCaptchaText = SoundCaptchaText.replace(".", "")
# SoundCaptchaText = SoundCaptchaText.split(" ")
# if SoundCaptchaText[2] == "Option":
#     Error+=1
#     solution=1
# elif SoundCaptchaText[2] == "option":
#     Error+=1
#     solution=1
# try:
#     find_option_2 = SoundCaptchaText.index("2")
# except ValueError:
#     find_option_2 = SoundCaptchaText.index("two")
# except ValueError:
#     find_option_2 = SoundCaptchaText.index("to")
# except ValueError:
#     raise Exception("SpeechRecognitionError")
# if SoundCaptchaText[find_option_2+1] == "Option":
#     Error+=1
#     solution=2
# elif SoundCaptchaText[find_option_2+1] == "option":
#     Error+=1
#     solution=1
# try:
#     find_option_3 = SoundCaptchaText.index("three")
# except ValueError:
#     find_option_3 = SoundCaptchaText.index("3")
# except ValueError:
#     find_option_3 = SoundCaptchaText.index("tree")
# except ValueError:
#     raise Exception("SpeechRecognitionError")
# try:
#     SoundCaptchaText[find_option_3+1]
# except IndexError:
#     Error+=1
#     solution=3

# if Error > 1:
#     pass
# print("Errors:" + str(Error))
# print("solution:" + str(solution))


if "options" == "Options":
    print("mark")

