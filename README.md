# bx_bot

This module collects and references the treasure tables from the Moldvay Basic D&D Rules Set.

You can print out a treasure type with: print_table(treasure_type)
if you want to roll the dice for yourself.

If you want the dice rolled for you, use: gen_and_print(treasure_type).

If you want to manipulate the treasure in some way, you can get it as a list using the command: generate_treasure(t_type).
Note that the last entry in this list is the total xp value of the treasure.

Use this at your own risk. There is no error correction or garbage collection.

I wrote this for use with a Slack bot, which I'm not distributing at this time because the code is cobbled together garbage. If you want to integrate this into a Slack bot, I recommend you do it! It's great! Slack + Hangouts is my preferred way to play old-school D&D online. If you want to try it out, you'll do better to get instructions on how to set up a Slack bot from a Google search than from me.
