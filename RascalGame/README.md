Rascal
======
_A [Scoundrel] Variant_

[Scoundrel] ([BGG]) is a brilliant dungeon-crawling [roguelike] solitaire card game concept; however it has some mechanics I don't care for in the ways they make outcome depend on luck at least as much as player choices.  I also feel like the concept all-but-demands an "inventory", so I developed this variant.

[Scoundrel]: http://stfj.net/art/2011/Scoundrel.pdf
[BGG]: https://boardgamegeek.com/boardgame/191095/scoundrel
[roguelike]: https://en.wikipedia.org/wiki/Roguelike

Setup
-----
Start with a standard 52-card deck (jokers are not used), separate high red cards (J,Q,K,A ♦️/♥️); these can be used as the "life counter" by assigning 1-4 to J-A (1+2+3+4 = 10 x 2 suits = 20 life)

When damage is taken turn the appropriate value of life points face down; when life points are restored, turn that value back face-up.  Life points can never go above 20; if they ever go below one, the game is lost.

Thoroughly shuffle remaining cards (2-A ♣️/♠️, 2-10 ♦️/♥️); this will be the "dungeon" where:
- Black cards (♣️/♠️) are monsters and do damage equal to their value (2-A = 2-14).
- Diamonds (♦️) are weapons, and prevent damage based on their value, but degrade a point with each use.  You can have only one weapon equipped a time.
- Hearts (♥️) are healing potions and restore life points up to their value up to the starting life of 20, but only one potion per round is effective.

Layout is up to you and/or the space you are playing; you will need to have a place for the dungeon face-down, your life counter, four room cards face-up, a discard pile, an equipped weapon stack, and an inventory item.

Gameplay
--------
Play is a series of four card "rooms".

Upon "entering" a room, you may choose to fight or flee; if you flee, all four room cards are scooped up and added back to the bottom of the dungeon to come up again later.  You may not flee two rooms in a row.

If you fight, cards may be dealt with in any order, but only one at a time:
- ♦️ When equipping a weapon, any previously held weapon must be discarded.
- ♣️/♠️ Fighting a monster can be done with or without your equipped weapon.  Fighting barehanded, you take the full damage and discard the monster.  Fighting with your weapon deducts the weapon's current value from the damage taken (face value minus the number of previously vanquished monsters); place the monster on the weapon card to help track its degraded value.
- ♥️ Taking a healing potion restores life points immediately and is discarded.

Weapons or potions in the room may also simply be discarded.

When three of the room cards have been disposed of, you have the option to moving to the next room and the remaining card carries over.  Deal cards from the top of the dungeon back up to four.

You win when the dungeon is cleared.

Special Rules
-------------
### Inventory
You also have one inventory slot, however you cannot access it (either to store or retrieve an item) when any monsters are present.  If the room has been cleared of all four cards, the inventory item can be dropped and will carry over as normal.

### Knife
The 2♦️ can be added to your equipped weapon, increasing its effectiveness; after the combination has been used twice, however, the "knife" and the two monster cards it helped slay are discarded.

Balance
-------
As-designed, Rascal is very winnable; no, not every dungeon can be beaten, and mis-steps are often costly, but if you're making good choices about conserving resources, etc. you win most of the time.  That's how I like it.  There are also many ways you can tune the game; a few ideas follow.

### Pull Cards
The deck is already literally stacked against you; when you think about it, that means that pulling red cards (especially ♦️) will make it harder to win, moreso than removing black cards will make it easer.

On the flip-side, using another mechanism for a life-counter and adding a high-value red card would tilt the game significantly in your favor.

### Tweak Special Rules
You could drop the "knife" rule.  Even harder, pull the 2♦️; though it seems of minimal value (which is the main reason I added the knife rule), it means one less monster in a room, which can make all the difference.

You could drop the inventory rule, forcing more discards of mid-value items.  Or, relaxing some of the inventory rules could make it easier: access even if a monster is carrying over, or even access during combat.
