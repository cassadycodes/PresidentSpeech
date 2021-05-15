"""
Cassady Shoaff | Montclair State University | APLN580 Corpus Linguistics | Spring 2021
Text cleaning to remove non-president's speech
FINAL VERSION
"""
import pathlib
import re

president = "biden"

text = ""
# loading the files
for path in pathlib.Path(president).iterdir(): # using pathlib so we can avoid the other files
    if path.is_file() and f"{president}_speeches" in path.name:
        file = open(path, "r") # file = open(path, "rb") <- use if special characters in text
        raw = file.read() #.decode(errors='replace') <- ^^^ 
        text += raw
        # ^^^ this is probably horribly inefficient but I can't remember why
        file.close()

## Remove non-presidential speech
# delete white house address
whitehouse = "The White House\s+1600 Pennsylvania Ave NW\s+Washington, DC 20500\s+.+"
text = re.sub(whitehouse, "", text)

# delete "THE PRESIDENT:" labels
thepres = "THE PRESIDENT:" 
text = re.sub(thepres, "", text)
# this has to be taken out individually rather than in the [A-Z] step
# because of inconsistent use of dialogue tags by the transcribers

# delete somebody else talking
questions = "[A-Z]+\s+.+\n+" # starts with ALLCAPS ends with newline
text = re.sub(questions, "", text)
# this must come after the PRESIDENT step because otherwise it also removes president speech

# remove parenthetical comments like (Laughs.) and (The document is signed.)
parenthesis = "\(.+\)"
text = re.sub(parenthesis, "", text)

# remove footer
footer = "We'll be in touch with the latest information on how President Biden and his administration are working for the American people, as well as ways you can get involved and help our country build back better."
text = re.sub(footer, "", text)

# remove the metadata headers
parenthesis = "\<.+\>"
text = re.sub(parenthesis, "", text)

# lastly, clean up line breaks. sometimes paragraph doesn't start/end with space so we add it
text = re.sub("\n", " ", text) # **this step MUST be last because we used \n in regex above!

# final check
print(text)

# save cleaned text
file = open(f"{president}_cleaned.txt", "w", encoding="utf-8")
file.writelines(text)
file.close()
