```

                     ____                          _   _
                     | __ )  __ _ _ __  _ __   ___ | |_(_)
                     |  _ \ / _` | '_ \| '_ \ / _ \| __| |
                     | |_) | (_| | | | | | | | (_) | |_| |
                     |____/ \__,_|_| |_|_| |_|\___/ \__|_|

                                        Desktop notification tool for banano (https://banano.cc)
                                         by Mateo Cruz  (https://github.com/wolfrust)


```


✨You can use Bannoti to recieve notifications for Banano transactions on your computer.


---


**For everything below, replace `bannoti.py` with the file in your tree. (`bannoti.exe` on windows and `bannoti` on Linux)**


### Installation

Using already compiled excectables is the recommended option, as you will simply have to run the excecutable without installing any programming languages.
However, if you'd like to use the source code, that is documented as well below.

#### Compiled (5m)


1. Grab [the latest release](https://github.com/wolfrust/bannoti/releases/latest).
2. Unzip the file you just downloaded
3. Open a terminal window
4. [Move into the directory](https://help.ubuntu.com/community/UsingTheTerminal) in which you placed the files
5. Run ```bannoti.py --yesstartup``` to add Bannoti to startup

Step 5 is optional but recommended, because otherwise you will have to start Bannoti manually *every time you log on*, which could get annoying.


#### Source (15m)

Installing through source is a bit more gritty, but not very hard.

1. Install [Rust](https://rust-lang.org) and [Python (3)](https://python.org).
2. Download Bannoti's [source code](https://github.com/wolfrust/bannoti/releases/latest).
3. Unzip the file you just downloaded.
4. Open a terminal window.
5. Move into the directory of the files.
6. Move into assets/notify/
7. Run `cargo build`. This will build the binary.
8. Run `mv target/debug/notify ..` (Linux) or `move target\debug\notify.exe ..` (Windows)
9. Move back into the root of the project : `cd ../../`
10. Delete the assets/notify/ directory : `rm -rf assets/notify/`. **Make sure you type this out carefully, because you don't want to end up deleting the binary you just made.**

At this point you can do two things.
1. Start using Bannoti without compiling bannoti.py : Run `python bannoti.py --yesstartup`, and you're ready.
2. Compile bannoti.py as well. Please refer to [this guide](https://datatofish.com/executable-pyinstaller/) if you do not know how to compile python files.

---

### Usage ⌨

Running ``` bannoti.py --help ``` will show you a nice help message.

```

$> bannoti.py --help


  -- snip --


    bannoti.py <option>

    run : run the program
    --add : add an address to get notified for
    --remove : stop getting notifications for an address
    --gettracked : get tracked accounts
    --yesstartup : add program to startup
    --nostartup : remove program from startup


    If this is your first time using Bannoti, I recommend you see the README (./README.md).


```

It's pretty straightforward. You don't have to supply any other arguments, just one of these.

For example : `$> bannoti.py --add`


---

### Tips 😘

A small tip would go a long way :). 

Banano 🍌 : `ban_3qhzq3kxhe95hdq3q6uzmqg7ewp5js8ebcoxq1httmguzf7s5bb3a9894waf`

Nano 🍂 : `nano_1rhj7y5hkm5sx5rcn3p5tgsgyij1qwty1ja66197yacw3sjwoob3yyc76jbt`

If you'd like to tip me via some other means, please [contact me](https://github.com/wolfrust/wolfrust/#reach-me).

---


### Safety 🐙

Bannoti is free of any malware and bloatware. I provide binary packages to make things easier for you, but if you'd rather install through the source code, that's documented as well. You can look at the source code yourself to verify that nothing's sus. So I think it's reasonable to conclude that **your computer is safe.**

**Bannoti cannot access your wallet**. It relies on public information to do it's thing. This means **your funds are safe.**

**Bannoti respects your privacy.** It doesn't ask for any confindential information, just addresses. They are stored offline in `assets/track.ini` on your computer.

---

### Legal ⚖

Bannoti is licensed under the MIT License. You can find it [here](https://github.com/wolfrust/bannoti/blob/main/docs/LICENSE). A short summary is given below.

![Bannoti's License](mit-license-quick.png)



The tool that *sends the notifications* is called [notify-rust](https://github.com/hoodie/notify-rust), and is distributed under [this license](https://github.com/hoodie/notify-rust/blob/main/LICENSE-Apache).

The tool that allows python to interact with the Banano node is [bananopy](https://github.com/milkyklim/bananopy), and is distributed under [this license](https://github.com/milkyklim/bananopy/blob/master/LICENSE). It is Copyright (c) 2020 milkyklim.

---

### Feature Requests & Bug Reporting  🐞

Please use the [issues tab](https://github.com/wolfrust/bannoti/issues) for this, as that provides me with an organized way to look at requests & reports.
For bug reports, please attach the `bug` label, and for feature requests please attach the `enhancment` label.

---

### Credits

This project would not have been possible without [bananopy](https://github.com/milkyklim/bananopy) by @milkyklim, and [notify-rust](https://github.com/hoodie/notify-rust) by @hoodie.

---


### Contact 📱

You can email me at mateo.xzf@protonmail.ch. Please set the subject line to "Bannoti" (without the quotes).


