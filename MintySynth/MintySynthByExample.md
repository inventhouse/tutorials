# MintySynth By Example
_By Benjamin Holt_

([PDF Version](./MintySynthByExample.pdf))

Here is one basic, reasonably efficient, workflow I've come up with for programming songs on the MintySynth; it's just a starting point, by all means experiment and find what works well for you.

I've annotated the steps below with the control notation I came up with for my [quick reference card](./MintySynthMiniRef.pdf); briefly:

**+** = "together" (usually first-one-first), **|** = hold button, **.** = press button, **w** = wheel, **x-y** = “choose one of” (here sometimes "do each"), **↑**/**↓** = full up/down

- Turn the MintySynth on to start fresh.

- Use the mixer to turn down all four parts (**|5+w1-w4 ↓**) to quiet the initial tones; it’s good that the synth has some output by default, but I just turn that off to get it out of the way.

- Switch to live mode (**.1+.5**, see the yellow LED start blinking.)  Aside, when switching between live and programming modes, I think of "throwing" the LED: .1+.5 sends the tempo blinks from the red (near button 1) to the yellow LED (near button 5) and vice-versa to switch back (though when going to program mode you also choose which part, .1-.4)

- Choose voices to be your palette for the programmed parts.  (**|1-|4+w1**)

- Switch to programming part 1 (**.5+.1**, see the red LED start blinking again.) and turn part 1 back up.  (**|5+w1 ↑**)

- Select one of your voice buttons (**.1-.4**) (though you can go back and change the part’s voice later.)  

- Perhaps choose a scale.  (**|1+w5**)

- Hold button 1 and sequence the first measure of part 1.  (**|1+w1-w4**, ↓ turns that note off, ↑ takes the "reference note" see [Pitch Wheel Quirks](./README.md#pitch-wheel-quirks))

- Skip measure 2 for now and hold button 3, nudge each wheel and return it to position to sequence the same thing in.  (**|3+w1-w4**)

- You can now similarly sequence measures 2 & 4 for an A-B-A-B structure or do different things for A-B-A-C (**|2+w1-w4**, **|4+w1-w4**) (of course, you can also program all different sequences, too.)

- Experiment with tempo (**w1**), duration (**w3**), envelope (**w4**), modulation (**|5+w5**, ↓ to turn back off), etc.  ***Don't touch w2!*** It will change one of the notes you just programmed to something weird; see [Pitch Wheel Quirks](./README.md#pitch-wheel-quirks).

- Use the mixer to turn part 1 down (more or less, depending on how much you want to keep hearing it) and turn part 2 up.  (**|5+w1 ↓**, **|5+w2 ↑**)

- Switch to programming part 2.  (**.5+.2**)

- Repeat with the other parts you want to program; if you have a system like bassline in part 1, percussion(ish) in part 2, melody in part 3, etc. it's easier to build and work with.  (**.5+.3**)

- The mixer is your friend; use it to solo parts, mute others, “check in on” the whole, whatever helps you hear what you’re doing.  (**|5+w1-w4**)

- If you want, you can “really” sequence part 4 or treat it like a rhythm track and just program which notes you want to sound, since live mode takes over the pitch.  (**.5+.4**)

- Switch to live mode (**.1+.5**) and reprogram your bank of voices for more options.  (**|1-|4+w1**)

- Jam!  Experiment!  Have fun!  For more about live mode, see the [Quick Start](https://mintysynth.com/MintySynth%202.0%20Quick%20Start%20guide.pdf)

- Don’t be shy with the mixer here either; build parts in, drop some drops, cut parts that are sounding repetitive for a while, keep things lively.   (**|5+w1-w4**)

---
