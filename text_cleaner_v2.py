"""
Cassady Shoaff | Montclair State University | APLN580 Corpus Linguistics | Spring 2021
Text cleaning to remove non-president's speech
"""
import pathlib
import re

text = ""
# loading the files
for path in pathlib.Path("biden").iterdir(): # using pathlib so we can avoid the other files
    if path.is_file() and "biden_speeches" in path.name:
        file = open(path, "r")
        text += file.read()
        # ^^^ this is probably horribly inefficient but I don't remember why
        file.close()

## Remove non-presidential speech
# delete white house address
whitehouse = "The White House\s+1600 Pennsylvania Ave NW\s+Washington, DC 20500\s+.+"
text = re.sub(whitehouse, "", text)

# delete somebody else talking
questions = "[A-Z]+\s+.+\n+" # starts with ALLCAPS ends with newline
text = re.sub(questions, "", text)

# delete "THE PRESIDENT:" labels
pres = "THE PRESIDENT:" 
# this has to be taken out individually rather than in the previous step
# because not every instance of a reporter speaking was followed by this label

# remove parenthetical comments like (Laughs.) and (The document is signed.)
parenthesis = "\(.+\)"
text = re.sub(parenthesis, "", text)

# remove [sic] and the word before it
## TODO get previous word. (Joe Biden has a stutter. The transcriber included them.)
sic = "\[sic\]"
text = re.sub(sic, "", text)

# remove the metadata headers
parenthesis = "\<.+\>"
text = re.sub(parenthesis, "", text)

# lastly, clean up line breaks **sometimes paragraph doesn't start/end with space so we add it
text = re.sub("\n", " ", text) # **this step MUST be last because we used \n in regex above

# check
print(text)

# save cleaned text
file = open("biden_cleaned.txt", "w")
file.writelines(text)
file.close()
