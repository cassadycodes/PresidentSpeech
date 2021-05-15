"""
Cassady Shoaff | Montclair State University | APLN580 Corpus Linguistics | Spring 2021
Text cleaning to remove non-president's speech
Trump specific version needed adaptation for special characters and inconsistent formatting
"""
import pathlib
import re

president = "trump"

output = ""
# loading the files
for path in pathlib.Path(president).iterdir(): # using pathlib so we can avoid the other files
    if path.is_file() and f"{president}_speeches" in path.name:
        file = open(path, "rb") # Trump transcripts contain non-unicode so we need "rb"
        text = file.read().decode(errors='replace') # decode replace fixes non-unicode chars

        # remove parenthetical comments like (Applause.) 
        parenthesis = "\(.+?\)" #
        text = re.sub(parenthesis, "", text)
        
        # remove linebreaks ** if you don't, make sure to enable regex dotall
        text = re.sub("\s+", " ", text) # \n newline \r carriage return
        
        # check if this is a standalone speech without dialogue tags
        if "THE PRESIDENT:" not in text:
            
            # remove remarks header
            remarks = "\s+Remarks([\s\S]*?)(?:EST|EDT|CST)"
            text = re.sub(remarks, "", text)
            
            # remove title and date tags
            parenthesis = "\<.+\>"
            text = re.sub(parenthesis, "", text)
            
            # remove END 
            text = re.sub("END", "", text)
            
            output += text
            file.close()
            continue
        
        # if there are dialogue tags, need to exclude non-president speech
        
        # It was pointed out to me that rather than deleting non-president speech 
        # (as I did in the Biden version of the text cleaner) I could instead
        # extract the president's speech directly, while checking each file.
        
        # find everything between "THE PRESIDENT" and the next dialogue tag
        
        speech = "(?s)(?<=THE PRESIDENT:)(.+?)(?=[A-Z\s\.-]*[A-Z]+:|Q\s|$)"

        # regex says: (?s) dotall mode [include spaces]
        #   (?<=THE PRESIDENT:) starts with "THE PRESIDENT:" [lookbehind]
        #   (?=[A-Z\s\.-]*[A-Z]+:|Q|$) ends with "ALL CAPS:" or "Q  " [lookahead]
        #   .*? capture and return all text between
        
        matches = re.findall(speech, text)
        
        # findall returns a list so convert text back to a string
        for match in matches:
            output += match
        file.close()

# final check
print(output)

# save cleaned text
file = open(f"{president}_cleaned.txt", "w", encoding="utf-8")
file.writelines(output)
file.close()

print(f"Saved {president}_cleaned.txt")
