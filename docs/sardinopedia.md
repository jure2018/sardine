---
hide:
    - navigation
---

The Sardinopedia is a growing collection of interesting **Sardine** patterns. Patterns worthy of inclusion in the Sardinopedia must at least possess one of the following qualities:

- **they are demonstrative**: they demonstrate something made possible by **Sardine**.

- **they are didactic**: they teach you how to use **Sardine**.

- **they are musical**: they have an interesting musical result.

- **they are odd**: they show something odd, unexpected, funny, etc...

This is a collaborative **Sardine** patterns repository. Feel free to contribute by altering the file in your `docs/` folder and to add whatever you see fit! There are some areas where the Sardinopedia is a bit lacking!

## Demonstration patterns

These patterns are small songs and/or long patterns that you can copy and paste to familiarise yourself with the syntax. Change some values, comment a few lines here and there. Try to learn how to move and alter **Sardine** code.


## Basic (Swimming lessons)

This section will help you to grow more confident with *swimming functions*. They must dance before your eyes like a group of sardines swimming in the ocean. They are not really elegant Python code. It's better to be acustomed to using them before attempting to play live.

### Out-of-time

```python3
S('bd').out()
```

This command emits a single bass kick. How? Let's break it down.

1. It uses the [Sender objects](#senders) class generator `S('...')`. 
2. As the parameter is `'bd'`, a string refering to a bass drum, a sample with this file name is searched in the right directory.
3. When the `.out()` method of the Sender object is called, **Sardine** sends a message to SuperCollider which emits the sound.

In **Sardine**, you can use Sender objects outside of a recursive function. It will work, but you will be un-timed, or out-of-time. This technique can be used to trigger long samples, FXs, etc... It can also be used to change (non-periodcally) some values on your MIDI synthesizers or OSC receivers.

### Swimming

```python3
@swim # or @die
def basic():
    print('I am swimming now!')
    again(basic)

hush(basic) # or panic()
```
The most basic function you can write. This is the skeleton of a *swimming function*. You will encounter it everytime you play with **Sardine**.

Behind the stage, the `@swim` decorator will provide all the necessary plumbing required to play sounds.

The `again(...)` function is how the recursion happens, by adding a future execution of the function to the clock.

Redeclaring the function with the `@die` decorator will stop the recursivity, ending the production of sound.

Using `hush(function_name)` will halt the function execution. `panic()` is a more powerful function than `hush`. It will halt all *swimming functions* in **Sardine** and also kill every synthesizer / sampler currently running. This is useful if you feel that you are loosing control when playing with loud or very long samples.


### Swimming with style

```python3
@swim 
def basic(d=0.5, i=0):
    print('I am swimming now!')
    again(basic, d=0.5, i=i+1)

hush(basic)
```

The most common function. A function with a duration and an iterator passed as argument. This is the one you should save as a snippet somewhere in your text editor.

- The `d` parameter is the function's **duration**,  the `0.5` value representing half of a beat.  

- The `i` parameter is an hand-crafted **iterator**, here progressively incremented. It works by adding 1 every time the *swimming function* loops around.

### Drowning in numbers

```python3
@swim 
def basic(d=0.5, i=0, j=0, k=0):
    print(f'I am swimming with {i}, {j}, and k{}!')
    again(basic, d=0.5, i=i+1, j=j+2, k=P('r*10', i))

hush(basic)
```

A function with three different iterators. Why not? Notice how the iterator values are evolving independently. 

`i` is a basic increment, while `j` walks through even numbers. And `k` is randomized using the notation `P('r*10', i)`. To learn more about this, please refer below to [Patterning basics](#patterning-basics) and [Time tokens](#time-tokens).
 
### Swimming with friends

```python3
def calling_you():
    print('I hear you')

@swim 
def basic():
    calling_you()
    again(basic)

hush(basic)
```
A swimming function can call a regular function (*i.e.* a function with no **Sardine** decorator).

### Synchronized Swimming

```python3
@swim
def first():
    print('first!')
    again(second)
def second():
    print('second!')
    again(first)
```
A swimming function calling another one, calling back the first. This is a bit hacky but it is possible.

### Waterpolo

```python3
@swim
def first(d=0.5, rng=0):
    print(f"Received: {rng}")
    rng = randint(1,10)
    print(f"Sending: {rng}")
    again(second, d=0.5, rng=rng)

# evaluate me first
def second(d=0.5, rng=0):
    print(f"Received: {rng}")
    rng = randint(1,10)
    print(f"Sending: {rng}")
    again(first, d=0.5, rng=rng)
```
Feeding one swimming function with the data of another.

### Recursion aliases

The function to perform recursion has multiple names because it is very important: `again`, `anew`, `a`. These aliases all refer to the same low-level function named `c.schedule` that talks directly to **Sardine**'s scheduler.


## Advanced (Swimming fast)

This section requires a good understanding of general **Sardine** concepts. I recommend reading the rest of documentation / *Sardinopedia* before diving into the following section. You need to understand [patterns](#patterning-basics), [senders](#senders), and a few other concepts. Moreover, you don't need it to be a proficient **Sardine** user anyway!

### Swimming at clock speed

```python

@swim 
def fast(d=0.25, i=0):
    S('bd', speed='0.5,2', legato=0.1).out(i, div=4, speed=2)
    S('hh, jvbass:0|8|4,', 
            pan='{0,1,0.1}',
            legato=0.1).out(i, div=8 if rarely()
                    else 5, speed=2)
    S('cp', legato=0.1).out(i, div=8)
    a(fast, d=1/8, i=i+1)
```
**Sardine** swimming functions are usually slow (compared to clock speed). However, you can speed up your recursions by working closer to the **clock tick** level. It means that you will get better rythmic precision, a more fined grained control over time and events and that you can will be able to write more groovy or swinging code. It will also make your LFOs and signal-like patterns much more efficient. 

The recipe for *fast swimming* is the following:

- Use a very fast recursion speed (`1/8`, `1/16`, `1/32`), usually constant (no patterning).

- Play a lot with silences and with the arguments of `.out(iterator, div, speed)`. 

### Fast swimming template

```python
@swim 
def fast(d=0.5, i=0):
    # print("Damn, that's fast!")
    a(fast, d=1/32, i=i+1)
```
This is the template for a fast swimming function. You can skip the iterator if you don't need it or if you wish to use another iteration tool (such as [amphibian variables](#amphibian-variables)). This function is really fast. Uncomment the `print` statement to notice how fast it is. To learn how to control it efficiently, take a look at the following sections about divisors and the speed factor.

### Divisors

```python

@swim 
def fast(d=0.5, i=0):
    S('bd').out(i, div=8)
    a(fast, d=1/16, i=i+1)
```
The `.out()` method as well as the independant `P()` [object](#patterning-freely-p) can take up to three arguments:

- `i` (*int*): the iterator for patterning. **Mandatory** for the two other arguments to work properly. It gives an index on which other operations will be based.

- `div` (*int*): **a timing divisor**. It feels like using a modulo operation. If `div=4`, the event will hit once every 4 iterations. The default is `div=1`, where every event is a hit!

- `speed` (*float*): a speed factor for iterating over pattern values. It will slow down or speed up the speed at which the pattern values are indexed on. For the pattern `1, 2, 3` and a speed of `0.5`, the result will be `1, 1, 2, 2, 3, 3`.

In the above example, we are playing with various divisors to get an interesting rythmic pattern.

```python
@swim 
def fast(d=0.5, i=0):
    S('bd').out(i, div=8)
    S('hh').out(i, div=7)
    S('sd').out(i, div=16)
    a(fast, d=1/16, i=i+1)
```

### Pattern speed

```python
# This is the classic Sardine slow function
@swim 
def slow(d=0.5):
    S('bd, hh, sn, hh').out(i.i)
    a(slow, d=0.25)

hush()    
  
# This is a fast Sardine function
@swim 
def fast(d=1/16):
    S('bd, hh, sn, hh').out(i.i, div=4, speed=1)
    a(fast, d=1/16)
```
The two functions above yield a similar musical result. However, the fast version goes further by making use of all the parameters `.out()` can take. As you can see, there is a `speed` argument determining how fast we should iterate over the values of our pattern. Try altering it to see what is going on!

By default, `speed=1` means that we will move forward to the next index of our patterns for every division (`1`). Changing speed to `2` (`speed=2`) means that we will move forward to the next index of the pattern twice as slow, because it will take 2 divisions to do so. You can also move in a pattern twice as fast (`speed=0.5`), etc...

It is not currently possible to have one speed for each and every value in the pattern. The speed is globally applied to each and every parameter. However, clever use of the pattern notation will allow you to give a duration to each and every event :)

## Senders

### Bassdrum (S)

```python3
@swim
def bd(d=0.5):
    S('bd').out()
    again(bd, d=0.5)
```
A simple bassdrum playing on every half-beat. This is the most basic sound-making function you can write. 

### Bassdrum fun (S)

```python3
@swim
def bd(d=0.5):
    S('bd', speed='r*4', legato='r', cutoff='100+(r*4000)').out()
    again(bd, d=0.25)
```
A simple bassdrum but some parameters have been tweaked to be random.

The additional parameters are :

- `speed` will reverse (<0), slow (0-1), or accelerate the sample (>1) by altering the playback speed. The `r` token provides randomization between `0.0` and `1.0` (*float*).
- `legato` defines the maximum duration of the sample before cutting it, here randomized in the `0` to `1` range that corresponds to a second.
- `cutoff` will attenuate some frequencies. This is the cutoff frequency of a lowpass filter that shuts down frequencies higher to the frequency cutoff. The cutoff frequency is guaranteed to be at least `100` plus a certain amount between `0` and `4000`.

### Breakbeat (S)

```python3
@swim
def bd(d=0.5, i=0):
    S('amencutup:r*20').out(i)
    again(bd, d=0.25, i=i+1)
```
Picking a random sample in a folder containing slices of the classic [amen break](https://en.wikipedia.org/wiki/Amen_break). You could have a successful career doing this in front of audiences. Once again, the *magic* happens with the `sample:r*X` notation, which randomizes which sample is read on each execution, making it unpredictable.

### Sample sequence (S)

```python3
@swim
def bd(d=0.5, i=0):
    S('bd,hh,sn,hh').out(i)
    again(bd, d=0.5, i=i+1)
```
Your classic four-on-the-floor written on one line.

### Piling up samples (S)

```python3
@swim
def pluck(d=0.5, i=0):
    S('pluck').out(i)
    S('pluck:1').out(i)
    S('pluck:2').out(i)
    S('pluck:3').out(i)
    again(pluck, d=0.5, i=i+1)
```
You can stack events easily by just calling `S()` multiple times. In the above example, it happens that `pluck` samples are nicely order and are generating a chord if you struck them in parallel. How cool!

### MIDI Note (M)

```python3
@swim
def midi(d=0.5, i=0):
    M().out()
    again(midi, d=0.5, i=i+1)
```
No argument required to send a MIDI Note (60) at full velocity (127) on the first default MIDI channel. Arguments are only used to specify further or to override default values.

### MIDI Tune (M)

```python3
@swim
def midi(d=0.5, i=0):
    M(note='C5,D5,E5,G5,E5,D5,G5,C5').out(i)
    again(midi, d=0.5, i=i+1)
```
Playing a little melody by tweaking the `note` argument.

### Full MIDI Tune (M)

```python3
@swim
def midi(d=0.5, i=0):
    M(channel='0,1,2,3',
      velocity='20 + (r*80)',
      dur=0.4,
      note='C5,D5,E5,G5,E5,D5,G5,C5').out(i)
    again(midi, d=0.5, i=i+1)
```
The same melody spreaded out on three MIDI channels (one per note) with random velocity.

### Other messages (M)

```python3
@swim
def midi(d=0.5, i=0):
    M(channel='0,1,2,3',
      velocity='20 + (r*80)',
      dur=0.4,
      note='C5,D5,E5,G5,E5,D5,G5,C5').out(i)
    pgch(P('1,2,3,4', i)) # switching
    cc(channel=0, control=20, value=50) # control
    again(midi, d=0.5, i=i+1)
```
Switching between program `1`, `2`, `3` and `4` on your MIDI Synth. Sending a control change on channel `0`, number `20` for a value of `50`.

### Sending OSC (O)

```python3
my_osc = OSC(ip="127.0.0.1", port=23000, name="Bibu", ahead_amount=0.25)
```
This is the command you must use if you would like to create a new OSC client. The `ahead_amount` parameter is used to determine a certain amount of time nudge between calling the OSC Sender and sending the message. It can be useful for synchronisation purposes.

Once this is done, you can use `O()` for sending OSC messages to that address:
```python
# Simple address
O(my_osc, 'loulou', value='1,2,3,4').out()

# Composed address (_ equals /)
O(my_osc, 'loulou/yves', value='1,2,3,4').out()

```
Note how `O()` takes an additional argument compared to other senders. You must provide a valid OSC client for it to work because you can have multiple senders sending at different addresses. Everything else is patternable like usual.

### Receiving OSC (O)

You can also receive and track incoming OSC values. In fact, you can even attach callbacks to incoming OSC messages and turn **Sardine** into a soundbox so let's do it!

```python
info = Receiver(25000)
def funny_sound():
    S('bip', shape=0.9, room=0.9).out()
info.attach('/bip/', funny_sound)
```
Yeah, that's everything you need! In the above example, we are declaring a new `Receiver` object that maps to a given port on the given IP address (with `localhost` being the default). All we have to do next is to map a function to every message being received at that address and poof. We now have a working soundbox. Let's break this down and take a look at all the features you can do when receiving OSC.

Let's take a look at the `Receiver`:
```python
info = Receiver(port, ip, name)
```
You will find your usual suspects: `port`, `ip` and `name` (that is not used for anything useful really). There are three methods you can call on your `Receiver` object:

- `.attach(address: str, function: Callable, watch: bool)` : attach a callback to a given address. It must be a function. Additionally, you can set `watch` to `True` (`False` by default) to also run the `.watch` method automatically afterhands.

- `.watch(address: str)` : give an address. The object will track the last received value on that address. If nothing has been received yet, it will return `None` instead of crashing \o/.

- `.get(address)` : retrieve the last received value to that address. You must have used `.watch()` before to register this address to be watched. Otherwise, you will get nothing.

### Blending OSC in a pattern

If you are receiving something, you can now use it in your patterns to map a captor, a sensor or a controller to a **Sardine** pattern. If you combo this with [amphibian-variables](#amphibian-variables), you can now contaminate your patterns with values coming from your incoming data:

```python
info = Receiver(25000)
info.watch('/sitar/speed/')

@swim 
def contamination(d=0.5, i=0):
    v.a = info.get('/sitar/speed/')['args'][0]
    S('sitar', speed='v.a').out()
    a(contamination, d=0.5, i=i+1)
```

This opens up the way for environmental reactive patterns that can be modified on-the-fly and that will blend code and human interaction.

## Rhythm

### Probability rhythm

```python3
@swim
def bd(d=0.5):
    if often():
        S('bd').out()
    if sometimes():
        S('hh').out()
    else:
        S('pluck').out()
    # condensed 
    S('sd', trig=1 if sometimes() else 0).out()
    again(bd, d=0.5)
```

Building rhythms based on chance that an event will happen. Rolling a dice. These small functions are borrowed from **TidalCycles** that is using them intensively in its very thorough patterning system.

### Binary rhythm

```python3
@swim
def bd(d=0.5, i=0):
    S('bd', trig=bin(20103)).out(i)
    again(bd, d=0.5, i=i+1)
```
Using the binary representation of a number to build a rhythm. You don't need to know what the representation is to get an interesting rhythm out of it. Feed anything to the `bin` function and get something out!

### Euclidian rhythm

```python3
@swim
def bd(d=0.5, i=0):
    S('bd:r*20', trig=euclid(1,4)).out(i)
    S('hh:r*20', trig=euclid(6,8)).out(i)
    S('sd:r*20', trig=euclid(2,4)).out(i)
    again(bd, d=0.5, i=i+1)
```
Building euclidian rhythms by using the `trig` argument. Note that this is not really an euclidian rhythm but it sure does look and feel like it. Trig allows you to skip an event.

### Shifting rhythm

```python3
@swim
def bd(d=0.5, i=0):
    S('bd:r*20', trig=euclid(1,4)).out(i)
    S('hh:r*20', trig=euclid(6,8)).out(i)
    S('sd:r*20', trig=euclid(2,4)).out(i)
    again(bd, d=P('0.5!8, 0.25!4', i), i=i+1)
```
Pattern the recursion delay to get free rhythms! You can even skip playing with `trig` and just play with the recursion `delay` if you feel like it!

### Imperative rhythm

```python3
@swim
def zoom(d=0.5, i=0):
    S('bd:r*20').out(i)
    sleep(0.25)
    S('hh:r*20', trig=euclid(6,8)).out(i)
    sleep(0.125)
    S('sd:r*20', trig=euclid(2,4)).out(i)
    again(zoom, d=0.5, i=i+1)
```
Create rhythm using the `sleep()` function. Fully compatible with everything else! It is usually a good idea to use `sleep()` after having composed something complex to slice time even more.

### Silence rhythms

```python3
@swim 
def silence_rhythm(d=0.5, i=0):
    S('bd').out(i, div=4)
    S('hh:2').out(i, div=2)
    S('drum:2+r*5').out(i, div=3)
    a(silence_rhythm, d=1/8, i=i+1)
```

Play with the `div` amount to generate interesting rhythms.

## Sampling

Sampling is taken care of by **SuperDirt** but I don't think that an official documentation of the API exists outside of the documentation provided by libraries using it. So be it, here are some basics for you to get started :)

### Sampler basics (S)

```python3
@swim
def hh(d=0.5):
    S('hh').out(i)
    again(hh, d=0.5)
```
This will play the first file in the `hh` folder, loaded via **SuperDirt**.

```python3
@swim
def hh(d=0.5):
    S('hh:1').out(i)
    again(hh, d=0.5)
```
This will play the second file, etc... Numbers wrap around, so you can't overflow and play a file that doesn't exist. It means that you can iterate freely on the sample number without fear.

### Sample playback speed (S)

```python
@swim
def hh(d=0.5):
    S('jvbass:0', speed='1,2,3,4').out(i.i)
    again(hh, d=0.5)=
```
You can pitch samples up or down by changing the playback speed. `1` is the normal playback speed, `2` twice as fast and `0` will not play anything at all. You can play a file in reverse speed by inputting negative values such as `-1` for backwards normal speed, etc... Beware of very low numbers close to `0` as they will be sometimes harder to hear but will still take memory to be played, especially if there is nothing to stop them.

### Sample playback volume (S)

```python
@swim
def loud(d=0.5):
    S('bd', speed='1', amp=1).out(i.i)
    again(hh, d=0.5)
```
This bassdrum will be played very loud. The `amp` parameter will determine the volume of audio playback for a given sample. `0` equals to silence. `1` corresponds to full volume, with distortion of the audio signal being allowed for larger values.

```python
@swim
def loud(d=0.5):
    S('bd', speed='1', gain=1).out(i.i)
    again(hh, d=0.5)
```
Gain is slightly similar to `amp`. The difference lies in the scaling. While `amp` is defined as a value on a linear scale, `gain` is defined on an exponential scale. The higher you go, the more subtle the change. Folks from the TidalCycles documentation recommend a value between `0` and `1.5` for better use.

### Cutting/Stopping samples (S)

```python
@swim
def cutting(d=0.5):
    S('jvbass:0', legato=0.1).out(i.i)
    again(cutting, d=0.5)
```
The `legato` parameter can be used to cut a sample hard after a given amount of time. It is a very useful parameter not to overlap sounds too much if you ever needed it. It can also be used a safety parameter for playing back long samples without loosing control over the stop time.


```python
@swim
def cutting(d=0.5):
    S('jvbass:0', cut=1).out(i.i)
    again(cutting, d=0.5)
```
The `cut` parameter will cut the previously playing sample if trigerred on the same orbit. This is just like `legato` except that the duration of the `legato` will depend on the time spent between two sounds.


```python
@swim
def cutting(d=0.5):
    S('jvbass:0', sustain=0.01).out(i.i)
    again(cutting, d=0.5)
```
The `sustain` value will determine the length of audio playback (in seconds).

### Sample position (S)

```python
@swim
def position(d=0.5):
    S('fire', speed='1', begin=0.1, end=0.5, amp=0.5).out(i.i)
    again(position, d=2)
```
When playing long audio samples, you might want to *scroll* through the file, moving the playhead accross the file. You can use the `begin` and `end` parameters (from `0` to `1`) to set the begin playback point and the end playback point. You can pattern the `begin` parameter with great expressive effect.

### Sample stretching (S)

```python
@swim
def streeeetch(d=0.5):
    S('fire', 
            begin='r/2',
            legato=1,
            amp=0.5,
            timescale=2.7).out()
    a(streeeetch)
```

You can get some interesting effects by using the `timescale` parameter (between `0` and `3` recommended) for stretching a sample over a given amount of time. This will result in a more *grainy* sound. This is some sort of timestretching for audio samples. Higher values ( >3 ) for timescale work with more distortion to the sound. This can yield interesting results for more experimental sound.

## Pitch

### Playback speed (S)

```python3
@swim
def hh(d=0.5, i=0):
    S('hh', speed='{1,8}').out(i)
    again(hh, d=0.5, i=i+1)
```
Changing the speed of audio playback for a given audio sample. Cheap version of tuning.

### Sample to pitch (S)

```python3
@swim
def hh(d=0.5, i=0):
    S('hh', midinote='C5!3, E5, G5').out(i)
    again(hh, d=0.5, i=i+1)
```
Pitching an audio sample relatively to a MIDI note.

### Sample to freq (S)

```python3
@swim
def hh(d=0.5, i=0):
    S('hh', freq='100 + (r*2000)').out(i)
    again(hh, d=0.5, i=i+1)
```
Pitching an audio sample relatively to a given frequency (in `hertz`).

## Texture and effects

## Patterning basics

### Patterning freely (P)

```python3
@swim
def free(d=0.5, i=0):
    # Look at P
    print(P('1,2,3,4', i))
    again(free, d=0.5, i=i+1)
```
`P()` is an interface to the patterning system. Write a pattern between quotation marks (`''` or `""`) and get something back. You will need to feed the pattern system a value to extract an index (`i`).

### Patterning in Senders (P)

```python3
@swim
def boom(d=0.5, i=0):
    S('bd', 
        cutoff='r*2000',
        speed='1,2,3,4').out(i)
    again(boom, d=0.5, i=i+1)
```
Sender objects are automatically turning string arguments into patterns. Feed the index value to the `.out()` method.

### Patterning using both methods (P)

```python3
@swim
def boom(d=0.5, i=0):
    S('bd', 
        cutoff=P('r*2000', i),
        speed='1,2,3,4').out(i)
    again(boom, d=0.5, i=i+1)
```
The result of this *swimming function* is strictly similar to the one directly above. Notice the difference in coding style, with the usage of `P()`.

### See me change (P)

```python3
@swim
def boom(d=0.5, i=0):
    S('bd', 
        cutoff=P('r*2000', i),
        speed='1,2,3,4').out(i)
    again(boom, d=0.5, i=i+1 if random() > 0.5 else -1)
```
Playing around with the basic `i` iterator structure.

### Index madness (P)

```python3
@swim
def boom(d=0.5, i=0):
    S('bd', 
        cutoff=P('r*2000, 500, 1000', i%2),
        speed='1,2,3,4').out(randint(1,4))
    again(boom, d=0.5, i=i+1)
```
You can be creative with pattern indexes and get random sequences, drunk walks, reversed sequences, etc... Be sure to always have a few different iterators close by to morph your sequences really fast.

## Pattern syntax

This section is very likely to change in upcoming versions.

### Numbers

```python3
@swim
def number(d=0.5, i=0):
    print(P('1, 1+1, 1*2, 1/3, 1%4, 1+(2+(5/2))')).out(i)
    again(number, d=0.5, i=i+1)
```
You can write numbers and use common operators such as addition, substraction, division, multiplication, modulo, etc... You can be specific about priority by using parenthesis.

### Time tokens

```python3
@swim
def number(d=0.5, i=0):
    print(P('$, r, m, p')).out(i)
    again(number, d=0.5, i=i+1)
```
Some number tokens are time dependant (based on **Sardine** clock time) and refer to a moment in time. Depending on the moment where your recursion takes place, you might see some values recurring because you are not polling continuously but polling just a predictible moment in time. 

- `$`: tick, the tick number since the clock started.
- `r`: random, between `0` and `1`.
- `p`: phase, a number between `0` and your `c.ppqn`.
- `m`: measure, the measure since the clock started.

```python3
@swim
def number(d=0.5, i=0):
    print(P('r, m, p')).out(i)
    again(number, d=0.5, i=i+1)
```

Some number tokens are time dependant, but will refer to absolute time. They are mostly used for long-running sequences and/or for introduction a random factor in your computation. You will notice that they are prefixed by `$`.
```python3
@swim
def random(d=0.5, i=0):
    print(P('$.Y, $.M, $.D, $.H, $.m, $.S, $.µ', i))
    again(random, d=0.5, i=i+1)
```

- `$.Y`: year, the current year.
- `$.M`: month, the current month.
- `$.D`: day, the current day.
- `$.H`: hour, the current hour.
- `$.m`: minute, the current minute.
- `$.S`: second, the current second.
- `$.µ`: microsecond, the current microsecond.

### Timed maths

```python3
@swim
def random(d=0.5, i=0):
    S('cp', speed='$%20').out(i)
    again(random, d=0.5, i=i+1)
```
Timed tokens make good low frequency oscillators or random values for generating interesting patterns. Playing with time tokens is a great way to get generative results out of a predictible sequence.

### Notes

```python3
@swim
def notes(d=0.5, i=0):
    S('pluck', midinote='C5,D5,E5,F5,G5').out(i)
    again(notes, d=0.5, i=i+1)
```
You can write notes in patterns. Notes will be converted to some MIDI value used by **SuperDirt**. It means that notes are numbers too and that you can do math on them if you wish to. The syntax to write notes is the following. The steps 2 and 3 can be omitted:

- 1) capital letter indicating the note name: `C`,`D`,`E`,`F`,`G`,`A`,`B`
- 2) flat or sharp: `#`, `b` 
- 3) octave number: `0`..`9` 

### Note qualifiers

```python3
@swim
def notes(d=0.5, i=0):
    S('pluck', midinote='C5->penta').out(i)
    again(notes, d=0.5, i=i+1)
```
Use the `print_scales()` function to print out the list of possible scales, chords and structures you can play with. You can use the `->` to **qualify** a note, to summon a collection of notes or a structure based on the provided note. `C->penta` will raise a major pentatonic scale based on middle C.

### Note modifiers

```python3
@swim
def notes(d=0.5, i=0):
    S('pluck', midinote='C5->penta.disco.braid').out(i)
    again(notes, d=0.5, i=i+1)
```
Some modifiers are available to fine-tune your note collections. There is currently no way to print out the list of `modifiers`. You will have to deep-dive in the source code to find them.

### Note maths

```python3
@swim
def notes(d=0.5, i=0):
    S('pluck', midinote='C5+0|4|8->penta.disco.braid').out(i)
    again(notes, d=0.5, i=i+1)
```
You can use arithmetic operators on notes.

### Names

```python3
@swim
def names(d=0.5, i=0):
    S('bd, pluck, bd, pluck:2+4').out(i)
    again(names, d=0.5, i=i+1)
```
You are using name patterns since you first started! You can also pattern names. The whole pattern syntax works just the same.

### Addresses

### Choice 

```python3
@swim
def choosing_stuff(d=0.5, i=0):
    S('bd|pluck', speed='1|2').out(i)
    again(choosing_stuff, d=0.5, i=i+1)
```
The pipe operator `|` can be used to make a 50/50% choice between two tokens. You can also chain them: `1|2|3|4`.

### Ranges

```python3
@swim
def ranges(d=0.5, i=0):
    S('pluck|jvbass', speed='1:5').out(i)
    again(ranges, d=0.5, i=i+1)
```
If you want to generate a number in the range `x` to `y` included, you can use the `:` operator.

### Ramps

```python3
@swim
def ramps(d=0.5, i=0):
    S('amencutup:{0,10}', 
        room='{0,1,0.1}',
        cutoff='{1,10}*100').out(i)
    again(ramps, d=0.5, i=i+1)
```

You can generate ramps using the `{1,10}` syntax. This will generate the following list: `[1, 2, 3, 4, 5, ..., 10]`. You can generate lists ramping up and down. This is an extended version of Python base `range` function. You can also generate a ramp with a floating point range by specifying it as the third argument: `{1,10,0.1}`.

### Repeat

```python3
@swim
def repeat_stuff(d=0.5, i=0):
    S('pluck|jvbass', speed='1:2', midinote='C4!4, E4!3, E5, G4!4').out(i)
    again(repeat_stuff, d=0.5, i=i+1)
```
The `!` operator inspired by TidalCycles is used to denote the repetition of a value. You can also sometimes use the `!!` operator from the same family. This operator is a bit special and will be detailed elsewhere.

### Silence

```python
@swim 
def silence_demo(d=0.5, i=0):
    S('bd,...').out(i, div=1)
    S('hh,., hh,..').out(i, div=1)
    a(silence_demo, d=1/8, i=i+1)
```

You can use a dot (`.`) inside any pattern to indicate a silence. Silence is a very important and complex topic. Adding silences is a great way to generate interesting patterns. Silences are different for each sender because silence doesn't have the same meaning for a sampler, a MIDI output or an OSC output (`S()`, `M()`, `O()`):

- `S()`: a silence is the absence of a sample. The event will be skipped.

- `M()`: a silence is the absence of a note. The event will be skipped.

- `O()`: a silence is the absence of an address. The event will be skipped.

There is also the interesting case of what I like to call *'parametric silences'*. Take a look at the following example:


```python
@swim 
def silence_demo(d=0.5, i=0):
    S('sitar', legato='0.5', speed='{1,4}, .!8').out(i, div=1)
    a(silence_demo, d=1/8, i=i+1)
```

We always have a sample here. There is no **real** silence but we have still have some silences included in the `speed` subpattern. It also has an effect. In the absence of a value for that silence, **Sardine** will backtrack and search the last value that could have been generated by the pattern. The result of the `speed` parameter will then be `[1,2,3,4,8,8,8,8,8,8,8,8]`. For people familiar with modular synthesis, this is pretty much equivalent to a *sample & hold* mechanism.

It is impossible to write a *parametric silence* composed only of silences. It doesn't mean anything to provide a value and actually not providing it.

## Amphibian variables

### Amphibian variables

```python
v.s = 60 # this is an amphibian variable

@swim 
def fun():
    # Calling it and setting it to v.s + 5
    M(note='v.s = v.s + 5').out()
    if random() > 0.8:
        v.s = 60 # resetting so it doesn't go too high
    again(fun)
```
There is a group of variables called *amphibian variables* that are both valid inside and outside the pattern notation. They are defined by `v` followed by a letter from the alphabet (uppercase or lowercase) : `v.a`, `v.A`, `v.Z`, `v.j`. These variables can be freely manipulated from the Python side or from the pattern side. They are totally transparent.

```python
@swim 
def fun(d=0.25):
    # Now having fun with it
    M(note='v.s = v.s + 5|2').out() # more fun
    if random() > 0.8:
        v.s = 50
    again(fun, d=0.25)
```
You can use them to leverage Python or the pattern syntax for what they do best: patterning or dealing with complex algorithmic transformations. Having them both available makes the pattern syntax even more expressive.

There is a finite list of actions you can perform on *amphibian variables*:

- using them (just by calling them)

- setting them (`v.i = 5`)

- resetting them to 0 (`v.i.reset`)

### Amphibian iterators

```python
@swim
def amphi_iter(d=0.25):
    S('amencutup:{1,10}').out(i.i)
    if random() > 0.8:
        i.i = 0
    a(amphi_iter, d=0.25)
```
Similarly to *amphibian variables*, there is a thing called *amphibian iterators* that are valid on both sides. They are defined by `i` followed by a letter from the alphabet (uppercase or lowercase) : `i.a`, `i.A`, `i.Z`, `i.j`. They can be use as substitutes for your regular manual recursive iterators. In the example above, I am using an *amphibian iterator* to summon a breakbeat.

```python
@swim
def amphi_iter(d=0.25):
    S('amencutup:{1,10}', speed='1|2|i.i=0').out(i.i)
    a(amphi_iter, d=0.25)
```
These iterators can be reset or set on the pattern side!

```python
@swim
def amphi_iter(d=0.25):
    if random() > 0.8:
        i.i = [1, 5]
    else:
        i.i = [1, 2]
    S('amencutup:{1,10}', speed='i.v|i.v=[1,2]').out(i.i)
    a(amphi_iter, d=0.25)
```
Similarly, you can define the step value between each value by providing a list of two numbers. This is valid on both sides.

## SuperCollider interface

### The SC Object
Note: the SC object is only available when you boot SuperCollider / SuperDirt from Sardine. (See the Install page for details.)

```python
SC.meter()
```
If `boot=True` in your `sardine-config`, **SuperCollider** and **SuperDirt** are booted as a subprocess when **Sardine** is initialized. The `SC` object acts as an interface if you ever need to talk directly with **SuperCollider**.

### VUmeter, Scope, FreqScope

```python
SC.meter()
SC.scope()
SC.freqscope()
```
You can open sound visualisation tools from the active **SuperCollider** session by running any of the commands above. Here is a short explanation of what each function do:

- `SC.meter()`: open a window showing VUMeters for each and every physical sound output.
- `SC.scope()`: open an oscilloscope to visualise every audio bus currently declared.
- `SC.freqscope()`: open a frequency spectrum visualizer of the global audio output.

### Sending code to SuperCollider

```python
# Generating a sinewave oscillating at 200hz.
SC.send('a={SinOsc.ar(200) * 0.1}; b = a.play;')

# Freing the synth
SC.send('b.free')
```
You can pipe code from your **Sardine** session to **SuperCollider**. Of course, this is not the best interface ever, but it can surely help to run short commands or to open an article from the **SuperCollider** documentation. To see **SuperDirt** documentation, you can type the following:

```python
SC.send('SuperDirt.help')
```

You will have to work without syntax highlighting. Copying and pasting short and useful commands is probably better if you are not an experienced **SuperCollider** user.
