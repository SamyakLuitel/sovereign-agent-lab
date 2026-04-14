"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = [ "search_venues","get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "It seems there are no Edinburgh venues currently available that can accommodate 300 guests with vegan options. Would you like to:\n\n1. Try a lower minimum capacity (e.g., 250 people)?\n2. Check for venues with vegetarian options instead?\n3. See available venues without dietary filters?\n\nLet me know how you'd like to adjust the search."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
After changing  the he Albanach's status to 'full' in mcp_venue_server.py, it
disappeared entirely from Query 1's search results  and  the tool returned only
one match (The Haymarket Vaults) instead of two.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
In exercise 2 , the tools were imported from another file venue_tools.py  and adding or importing new tools 
means editing the venue_tools.py file and then importing it in the exercise2_langgraph.py file while in exercise 4
 with the MCP client there is no need to edit any file to add a new tool as long as it is discoverable by the MCP server
and it is registered in the server it can be used by the agent without any code change which makes it more flexible and easier 
to maintain as you can add or remove tools without changing the agent code.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The architecture would consist of a Planner , a shared MPC tool server  , an Executor, Coordinator, and the Structured Rasa CALM flow for the agent, 

- The Planner will use some strong reasoning model and take the input from whatsapp from the user.

- The executor will be a ReAct agent and will be made using langgraph and this will call MCP tools and handle failures if any like venue being full.

- The MCP server will serve as tool to provide single source of truth to executor and also to the structured flow 

- The Structured flow will have access to the shared MCP tools and will have an extended knowledge base with RAG

- The Coordinator  this will act as a coordination layer that detects when the Executor has confirmed the venue and triggers the Structured flow to take over.

"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph reAct agent will be better for research as it is able to reason and also handle non deterministic workflow better . I can independently decide relevant tool calling to see what it can do or not based on the experiment i did in the earlier exercise 
I think Rasa CALM agent suits for the call because the call is for a commitment and the structured flow forces a hard rule that cannot be overridden by a probabilistic model.While running the Rasa flow it was able to stop when the deposit exceeded the max amount 
or when I experimented with the time and it stopped such type of hard validation flow is good for the flow 
"""