from gtts import gTTS 
import os
from playsound import playsound 

def text_to_speech(text, lang='hi'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = "output.mp3"
        tts.save(filename)
        print(f"ऑडियो फ़ाइल '{filename}' के रूप में सहेजी गई।")
        if playsound:
            playsound(filename)
        else:
            print("ऑडियो चलाने के लिए 'playsound' लाइब्रेरी इंस्टॉल नहीं है। कृपया '{}' फ़ाइल को मैन्युअल रूप से चलाएँ।"  .format(filename))
        os.remove(filename)
    except Exception as e:
        print(f"एक त्रुटि हुई: {e}")
if __name__ == "__main__":
    while True:
        input_text = input("टेक्स्ट लिखें जिसे आप सुनना चाहते हैं (या 'exit' दबाएँ): ")
        if input_text.lower() == 'exit':
            break
        if input_text:
            text_to_speech(input_text)
        else:
            print("कृपया कुछ टेक्स्ट लिखें।")
from gtts import gtts
import os
from playsound import playsound 

def text_to_speech(text, lang='hi'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = "output.mp3"
        tts.save(filename)
        print(f"ऑडियो फ़ाइल '{filename}' के रूप में सहेजी गई।")
        if playsound:
            playsound(filename)
        else:
            print("ऑडियो चलाने के लिए 'playsound' लाइब्रेरी इंस्टॉल नहीं है। कृपया '{}' फ़ाइल को मैन्युअल रूप से चलाएँ।".format(filename))
        os.remove(filename)
    except Exception as e:
        print(f"एक त्रुटि हुई: {e}")

if __name__ == "__main__":
    while True:
        input_text = input("टेक्स्ट लिखें जिसे आप सुनना चाहते हैं (या 'exit' दबाएँ): ")
        if input_text.lower() == 'exit':
            break
        if input_text:
            text_to_speech(input_text)
        else:
            print("कृपया कुछ टेक्स्ट लिखें।")
