import json

PROMPT_TEMPLATE = """
This is a dialogue (Dialogue) from the Wuthering Waves game. Of course, you must already know it. Your task is to translate all dialogues and analogs into natural Thai, making them sound like real conversations with proper emotions based on the context. You must focus only on the character dialogues in the game and format the output as JSON as follows:

The data I provide comes from using computer vision to read in-game screenshots. 

Normally, in games with dialogue, players don't get only one response choice. However, when I provide you with the extracted text, it may appear merged together—even if they are separate response options. Your job is to differentiate them and determine which ones are similar in meaning, as they could be distinct player responses.

You must think and process everything in either English or Thai only—absolutely no other languages.

For player responses, if the translated sentence naturally includes polite endings like ครับ/ค่ะ and DON'T use XX ผม or นาย XX **USE ฉัน เธอ intends**, you must omit them to avoid making the response unnatural or confusing.

If A1 is has something wrong maybe it's alien word, you can skip it. You should understand it's a computer vision and maybe it missing or ghost detected and if wrong **if you can make it right, please do it**.

**Only some word, If it's a Game's specifically vocab you can skip that word for translation, BUT YOU NEED to continue translate conversation.**
**"A1" is a A1 from character, so you need to translate this too and "B1" is all B1 that game give player select you need to translate too, if "B1" is nothing that mean no option, So you can make it null. YOU NEED TO TRANSLATE BOTH**
DATA I GIVE YOU: {data} 

THIS IS JUST A FORMAT EXAMPLE:

"A1": "",
"B1": [""],[""],[""] "unlimit if it have more (please parse it be careful and separate it with array)"
]

Each response should contain only one JSON set at a time. If you think there are multiple, you may have misread or incorrectly separated the text.

**Don't text anymore without json and without data i sent you, Because my program listening your answer and it support just json format.**
"""

def collect_data():
    with open("data.jsonl", "a", encoding="utf-8") as file:
        while True:
            a1 = input("Enter A1 (or type /exit to quit): ").strip()
            if a1.lower() == "/exit":
                print("Exiting... Data saved.")
                break

            b1_options = []
            while True:
                b1 = input("Enter B1 option (or /next to proceed, /skip to discard): ").strip()
                if b1.lower() == "/next" or b1.lower() == "":
                    break
                elif b1.lower() == "/skip":
                    print("Skipping this entry...")
                    return  # Don't save anything for this entry
                b1_options.append(b1)

            context = input("Enter context (or /skip to leave empty): ").strip()
            if context.lower() == "/skip":
                context = ""

            # Generate the translation request prompt
            translation_prompt = PROMPT_TEMPLATE.format(data=json.dumps({"A1": a1, "B1": b1_options}, ensure_ascii=False))
            print("\nProvide the translation for the following:\n")
            print(translation_prompt)
            translated_a1 = input("Translated A1: ").strip()
            translated_b1_options = [input(f"Translated B1 ({b1}): ").strip() for b1 in b1_options]

            # Prepare JSON entry
            data_entry = {
                "instruction": translation_prompt,
                "context": context,
                "response": {"A1": translated_a1, "B1": translated_b1_options},
                "category": "wuthering_waves"
            }
            
            # Save as JSONL
            file.write(json.dumps(data_entry, ensure_ascii=False) + "\n")
            print("Data saved!")

if __name__ == "__main__":
    collect_data()
