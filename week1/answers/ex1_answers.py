"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
For part A, I got correct anwers for all three cases .The plain context returned the "The Haymarket Vaults" while
XML and Sandwich contexts returned "The Albanach".  The model with primary bias should return "The Albanach" and this 
was the case for both XML and Sandwich contexts. The plain context returned "The Haymarket Vaults" which is also correct 
but it is not the primary bias. The  "The Albanach" might be choosen in XML and Sandwich contexts because of the structured tags.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
I think the "The Hollyrood Arms" is the hardest distractor because it is has satisfies 
the sompe containts and it is similar to the correct answer "The Haymarket Vaults". 
The capacity of 160 and vegan = yes are the same as the correct answer and 
it is also a pub. The only thing that made it a wrong answer is that the status=full 
 while the correct one should be status=available. 
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Even with the small model (google/gema-2-2b) the results were correct for all three contexts. 
The answer was Haymarket Vaults for all three context, the effect of primary bias was less or not visible 
in the small model. Also another thing to note is that the distractors well also not able 
to change the answer in the small model, this may be due to the small short data set . The answer had "The Haymarket Vaults" 
in the structured context but "The " is missing .
 """

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
While the experment for this exercise was designed to show the effect of context formating in the low singal-to-noise ratio,
the used model was able to get correct answer for the small dataset but what I have observed is that in part C in the Plain context
the answer was "Haymarket Vaults" without "The" , which isnt a big deal here but there might be cases where these small details matter or 
changes the answer completely. I think proper context formatting is important to get better objective results on the tasks .
"""
