# Generators, Sockets, and Our Project

## Week 4 objective
1. Review generator functions with yield
1. Use inline generators
1. Create a socket to listen
1. Connect to a socket
1. Vote on raw sockets vs. Django
1. (optional?) Review the skeleton of a django app before deciding?
1. Wrap up any questions/concerns about what we have covered so far or what may have been left out.

## Generator Functions
Functions with at least one "yield"
Order of evaluation is interesting

## Inline Generators
More like a comprehension than a function
syntax can definitely be confusing
has very good performance in some use cases

## Sockets!
What is a port, ip address, resolved name, etc.
All of the lingo around listening, connecting, sending

## Django?
Handles three major things so we don't have to write "boilerplate" code ourselves:
1. Socket connections
2. URL resolution
3. Database connections

## Quick Review / Questions
Going back over the list of keywords from week 1 and making sure we have the basics at an acceptable level of understanding.

## Project Description
We will make an application from classes, functions, connections, data storage, and interactive components.
The application will manage a small bingo game.
The bingo game will have several foundational concepts including the bingo card, daubing numbers, winning patterns, ball caller, and game lifetime.
-The player can buy bingo cards from the bingo hall at a certain price.
-Each color of bingo card has a different list of winning patterns and prizes.
-The player must claim the prizes for them to be awarded.
-A caller calls out the balls that have been chosen and in what order.
-The game ends when a player claims the final prize "cover all" and is verified.
