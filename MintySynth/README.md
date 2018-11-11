# MintySynth Supplementary Docs

[MintySynth](https://mintysynth.com) is a remarkable little Arduino-based sequencer / synthesizer I picked up from [Adafruit](https://www.adafruit.com/product/2648); it is a really well-done kit that packs a **LOT** of noisemaking capability into a very small and inexpensive package.

The [Quick Start](https://mintysynth.com/MintySynth%202.0%20Quick%20Start%20guide.pdf) is great to start having fun right away, and the [manual](https://mintysynth.com/MintySynth%20Software%20Manual%204.2.pdf) covers all the myriad things it can do, but there were a couple guides I wished I had - so I wrote them:

- [An example workflow](./MintySynthByExample.md) - There are a lot of modes and options and whatnot, this is a walk-through showing one way they can fit together into a composing and playing workflow.

- [A quick-reference card](./MintySynthMiniRef.pdf) - Once you've read the manual, this can help you find all the control combinations in one place.  It is organized into three panels, two for the controls and one that explains the compact notation I devised.  There are two versions, one that shows the concepts in bold and the other highlighting the controls; use whichever is clearest to you.  It can be cut out, folded, and kept in the tin.

## Pitch Wheel Quirks

I found the behavior of the pitch wheel (**w2**) somewhat complicated and not always what I expected / wanted; here I try to document it in detail:

In live mode, the pitch wheel overrides part 4 note value except note-off.

In program mode, the pitch wheel sets the current part’s “reference note”; for part 1 this is the first note of measure 1; for part 2, the first note of measure 2, etc.  You can set other notes in the sequence to this reference by turning their wheel all the way up (↑)

If you have sequenced that note to be something else the pitch wheel will override and reset it.  However, if you set the reference note, then reprogram it, notes set with ↑ still take their value from the pitch wheel.

Notes set with ↑ copy the current value of the pitch wheel / reference note and do not “follow” it.

__How I Wish The Pitch Wheel Worked__

In live mode, I wish the MintySynth reverted to playing part 4 as programmed after a measure of no pitch wheel movement.

In program mode, I want the pitch wheel to only affect notes set to the "reference note", **NEVER** change any note I've programmed to something else, and all notes set to the reference should follow the pitch wheel while programming that part.

---
