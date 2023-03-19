import re
import json

with open("florida.txt", "r") as f:
    text = f.read()
    pattern = '<.*?>'
    replacement = ''
    text = re.sub(pattern, replacement, text)
    pattern = '"'
    replacement = ''
    text = re.sub(pattern, replacement, text)

    pattern = r"NO. OF CUES:  (\d*)"
    replacement = r"NO. OF CUES:  \1 ~~"
    text = re.sub(pattern, replacement, text)
    # print(text3)
    text = text.replace(r"\n", "\n")
    # print(fixed_text)
    pattern = r'(.*?)~~'
    matches = re.findall(pattern, text, flags=re.DOTALL)

    data = dict()
    counter = len(matches)
    for match in matches:

        # node word
        word = re.search(r"([A-Z].*?)FSG", match)[1].strip()
        # string of association - word + data
        associations = re.findall(r'(.*0.*)\n', match)

        # no. of ties
        cues = re.search(r'CUES: *(\d*)', match)[1]

        assoc = dict()
        for a in associations:

            # assoc word
            name = re.search(" ([A-Z].*?)0", a)[1].strip()

            # initialize dict for data of assoc word & parse data string
            assoc[name] = dict()
            values = re.search(r'0\.(\d*)\.(\d*)\.(\d*)\.(\d*) *(\d*) *(\d*) *(\d*) *(\d*) *(\d*\.\d*) *(\d*\.\d*) *(\d*) *(\d*)', a)

            val_names = ["FSG", "BSG", "MSG", "OSG", "QSS", "TSS", "QFR", "TFR", "QMC", "TMC", "QUC", "TUC"]

            x = 1
            for val in val_names:
                assoc[name][val] = values[x]
                x += 1

        data[word] = dict()
        data[word]["cues"] = cues
        data[word]["associations"] = assoc
        counter -= 1
        print(counter)

    print("dict done, time to write")

    with open("data_florida.json", "w") as destination:
        json.dump(data, destination)












