#Giraffe Language
#vowel -> g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":   #can be written also as .. if letter.lower() in "aeiou": -->see below
                translation = translation + "g"
        else:
                translation = translation + letter
    return translation

print(translate(input("Enter phrase:")))



#def translate(phrase):
    #translation = ""
    #for letter in phrase:
      #  if letter.lower() in "aeiou":
       #     if letter.isupper:
        #        translation = translation + "g"
         #   else:
          #      translation = translation + letter
        #return translation

#print(translate(input("Enter phrase: ")))
